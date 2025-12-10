#!/usr/bin/env python3
"""Lightweight dev server for the MuseDash frontend with basic API hooks."""

import argparse
import json
import os
import subprocess
import sys
import urllib.parse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
QUARTUS_QSF = ROOT / "quartus" / "MuseDash.qsf"


def _open_with_system(path: Path):
    """Open a file with the OS default handler."""
    if not path.exists():
        return False, f"{path} not found"
    try:
        if sys.platform.startswith("win"):
            os.startfile(path)  # type: ignore[attr-defined]
        elif sys.platform == "darwin":
            subprocess.Popen(["open", str(path)])
        else:
            subprocess.Popen(["xdg-open", str(path)])
        return True, f"launched {path.name}"
    except Exception as exc:  # pragma: no cover - best effort helper
        return False, str(exc)


class FrontendHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == "/quartus/open":
            self._handle_open_quartus()
            return
        if parsed.path == "/chart_engine/process":
            self._respond_json({"success": True, "message": "process stub"})
            return
        if parsed.path == "/chart_engine/generate_random":
            self._respond_json({"success": True, "message": "generate_random stub"})
            return
        self.send_error(404, "Unknown POST endpoint")

    def _handle_open_quartus(self):
        ok, msg = _open_with_system(QUARTUS_QSF)
        status = 200 if ok else 500
        self._respond_json({"success": ok, "message": msg}, status=status)

    def _respond_json(self, payload, status=200):
        data = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


def run_server(host: str, port: int):
    handler_cls = partial(FrontendHandler, directory=str(ROOT))
    httpd = ThreadingHTTPServer((host, port), handler_cls)
    print(f"Serving {ROOT} on http://{host}:{port}")
    httpd.serve_forever()


def main():
    parser = argparse.ArgumentParser(description="Serve frontend with simple API helpers")
    parser.add_argument("--host", default="127.0.0.1", help="Bind address (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=8000, help="Port to listen on (default: 8000)")
    args = parser.parse_args()
    run_server(args.host, args.port)


if __name__ == "__main__":
    main()
