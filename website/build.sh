#!/usr/bin/env bash
set -euo pipefail

root_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
out_dir="$root_dir/dist"
[[ "$out_dir" == "$root_dir/dist" ]] || { echo "unsafe output path" >&2; exit 1; }
rm -rf "$out_dir"
mkdir -p "$out_dir/course"
cp "$root_dir/website/index.html" "$root_dir/website/styles.css" "$root_dir/website/app.js" "$out_dir/"
cp "$root_dir/README.md" "$root_dir/COURSE.md" "$root_dir/LAB-INDEX.md" "$root_dir/SETUP-WSL.md" "$root_dir/REMOTE-TARGETS.md" "$out_dir/course/"
cp -r "$root_dir/modules" "$root_dir/labs" "$root_dir/reference" "$out_dir/course/"
touch "$out_dir/.nojekyll"
if command -v zip >/dev/null 2>&1; then
  (cd "$out_dir/course" && zip -qr "$out_dir/course.zip" modules labs reference README.md COURSE.md LAB-INDEX.md SETUP-WSL.md REMOTE-TARGETS.md)
else
  python3 "$root_dir/website/make-course-zip.py"
fi
printf 'Built GitHub Pages artifact at %s\n' "$out_dir"
