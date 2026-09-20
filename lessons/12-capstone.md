# Lesson 12 — Sandboxes and custom capstones

The final step is chain design under multiple constraints. You will reason about seccomp filters, restricted syscalls, advanced ROP/SROP ideas, and how to create a new chain from an unfamiliar primitive instead of matching a tutorial title.

## Lab package

Start with `labs/08-advanced-linux/seccomp-rop`, then choose a capstone from `capstones/`. Produce an attack graph, list every assumption, implement the exploit against the localhost target, and write a patch that removes the root cause. The capstone rubric rewards evidence and explanation, not payload length.

**Exit test:** defend why your chain works, which mitigation it bypasses, and what code change actually fixes the bug.
