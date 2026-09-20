# Stage 03 — mitigations as a planning tool

Run `checksec` before writing a payload. NX changes code injection into code reuse; ASLR changes absolute addresses into base-plus-offset arithmetic; PIE applies that reasoning to the main executable; canaries constrain contiguous stack writes; RELRO changes whether GOT redirection is available.

For each earlier stack lab, make a matrix with: bug, primitive, blocked payload, new evidence needed, and candidate replacement chain. The correct habit is not “bypass every mitigation,” but “choose the smallest primitive that still meets the objective.”

Exercises: rebuild `ret2win` with PIE, add a canary, compare partial/full RELRO, and explain which parts of the original proof remain valid.

