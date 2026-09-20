# Lesson 7 — ROP chain engineering

When NX prevents injected code, existing instructions become a programmable vocabulary. ROP requires a chain model: stack words, gadget side effects, ABI alignment, bad-byte constraints, and a final call that has a clear postcondition.

## Lab package

Solve `labs/05-rop/rop-call`. Enumerate gadgets, build a register-loading chain, check stack alignment, and make the chain call the target function. Then remove one convenient gadget and redesign the chain around what remains.

**Exit test:** draw the stack after each `ret` and predict the register state before the final call.
