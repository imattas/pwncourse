# Writeup: fmt-write

Root cause: attacker-controlled bytes reach `printf` as the format string. Primitive: arbitrary-width output plus `%hn` can update a chosen two-byte target once the positional argument and address layout are proven.

Chain: positional reconnaissance → target address disclosure → width calculation → `%hn` write → `auth == 0x1337`. Repair with `printf("%s", input)` and avoid exposing target addresses.

