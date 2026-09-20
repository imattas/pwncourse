from pathlib import Path


ROOT = Path(__file__).parents[1]


def test_mkdocs_site_contract_exists():
    for filename in ("mkdocs.yml", "mkdocs/build.sh", "mkdocs/requirements.txt", "mkdocs/docs/index.md", ".github/workflows/pages.yml"):
        assert (ROOT / filename).is_file(), filename


def test_mkdocs_config_exposes_course_sections():
    config = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
    assert "Lessons:" in config
    assert config.count("course/lessons/") == 12
    assert "course/chapters/" not in config
    assert "course/labs/tracks/" not in config
    assert "course/reference/" not in config


def test_course_chapters_are_substantive():
    chapters = list((ROOT / "chapters").glob("*.md"))
    assert len(chapters) == 7
    for chapter in chapters:
        assert len(chapter.read_text(encoding="utf-8").splitlines()) >= 50, chapter


def test_course_has_twelve_combined_lesson_sources():
    lessons = list((ROOT / "lessons").glob("*.md"))
    assert len(lessons) == 12
    for lesson in lessons:
        content = lesson.read_text(encoding="utf-8")
        assert "## Lab package" in content, lesson
        assert "**Exit test:**" in content, lesson


def test_twelve_lab_tracks_are_substantive():
    tracks = list((ROOT / "labs" / "tracks").glob("*.md"))
    assert len(tracks) == 12
    for track in tracks:
        assert len(track.read_text(encoding="utf-8").splitlines()) >= 12, track
