# Lab index

Every success marker uses the canonical form `flag{...}`. Build from WSL with `make` inside a lab; run the reference solution only after completing the learner exercise.

| Stage | Lab | Main concept | Status |
|---|---|---|---|
| 00 | hello-elf | ELF inspection | runnable |
| 00 | argv-memory | process memory and ASLR observation | runnable |
| 00 | abi-registers | x86-64 calling convention | runnable |
| 01 | crash-course | overflow crash triage | runnable |
| 01 | find-the-offset | cyclic offset discovery | learner exercise |
| 02 | ret2win | buffer overflow to function | runnable |
| 02 | ret2arg | overflow plus register setup | runnable |
| 02 | split-input | staged input | runnable |
| 04 | got-leak | pointer leak and base reasoning | runnable |
| 05 | rop-call | explicit ROP chain | runnable |
| 06 | fmt-read | format-string disclosure | runnable |
| 06 | fmt-write | format-string `%hn` write | learner exercise |
| 07 | uaf | stale-pointer read | runnable |
| 07 | chunk-inspect | allocator observations | runnable |
| 07 | tcache-reuse | same-size reuse | runnable |
| 07 | menu-uaf | menu-driven UAF | runnable |
| 07 | heap-leak-chain | UAF to callback control | runnable |
| 08 | seccomp-rop | syscall-constraint planning | runnable fixture |

## Twelve lab tracks

The course is organized into twelve lab tracks, each with a tutorial objective, a challenge ladder, required evidence, and an extension. The individual binaries under `labs/` are the downloadable fixtures used by these tracks.

| Lab | Track | Core work |
|---:|---|---|
| 01 | Warmup and ELF | Artifact inspection, sections, symbols, ABI |
| 02 | GDB and x86-64 | Crash evidence, cyclic offsets, stack frames |
| 03 | First stack overflow | ret2win and argument-aware control |
| 04 | Exploits with pwntools | Automation, synchronization, assertions |
| 05 | Stack protections | NX, ASLR, PIE, canaries, RELRO |
| 06 | Format strings | Positional reads and `%hn` writes |
| 07 | ROP | Gadgets, alignment, pivots, staged input |
| 08 | Leaks and ret2libc | Base arithmetic and second-stage chains |
| 09 | Remote services | Local TCP service and remote-style I/O |
| 10 | Heap fundamentals | Chunks, reuse, UAF, ownership |
| 11 | Advanced heap | Menu UAF and callback-control chain |
| 12 | Sandbox and capstone | Syscall constraints and custom chains |

“Learner exercise” means the repository intentionally leaves the final payload derivation to the student while still providing the vulnerable binary, objective, and complete writeup guidance.
