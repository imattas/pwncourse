from pathlib import Path
import re


ROOT = Path(__file__).parents[1]


def test_all_course_stages_have_lessons():
    for stage in range(11):
        matches = list((ROOT / "modules").glob(f"{stage:02d}-*/README.md"))
        assert matches, f"missing lesson for stage {stage:02d}"


def test_each_included_lab_has_writeup_and_solution():
    labs = [path for path in (ROOT / "labs").glob("**/challenge.c") if "common" not in path.parts]
    assert len(labs) >= 6
    for source in labs:
        assert (source.parent / "README.md").is_file(), source
        assert (source.parent / "WRITEUP.md").is_file(), source
        assert (source.parent / "solve.py").is_file(), source


def test_docs_do_not_leave_template_placeholders():
    files = list((ROOT / "modules").glob("**/*.md")) + list((ROOT / "reference").glob("*.md")) + list((ROOT / "labs").glob("**/*.md"))
    forbidden = ("TBD", "TODO", "implement later")
    for path in files:
        text = path.read_text(encoding="utf-8").lower()
        assert not any(token.lower() in text for token in forbidden), path


def test_all_success_markers_use_flag_braces():
    files = list((ROOT / "labs").glob("**/*.c")) + list((ROOT / "labs").glob("**/*.py"))
    for path in files:
        text = path.read_text(encoding="utf-8")
        assert "FLAG:" not in text, path
        for marker in re.findall(r"flag\{[^\r\n{}]+\}", text):
            assert marker.startswith("flag{") and marker.endswith("}"), (path, marker)
