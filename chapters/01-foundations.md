# Chapter 1 — Foundations and debugging

Binary exploitation starts with a model of the program, not a payload. You need to know what bytes enter the process, where they are stored, which code consumes them, and what evidence proves your hypothesis.

## 1.1 The process you are attacking

An ELF process has code (`.text`), read-only constants, initialized data, zero-initialized data, a heap, a stack, shared libraries, and loader-created mappings. Addresses are virtual; the same source can receive different addresses across executions because ASLR randomizes mappings. An address is not a secret by itself. It becomes useful when you identify the mapping and a stable offset within it.

Start every lab with:

```bash
file ./challenge
checksec --file=./challenge
readelf -hW ./challenge
readelf -lW ./challenge
nm -C ./challenge | head -30
objdump -dM intel ./challenge | less
```

Write down architecture, PIE, NX, RELRO, canary state, imported functions, and whether symbols are present. This notebook becomes the chain plan later.

## 1.2 The x86-64 calling convention

On Linux System V AMD64, integer or pointer arguments arrive in `rdi`, `rsi`, `rdx`, `rcx`, `r8`, and `r9`; additional arguments are on the stack. Return values arrive in `rax`. The stack grows toward lower addresses, and `call` pushes a return address. A typical frame is:

```text
higher addresses  saved RIP
                  saved RBP
                  local buffer
lower addresses
```

Compilers may omit the frame pointer or reorder locals, so source-level buffer size is not a replacement for a measured offset.

## 1.3 Your first GDB session

```text
gdb -q ./challenge
set pagination off
set disassemble-next-line on
break main
run
info registers
disassemble /m main
x/32gx $rsp
continue
```

Use a breakpoint immediately before the vulnerable call and another after it. Compare `$rsp`, the local buffer, and the saved return address. When the program crashes, save the signal, instruction pointer, stack pointer, and exact input. A crash without the input that caused it is not reproducible evidence.

## 1.4 Cyclic patterns

Repeated `A` bytes tell you that data overflowed. A cyclic pattern tells you which position reached saved control data:

```python
from pwn import *
print(cyclic(200).decode())
print(cyclic_find(0x6161616c))
```

On a 64-bit crash, inspect the actual bytes in memory; truncation, newline handling, and endianness can make the register value look reversed. Verify the candidate with a marker payload such as `b'A' * offset + p64(0x4242424242424242)`.

## Exercises

1. Build `labs/00-foundations/hello-elf` and identify its ELF class.
2. Break on `add_three` in `abi-registers` and record the three argument registers.
3. Crash `crash-course`, calculate the offset, and reproduce the crash with a marker.
4. Explain why the `argv-memory` address changes across runs.

## Checkpoint

You are ready for the next chapter when you can state the exact input path, offset, overwritten value, and mitigation profile for a crash without guessing.

