# seccomp-rop

Objective: distinguish `no_new_privs` from a syscall filter and learn to enumerate constraints before designing a chain. This fixture deliberately does not install a host-affecting filter.

Use `strace -f ./challenge` and list the syscalls needed for startup, output, and exit. The exercise is planning, not a claim that a full sandbox escape is implemented here.

