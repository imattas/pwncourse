from pathlib import Path


ROOT = Path(__file__).parents[1]


def test_mkdocs_site_contract_exists():
    for filename in ("mkdocs.yml", "mkdocs/build.sh", "mkdocs/requirements.txt", "mkdocs/docs/index.md", ".github/workflows/pages.yml"):
        assert (ROOT / filename).is_file(), filename


def test_mkdocs_config_exposes_course_sections():
    config = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
    for label in ("Course chapters", "Labs and downloads", "References"):
        assert label in config


def test_course_chapters_are_substantive():
    chapters = list((ROOT / "chapters").glob("*.md"))
    assert len(chapters) == 7
    for chapter in chapters:
        assert len(chapter.read_text(encoding="utf-8").splitlines()) >= 50, chapter


def test_twelve_lab_tracks_are_substantive():
    tracks = list((ROOT / "labs" / "tracks").glob("*.md"))
    assert len(tracks) == 12
    for track in tracks:
        assert len(track.read_text(encoding="utf-8").splitlines()) >= 12, track
