# Writeup: uaf

Root cause: `record` is used after `free`. Primitive: stale-pointer read when the allocator reuses the chunk for `replacement`.

Chain: freed ownership → same-size reuse → stale read → disclosure of replacement bytes. Repair by setting the pointer to `NULL` after `free` and enforcing ownership rules.

