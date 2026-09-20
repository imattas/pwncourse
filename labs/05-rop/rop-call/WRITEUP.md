# Writeup: rop-call

Root cause: stack overflow controls RIP. Chain: 72-byte offset → register-loading gadget → `0x42424242` in RDI → target. The explicit gadget keeps the lesson deterministic. Repair the read bound and retain NX as defense in depth.

