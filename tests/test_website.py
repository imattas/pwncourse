from pathlib import Path


ROOT = Path(__file__).parents[1]


def test_website_shell_exists():
    for filename in ("website/index.html", "website/styles.css", "website/app.js", "website/build.sh", ".github/workflows/pages.yml"):
        assert (ROOT / filename).is_file(), filename


def test_website_mentions_downloadable_course_surfaces():
    html = (ROOT / "website/index.html").read_text(encoding="utf-8")
    assert "Download" in html
    assert "Labs" in html
    assert "WSL" in html
    assert "flag{" in html

