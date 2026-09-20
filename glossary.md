# Glossary

- **ASLR:** randomizes mappings such as libc, stack, heap, and PIE base.
- **ELF:** Linux executable and object-file format.
- **GOT/PLT:** relocation table and call stubs used for dynamically linked functions.
- **NX:** non-executable data pages; pushes a chain toward existing code.
- **PIE:** position-independent executable; makes the main binary base-dependent.
- **Primitive:** a capability obtained from a bug, such as arbitrary read, write, or control flow.
- **ROP:** return-oriented programming; chaining existing instruction sequences.
- **RELRO:** relocation hardening; full RELRO makes the GOT read-only after loading.
- **SROP:** sigreturn-oriented programming; uses a crafted signal frame to set registers.
- **tcache:** per-thread allocator cache in modern glibc.

