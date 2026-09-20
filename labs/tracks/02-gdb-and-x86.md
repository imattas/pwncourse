# Lab 02 — GDB and x86-64

## Goal

Turn crashes and breakpoints into reproducible evidence.

## Work

Complete `crash-course` and `find-the-offset`. Generate a cyclic input, run it under GDB, inspect `$rip`, `$rsp`, the stack bytes, and the backtrace, then calculate and verify the control-data offset with a marker. Compare `disassemble /m` with `disassemble /r`.

## Deliverables

Provide the exact command transcript, input bytes, faulting value, calculated offset, and a short explanation of endianness. A correct submission can be repeated from a clean shell without guessing.

## Extension

Set a watchpoint on the saved return address and identify the instruction that overwrites it. Explain why a watchpoint may be more useful than stepping every instruction.

