# Lesson 4 — Pwntools exploit development

A reliable exploit is a small program with explicit I/O states, architecture-aware packing, local process support, and useful failure evidence. This lesson turns manual debugger work into repeatable exploit engineering.

## Lab package

Port the Lesson 3 solutions to `solve.py` using `context`, `ELF`, `process`, `sendafter`, `p64`, and `interactive`. Add a `LOCAL`/`REMOTE` switch even though the course services run on localhost. Test repeated runs and preserve logs when a prompt or newline assumption fails.

**Exit test:** one exploit script works against the local process and the matching localhost socket target.
