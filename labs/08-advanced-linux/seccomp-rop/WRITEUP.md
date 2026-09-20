# Writeup: seccomp-rop

The fixture enables `PR_SET_NO_NEW_PRIVS`, a process property relevant to sandbox design, but does not install a restrictive filter. Primitive: observation of a constraint boundary, not code execution.

Chain: process setup → syscall trace → allowed-operation inventory → constrained-chain design. The safe extension is to add a local, documented filter and update the syscall inventory.

