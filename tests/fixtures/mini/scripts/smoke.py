"""Smoke test: drives the CLI mode against a temporary home."""
import json
import os
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DLL = Path(os.environ.get("MINI_TEST_DLL", ROOT / "bin/Release/net8.0/Mini.dll"))


def run(op, *args):
    return subprocess.run(["dotnet", str(DLL), "cli", op, *args], capture_output=True, text=True,
                          env=dict(os.environ, APP_HOME="tmp-home"))


def cli(op, *args):
    return json.loads(run(op, *args).stdout)


if __name__ == "__main__":
    assert cli("list") == []
    cli("notes.add", "hi")
    print(cli("get", "1"))
