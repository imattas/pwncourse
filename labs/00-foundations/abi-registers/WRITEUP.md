# Writeup: abi-registers

There is no vulnerability. The observable behavior is a controlled function call with three integer arguments.

Chain: C call → compiler-generated register setup → function entry → return value in `rax`.

At `add_three`, `rdi`, `rsi`, and `rdx` contain 10, 20, and 12; the return value is 42. Recompile at `-O2` and compare the disassembly as an extension.

