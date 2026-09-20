from pathlib import Path


ROOT = Path(__file__).parents[1]


def test_course_contract_files_exist():
    expected = [
        "README.md",
        "COURSE.md",
        "SETUP-WSL.md",
        "glossary.md",
        "reference/mitigation-matrix.md",
        "scripts/check-env.sh",
        "scripts/build-all.sh",
        "scripts/test-all.sh",
        "scripts/reset-labs.sh",
    ]
    missing = [path for path in expected if not (ROOT / path).is_file()]
    assert not missing, f"missing course files: {missing}"


def test_shell_scripts_are_strict_mode_scripts():
    for path in (ROOT / "scripts").glob("*.sh"):
        content = path.read_text(encoding="utf-8")
        assert content.startswith("#!/usr/bin/env bash\nset -euo pipefail"), path

