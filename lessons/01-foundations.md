# Lesson 1 — ELF, memory, and the ABI

This lesson establishes the evidence-first workflow: identify the executable, map its memory, understand the x86-64 calling convention, and make an address observation reproducible.

## Lab package

Work in `labs/00-foundations` with `hello-elf`, `argv-memory`, and `abi-registers`. Build with `make`, inspect with `file`, `checksec`, `readelf`, and `objdump`, then use GDB to record argument registers and mappings. The lab writeups are beside each challenge; do not open them until your artifact sheet is complete.

**Exit test:** explain one input-to-memory path and why an ASLR-changing address can still have a stable image-relative offset.
