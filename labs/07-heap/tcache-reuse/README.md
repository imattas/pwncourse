# tcache-reuse

Objective: observe the simplest per-thread cache behavior: free a small chunk, then request the same size. This is a prerequisite for understanding why stale pointers and metadata corruption can influence later allocations.

This lab demonstrates reuse, not a complete poisoning exploit. The extension is to inspect freed bytes and explain safe-linking on the glibc version in your WSL image.

