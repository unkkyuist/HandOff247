"""Optional: short descriptions of files, written by a language model through a command-line
tool the user is already signed in to (today: the Codex CLI). Nothing here runs unless
``--summarize`` is given, and no API key is read or stored by HandOff247.

What a model writes is kept apart from what people write. It lives in its own cache file next
to the notes file (``HANDOFF.summaries.json``), it is shown with a "written by a language
model" label, and it never counts as a note in the handover checklist. Each summary is tied to
a hash of the file it describes; when the file changes, the old summary is no longer shown and
the next ``--summarize`` run writes a new one. Files that already have a note are skipped.

Before anything is sent, lines that match a key or token pattern, or that assign a value to a
password- or secret-like name, are replaced with ``[removed]``.
"""
from __future__ import annotations

import datetime
import hashlib
import json
import re
import shutil
import subprocess
import tempfile
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from . import __version__, leaving
from .model import Project

PROMPT_VERSION = 1
MAX_FILE_CHARS = 14000          # per file in one prompt
MAX_BATCH_CHARS = 60000         # per prompt
MAX_BATCH_FILES = 12
MAX_SUMMARY = 700
TIMEOUT = 600
CATEGORIES = ("code", "script", "test", "web")
ASSIGNED_SECRET = re.compile(r"(?i)\b[\w.-]*(?:password|passwd|secret|token|api[_-]?key|credential)s?\b\s*[:=]\s*['\"]?[^\s'\"]{6,}")

SCHEMA = {"type": "object", "additionalProperties": False, "required": ["items"],
          "properties": {"items": {"type": "array", "items": {
              "type": "object", "additionalProperties": False, "required": ["id", "summary"],
              "properties": {"id": {"type": "string"}, "summary": {"type": "string"}}}}}}

PROMPT = """You are writing short descriptions of source files for a handoff wiki. The person taking over the project "{project}" will read them to find their way around.

Rules:
- For each file below, write 1 to 3 plain sentences: what the file is for and what it does, as far as its code and the listed facts show.
- State only what the code shows. Do not guess intent, history, quality, plans or how well it works. When the purpose is not visible, describe what the code visibly does.
- Do not start with the file name or with "This file". No Markdown headings, no lists.
- Lines shown as [removed] were hidden on purpose. Never guess what they contained.
- Do not run commands or open other files; everything you may use is in this message.
- Answer with JSON only: one item per file, using the id given for it.

{files}"""


class EngineError(RuntimeError):
    pass


# ---------------------------------------------------------------- cache
def cache_path(notes_path: Path) -> Path:
    name = notes_path.name
    base = name[: -len(".notes.md")] if name.endswith(".notes.md") else notes_path.stem
    return notes_path.with_name(base + ".summaries.json")


def digest(text: str) -> str:
    return hashlib.sha256(text.replace("\r\n", "\n").encode("utf-8", "replace")).hexdigest()[:16]


