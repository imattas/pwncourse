# Lab 03 — First stack overflow

## Goal

Convert a measured stack overwrite into a controlled return.

## Work

Solve `ret2win`, then `ret2arg`. Prove the offset, locate `win` and `pop_rdi_ret`, and draw the post-return stack. The expected chains are `padding → win` and `padding → pop rdi; ret → value → win`.

## Deliverables

Submit an annotated exploit, a GDB screenshot or transcript showing the target reached, and a source-level patch that bounds the read. Include why NX does not prevent this code-reuse chain.

## Extension

Build with PIE, locate the main-image base at runtime, and update the target calculation. Do not hard-code the address from one run.

