# chunk-inspect

Objective: observe allocations, spacing, and free order. Inspect the returned pointers in GDB and compare the requested size with the allocator's chunk size. Do not infer metadata layout from one glibc version without checking it.

