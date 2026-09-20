# Lab 08 — Leaks and ret2libc

## Goal

Turn an information disclosure into reliable address arithmetic and a second-stage chain.

## Work

Start with `got-leak`. Identify the library, compare the tested libc, calculate a base from a known symbol, and assert alignment. Then combine the leak with a stack-control target using the chain `leak → restore input → calculate → second stage`.

## Deliverables

Submit the exact libc evidence, arithmetic, parser, and failure behavior for an impossible leak. Explain partial pointer reads and why a local hard-coded address is not a remote solution.

## Extension

Introduce a bad-byte constraint and choose an alternate leak or gadget path that survives it.

