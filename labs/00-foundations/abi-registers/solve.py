from pathlib import Path
import subprocess

result = subprocess.run([str(Path("challenge").resolve())], capture_output=True, text=True, check=True)
assert "sum=42" in result.stdout
print("flag{abi-registers}")
