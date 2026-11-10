"""What the code alone cannot hand over: unfinished work, things that exist only on the
computer the pack was generated on, accounts and services, tools to install, people.

Everything here is observed, never guessed: Git answers the questions about state, and the
scans report a file and line for each hit. Secret-looking values are reported by location
and kind only; the value itself is never copied into the pack.
"""
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

from .inventory import ALWAYS_SKIP_DIRS
from .model import Project

NOTES_FILE = "HANDOFF.notes.md"
MAX_HITS = 400

# ---------------------------------------------------------------- patterns
SEP = r"(?:\\{1,2}|/)"
SEG = r"[A-Za-z0-9_.$%~+@#-]+"
WIN_PATH = re.compile(rf"(?<![A-Za-z0-9_])([A-Za-z]:{SEP}{SEG}(?:{SEP}{SEG})+)")
HOME_PATH = re.compile(rf"(?<![\w.~/-])(/(?:home|Users)/{SEG}(?:/{SEG})*)")
USER_DIR = re.compile(r"[\\/](?:Users|home)[\\/]([^\\/]+)", re.I)
SHARED_USERS = {"public", "default", "all users", "shared", "%username%", "$user", "$env", "username", "user", "you", "me"}

HOST = re.compile(r"\bhttps?://([A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,})(?![A-Za-z0-9-])")
SKIP_HOSTS = {"example.com", "example.org", "example.net", "www.example.com", "www.w3.org", "json-schema.org",
              "schemas.microsoft.com", "schemas.xmlsoap.org", "schemas.openxmlformats.org", "img.shields.io"}
SKIP_HOST_SUFFIX = (".example", ".invalid", ".test", ".localhost", ".example.com")

TODO = re.compile(r"(?:(?:^|[\s;{})])(?:#|//|/\*|<!--|--|::|[Rr][Ee][Mm]\b)\s*|^\s*\*\s*)(TODO|FIXME|HACK|XXX)\b[\s:(\])-]*(.*)")

SECRET_PATTERNS = [
    ("private key", re.compile(r"-----BEGIN (?:[A-Z]+ )?PRIVATE KEY-----")),
    ("AWS access key id", re.compile(r"(?<![A-Z0-9])AKIA[0-9A-Z]{16}(?![A-Z0-9])")),
    ("GitHub token", re.compile(r"(?<![A-Za-z0-9])(?:gh[pousr]_[A-Za-z0-9]{36,}|github_pat_[A-Za-z0-9_]{50,})")),
    ("Slack token", re.compile(r"(?<![A-Za-z0-9])xox[abprs]-[A-Za-z0-9-]{20,}")),
    ("Google API key", re.compile(r"(?<![A-Za-z0-9])AIza[0-9A-Za-z_-]{35}(?![A-Za-z0-9_-])")),
    ("API key (sk-…)", re.compile(r"(?<![A-Za-z0-9])sk-(?:(?:ant|proj)-[A-Za-z0-9_-]{40,}|[A-Za-z0-9]{40,})")),
]
SECRET_WORDS = {"KEY", "APIKEY", "TOKEN", "SECRET", "PASSWORD", "PASSWD", "PWD", "CREDENTIAL", "CREDENTIALS", "AUTH"}

CRON = re.compile(r"^\s*-?\s*cron:\s*['\"]?([^'\"#\n]+?)['\"]?\s*(?:#.*)?$")
SCHEDULER = re.compile(r"\b(schtasks(?:\.exe)?\s+/create|Register-ScheduledTask|crontab\s+-)", re.I)

KNOWN_COMMANDS = {"dotnet", "python", "python3", "py", "node", "npm", "npx", "pnpm", "yarn", "bun", "deno", "pwsh",
                  "powershell", "docker", "docker-compose", "git", "cargo", "go", "java", "mvn", "gradle", "make",
                  "cmake", "ffmpeg", "wrangler", "gh", "az", "aws", "gcloud", "kubectl", "terraform", "pip", "uv",
                  "poetry", "pytest", "ruby", "bundle", "php", "composer", "curl", "sqlite3", "psql", "mysql"}

# ignored-by-Git entries that are build or tool output, not something a successor is missing
JUNK_DIRS = ALWAYS_SKIP_DIRS | {".git", ".cache", ".tox", ".nox", "tmp", "temp", "logs", ".parcel-cache", ".turbo",
                                ".angular", "packages", "testresults", ".terraform", ".claude"}
