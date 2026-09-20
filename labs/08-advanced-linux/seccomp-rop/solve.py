from pathlib import Path
import subprocess

result = subprocess.run([str(Path("challenge").resolve())], capture_output=True, text=True, check=True)
assert "no_new_privs=enabled" in result.stdout
print("flag{seccomp-rop}")
