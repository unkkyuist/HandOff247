"""Per-language analyzers. Each takes a FileInfo (text already loaded) and appends Facts."""
from __future__ import annotations

from ..model import Fact, FileInfo
from . import csharp, docs, python, shell, web

DISPATCH = {
    "csharp": csharp.analyze,
    "python": python.analyze,
    "javascript": web.analyze_js,
    "typescript": web.analyze_js,
    "html": web.analyze_html,
    "css": web.analyze_css,
    "powershell": shell.analyze_powershell,
    "shell": shell.analyze_shell,
    "batch": shell.analyze_batch,
    "markdown": docs.analyze_markdown,
    "text": docs.analyze_text,
    "json": docs.analyze_json,
    "toml": docs.analyze_toml,
    "requirements": docs.analyze_requirements,
    "msbuild": docs.analyze_msbuild,
    "dockerfile": docs.analyze_dockerfile,
    "yaml": docs.analyze_yaml,
}


def analyze(f: FileInfo, facts: list[Fact]) -> None:
    fn = DISPATCH.get(f.lang)
    if fn is None or f.skipped or not f.text:
        return
    try:
        fn(f, facts)
    except RecursionError:
        f.skipped = "analyzer recursion limit"
    except Exception as e:  # an analyzer bug must never stop the whole handoff
        f.skipped = f"analyzer error: {e.__class__.__name__}: {e}"[:200]
