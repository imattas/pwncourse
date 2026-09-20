# Writeup: ret2arg

Root cause: the same stack overflow gives control of RIP. Unlike ret2win, `win` checks its first argument, so control flow alone is insufficient.

Primitive: controlled RIP plus register setup. Chain: overflow → `pop rdi; ret` → magic value in RDI → `win`.

The explicit gadget makes the teaching binary deterministic. The repair is a bounded read. In a real binary, gadget availability and stack alignment must be proven from the artifact.

