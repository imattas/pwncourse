# argv-memory

Observe that arguments and local variables occupy process memory. Run the program repeatedly, compare addresses, and confirm the frame in GDB.

```bash
make
./challenge alpha
gdb -q ./challenge
```

Questions: which value is a pointer, which is an integer, and why can the address change between runs?

