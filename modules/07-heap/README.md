# Stage 07 — heap exploitation

Treat the allocator as a state machine. For every allocation, record requested size, chunk size, neighboring metadata, bin/tcache state, and ownership. A use-after-free is not automatically an arbitrary write: prove what pointer remains, when it is reused, and which bytes are attacker-controlled.

The labs are version-pinned. Safe-linking and allocator changes are part of the lesson, so a failed solution should report the glibc profile rather than silently use an incompatible trick. Heap-to-control-flow chains should be written as `lifetime bug → metadata/pointer primitive → disclosure → target selection → final control`.

