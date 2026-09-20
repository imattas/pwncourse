# Writeup: crash-course

Root cause: 128 bytes are read into a 32-byte stack buffer. Primitive: memory corruption with an initially unknown control-data offset. Prove the offset with a cyclic pattern and inspect saved RIP in GDB. Repair by bounding the read to `sizeof buffer`.

