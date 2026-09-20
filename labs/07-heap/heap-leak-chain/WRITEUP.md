# Writeup: heap-leak-chain

Root cause: the program assumes a newly allocated same-sized object is safe after the original object's lifetime ended, then accepts a complete object image from input. Primitive: controlled function pointer in a reused allocation.

Chain: allocation disclosure → free → same-size reuse → 16 bytes of object data → callback pointer set to `win` → local success marker. Real allocator attacks add metadata, safe-linking, and target-validity constraints; this fixture isolates the chain composition first.

Repair by retaining ownership, clearing stale references, initializing every field, and avoiding untrusted complete-object writes.