def load_cache(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    return data.get("files", {}) if isinstance(data, dict) and data.get("generator") == "HandOff247" else {}


def save_cache(path: Path, files: dict) -> None:
    data = {"generator": "HandOff247", "kind": "summaries", "version": __version__,
            "note": "Written by a language model, not by a person. Regenerate with --summarize; "
                    "an entry is ignored once its file changes.",
            "files": dict(sorted(files.items()))}
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    tmp.replace(path)


def fresh(project: Project, cache: dict) -> dict:
    """Cache entries whose file still has the content they were written for."""
    out = {}
    for f in project.files:
        e = cache.get(f.path)
        if e and f.text and e.get("sha") == digest(f.text) and e.get("summary"):
            out[f.path] = e
    return out


def attach(project: Project, cache_file: Path | None) -> int:
    """Put the fresh summaries into ``project.links['model_summaries']``; returns how many."""
    got = fresh(project, load_cache(cache_file)) if cache_file else {}
    project.links["model_summaries"] = got
    return len(got)


# ---------------------------------------------------------------- prompt
def redact(text: str) -> tuple[str, int]:
    lines, n = [], 0
    for line in text.replace("\r\n", "\n").split("\n"):
        if any(rx.search(line) for _, rx in leaving.SECRET_PATTERNS) or ASSIGNED_SECRET.search(line):
            lines.append("[removed]")
            n += 1
        else:
            lines.append(line)
    return "\n".join(lines), n


def _facts(project: Project, path: str) -> str:
    f = project.file(path)
    bits = []
    syms = [s for s in f.symbols if s.public and s.kind not in ("h3",)]
    if syms:
        bits.append("defines " + ", ".join(f"{s.kind} {s.name}" for s in syms[:25]) + (" …" if len(syms) > 25 else ""))
    outs, ins = {}, {}
    for e in project.edges:
        if e.src == path:
            outs.setdefault(e.kind, []).append(e.dst)
        elif e.dst == path:
            ins.setdefault(e.kind, []).append(e.src)
    for k, v in sorted(outs.items()):
        bits.append(f"{k}: " + ", ".join(sorted(set(v))[:10]))
    for k, v in sorted(ins.items()):
        bits.append(f"{k} (from): " + ", ".join(sorted(set(v))[:8]))
    L = project.links
    for m in L.get("modes", []):
        if m["file"] == path:
            bits.append(f"run mode '{m['name']}' (lines {m['start']}-{m['end']})")
    for r in L.get("routes", []):
        if r["file"] == path:
            bits.append(f"HTTP route {r['verb']} {r['path']}")
    tools = [x["name"] for x in L.get("mcp_tools", []) if x["file"] == path]
    if tools:
        bits.append("MCP tools: " + ", ".join(tools[:20]))
    for tb in L.get("tables", []):
        if tb["file"] == path:
            bits.append(f"dispatch table {tb['id']} with {len(tb['ops'])} operations")
    return "; ".join(bits) or "none"


def _block(project: Project, fid: str, path: str) -> str:
    f = project.file(path)
    text, _ = redact(f.text)
    shown = text
    note = ""
    if len(text) > MAX_FILE_CHARS:
        shown = text[:MAX_FILE_CHARS].rsplit("\n", 1)[0]
        note = f"; only the first {shown.count(chr(10)) + 1} of {f.lines} lines are shown"
    fence = "````" if "```" in shown else "```"
    return (f"### id: {fid}\npath: {path} ({f.lang}, {f.lines} lines{note})\n"
            f"facts found by static analysis: {_facts(project, path)}\n{fence}\n{shown}\n{fence}\n")


def targets(project: Project, notes, cache: dict) -> list[str]:
    have = fresh(project, cache)
    out = []
    for f in project.files:
        if f.category in CATEGORIES and f.text and not f.skipped and "vendored" not in f.tags \
                and not notes.get(f"File: {f.path}") and f.path not in have:
            out.append(f.path)
    return out


def batches(project: Project, paths: list[str]) -> list[list[tuple[str, str, str]]]:
    out, cur, size = [], [], 0
    for i, p in enumerate(paths, 1):
        block = _block(project, f"f{i}", p)
        if cur and (size + len(block) > MAX_BATCH_CHARS or len(cur) >= MAX_BATCH_FILES):
            out.append(cur)
            cur, size = [], 0
        cur.append((f"f{i}", p, block))
        size += len(block)
    if cur:
        out.append(cur)
    return out


def parse_answer(raw: str, ids: set[str]) -> dict[str, str]:
    """id -> summary, keeping only ids that were asked for and non-empty text."""
    raw = raw.strip()
    m = re.search(r"\{.*\}", raw, re.S)
    try:
        data = json.loads(m.group(0) if m else raw)
    except ValueError:
        return {}
    out = {}
    for item in data.get("items", []) if isinstance(data, dict) else []:
        if not isinstance(item, dict):
            continue
        fid, text = str(item.get("id", "")), re.sub(r"\s+", " ", str(item.get("summary", ""))).strip()
        if fid in ids and text and fid not in out:
            out[fid] = text if len(text) <= MAX_SUMMARY else text[: MAX_SUMMARY - 1].rstrip() + "…"
    return out


# ---------------------------------------------------------------- engines
def codex_status() -> str:
    exe = shutil.which("codex")
    if not exe:
        raise EngineError("the Codex CLI was not found on PATH (install it, then run `codex login`)")
    try:
        r = subprocess.run([exe, "login", "status"], capture_output=True, text=True, encoding="utf-8",
                           errors="replace", timeout=60)
    except (OSError, subprocess.SubprocessError) as e:
        raise EngineError(f"could not run codex: {e}") from e
    text = (r.stdout + r.stderr).strip().splitlines()
    status = text[-1].strip() if text else ""
    if r.returncode != 0 or "logged in" not in status.lower():
        raise EngineError(f"Codex is not signed in ({status or 'no answer'}); run `codex login` first")
    return status


def codex_call(prompt: str, model: str | None = None, timeout: int = TIMEOUT) -> str:
    exe = shutil.which("codex")
    if not exe:
        raise EngineError("the Codex CLI was not found on PATH")
    with tempfile.TemporaryDirectory(prefix="handoff247-") as tmp:
        work = Path(tmp)
        schema, answer = work / "schema.json", work / "answer.json"
        schema.write_text(json.dumps(SCHEMA), encoding="utf-8")
        cmd = [exe, "exec", "-s", "read-only", "--ephemeral", "--skip-git-repo-check", "--color", "never",
               "--output-schema", str(schema), "-o", str(answer)]
        if model:
            cmd += ["-m", model]
        cmd.append("-")
        try:
            r = subprocess.run(cmd, input=prompt, capture_output=True, text=True, encoding="utf-8", errors="replace",
                               cwd=work, timeout=timeout)       # an empty folder: there is nothing else to read
        except subprocess.TimeoutExpired as e:
            raise EngineError(f"codex did not answer within {timeout} s") from e
        except OSError as e:
            raise EngineError(f"could not run codex: {e}") from e
        if r.returncode != 0:
            tail = " ".join((r.stderr or r.stdout).strip().splitlines()[-3:])[:300]
            raise EngineError(f"codex exited with {r.returncode}: {tail}")
        try:
            return answer.read_text(encoding="utf-8")
        except OSError as e:
            raise EngineError("codex wrote no answer") from e


# ---------------------------------------------------------------- run
def prepare(project: Project, notes, cache: Path, args=None, log=print) -> dict | None:
    """What every command does before writing a pack: load the cached summaries and, when
    ``args.summarize`` is set, write the missing ones first. A missing or signed-out CLI is
    reported and the pack is built without new summaries."""
    if not getattr(args, "summarize", False):
        n = attach(project, cache)
        if n:
            log(f"summaries: {n} model-written summary(ies) from {cache.name} (run with --summarize to add the rest)")
        return None
    try:
        st = run(project, notes, cache, getattr(args, "model", None), getattr(args, "jobs", 3) or 3,
                 getattr(args, "limit", 0) or 0, log=log)
    except EngineError as e:
        log(f"summaries: not written: {e}")
        attach(project, cache)
        return None
    if st["asked"]:
        log(f"summaries: {st['written']} of {st['asked']} written to {cache}"
            + (f", {st['failed']} request(s) failed" if st["failed"] else ""))
    return st


def run(project: Project, notes, cache_file: Path, model: str | None = None, jobs: int = 3, limit: int = 0,
        call=None, log=print, date: str | None = None) -> dict:
    """Summarize every code file that has no note and no fresh summary yet. ``call(prompt)``
    returns the model's raw answer; it defaults to the Codex CLI."""
    date = date or datetime.date.today().isoformat()
    engine = "codex"
    if call is None:
        log(f"summaries: Codex CLI, {codex_status()}")
        call = lambda prompt: codex_call(prompt, model)          # noqa: E731
    else:
        engine = getattr(call, "engine", "test")
    cache = load_cache(cache_file)
    todo = targets(project, notes, cache)
    skipped = 0
    if limit and len(todo) > limit:
        skipped, todo = len(todo) - limit, todo[:limit]
    groups = batches(project, todo)
    if not groups:
        log("summaries: nothing to do (every code file has a note or a current summary)")
        attach(project, cache_file)
        return {"asked": 0, "written": 0, "failed": 0, "batches": 0, "left": skipped}
    log(f"summaries: {len(todo)} file(s) in {len(groups)} request(s)" + (f"; {skipped} left for a later run (--limit)" if skipped else ""))
    lock = threading.Lock()
    stats = {"asked": len(todo), "written": 0, "failed": 0, "batches": len(groups), "left": skipped, "errors": []}

    def one(group):
        prompt = PROMPT.format(project=project.name, files="\n".join(b for _, _, b in group))
        return group, call(prompt)
    with ThreadPoolExecutor(max_workers=max(1, jobs)) as pool:
        futures = [pool.submit(one, g) for g in groups]
        for n, fut in enumerate(as_completed(futures), 1):
            try:
                group, raw = fut.result()
            except Exception as e:                      # one failed request must not lose the others
                with lock:
                    stats["failed"] += 1
                    stats["errors"].append(str(e)[:300])
                log(f"  request {n}/{len(groups)} failed: {e}")
                continue
            got = parse_answer(raw, {fid for fid, _, _ in group})
            with lock:
                for fid, path, _ in group:
                    if fid in got:
                        cache[path] = {"sha": digest(project.file(path).text), "summary": got[fid], "engine": engine,
                                       "model": model or "", "date": date, "prompt": PROMPT_VERSION}
                        stats["written"] += 1
                save_cache(cache_file, cache)
            log(f"  request {n}/{len(groups)}: {len(got)}/{len(group)} summaries")
    attach(project, cache_file)
    return stats
