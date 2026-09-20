# Lab 05 — Stack protections

## Goal

Make mitigation output drive exploit planning.

## Work

Rebuild a stack lab with combinations of canary, PIE, NX, and RELRO. For each build, write the original chain, the exact reason it fails, the missing primitive, and the smallest next experiment. Use GDB to inspect the canary check and `readelf` to confirm PIE.

## Deliverables

Complete a mitigation matrix and patch at least one bug. Your report must distinguish “the process crashed” from “the mitigation blocked the intended control-flow path.”

## Extension

Find a non-contiguous or information-disclosure path that survives the canary, then explain why it is a different primitive rather than a canary bypass by magic.

