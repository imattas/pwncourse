# Course map

## How to study

For every lab, follow this order: read the objective, build the binary, inspect it with `file`, `checksec`, `readelf`, and `objdump`, reproduce the crash or leak, write a starter exploit, then compare with the reference solution. Keep a notebook containing the primitive, its constraints, and the next chain stage.

| Stage | Topic | Exit skill |
|---|---|---|
| 00 | Linux, C, ELF, memory, ABI | Explain what a process and ELF contain |
| 01 | GDB and crash triage | Prove an offset and control point |
| 02 | Stack control | Build ret2win and argument-aware payloads |
| 03 | Mitigations | Turn checksec output into a plan |
| 04 | Leaks and libc | Calculate bases and build ret2libc |
| 05 | ROP | Compose gadgets under constraints |
| 06 | Format strings | Read and write through a variadic bug |
| 07 | Heap | Track allocator state and lifetime primitives |
| 08 | Advanced Linux | Reason about seccomp, SROP, and loaders |
| 09 | Kernel concepts | Understand user/kernel boundaries safely |
| 10 | Capstones | Design and explain custom exploit chains |

## Mastery rubric

You are at mastery when you can start from source plus a stripped binary, derive a chain without copying a payload, make it reliable across repeated local runs, explain why each mitigation is bypassed, and write a repair that removes the primitive.

