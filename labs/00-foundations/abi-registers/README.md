# abi-registers

Learn the x86-64 System V calling convention used by later stack and ROP labs.

```bash
make
gdb -q ./challenge
(gdb) break add_three
(gdb) run
(gdb) info registers rdi rsi rdx rax
```

Record the argument order before continuing. ROP chains must reproduce this convention with gadgets.

