# Writeup: hello-elf

There is no vulnerability here. The learning primitive is observation: ELF metadata and symbols provide evidence about what will execute.

Chain: source → compiler → ELF header/symbols → process entry point.

`file` identifies architecture, `readelf -h` shows ELF class and machine, and `nm` exposes the non-stripped `main` symbol. Rebuild stripped and compare the evidence.

