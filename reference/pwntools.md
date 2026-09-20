# pwntools field guide

```python
from pwn import *
context.binary = elf = ELF('./challenge', checksec=False)
io = process(elf.path)
io.recvuntil(b'> ')
io.sendline(payload)
io.interactive()
```

Prefer `recvuntil` and `recvn` to sleeps. Use `p64`, `u64`, `cyclic`, `cyclic_find`, `ELF.symbols`, and `ELF.got` only after proving the binary matches the assumptions. Keep local/debug/remote selection explicit and default to local.

