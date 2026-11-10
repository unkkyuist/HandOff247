"""Find the project's files and classify them.

Inside a Git work tree the file list comes from ``git ls-files`` (tracked + untracked,
respecting .gitignore), so generated output, secrets and build folders that the project
already ignores stay out of the handoff. Outside Git a conservative walk is used.
"""
from __future__ import annotations

import fnmatch
import os
import subprocess
from pathlib import Path

from .model import FileInfo

MAX_PARSE_BYTES = 1_500_000

ALWAYS_SKIP_DIRS = {".git", ".hg", ".svn", "node_modules", "__pycache__", ".venv", "venv", "env",
                    "bin", "obj", "dist", "build", ".idea", ".vs", ".vscode", ".next", ".nuxt",
                    "target", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".gradle", "coverage"}
VENDOR_HINTS = ("vendor/", "third_party/", "third-party/", "external/", "/vendor/", "/third_party/")

LANG_BY_EXT = {
    ".cs": "csharp", ".csx": "csharp",
    ".py": "python", ".pyw": "python",
    ".js": "javascript", ".mjs": "javascript", ".cjs": "javascript", ".jsx": "javascript",
    ".ts": "typescript", ".tsx": "typescript", ".mts": "typescript",
    ".ps1": "powershell", ".psm1": "powershell", ".psd1": "powershell",
    ".sh": "shell", ".bash": "shell", ".zsh": "shell",
    ".cmd": "batch", ".bat": "batch",
    ".md": "markdown", ".markdown": "markdown", ".txt": "text", ".rst": "text",
    ".html": "html", ".htm": "html", ".css": "css", ".scss": "css",
    ".json": "json", ".jsonc": "json", ".toml": "toml", ".yaml": "yaml", ".yml": "yaml",
    ".xml": "xml", ".csproj": "msbuild", ".fsproj": "msbuild", ".vbproj": "msbuild",
    ".props": "msbuild", ".targets": "msbuild", ".sln": "sln", ".ini": "ini", ".cfg": "ini",
    ".env": "dotenv", ".gd": "gdscript", ".go": "go", ".rs": "rust", ".java": "java",
    ".kt": "kotlin", ".swift": "swift", ".rb": "ruby", ".php": "php", ".lua": "lua",
    ".c": "c", ".h": "c", ".cpp": "cpp", ".hpp": "cpp", ".cc": "cpp",
}
SPECIAL_NAMES = {"dockerfile": "dockerfile", "makefile": "make", "procfile": "procfile",
                 ".gitignore": "ignore", ".gitattributes": "ignore", ".dockerignore": "ignore",
                 "requirements.txt": "requirements"}
BINARY_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".bmp", ".svg", ".mp4", ".mov",
              ".webm", ".mp3", ".wav", ".ogg", ".flac", ".pdf", ".zip", ".7z", ".gz", ".tar",
              ".dll", ".exe", ".so", ".dylib", ".pdb", ".pyc", ".woff", ".woff2", ".ttf", ".otf",
              ".db", ".sqlite", ".bin", ".onnx", ".pt", ".safetensors", ".psd", ".blend", ".fbx",
              ".glb", ".gltf", ".mid", ".midi", ".apk", ".jar", ".class", ".lock"}

CODE_LANGS = {"csharp", "python", "javascript", "typescript", "go", "rust", "java", "kotlin",
              "swift", "ruby", "php", "lua", "c", "cpp", "gdscript"}
SCRIPT_LANGS = {"powershell", "shell", "batch"}
CONFIG_LANGS = {"json", "toml", "yaml", "xml", "msbuild", "sln", "ini", "dotenv", "ignore",
                "dockerfile", "make", "procfile", "requirements"}
TEST_HINTS = ("test", "spec", "smoke", "fixture")


IGNORE_FILE = ".handoffignore"


def read_ignore(root: Path, extra: list[str] | None = None) -> list[str]:
    """fnmatch patterns from <project>/.handoffignore plus --exclude options."""
    pats = list(extra or [])
    f = root / IGNORE_FILE
    if f.is_file():
        for line in f.read_text(encoding="utf-8-sig").splitlines():
            s = line.strip()
            if s and not s.startswith("#"):
                pats.append(s)
    return pats


def excluded(path: str, patterns: list[str]) -> bool:
    for pat in patterns:
        pat = pat.lstrip("/")
        if pat.endswith("/"):
            if path.startswith(pat) or ("/" + pat) in ("/" + path):
                return True
        elif fnmatch.fnmatch(path, pat) or fnmatch.fnmatch(path.rsplit("/", 1)[-1], pat):
            return True
    return False


def list_files(root: Path, excludes: list[str] | None = None) -> tuple[list[str], dict]:
    paths, git = _list_files(root)
    pats = read_ignore(root, excludes)
    if pats:
        paths = [p for p in paths if not excluded(p, pats)]
    return paths, git


