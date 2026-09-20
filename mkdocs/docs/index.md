# PwnCourse

## Zero to master binary exploitation

Learn the reasoning loop behind a reliable exploit chain: inspect the artifact, prove the bug, obtain a primitive, compose a chain, automate it, and document the repair.

!!! warning "Authorized local labs only"
    Every binary in this course is intentionally vulnerable and designed for local WSL execution. Use remote mode only for an authorized CTF instance or the included localhost test server.

## Start the path

1. Complete [WSL setup](course/SETUP-WSL.md).
2. Read the [course map](course/COURSE.md).
3. Work through the [lab index](course/LAB-INDEX.md).
4. Download sources from each lab page under `downloads/labs/`.
5. Read a writeup only after you have your own crash, leak, or chain notes.

## The core promise

You will not only learn what ret2win, ROP, format strings, and heap bugs are. You will learn how to choose a primitive under mitigations, join multiple stages, validate assumptions, and explain every address and constraint.

## Flag format

All challenge success markers use the canonical format:

```text
flag{...}
```

