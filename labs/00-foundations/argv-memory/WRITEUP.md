# Writeup: argv-memory

The program intentionally prints addresses. This is an educational information disclosure, not a control-flow exploit.

Chain: argument vector → stack/local address observation → GDB frame inspection → ASLR hypothesis.

The exact address is expected to vary, so the solution asserts only stable format and argument count. Remove the diagnostic print and compare two ASLR-enabled runs as an extension.

