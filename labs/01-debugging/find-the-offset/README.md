# find-the-offset

Use `cyclic 200` or `pwn cyclic 200`, feed it to the binary under GDB, inspect the overwritten value, and use `cyclic -l <value>` to recover the offset. Do not assume the offset equals buffer size.

