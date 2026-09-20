from pathlib import Path


ROOT = Path(__file__).parents[1]
LABS = [
    "labs/07-heap/chunk-inspect",
    "labs/07-heap/tcache-reuse",
    "labs/07-heap/heap-leak-chain",
]


def test_heap_progression_contracts_exist():
    for relative in LABS:
        lab = ROOT / relative
        for filename in ("challenge.c", "Makefile", "README.md", "WRITEUP.md", "solve.py"):
            assert (lab / filename).is_file(), f"{relative} missing {filename}"

