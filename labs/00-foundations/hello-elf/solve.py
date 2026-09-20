from pathlib import Path
import subprocess

result = subprocess.run([str(Path("challenge").resolve())], capture_output=True, text=True, check=True)
assert "ELF process" in result.stdout
print("flag{hello-elf}")
