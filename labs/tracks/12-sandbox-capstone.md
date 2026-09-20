# Lab 12 — Sandboxes and capstone

## Goal

Design an exploit chain from evidence under multiple constraints.

## Work

Use `seccomp-rop` to inventory syscalls and then choose one capstone: guided stack chain, leak plus ROP, format-string control, or heap lifetime chain. Start with a blank chain table and do not open the reference writeup until you have a crash/leak transcript.

## Deliverables

Submit the binary hash, environment, root cause, primitive limitations, chain table, exploit with assertions, repeated-run evidence, and source repair. The result marker must use `flag{...}`.

## Mastery extension

Create a new vulnerable local C program, write its challenge README and reference writeup, choose two mitigations, and make a second learner solve it without seeing your exploit.

