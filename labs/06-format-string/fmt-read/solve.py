from pathlib import Path
import subprocess

result = subprocess.run([str(Path("challenge").resolve())], input=b"marker=%p\n", capture_output=True, check=True)
assert b"marker=0x" in result.stdout
print("flag{fmt-read}")
