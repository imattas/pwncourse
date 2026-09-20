# PwnCourse: zero to master

An offline, WSL-first binary exploitation course built around intentionally vulnerable local programs. The course teaches the full reasoning loop: inspect the artifact, prove the bug, obtain a primitive, compose an exploit chain, automate it, and document the repair.

## Start here

```bash
cd ~/pwncourse
bash scripts/check-env.sh
bash scripts/build-all.sh
bash scripts/test-all.sh
```

Then open [`COURSE.md`](COURSE.md), begin with `modules/00-foundations`, and work through the lab README before reading its `WRITEUP.md`.

The complete inventory is in [`LAB-INDEX.md`](LAB-INDEX.md).

Remote CTF support is documented in [`REMOTE-TARGETS.md`](REMOTE-TARGETS.md). Local mode is always the default.

## Scope

Everything in this repository targets local challenge binaries or explicitly authorized CTF environments. Nothing here requires a real third-party target, persistence, stealth, credential theft, or host-kernel modification.

## Evidence labels

- **Build proof:** the source compiles with the documented flags.
- **Harness proof:** the reference solution reaches the local lab success marker.
- **Learner proof:** you can reproduce the reasoning in GDB and explain every address, offset, and constraint.

The first two are automated. The third is deliberately yours.
