# Lab 11 — Advanced heap

## Goal

Compose a lifetime error into a control-flow effect without hiding allocator assumptions.

## Work

Use `menu-uaf` and `heap-leak-chain`. Trace the menu state machine, prove the stale pointer, observe same-size reuse, and identify the callback field. Then write the chain as `free → reuse → controlled object image → callback`.

## Deliverables

Submit allocator state after each menu operation, the object layout, the callback overwrite evidence, and a compatibility note. Explain why this fixture is simpler than full safe-linking-aware tcache poisoning.

## Extension

Build a separate version-pinned metadata fixture and record the exact glibc checks that accept or reject the corrupted state.

