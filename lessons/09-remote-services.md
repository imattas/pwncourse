# Lesson 9 — Localhost socket services

CTF remotes add a protocol boundary, not magical exploitation. The course uses localhost daemons so you can practice connection lifecycle, prompt synchronization, timeouts, retries, and clean separation between target logic and exploit logic.

## Lab package

Start the service with `scripts/serve-lab.sh` for the remote-services track, then connect with the same pwntools script using `HOST=127.0.0.1` and the printed port. Test a fresh connection for each run and inspect the server log only to diagnose transport problems, not to obtain hidden target state.

**Exit test:** one exploit supports `MODE=local` and `MODE=remote` without changing the payload-building code.
