# heap-leak-chain

Objective: compose a lifetime bug with a same-size reuse and a function-pointer overwrite. The program frees an object, obtains a replacement at the reused size, and reads attacker-controlled bytes into the replacement.

The chain is `freed object → reuse → controlled callback pointer → win`. The printed heap address is evidence for analysis; the local solution resolves `win` from the ELF rather than guessing an address.

