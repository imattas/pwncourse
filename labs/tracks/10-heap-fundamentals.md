# Lab 10 — Heap fundamentals

## Goal

Model allocation lifetime, reuse, and stale aliases.

## Work

Complete `chunk-inspect`, `tcache-reuse`, and `uaf`. Record requested size, returned pointer, free operation, reuse address, and bytes observed through the stale pointer. Compare raw GDB memory with allocator helpers.

## Deliverables

Submit before/after heap diagrams, glibc version, and a classification of each primitive as read, write, reuse, or control. Include the ownership repair.

## Extension

Repeat the same sequence under another glibc version and explain any changed metadata or reuse behavior.

