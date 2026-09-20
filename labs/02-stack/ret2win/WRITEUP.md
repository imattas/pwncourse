# Writeup: ret2win

Root cause: `read` accepts 200 bytes into a 64-byte stack buffer. The saved return pointer is 72 bytes from the buffer start in the documented build.

Primitive: controlled saved RIP. Chain: input → 72-byte offset → `win` address → local success marker.

NX remains enabled, so no injected code is needed. The repair is to bound the read to `sizeof buffer` and check its return value. Reconfirm the offset with a cyclic pattern after changing compiler flags.

