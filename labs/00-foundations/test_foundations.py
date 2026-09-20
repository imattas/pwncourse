from pathlib import Path
import shutil

import pytest

from labs.common.test_support import build_lab, run_solution


ROOT = Path(__file__).parent


@pytest.mark.parametrize("name", ["hello-elf", "argv-memory", "abi-registers"])
def test_foundation_lab_has_contract(name):
    lab = ROOT / name
    for filename in ("challenge.c", "Makefile", "README.md", "WRITEUP.md", "solve.py"):
        assert (lab / filename).is_file(), f"{name} missing {filename}"


@pytest.mark.skipif(shutil.which("gcc") is None, reason="run inside WSL with gcc")
@pytest.mark.parametrize("name", ["hello-elf", "argv-memory", "abi-registers"])
def test_foundation_solution_reaches_flag(name):
    lab = ROOT / name
    build_lab(lab)
    result = run_solution(lab)
    assert result.returncode == 0, result.stderr
    assert f"flag{{{name}}}" in result.stdout
