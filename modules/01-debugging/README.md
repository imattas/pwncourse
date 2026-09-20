# Stage 01 — debugging and crash triage

A crash is evidence, not a solution. Use a cyclic pattern to determine which input bytes reached saved control data, then confirm the offset in GDB. Record registers, stack bytes, and the exact input path before writing a payload.

Suggested sequence: `crash-course` → `find-the-offset` → `bad-input`.

