from __future__ import annotations

import os
from pathlib import Path
from typing import Any


def target_configuration() -> dict[str, Any]:
    if os.environ.get("PWN_REMOTE", "0") not in {"1", "true", "yes"}:
        return {"mode": "local"}
    host = os.environ.get("PWN_HOST", "127.0.0.1")
    port_text = os.environ.get("PWN_PORT")
    if not port_text:
        raise ValueError("PWN_PORT is required when PWN_REMOTE=1")
    try:
        port = int(port_text)
    except ValueError as exc:
        raise ValueError("PWN_PORT must be an integer") from exc
    if not 1 <= port <= 65535:
        raise ValueError("PWN_PORT must be between 1 and 65535")
    return {"mode": "remote", "host": host, "port": port}


def start_target(binary: str | Path, *, argv: list[str] | None = None):
    """Start the local challenge or connect to an authorized CTF instance.

    Remote mode is opt-in and configured only through PWN_REMOTE, PWN_HOST,
    and PWN_PORT. TLS, authentication, and challenge-specific handshakes stay
    in the individual lab because they are target contracts, not defaults.
    """
    from pwn import process, remote

    config = target_configuration()
    if config["mode"] == "remote":
        return remote(config["host"], config["port"])
    command = [str(Path(binary))]
    if argv:
        command.extend(argv)
    return process(command)
