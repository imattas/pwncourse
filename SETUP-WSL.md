# WSL setup

Use WSL2 with Ubuntu 22.04 or 24.04. Keep the repository inside the Linux filesystem for predictable permissions and faster builds.

```bash
sudo apt update
sudo apt install -y build-essential gdb binutils checksec python3 python3-venv python3-pip strace ltrace file
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip pwntools pytest
```

Install either pwndbg or GEF using its official installer, then verify:

```bash
python3 --version
gcc --version
gdb --version
python3 -c 'from pwn import context; context.arch="amd64"; print("pwntools: ok")'
bash scripts/check-env.sh
```

If `checksec` is not found after installing it, use `checksec --file=./challenge` from a lab after installing the Ubuntu package or the upstream script. Do not run challenge binaries with `sudo`; the labs are designed for an unprivileged local user.

## Windows/WSL path note

From PowerShell, enter WSL with `wsl`. From WSL, use `/home/<user>/pwncourse`, not `/mnt/c/...`, for the lab tree.

