# Lesson 2 — GDB and crash triage

The first exploit primitive is not a payload; it is a proven control point. You will learn to reproduce a crash, calculate an exact offset, distinguish a faulting instruction from corrupted data, and turn debugger observations into a small hypothesis.

## Lab package

Use `labs/01-debugging/crash-course` and `find-the-offset`. Run the target under GDB, collect the signal, registers, stack bytes, and input, then validate the offset with a cyclic pattern and a `BBBBBBBB` marker. Record the final `RIP`, `RSP`, and mitigation profile in your writeup.

**Exit test:** reproduce the same control overwrite twice from a clean process.
