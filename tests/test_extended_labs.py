from pathlib import Path


ROOT = Path(__file__).parents[1]
LABS = [
    "labs/01-debugging/crash-course",
    "labs/01-debugging/find-the-offset",
    "labs/04-libc/got-leak",
    "labs/05-rop/rop-call",
    "labs/06-format-string/fmt-write",
    "labs/07-heap/menu-uaf",
]


def test_extended_lab_contracts_exist():
    for relative in LABS:
        lab = ROOT / relative
        assert lab.is_dir(), relative
        for filename in ("challenge.c", "Makefile", "README.md", "WRITEUP.md", "solve.py"):
            assert (lab / filename).is_file(), f"{relative} missing {filename}"

