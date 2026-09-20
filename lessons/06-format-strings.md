# Lesson 6 — Format-string exploitation

Variadic formatting bugs provide two families of primitives: reads from unintended argument positions and writes through `%n`. The hard part is indexing, byte-count accounting, and choosing a target whose update survives the rest of the program.

## Lab package

Work through `labs/06-format-string/fmt-read` and `fmt-write`. Find the format offset, leak a stack or image pointer, then perform a controlled partial write. Confirm every write in memory before attempting the final control-flow effect, and document why width/precision changes the byte count.

**Exit test:** produce a minimal format payload and explain its positional arguments and write order.
