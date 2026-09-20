from pathlib import Path
import subprocess

result = subprocess.run([str(Path("challenge").resolve())], input=b"A" * 128, capture_output=True)
assert result.returncode != 0
print("OBSERVED: controlled overflow crash")

