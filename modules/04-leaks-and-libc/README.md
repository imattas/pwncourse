# Stage 04 — leaks, bases, and libc chains

A leaked pointer is useful only after you identify its mapping and a stable offset. The standard chain is: obtain a code pointer → normalize its bytes → subtract a symbol offset → validate page alignment → derive a second address → return to a controlled read or final function.

Never hard-code a remote address. In a local lab, record `ldd ./challenge`, the glibc build, the leaked symbol, and the arithmetic that turns the leak into a base. Treat newline truncation and partial pointer leaks as first-class constraints.

Exercises: leak a GOT entry, calculate libc base, return to `read` for a second stage, and add an assertion that rejects an impossible base.

