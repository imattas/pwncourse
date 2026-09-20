#!/usr/bin/env bash
set -euo pipefail

root_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
status=0
while IFS= read -r makefile; do
  lab_dir="$(dirname "$makefile")"
  printf '\n==> %s\n' "${lab_dir#"$root_dir"/}"
  if ! (cd "$lab_dir" && make clean all); then
    status=1
  fi
done < <(find "$root_dir/labs" -name Makefile -not -path '*/common/*' -print | sort)
exit "$status"
