# ret2win

Objective: prove the saved return address offset and redirect execution to `win`.

Build with `make`, inspect `checksec --file=./challenge`, and use a cyclic pattern in GDB before reading the solution. The reference payload is `72 bytes of padding + address of win`.

