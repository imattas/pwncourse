# Lesson 8 — ret2libc and remote reliability

ret2libc is a complete exploit chain: disclose a known libc symbol, calculate the base, resolve useful symbols, satisfy the ABI, and invoke a stable primitive. Reliability comes from parsing the protocol and validating every derived address.

## Lab package

Use `labs/04-libc/got-leak` and the ret2libc track. First leak a GOT entry, then calculate libc base and call a libc function with a controlled argument. Run the chain repeatedly against the local process and record how buffering, line endings, and delayed output affect the parser.

**Exit test:** the script fails loudly on a malformed leak instead of sending a guessed second-stage payload.
