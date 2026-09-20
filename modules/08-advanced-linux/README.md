# Stage 08 — advanced Linux constraints

Seccomp turns a successful control-flow hijack into a syscall-planning problem. SROP uses a kernel-restored signal frame to set many registers at once. Dynamic-linker behavior explains why some resolution paths survive full RELRO. These topics are taught through local fixtures and defensive reasoning, not against third-party services.

Before attempting a chain, enumerate allowed syscalls, writable memory, available code, signal-frame layout, and the exact success condition. An advanced chain is credible only when each constraint is demonstrated.

