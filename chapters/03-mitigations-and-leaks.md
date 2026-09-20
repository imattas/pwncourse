# Chapter 3 — Mitigations, leaks, and address arithmetic

## 3.1 Read checksec as a decision tree

Mitigations do not make exploitation impossible; they change the primitive you need.

| State | Consequence | Question |
|---|---|---|
| NX enabled | input bytes are not executable | what existing code can be chained? |
| PIE enabled | main image base varies | can a code pointer disclose it? |
| ASLR enabled | libc/stack/heap vary | which mapping can be leaked? |
| Canary enabled | contiguous overwrite is detected | is there a leak or alternate write? |
| Full RELRO | GOT is read-only | can ROP or another target replace it? |

The chain is a sequence of proofs. If a payload depends on a libc address, the writeup must show how that address was obtained and which libc version supplies the offset.

## 3.2 A leak is a mapping plus an offset

`got-leak` prints a pointer associated with `puts`. In a real target, normalize the leak, identify the library, and calculate:

```text
libc_base = leaked_puts - known_puts_offset
system    = libc_base + known_system_offset
```

Then validate the result. Page alignment is a useful sanity check, but it is not proof that you picked the right library. Compare `ldd ./challenge`, the challenge-provided libc, and the symbols in that exact file.

## 3.3 Partial leaks and bad bytes

A newline-terminated print may disclose only six meaningful pointer bytes. Use `recvuntil`, `recvline`, or a fixed-length read according to the target protocol. Pad before `u64` only when you know which end is missing:

```python
leak = u64(io.recvn(6).ljust(8, b'\0'))
```

If the input path rejects `\x00`, `\x0a`, or `\x20`, the chain must choose addresses and encodings that survive. Document the constraint rather than silently relying on a local coincidence.

## 3.4 Leak-to-control chain

The canonical two-stage chain is:

```text
bug → leak function pointer → calculate base → return to read → receive stage two → final ROP
```

The first stage must leave the process alive and restore a usable input path. The second stage can use libc gadgets because the base is now known. This is why exploit development is chain engineering: the first effect exists to make the second effect possible.

## Exercises

1. Run `got-leak` repeatedly and classify the pointer as executable image, libc, stack, or heap.
2. Change the leak to six bytes and update the parser with an explicit length assertion.
3. Write a small script that rejects a non-page-aligned candidate base.
4. Explain why a hard-coded local libc address is not a remote exploit.

