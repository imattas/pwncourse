from pathlib import Path
import re
import subprocess

result = subprocess.run([str(Path("challenge").resolve())], capture_output=True, text=True, check=True)
addresses = re.findall(r"0x[0-9a-f]+", result.stdout)
assert len(addresses) == 2 and addresses[0] == addresses[1]
print("OBSERVED: same-size allocation reuse")

