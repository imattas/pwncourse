# Stage 09 — kernel exploitation foundations

This stage models the boundary without loading a module or touching the host kernel. Study copy-in/copy-out, integer truncation, object lifetime, ioctl-like request handling, and the difference between a user pointer and a kernel-owned buffer inside the supplied toy fixture.

The learning target is threat modeling: identify trust transitions, state which primitive a bug would provide, and write a safe fix. Real kernel exploitation requires a separately isolated research environment and is outside this repository's execution contract.

