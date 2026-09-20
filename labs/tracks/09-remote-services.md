# Lab 09 — Remote services

## Goal

Make a local exploit behave like a CTF network service.

## Work

Start `scripts/serve-lab.sh` for a local binary. Run the same pwntools solution with `PWN_REMOTE=1`, `PWN_PORT=31337`, and the default localhost host. Replace sleeps with prompt synchronization, bound all receives, and make EOF a visible failure.

## Deliverables

Submit local-process and TCP transcripts, a timeout policy, and a paragraph describing which assumptions belong to the service protocol rather than the binary.

## Extension

Add a banner and a reconnect loop to the fixture. Keep the exploit authorized and local; do not scan for or target unrelated hosts.

