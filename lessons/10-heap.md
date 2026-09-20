# Lesson 10 — Heap fundamentals and use-after-free

Heap exploitation starts with allocator state and object lifetime. Track allocation size, chunk reuse, metadata boundaries, ownership, and the difference between an out-of-bounds write and a stale pointer.

## Lab package

Use `labs/07-heap/chunk-inspect`, `tcache-reuse`, and `uaf`. Draw the chunks after every menu action, prove reuse with addresses, then turn a stale pointer into a controlled read or write. Explain which behavior is allocator mechanics and which is the program’s lifetime bug.

**Exit test:** predict the next allocation address before running it and explain why the prediction is valid.
