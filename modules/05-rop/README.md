# Stage 05 — ROP and constrained execution

Represent a chain as a table before encoding it: stack offset, gadget, register effect, next stack word, and invariant. A useful chain has a purpose for every word. Check stack alignment before a libc call, account for bad bytes, and distinguish a gadget that sets a register from one that merely passes through it.

Progression: direct function call → register setup → staged read → stack pivot → syscall-oriented chain → SROP as a constrained-register-setting technique.