JUNK_SUFFIX = (".pyc", ".pyo", ".log", ".tmp", ".temp", ".cache", ".swp", ".bak", ".orig", ".user", ".suo",
               ".tsbuildinfo", ".egg-info", ".egg-info/", ".ds_store")
JUNK_NAMES = {"thumbs.db", "desktop.ini", ".ds_store", "npm-debug.log"}
SETTINGS_HINT = re.compile(r"(^\.env($|\.)|secret|credential|password|token|\.pem$|\.key$|\.pfx$|\.p12$|\.jks$|\.keystore$|"
                           r"\.local\.|^local\.settings\.json$|^appsettings\.[^.]+\.json$|^\.npmrc$|^\.pypirc$|^id_[rd]sa)", re.I)
DATA_SUFFIX = (".db", ".sqlite", ".sqlite3", ".mdf", ".ldf", ".bak", ".dump", ".sql.gz", ".parquet", ".duckdb")

CI_FILES = (".github/workflows/", ".gitlab-ci.yml", "azure-pipelines.yml", ".circleci/", "jenkinsfile", ".drone.yml",
            "bitbucket-pipelines.yml")
README_NAMES = ("readme.md", "readme.en.md", "readme.txt", "readme", "readme.rst")
LICENSE_NAMES = ("license", "license.md", "license.txt", "licence", "licence.md", "licence.txt", "copying", "unlicense")


# ---------------------------------------------------------------- Git
def _git(root: str, *args: str) -> str | None:
    try:
        r = subprocess.run(["git", "-C", root, "-c", "core.quotepath=off", *args], capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=40)
    except (OSError, subprocess.SubprocessError):
        return None
    return r.stdout.rstrip("\n") if r.returncode == 0 else None


def git_state(project: Project) -> dict:
    """State of the checkout the pack is generated from. ``repo`` False = not a Git work tree."""
    root = project.root
    g = project.git
    if not g:
        return {"repo": False}
    out: dict = {"repo": True, "branch": g.get("branch", ""), "subdir": g.get("subdir", ""), "has_commits": bool(g.get("head"))}
    remotes = (_git(root, "remote") or "").split()
    out["remotes"] = remotes
    status = _git(root, "status", "--porcelain", "--", ".") or ""
    changes = [l for l in status.split("\n") if l.strip()]
    out["uncommitted"] = len(changes)
    out["uncommitted_files"] = [{"state": l[:2].strip() or "?", "path": l[3:].strip().strip('"')} for l in changes[:15]]
    unpushed = []
    if remotes and out["has_commits"]:
        refs = _git(root, "for-each-ref", "--format=%(refname:short)", "refs/heads") or ""
        for br in [b for b in refs.split("\n") if b.strip()]:
            n = _git(root, "rev-list", "--count", br, "--not", "--remotes")
            if n and n.isdigit() and int(n) > 0:
                unpushed.append({"branch": br, "commits": int(n)})
    out["unpushed"] = unpushed
    stash = _git(root, "stash", "list")
    out["stashes"] = len([l for l in (stash or "").split("\n") if l.strip()])
    shallow = _git(root, "rev-parse", "--is-shallow-repository") == "true"
    out["shallow"] = shallow
    out["authors"] = []
    if out["has_commits"] and not shallow:
        log = _git(root, "log", "--format=%an%x09%ad", "--date=short", "--", ".") or ""
        people: dict[str, dict] = {}
        dates = []
        for line in log.split("\n"):
            name, _, date = line.partition("\t")
            if not name or not date:
                continue
            dates.append(date)
            p = people.setdefault(name, {"name": name, "commits": 0, "last": date, "first": date})
            p["commits"] += 1
            p["last"], p["first"] = max(p["last"], date), min(p["first"], date)
        out["authors"] = sorted(people.values(), key=lambda p: (-p["commits"], p["name"]))[:12]
        out["commits"] = len(dates)
        if dates:
            out["first_commit"], out["last_commit"] = min(dates), max(dates)
    elif g.get("commits"):
        out["last_commit"] = g["commits"][0]["date"]
    return out


