# ret2arg

Objective: redirect control flow and satisfy a function argument. Find the `pop rdi; ret` gadget, then place the magic value in the first integer-argument register before returning to `win`.

The chain layout is `padding | pop_rdi_ret | 0x13371337 | win`.

