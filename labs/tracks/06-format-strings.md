# Lab 06 — Format strings

## Goal

Use a variadic-format bug first as a read primitive and then as a controlled write.

## Work

Complete `fmt-read`: map positional arguments with a marker and classify values. Then work through `fmt-write`: identify the target address, calculate `%hn` widths, and verify the resulting state. Keep a table of index, value, source, stability, and usefulness.

## Deliverables

Submit the probe transcript, positional index, payload arithmetic, and a safe repair using a constant format string. Explain newline, NUL, width, and alignment constraints.

## Extension

Use the disclosure to derive a base and feed it into a second-stage control-flow plan without assuming a fixed address.

