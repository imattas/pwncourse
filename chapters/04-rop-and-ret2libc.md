# Chapter 4 — ROP, ret2libc, and constrained chains

## 4.1 ROP is a register program

ROP chains use existing instruction sequences ending in `ret`. Each gadget consumes stack words and changes machine state. Treat a chain like a tiny program:

| Word | Gadget/effect | Invariant |
|---|---|---|
| 0 | `pop rdi; ret` | next word becomes first argument |
| 1 | pointer/value | must be a valid target or scalar |
| 2 | call target | stack alignment must be acceptable |

The `rop-call` lab isolates this model with a deterministic gadget. Start from the stack offset, locate the gadget, place the argument, and then return to the target.

## 4.2 ret2libc

When NX blocks shellcode, a common educational chain calls existing libc functions. A typical sequence needs a leak, a calculated libc base, a `pop rdi; ret` gadget, a pointer to a desired string, and the resolved function address. The chain is not “call system”; it is:

```text
leak → libc base → stack alignment → argument pointer → resolved call → success condition
```

For safe local labs, use the provided flag functions and local success markers. The reasoning is the same without turning the course into a ready-made target attack.

## 4.3 Alignment and pivots

Some x86-64 libc code assumes 16-byte stack alignment. If the chain crashes inside a vector instruction, inspect `$rsp % 16` at the call boundary. A one-gadget `ret` can repair alignment, but it changes the chain's stack consumption and must be justified.

A pivot changes the stack pointer to attacker-controlled memory. Common shapes include `leave; ret` with a prepared fake frame or a gadget that moves a register into `rsp`. Prove that the destination is mapped, writable, and populated before using it.

## 4.4 Syscall-oriented extensions

When function calls are unavailable or filtered, a chain can set syscall registers directly. On AMD64, `rax` selects the syscall and `rdi`, `rsi`, `rdx`, `r10`, `r8`, and `r9` carry arguments. The advanced lessons ask you to enumerate allowed syscalls first; a chain that ignores seccomp is not a solution.

## Exercises

1. Annotate every word in `rop-call` with its effect on `rsp` and `rdi`.
2. Add a harmless alignment check to a local ROP target.
3. Use `ROP(elf).find_gadget` and compare its result with `objdump`.
4. Build a two-stage local chain where stage one returns to a read-like function.

## Worked planning example

Suppose a binary gives you a 72-byte overwrite, a `pop rdi; ret` gadget, and a leak of `puts`. Do not immediately write a giant payload. Make the dependency order explicit:

1. Use the first return to call the existing leak path.
2. Return to a clean input path so the process remains alive.
3. Parse exactly the bytes that the target prints.
4. Subtract the `puts` offset from the matching libc and assert the base.
5. Build the second stage from the calculated base.
6. Check alignment and repeat the run several times.

If step 2 is missing, the final call is irrelevant because the process dies after the leak. If step 4 uses a different libc, the arithmetic is precise but wrong. Exploitation is the discipline of preserving these dependencies.
