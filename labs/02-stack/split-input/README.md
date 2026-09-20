# split-input

Objective: understand that a chain can be staged across multiple reads. The first input is bounded and becomes a note; the second input contains the vulnerable overwrite.

Use `recvuntil` on prompts rather than sleeping. The reference solution demonstrates synchronization before sending each stage.

