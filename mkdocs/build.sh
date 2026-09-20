#!/usr/bin/env bash
set -euo pipefail

root_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
docs_dir="$root_dir/mkdocs/docs/course"
dist_dir="$root_dir/dist"
[[ "$docs_dir" == "$root_dir/mkdocs/docs/course" ]] || { echo "unsafe docs path" >&2; exit 1; }
rm -rf "$docs_dir" "$dist_dir"
mkdir -p "$docs_dir"
cp "$root_dir/README.md" "$root_dir/COURSE.md" "$root_dir/LAB-INDEX.md" "$root_dir/SETUP-WSL.md" "$root_dir/REMOTE-TARGETS.md" "$docs_dir/"
cp -r "$root_dir/modules" "$root_dir/labs" "$root_dir/reference" "$root_dir/capstones" "$docs_dir/"
python -m mkdocs build --strict --config-file "$root_dir/mkdocs.yml" --site-dir "$dist_dir"
mkdir -p "$dist_dir/downloads"
cp -r "$root_dir/labs" "$root_dir/modules" "$root_dir/reference" "$root_dir/capstones" "$dist_dir/downloads/"
python3 "$root_dir/website/make-course-zip.py"
printf 'Built MkDocs site at %s\n' "$dist_dir"
