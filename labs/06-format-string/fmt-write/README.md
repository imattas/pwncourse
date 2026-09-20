# fmt-write

Objective: turn format-string reconnaissance into a controlled write. First find the positional argument index with harmless markers, then use `%hn` to write `0x1337` to the disclosed `auth` address. Account for output width modulo 16 bits and newline/input placement.

This is a learner-driven lab: the starter intentionally does not guess a platform-specific stack index.

