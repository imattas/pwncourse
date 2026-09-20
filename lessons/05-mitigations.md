# Lesson 5 — Mitigations and information leaks

`checksec` is a constraint summary, not an exploit plan. You will connect NX, PIE, ASLR, canaries, and RELRO to the primitive you need, then use a leak to recover the missing address information without confusing disclosure with control.

## Lab package

Solve the stack-protection track and the `labs/04-libc/got-leak` challenge. Identify what each mitigation blocks, find the remaining disclosure primitive, parse the leak, and calculate the relevant image or libc base. Include a mitigation-before/after table in the writeup.

**Exit test:** state which bytes are known, which are randomized, and which primitive bridges the gap.
