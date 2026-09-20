# fmt-read

Objective: prove that user bytes are interpreted as a format string. Start with literal text, then try `%p` and positional probes. Record which values are stable and which are artifacts of the current process.

The reference solution demonstrates disclosure only. A later exercise asks you to identify a write target in a separate fixture rather than guessing from this one.

