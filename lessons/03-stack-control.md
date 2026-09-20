# Lesson 3 — Stack control and ret2win

Once saved control data is reachable, the task becomes constrained data placement: preserve the exact offset, satisfy the ABI, and redirect execution to a useful function. This is where ret2win, ret2arg, and split-input payloads become understandable rather than copied recipes.

## Lab package

Solve `labs/02-stack/ret2win`, `ret2arg`, and `split-input`. Start with a direct return overwrite, then add a controlled argument and finally satisfy a target that reads a second input. Compare a working payload with a failed one and explain the difference in stack alignment and input lifetime.

**Exit test:** derive all payload fields from the binary and ABI, with no hard-coded guess left unexplained.