def local_only(project: Project) -> list[dict] | None:
    """Files and folders Git ignores that are present in this checkout: the successor will not
    get them through the repository. None when the folder is not in Git."""
    if not project.git:
        return None
    raw = _git(project.root, "ls-files", "-z", "--others", "--ignored", "--exclude-standard", "--directory", "--", ".")
    if raw is None:
        return None
    root = Path(project.root)
    out = []
    for p in sorted(x for x in raw.split("\0") if x):
        is_dir = p.endswith("/")
        parts = [x.lower() for x in p.strip("/").split("/")]
        name = parts[-1]
        if any(x in JUNK_DIRS for x in parts) or name in JUNK_NAMES or name.endswith(JUNK_SUFFIX):
            continue
        if is_dir and (root / p / "handoff.json").is_file():
            continue                                    # an earlier pack
        if SETTINGS_HINT.search(name):
            kind = "settings or secrets"
        elif name.endswith(DATA_SUFFIX):
            kind = "data"
        elif is_dir:
            kind = "folder"
        else:
            kind = "file"
        out.append({"path": p, "kind": kind})
    return out


# ---------------------------------------------------------------- scans
def _scan(project: Project) -> dict:
    paths: dict[str, dict] = {}
    hosts: dict[str, dict] = {}
    todos, secrets, schedules = [], [], []
    for f in project.files:
        if not f.text or f.skipped or "vendored" in f.tags or f.path.rsplit("/", 1)[-1] == NOTES_FILE:
            continue
        in_code = f.category in ("code", "script", "web", "test", "config")
        workflow = f.path.lower().startswith(".github/workflows/")
        for ln, line in enumerate(f.text.split("\n"), 1):
            if len(line) > 2000:
                continue
            if ":" in line or "/home/" in line or "/Users/" in line:
                for rx in (WIN_PATH, HOME_PATH):
                    for m in rx.finditer(line):
                        raw = m.group(1).rstrip(".")
                        shown = re.sub(r"\\{2,}", r"\\", raw)
                        um = USER_DIR.search(shown)
                        user = bool(um and um.group(1).lower() not in SHARED_USERS and not um.group(1).startswith(("$", "%", "{", "<")))
                        if rx is HOME_PATH and not user:
                            continue
                        e = paths.setdefault(shown.lower(), {"path": shown, "user": user, "where": [], "count": 0, "in_code": False})
                        e["count"] += 1
                        e["in_code"] = e["in_code"] or in_code
                        if len(e["where"]) < 3 and not any(w["file"] == f.path for w in e["where"]):
                            e["where"].append({"file": f.path, "line": ln})
            if "http" in line:
                for m in HOST.finditer(line):
                    host = m.group(1).lower()
                    if host in SKIP_HOSTS or host.endswith(SKIP_HOST_SUFFIX):
                        continue
                    e = hosts.setdefault(host, {"host": host, "code": [], "docs": [], "count": 0})
                    e["count"] += 1
                    bucket = e["code"] if in_code else e["docs"]
                    if len(bucket) < 3 and not any(w["file"] == f.path for w in bucket):
                        bucket.append({"file": f.path, "line": ln})
            if in_code and len(todos) < MAX_HITS and ("TODO" in line or "FIXME" in line or "HACK" in line or "XXX" in line):
                m = TODO.search(line)
                if m:
                    text = re.sub(r"\s*(\*/|-->)\s*$", "", m.group(2)).strip()
                    todos.append({"file": f.path, "line": ln, "tag": m.group(1), "text": text[:160]})
            if len(secrets) < MAX_HITS:
                for kind, rx in SECRET_PATTERNS:
                    if rx.search(line):
                        secrets.append({"file": f.path, "line": ln, "kind": kind})
                        break
            if workflow and "cron" in line:
                m = CRON.match(line)
                if m:
                    schedules.append({"file": f.path, "line": ln, "what": f"cron {m.group(1).strip()}"})
            elif f.category == "script" and SCHEDULER.search(line):
                schedules.append({"file": f.path, "line": ln, "what": SCHEDULER.search(line).group(1).strip()})
    plist = sorted(paths.values(), key=lambda e: (not e["user"], not e["in_code"], -e["count"], e["path"].lower()))
    hlist = sorted(hosts.values(), key=lambda e: (not e["code"], -e["count"], e["host"]))
    return {"machine_paths": plist, "hosts": hlist, "todos": todos, "secrets": secrets, "schedules": schedules}


