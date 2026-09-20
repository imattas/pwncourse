#!/usr/bin/env bash
set -euo pipefail

if [[ "$#" -lt 1 || "$#" -gt 3 ]]; then
  printf 'usage: %s /path/to/challenge [port] [host]\n' "$0" >&2
  exit 2
fi
binary="$1"
port="${2:-31337}"
host="${3:-127.0.0.1}"
python3 "$(dirname "$0")/serve-lab.py" "$binary" --host "$host" --port "$port"
