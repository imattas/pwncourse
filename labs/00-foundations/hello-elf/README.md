# hello-elf

Build the program, identify its architecture, inspect the ELF header, and locate `main` with `nm` or `objdump`.

```bash
make
file ./challenge
readelf -h ./challenge
nm -C ./challenge | grep main
gdb -q ./challenge
```

The solution only proves that the local binary runs. Your learner proof is the inspection notebook.

