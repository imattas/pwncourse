# Lab 04 — Writing exploits with pwntools

## Goal

Replace fragile manual interaction with a readable, testable exploit harness.

## Work

Rewrite one earlier exploit using `context.binary`, `ELF`, `process`, `recvuntil`, `send`, `p64`, `cyclic`, and assertions. The exploit must fail with a useful error if the prompt or success marker is absent.

## Deliverables

Submit local and GDB modes, a transcript of three successful runs, and a paragraph explaining why sleeps are not synchronization. Keep the target selection explicit and default to local.

## Extension

Use the repository’s target helper with `PWN_REMOTE=1` against the included localhost server. The same exploit should change transport without changing the chain logic.

