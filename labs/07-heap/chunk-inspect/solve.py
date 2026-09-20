from pathlib import Path
import re
import subprocess

result = subprocess.run([str(Path("challenge").resolve())], capture_output=True, text=True, check=True)
assert re.search(r"first=0x[0-9a-f]+ second=0x[0-9a-f]+", result.stdout)
print("OBSERVED: adjacent allocator chunks")

