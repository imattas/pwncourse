#!/usr/bin/env python3
"""Serve one local lab binary over TCP for remote-mode testing."""

from __future__ import annotations

import argparse
import socketserver
import subprocess
from pathlib import Path


class LabHandler(socketserver.BaseRequestHandler):
    binary: list[str]

    def handle(self) -> None:
        process = subprocess.Popen(self.binary, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        assert process.stdin is not None and process.stdout is not None
        self.request.settimeout(0.2)
        try:
            while True:
                try:
                    data = self.request.recv(4096)
                except TimeoutError:
                    data = b""
                if data:
                    process.stdin.write(data)
                    process.stdin.flush()
                output = process.stdout.read1(4096)
                if output:
                    self.request.sendall(output)
                if process.poll() is not None:
                    break
        finally:
            if process.poll() is None:
                process.terminate()
            process.wait(timeout=1)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("binary", type=Path)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=31337)
    args = parser.parse_args()
    handler = type("ConfiguredLabHandler", (LabHandler,), {"binary": [str(args.binary.resolve())]})
    with socketserver.ThreadingTCPServer((args.host, args.port), handler) as server:
        print(f"serving {args.binary} on {args.host}:{args.port}", flush=True)
        server.serve_forever()


if __name__ == "__main__":
    main()