def _first_line(text: str) -> str:
    for line in text.split("\n"):
        s = line.strip()
        if s and not s.startswith("#"):
            return s[:60]
    return ""


def _line_of(text: str, needle: str) -> int:
    i = text.find(needle)
    return text.count("\n", 0, i) + 1 if i >= 0 else 0


def prerequisites(project: Project) -> list[dict]:
    """Runtimes and tool versions the project declares."""
    out = []

    def add(tool: str, version: str, f, line: int = 0) -> None:
        if version:
            out.append({"tool": tool, "version": str(version)[:60], "file": f.path, "line": line})
    for f in project.files:
        if not f.text or "vendored" in f.tags:
            continue
        name = f.path.rsplit("/", 1)[-1].lower()
        if name == "pyproject.toml":
            m = re.search(r"^\s*requires-python\s*=\s*[\"']([^\"']+)", f.text, re.M)
            if m:
                add("Python", m.group(1), f, _line_of(f.text, m.group(0)))
        elif name in ("package.json", "global.json"):
            try:
                data = json.loads(f.text)
            except ValueError:
                continue
            if not isinstance(data, dict):
                continue
            if name == "global.json" and isinstance(data.get("sdk"), dict):
                add(".NET SDK", data["sdk"].get("version", ""), f, _line_of(f.text, '"sdk"'))
            elif isinstance(data.get("engines"), dict):
                for k, v in data["engines"].items():
                    add({"node": "Node.js"}.get(k, k), v, f, _line_of(f.text, f'"{k}"'))
        elif name in (".nvmrc", ".node-version"):
            add("Node.js", _first_line(f.text), f, 1)
        elif name == ".python-version":
            add("Python", _first_line(f.text), f, 1)
        elif name == ".tool-versions":
            for i, line in enumerate(f.text.split("\n"), 1):
                bits = line.split()
                if len(bits) >= 2 and not bits[0].startswith("#"):
                    add(bits[0], bits[1], f, i)
        elif name == "go.mod":
            m = re.search(r"^go\s+(\S+)", f.text, re.M)
            if m:
                add("Go", m.group(1), f, _line_of(f.text, m.group(0)))
        elif name == "dockerfile" or name.startswith("dockerfile."):
            for i, line in enumerate(f.text.split("\n"), 1):
                m = re.match(r"\s*FROM\s+(?:--\S+\s+)*(\S+)", line, re.I)
                if m and m.group(1).lower() != "scratch":
                    add("Docker image", m.group(1), f, i)
    for b in project.links.get("build_targets", []):
        if b.get("framework"):
            out.append({"tool": ".NET", "version": b["framework"], "file": b["file"], "line": 0})
    return out


def commands_used(project: Project) -> list[dict]:
    """Well-known command-line tools the project's scripts and configs start."""
    found: dict[str, dict] = {}
    for l in project.links.get("launches", []):
        cmd = re.split(r"[\\/]", str(l.get("cmd", "")).strip("\"'"))[-1].lower().removesuffix(".exe")
        if cmd in KNOWN_COMMANDS:
            e = found.setdefault(cmd, {"command": cmd, "where": [], "count": 0})
            e["count"] += 1
            if len(e["where"]) < 3 and not any(w["file"] == l["file"] for w in e["where"]):
                e["where"].append({"file": l["file"], "line": l["line"]})
    return sorted(found.values(), key=lambda e: (-e["count"], e["command"]))


def secret_env(project: Project) -> list[str]:
    names = []
    for name, use in project.links.get("env", {}).items():
        if not use.get("system") and set(re.split(r"[_\W]+", name.upper())) & SECRET_WORDS:
            names.append(name)
    return names


def collect(project: Project) -> None:
    """Fill ``project.links['leaving']``."""
    lower = {f.path.lower(): f.path for f in project.files}
    data = _scan(project)
    data["git"] = git_state(project)
    data["local_only"] = local_only(project)
    data["prerequisites"] = prerequisites(project)
    data["commands"] = commands_used(project)
    data["secret_env"] = secret_env(project)
    data["has"] = {
        "readme": next((lower[n] for n in README_NAMES if n in lower), ""),
        "license": next((lower[n] for n in LICENSE_NAMES if n in lower), ""),
        "tests": sum(1 for f in project.files if f.category == "test"),
        "ci": sorted(p for low, p in lower.items() if low.startswith(CI_FILES) or low.rsplit("/", 1)[-1] in CI_FILES),
    }
    project.links["leaving"] = data


