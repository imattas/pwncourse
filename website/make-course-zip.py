from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


dist = Path(__file__).resolve().parents[1] / "dist"
root = dist / "course" if (dist / "course").is_dir() else dist / "downloads"
output = dist / "course.zip"
with ZipFile(output, "w", ZIP_DEFLATED) as archive:
    for path in root.rglob("*"):
        if path.is_file():
            archive.write(path, path.relative_to(root).as_posix())
print(output)
