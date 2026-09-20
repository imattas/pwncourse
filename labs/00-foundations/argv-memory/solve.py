from pathlib import Path
import subprocess

result = subprocess.run([str(Path("challenge").resolve()), "alpha"], capture_output=True, text=True, check=True)
assert "argc=2" in result.stdout
assert "stack=0x" in result.stdout
print("flag{argv-memory}")
