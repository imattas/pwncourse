from pathlib import Path
import re
import subprocess

result = subprocess.run([str(Path("challenge").resolve())], input=b"stage\n", capture_output=True, text=True, check=True)
leak = re.search(r"puts=(0x[0-9a-f]+)", result.stdout)
assert leak and int(leak.group(1), 16) > 0x1000
print("OBSERVED: libc-style pointer leak")
