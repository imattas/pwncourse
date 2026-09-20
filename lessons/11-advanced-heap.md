# Lesson 11 — Advanced heap exploitation

This lesson composes primitives: leak heap or libc state, shape allocation order, redirect a pointer, and turn the resulting write into a meaningful target. The chain is only valid if every transition preserves allocator invariants.

## Lab package

Solve `labs/07-heap/menu-uaf` and `heap-leak-chain`. Keep a state table for sizes, bins, addresses, and aliases. Build the exploit in stages—layout, leak, corruption, target write—and add assertions after each stage so a changed allocator behavior is visible.

**Exit test:** explain the complete chain as a sequence of state transitions, not as a magic menu transcript.
