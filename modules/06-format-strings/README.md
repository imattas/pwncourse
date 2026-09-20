# Stage 06 — format strings

`printf(user_input)` is both an information-disclosure and write primitive. First map positional arguments with harmless markers. Then classify each candidate as stack, register spill, libc, PIE, or user-controlled data. For writes, calculate width modulo the target integer size and split writes into ordered half-word operations only after proving the target and alignment.

Chain pattern: format-string reconnaissance → pointer leak → base calculation → controlled write or ROP. The writeup must state which bytes are printed, which bytes are consumed as addresses, and what happens if a newline appears early.

