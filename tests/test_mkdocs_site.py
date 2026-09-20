from pathlib import Path


ROOT = Path(__file__).parents[1]


def test_mkdocs_site_contract_exists():
    for filename in ("mkdocs.yml", "mkdocs/build.sh", "mkdocs/requirements.txt", "mkdocs/docs/index.md", ".github/workflows/pages.yml"):
        assert (ROOT / filename).is_file(), filename


def test_mkdocs_config_exposes_course_sections():
    config = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
    for label in ("Foundations", "Stack Control", "Heap", "Capstones"):
        assert label in config

