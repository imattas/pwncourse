from __future__ import annotations

from pathlib import Path
import subprocess
import sys


def lab_dir(file: str) -> Path:
    return Path(file).resolve().parent


def build_lab(path: Path) -> None:
    subprocess.run(["make", "clean", "all"], cwd=path, check=True, text=True)


def run_solution(path: Path, timeout: float = 3.0) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(path / "solve.py")], cwd=path, capture_output=True, text=True, timeout=timeout, check=False)