def _list_files(root: Path) -> tuple[list[str], dict]:
    """Return project-relative paths and a small Git summary (empty when not a repo)."""
    git = {}
    try:
        top = subprocess.run(["git", "-C", str(root), "rev-parse", "--show-toplevel"],
                             capture_output=True, text=True, timeout=20)
        if top.returncode == 0:
            out = subprocess.run(["git", "-C", str(root), "-c", "core.quotepath=off", "ls-files", "-z",
                                  "--cached", "--others", "--exclude-standard", "--", "."],
                                 capture_output=True, timeout=60)
            if out.returncode == 0:
                toplevel = Path(top.stdout.strip())
                rel_root = root.resolve().relative_to(toplevel.resolve()) if root.resolve() != toplevel.resolve() else Path()
                paths = []
                for raw in out.stdout.decode("utf-8", "replace").split("\0"):
                    if not raw:
                        continue
                    p = Path(raw)
                    if rel_root.parts and p.parts[: len(rel_root.parts)] == rel_root.parts:
                        p = Path(*p.parts[len(rel_root.parts):])
                    paths.append(p.as_posix())
                git = _git_summary(root)
                git["subdir"] = rel_root.as_posix() if rel_root.parts else ""
                return sorted(set(_keep(paths, root, GIT_SKIP_DIRS))), git
    except (OSError, subprocess.SubprocessError, ValueError):
        pass
    paths = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in ALWAYS_SKIP_DIRS and not d.startswith("."))
        for name in filenames:
            full = Path(dirpath) / name
            if full.is_symlink():
                continue
            paths.append(full.relative_to(root).as_posix())
    return sorted(_keep(paths, root, ALWAYS_SKIP_DIRS)), git


GIT_SKIP_DIRS = {".git", "node_modules", "__pycache__"}


def _generated_dirs(paths: list[str], root: Path) -> set[str]:
    """Folders that hold a previous HandOff247 pack (identified by its handoff.json marker)."""
    found = set()
    for p in paths:
        if p.rsplit("/", 1)[-1] != "handoff.json":
            continue
        try:
            head = (root / p).read_text(encoding="utf-8", errors="replace")[:400]
        except OSError:
            continue
        if '"generator": "HandOff247"' in head:
            found.add(p.rsplit("/", 1)[0] + "/" if "/" in p else "")
    return found


def _keep(paths: list[str], root: Path, skip_dirs: set[str]) -> list[str]:
    kept = []
    generated = _generated_dirs(paths, root)
    for p in paths:
        parts = p.split("/")
        if any(part in skip_dirs for part in parts[:-1]):
            continue
        if any(g and p.startswith(g) for g in generated):
            continue
        if parts[-1].endswith(".summaries.json"):
            continue                        # HandOff247's own cache of model-written summaries
        full = root / p
        if not full.is_file() or full.is_symlink():
            continue
        kept.append(p)
    return kept


def _git_summary(root: Path) -> dict:
    def run(*args: str) -> str:
        r = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=20)
        return r.stdout.strip() if r.returncode == 0 else ""
    head = run("rev-parse", "--short", "HEAD")
    head_full = run("rev-parse", "HEAD")
    branch = run("rev-parse", "--abbrev-ref", "HEAD")
    remote = run("remote", "get-url", "origin")
    if "@" in remote and remote.startswith("http"):
        # drop any embedded credentials
        remote = "https://" + remote.split("@", 1)[1]
    log = run("log", "-8", "--format=%h%x09%ad%x09%s", "--date=short", "--", ".")
    dirty = run("status", "--porcelain", "--", ".")
    commits = []
    for line in log.splitlines():
        bits = line.split("\t", 2)
        if len(bits) == 3:
            commits.append({"sha": bits[0], "date": bits[1], "subject": bits[2]})
    return {"head": head, "head_full": head_full, "branch": branch, "remote": remote, "commits": commits,
            "uncommitted": len([l for l in dirty.splitlines() if l.strip()])}


def classify(path: str) -> tuple[str, str]:
    name = path.rsplit("/", 1)[-1]
    lower = name.lower()
    ext = os.path.splitext(lower)[1]
    if lower in SPECIAL_NAMES:
        lang = SPECIAL_NAMES[lower]
    elif lower.startswith("requirements") and ext == ".txt":
        lang = "requirements"
    elif lower.endswith(".min.js") or lower.endswith(".min.css"):
        lang = "minified"
    elif ext in BINARY_EXT:
        lang = "binary"
    else:
        lang = LANG_BY_EXT.get(ext, "other")
    if lang in CODE_LANGS:
        category = "code"
    elif lang in SCRIPT_LANGS:
        category = "script"
    elif lang in ("html", "css"):
        category = "web"
    elif lang in ("markdown", "text"):
        category = "docs"
    elif lang in CONFIG_LANGS:
        category = "config"
    elif lang in ("binary", "minified"):
        category = "asset"
    else:
        category = "other"
    if category in ("code", "script") and any(h in lower for h in TEST_HINTS):
        category = "test"
    if "/tests/" in "/" + path.lower() or path.lower().startswith(("test/", "tests/")):
        if category in ("code", "script"):
            category = "test"
    return lang, category


def load(root: Path, paths: list[str]) -> list[FileInfo]:
    files = []
    for p in paths:
        lang, category = classify(p)
        full = root / p
        try:
            size = full.stat().st_size
        except OSError:
            continue
        info = FileInfo(path=p, lang=lang, category=category, size=size)
        low = "/" + p.lower()
        if any(h in low for h in VENDOR_HINTS):
            info.tags.append("vendored")
        if lang in ("binary", "minified"):
            info.skipped = "binary" if lang == "binary" else "minified"
        elif size > MAX_PARSE_BYTES:
            info.skipped = "large"
        else:
            try:
                raw = full.read_bytes()
            except OSError as e:
                info.skipped = f"unreadable: {e.__class__.__name__}"
                files.append(info)
                continue
            if b"\0" in raw[:4096]:
                info.skipped = "binary"
            else:
                text = raw.decode("utf-8-sig", errors="replace").replace("\r\n", "\n").replace("\r", "\n")
                info.text = text
                info.lines = text.count("\n") + (0 if text.endswith("\n") or not text else 1)
        files.append(info)
    return files
