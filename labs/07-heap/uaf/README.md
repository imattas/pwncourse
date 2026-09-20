# uaf

Objective: observe allocator reuse after a pointer's lifetime ends. The fixture intentionally prints through a stale pointer after a same-sized allocation.

Use GDB breakpoints around `free` and the second `malloc`; record the pointer values and explain why the bytes now name a different object. Do not generalize this deterministic fixture to every allocator version.

