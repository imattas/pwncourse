from pathlib import Path
import subprocess

commands = b"alloc\nfree\nedit\nreused-by-stale-pointer\nshow\nquit\n"
result = subprocess.run([str(Path("challenge").resolve())], input=commands, capture_output=True, text=True, check=True)
assert "item=reused-by-stale-pointer" in result.stdout
print("OBSERVED: menu UAF write/read")

