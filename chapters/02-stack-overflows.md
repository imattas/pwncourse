# Chapter 2 — Stack overflows and ret2win

## 2.1 From memory corruption to control flow

The simplest stack overflow is useful because it has a clean chain. A read accepts more bytes than a local array can hold. The excess bytes overwrite adjacent stack state, eventually the saved return pointer. When the function returns, the CPU takes the attacker-supplied address.

The first goal is not code execution. It is a controlled, explainable redirect to a function already in the binary.

## 2.2 ret2win

For `labs/02-stack/ret2win`, the workflow is:

```bash
make
checksec --file=./challenge
nm -C ./challenge | grep win
python3 - <<'PY'
from pwn import *
print(cyclic(160).decode())
PY
gdb -q ./challenge
```

Once the measured offset is known, the payload is conceptually:

```python
payload = b'A' * OFFSET + p64(elf.symbols['win'])
```

The important facts are the measured offset, the target address, the architecture, and the reason NX does not matter here: no new instructions are injected. Existing code is reused.

## 2.3 Passing arguments

`ret2arg` adds a constraint. Reaching `win` is insufficient because it checks a magic value in `rdi`. The chain becomes:

```text
padding → pop rdi ; ret → 0x13371337 → win
```

Every ROP word is a stack value that becomes the next return address or gadget data. Draw the stack after each `ret`; this catches off-by-eight errors faster than trial and error.

## 2.4 Input protocols are part of exploitation

`split-input` teaches that a target is a protocol, not just a function. The exploit must wait for `first:\n`, send the first stage, wait for `second:\n`, and then send the overwrite. `sleep(1)` is not synchronization: it may work locally and fail under a remote scheduler.

Use:

```python
io.recvuntil(b'second:\n')
io.send(payload)
```

## 2.5 Defenses

The direct chain fails when a canary detects the overwrite, PIE randomizes the target, or a different build changes the offset. Do not “try more padding.” Re-run the evidence workflow and identify the new missing primitive.

## Exercises

1. Rebuild `ret2win` with PIE and explain which address calculation is now missing.
2. Find the `pop_rdi_ret` gadget in `ret2arg` with `objdump` and verify its effect in GDB.
3. Modify `split-input` so the first stage leaks a value; describe how that leak could feed a second stage.
4. Patch each source with a bounded read and prove the original chain no longer works.

## Checkpoint

Write a short report containing root cause, offset evidence, chain words, mitigation state, and a source-level repair.