# ---------------------------------------------------------------- readiness
def start_known(project: Project) -> bool:
    L = project.links
    return bool(L.get("launchers") or L.get("modes") or L.get("entries")
                or any(not l.get("ci") for l in L.get("launches", [])))


def readiness(project: Project, notes, topics: list[str], gaps: list[str]) -> list[dict]:
    """The handover checklist: one row per check, state 'ok', 'todo' or 'na' (cannot be known)."""
    lv = project.links["leaving"]
    g, has = lv["git"], lv["has"]
    rows = []

    def row(key: str, label: str, state: str, detail: str = "") -> None:
        rows.append({"key": key, "label": label, "state": state, "detail": detail})

    def yes(cond: bool) -> str:
        return "ok" if cond else "todo"
    row("readme", "The project has a README", yes(bool(has["readme"])), has["readme"] or "no README file at the top level")
    row("start", "How to start it can be found in the files", yes(start_known(project)),
        "launch scripts, an entry point or run modes were found" if start_known(project) else
        "no launch script or entry point was recognised; describe the start command in the notes")
    row("tests", "There are tests", yes(has["tests"] > 0), f"{has['tests']} test file(s)" if has["tests"] else "no test files found")
    row("license", "A license file says who may use the code", yes(bool(has["license"])), has["license"] or "no LICENSE file")
    if not g["repo"]:
        row("git", "The folder is in Git with a remote", "todo", "not a Git work tree: it exists only where this folder is copied")
    else:
        row("git", "The folder is in Git with a remote", yes(bool(g["remotes"])),
            ", ".join(g["remotes"]) if g["remotes"] else "no remote: the history exists only on this computer")
        row("committed", "Everything is committed", yes(g["uncommitted"] == 0),
            "clean work tree" if not g["uncommitted"] else f"{g['uncommitted']} uncommitted change(s)")
        if g["remotes"]:
            n = sum(u["commits"] for u in g["unpushed"])
            bits = []
            if n:
                bits.append(f"{n} commit(s) on no remote (" + ", ".join(u["branch"] for u in g["unpushed"]) + ")")
            if g["stashes"]:
                bits.append(f"{g['stashes']} stash(es)")
            row("pushed", "Everything is pushed", yes(not bits), "; ".join(bits) or "every local commit is on a remote")
    lo = lv["local_only"]
    if lo is not None:
        key = [x for x in lo if x["kind"] in ("settings or secrets", "data")]
        row("local", "Nothing the program needs exists only on this computer", yes(not key),
            f"{len(key)} ignored settings or data file(s) are present here but not in the repository" if key
            else ("no ignored settings or data files" + (f" ({len(lo)} other ignored item(s))" if lo else "")))
    user_paths = [x for x in lv["machine_paths"] if x["user"] and x["in_code"]]
    row("paths", "No personal folder paths are written into code", yes(not user_paths),
        f"{len(user_paths)} path(s) under a user's home folder" if user_paths else "none found")
    row("secrets", "No secret-looking values are stored in files", yes(not lv["secrets"]),
        f"{len(lv['secrets'])} place(s) match a key or token pattern" if lv["secrets"] else "no key or token patterns matched")
    row("project", "The notes say what the project is", yes(bool(notes.get("Project"))), "" if notes.get("Project") else "## Project is still TODO")
    done = [x for x in topics if notes.get(f"Topic: {x}")]
    missing = [x for x in topics if x not in done]
    row("topics", "The handover questions are answered", yes(not missing),
        f"{len(done)}/{len(topics)} answered" + (": missing " + ", ".join(missing) if missing else ""))
    row("files", "The most important files have notes", yes(not gaps), f"{len(gaps)} without notes" if gaps else "all have notes")
    left = project.links.get("untranslated", [])
    if left or project.links.get("translations"):
        row("english", "Comments in another language have English versions", yes(not left),
            f"{len(left)} still untranslated" if left else "all translated")
    return rows


def score(rows: list[dict]) -> tuple[int, int]:
    counted = [r for r in rows if r["state"] != "na"]
    return sum(1 for r in counted if r["state"] == "ok"), len(counted)
