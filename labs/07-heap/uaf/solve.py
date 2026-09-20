from pathlib import Path
import subprocess

result = subprocess.run([str(Path("challenge").resolve())], capture_output=True, text=True, check=True)
assert "stale-view=replacement" in result.stdout
print("flag{uaf}")
