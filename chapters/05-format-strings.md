# Chapter 5 — format strings

## 5.1 Why `printf(input)` is powerful

The format string controls how `printf` consumes variadic arguments. Conversion directives can disclose stack/register spill values; `%n`-family conversions write the number of bytes printed to a pointer. The bug is not “printf is dangerous” in the abstract. The bug is that data was used as the format specification.

Safe code is:

```c
printf("%s", input);
```

## 5.2 Reconnaissance

Start with a marker and positional probes. Keep the output bounded and record the exact index where your marker appears. Classify disclosed values by comparing them with GDB, the ELF base, libc mappings, and stack addresses. Do not treat the first hexadecimal value as a useful leak automatically.

```text
AAAA.%1$p.%2$p.%3$p.%4$p
```

The `fmt-read` lab is deliberately a disclosure exercise. Your report should explain which values are stable across runs and which change with ASLR.

## 5.3 Controlled writes

`fmt-write` discloses the target address and asks you to derive the positional layout. A `%hn` write stores 16 bits, so the desired width is calculated modulo `2^16`. Multiple writes must be ordered so the printed count only increases or wraps in a controlled way. Every address placed after the format string must be tracked as a word on the target's stack.

The write chain is:

```text
find argument index → identify target → calculate widths → write half-words → verify state
```

Never test a write against a real process you do not own. These labs are local and include a deterministic `flag{...}` marker.

## Exercises

1. Map the first twelve positional arguments in `fmt-read`.
2. Repeat the map with ASLR enabled and classify stable versus randomized values.
3. Derive a `%hn` payload for `0x1337` in the supplied fixture.
4. Replace the vulnerable call with `printf("%s", input)` and add a regression test.

## A disciplined format-string worksheet

Before writing a payload, answer these questions in order:

1. Where is the format string stored, and how many bytes can it contain?
2. Which positional argument contains the first bytes of your marker?
3. Is the value you want to read a stack pointer, a code pointer, a libc pointer, or your own input?
4. Does the output path stop at a newline, NUL byte, or maximum length?
5. Is the target address writable, and is it aligned for the conversion you selected?
6. What exact value should memory contain after the write?
7. How will the exploit verify the write without relying on a crash?

Keep a table while probing:

| Index | Printed value | Likely source | Stable? | Useful? |
|---:|---|---|---|---|
| 1 | `...` | register spill | no | no |
| 2 | `...` | stack | maybe | investigate |
| N | marker | input | yes | layout anchor |

The table is the lesson. A final payload without it teaches you almost nothing and will not survive a changed build.

## Defensive review

Audit every call that accepts a user-controlled first argument to a printf-family function. Compiler warnings such as `-Wformat-security` help, but they are not a repair by themselves. The repair is a constant format string and a separate data argument. Add a regression test that sends `%p.%p.%n` and confirms that no pointer disclosure or write occurs.
