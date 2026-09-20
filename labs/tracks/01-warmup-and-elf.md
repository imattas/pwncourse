# Lab 01 — Warmup and ELF

## Goal

Learn the artifact workflow before exploitation: identify architecture, symbols, sections, imports, and mitigation state.

## Work

Use `hello-elf`, `argv-memory`, and `abi-registers`. Run `file`, `readelf -hW`, `readelf -SW`, `readelf -sW`, `nm`, and `objdump -dM intel`. In GDB, break at `main` and at `add_three`; record the argument registers and stack pointer.

## Deliverables

Submit a one-page artifact sheet, a labeled process-memory sketch, and answers explaining why addresses vary while offsets inside one image remain stable. Do not read the writeups until the sheet is complete.

## Extension

Rebuild one program with symbols stripped and PIE enabled. List which observations disappeared and which can still be recovered from disassembly and relocation data.

