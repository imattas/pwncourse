# Writeup: split-input

Root cause: the second `read` accepts 200 bytes into a 64-byte buffer. The first read is intentionally harmless and teaches protocol synchronization.

Primitive: controlled RIP after a staged interaction. Chain: prompt → bounded first stage → prompt → 72-byte offset → `win`.

The repair is to bound the second read to `sizeof second`. A robust exploit waits for exact prompts and treats EOF as a failure, making timing independent.

