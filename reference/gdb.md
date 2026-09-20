# GDB field guide

```text
gdb -q ./challenge
set disassemble-next-line on
set pagination off
break main
run
info registers
x/32gx $rsp
x/20i $rip
vmmap
```

Use `telescope $rsp` with pwndbg when available. For a crash, save the exact input, signal, RIP, RSP, and the stack words around the fault. A cyclic pattern is evidence for an offset only when the crashed value is the pattern value you expected.

