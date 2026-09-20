# Mitigation matrix

| Mitigation | What it changes | Typical evidence | Common next question |
|---|---|---|---|
| NX | Stack/heap bytes are not executable | `checksec` says NX enabled | Can existing code be chained? |
| ASLR | Mapping addresses vary per process | repeated `/proc`/leak values differ | What leak gives a stable base? |
| PIE | Main executable address varies | PIE enabled | Can a code pointer disclose the image base? |
| Canary | Detects many contiguous stack overwrites | canary enabled | Is there a leak or non-linear write? |
| Partial RELRO | GOT may remain writable | partial RELRO | Can a call target be redirected? |
| Full RELRO | GOT is read-only after relocation | full RELRO | Can control flow use ROP or another target? |
| Fortify | Adds checked libc wrappers in some cases | fortified symbols | What exact size reaches the bug? |
| CET/IBT | Adds control-flow integrity features | platform-dependent | Which legitimate targets remain? |
| seccomp | Filters syscalls | `prctl`/filter behavior | Which allowed syscall sequence achieves the goal? |

