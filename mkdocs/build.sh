#!/usr/bin/env bash
set -euo pipefail

root_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
docs_dir="$root_dir/mkdocs/docs/course"
dist_dir="$root_dir/dist"
[[ "$docs_dir" == "$root_dir/mkdocs/docs/course" ]] || { echo "unsafe docs path" >&2; exit 1; }
rm -rf "$docs_dir" "$dist_dir"
mkdir -p "$docs_dir"
cp "$root_dir/COURSE.md" "$root_dir/LAB-INDEX.md" "$root_dir/SETUP-WSL.md" "$root_dir/REMOTE-TARGETS.md" "$docs_dir/"
cp -r "$root_dir/chapters" "$root_dir/reference" "$docs_dir/"
mkdir -p "$docs_dir/labs/tracks"
cp "$root_dir/labs/tracks"/*.md "$docs_dir/labs/tracks/"
if command -v py.exe >/dev/null 2>&1 && command -v cygpath >/dev/null 2>&1 && py.exe -c 'import mkdocs' >/dev/null 2>&1; then
  python_cmd=(py.exe)
  config_path="$(cygpath -w "$root_dir/mkdocs.yml")"
  site_path="$(cygpath -w "$dist_dir")"
  zip_script="$(cygpath -w "$root_dir/website/make-course-zip.py")"
else
  python_cmd=(python3)
  config_path="$root_dir/mkdocs.yml"
  site_path="$dist_dir"
  zip_script="$root_dir/website/make-course-zip.py"
fi
"${python_cmd[@]}" -m mkdocs build --strict --config-file "$config_path" --site-dir "$site_path"
mkdir -p "$dist_dir/downloads"
cp -r "$root_dir/chapters" "$root_dir/labs" "$root_dir/modules" "$root_dir/reference" "$root_dir/capstones" "$dist_dir/downloads/"
"${python_cmd[@]}" "$zip_script"
printf 'Built MkDocs site at %s\n' "$dist_dir"
