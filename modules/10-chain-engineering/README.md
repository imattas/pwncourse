# Stage 10 — exploit-chain engineering

An exploit chain is a dependency graph, not a magic string. Write each node as `primitive`, each edge as `data/control dependency`, and each terminal as a measured success condition. Then add assertions for architecture, prompt, leak shape, base alignment, writable target, and final output.

Recommended chain worksheet:

| Stage | Primitive | Input constraint | Evidence | Next dependency |
|---|---|---|---|---|
| 1 | leak | newline-safe pointer | parsed, page-aligned | image base |
| 2 | address math | known symbol offset | asserted base | gadget addresses |
| 3 | control | stack offset/alignment | RIP/register proof | second stage |
| 4 | final effect | local success marker | repeated runs | writeup |

