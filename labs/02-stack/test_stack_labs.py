from pathlib import Path
import shutil

import pytest


ROOT = Path(__file__).parent


@pytest.mark.parametrize("name", ["ret2win", "ret2arg", "split-input"])
def test_stack_lab_contract(name):
    lab = ROOT / name
    for filename in ("challenge.c", "Makefile", "README.md", "WRITEUP.md", "solve.py"):
        assert (lab / filename).is_file(), f"{name} missing {filename}"


@pytest.mark.skipif(shutil.which("gcc") is None, reason="run inside WSL with gcc")
@pytest.mark.parametrize("name", ["ret2win", "ret2arg", "split-input"])
def test_stack_solution(name):
    from labs.common.test_support import build_lab, run_solution
    lab = ROOT / name
    build_lab(lab)
    result = run_solution(lab)
    assert result.returncode == 0, result.stderr
    assert f"flag{{{name}}}" in result.stdout
