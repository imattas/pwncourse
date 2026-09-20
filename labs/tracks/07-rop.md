# Lab 07 — Return-oriented programming

## Goal

Build chains as register programs under stack and byte constraints.

## Work

Solve `rop-call`. Locate gadgets with both `objdump` and pwntools, annotate stack consumption, and verify `rdi` at the target. Then design a staged-read chain on paper: input path, read destination, byte count, return address, and second-stage layout.

## Deliverables

Provide a chain table for every word, an alignment check, and three successful runs. Explain why ROP reuses existing executable code and why a gadget search result is not automatically a valid chain.

## Extension

Add a stack pivot or a syscall-oriented stage in a detached local fixture and document the writable destination.

