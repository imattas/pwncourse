#!/usr/bin/env bash
set -euo pipefail

required=(gcc make python3 gdb readelf objdump file)
missing=0
for command_name in "${required[@]}"; do
  if ! command -v "$command_name" >/dev/null 2>&1; then
    printf 'MISSING: %s\n' "$command_name"
    missing=1
  fi
done

if command -v checksec >/dev/null 2>&1; then
  printf 'OK: checksec\n'
else
  printf 'MISSING: checksec\n'
  missing=1
fi

if python3 -c 'import pwn' >/dev/null 2>&1; then
  printf 'OK: pwntools\n'
else
  printf 'MISSING: pwntools (install with python3 -m pip install pwntools)\n'
  missing=1
fi

if [[ "$missing" -ne 0 ]]; then
  exit 1
fi
printf 'Environment ready for local labs.\n'
