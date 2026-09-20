#!/usr/bin/env bash
set -euo pipefail

root_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
docs_dir="$root_dir/mkdocs/docs/course"
dist_dir="$root_dir/dist"
[[ "$docs_dir" == "$root_dir/mkdocs/docs/course" ]] || { echo "unsafe docs path" >&2; exit 1; }
rm -rf "$docs_dir" "$dist_dir"
mkdir -p "$docs_dir/lessons"
cp "$root_dir/SETUP-WSL.md" "$docs_dir/"

lesson() {
  local slug="$1" chapter="$2" track="$3" challenge="$4"
  {
    cat "$root_dir/lessons/$slug.md"
    printf '\n\n---\n\n'
    cat "$root_dir/$chapter"
    printf '\n\n---\n\n'
    cat "$root_dir/$track"
    cat <<EOF

## Downloads and localhost remote

- [Download the complete course](https://pwncourse.zemi.gg/downloads/course.zip)
- [Challenge README](https://pwncourse.zemi.gg/downloads/$challenge/README.md)
- [Challenge source](https://pwncourse.zemi.gg/downloads/$challenge/challenge.c)
- [Starter exploit](https://pwncourse.zemi.gg/downloads/$challenge/solve.py)

To run this challenge as a local TCP service from the downloaded course directory:

\`\`\`bash
bash scripts/serve-lab.sh $challenge/challenge 31337
\`\`\`

In a second WSL terminal, point the exploit at that localhost service:

\`\`\`bash
PWN_REMOTE=1 PWN_HOST=127.0.0.1 PWN_PORT=31337 python3 $challenge/solve.py
\`\`\`

Stop the server with Ctrl-C when finished. The service is intentionally bound to localhost.
EOF
  } > "$docs_dir/lessons/$slug.md"
}

lesson 01-foundations chapters/01-foundations.md labs/tracks/01-warmup-and-elf.md labs/00-foundations/hello-elf
lesson 02-debugging chapters/01-foundations.md labs/tracks/02-gdb-and-x86.md labs/01-debugging/find-the-offset
lesson 03-stack-control chapters/02-stack-overflows.md labs/tracks/03-first-stack-overflow.md labs/02-stack/ret2arg
lesson 04-pwntools chapters/02-stack-overflows.md labs/tracks/04-pwntools.md labs/02-stack/ret2win
lesson 05-mitigations chapters/03-mitigations-and-leaks.md labs/tracks/05-stack-protections.md labs/04-libc/got-leak
lesson 06-format-strings chapters/05-format-strings.md labs/tracks/06-format-strings.md labs/06-format-string/fmt-read
lesson 07-rop chapters/04-rop-and-ret2libc.md labs/tracks/07-rop.md labs/05-rop/rop-call
lesson 08-ret2libc chapters/04-rop-and-ret2libc.md labs/tracks/08-ret2libc.md labs/04-libc/got-leak
lesson 09-remote-services chapters/07-advanced-chains.md labs/tracks/09-remote-services.md labs/05-rop/rop-call
lesson 10-heap chapters/06-heap-exploitation.md labs/tracks/10-heap-fundamentals.md labs/07-heap/uaf
lesson 11-advanced-heap chapters/06-heap-exploitation.md labs/tracks/11-advanced-heap.md labs/07-heap/heap-leak-chain
lesson 12-capstone chapters/07-advanced-chains.md labs/tracks/12-sandbox-capstone.md labs/08-advanced-linux/seccomp-rop
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
mkdir -p "$dist_dir/downloads/scripts"
cp "$root_dir/scripts/serve-lab.sh" "$root_dir/scripts/serve-lab.py" "$dist_dir/downloads/scripts/"
cp "$root_dir/CNAME" "$dist_dir/CNAME"
"${python_cmd[@]}" "$zip_script"
cp "$dist_dir/course.zip" "$dist_dir/downloads/course.zip"
printf 'Built MkDocs site at %s\n' "$dist_dir"
