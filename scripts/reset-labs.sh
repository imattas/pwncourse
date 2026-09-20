#!/usr/bin/env bash
set -euo pipefail

root_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
find "$root_dir/labs" -type d -name build -prune -exec rm -rf {} +
find "$root_dir/labs" -type f \( -name core -o -name challenge -o -name '*.o' \) -delete
printf 'Removed generated lab artifacts beneath %s/labs.\n' "$root_dir"
