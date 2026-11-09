"""PowerShell, POSIX shell and Windows batch analyzers (line based, no execution)."""
from __future__ import annotations

import re

from ..lexer import first_sentence
from ..model import Fact, FileInfo

LAUNCHERS = ("dotnet", "python", "python3", "py", "node", "npm", "npx", "pnpm", "yarn", "bun", "deno",
             "powershell", "powershell.exe", "pwsh", "bash", "sh", "zsh", "cmd", "cmd.exe", "java", "go",
             "cargo", "uv", "uvx", "pip", "docker", "docker-compose", "start", "Start-Process", "call",
             "exec", "wsl", "code", "git", "msbuild", "godot", "blender", "ffmpeg")
_LAUNCH_RE = re.compile(
    r"(?:^|[;{|(]\s*|&&\s*|\|\|\s*|\btry\s*\{\s*|\bthen\s+|\bdo\s+|\belse\s+)"
    r"(?P<amp>&\s*)?(?P<cmd>(?:" + "|".join(re.escape(x) for x in sorted(LAUNCHERS, key=len, reverse=True)) + r"))(?=[\s\"']|$)"
    r"(?P<rest>[^;|\n]*)", re.I)
_CALL_OP_RE = re.compile(r"(?:^|[;{(]\s*|\btry\s*\{\s*)&\s*(?P<target>[\"'$(][^;|\n]*)")


def _strip_comment(line: str, marker: str = "#") -> str:
    quote = ""
    for i, ch in enumerate(line):
        if quote:
            if ch == quote:
                quote = ""
            continue
        if ch in "'\"":
            quote = ch
        elif ch == marker and (i == 0 or line[i - 1] in " \t;"):
            return line[:i]
    return line


def _launches(f: FileInfo, facts: list[Fact], lineno: int, line: str) -> None:
    hits = []
    for m in _LAUNCH_RE.finditer(line):
        cmd = m.group("cmd")
        rest = m.group("rest").strip()
        if cmd.lower() in ("start", "call", "exec", "code", "git") and not rest:
            continue
        if cmd.lower() == "git" and not re.match(r"(clone|pull|submodule)\b", rest):
            continue
        hits.append((m.start("cmd"), cmd, (cmd + " " + rest).strip()))
    for m in _CALL_OP_RE.finditer(line):
        target = m.group("target").strip()
        if not any(h[0] >= m.start() and h[0] <= m.start("target") + 2 for h in hits):
            hits.append((m.start("target"), "&", "& " + target))
    for _, cmd, text in sorted(hits):
        facts.append(Fact("launch", f.path, lineno, {"cmd": cmd, "text": text[:220]}))


def analyze_powershell(f: FileInfo, facts: list[Fact]) -> None:
    text = f.text
    lines = text.split("\n")
    # block comments <# ... #>
    blocks = [(m.start(), m.end(), m.group(1)) for m in re.finditer(r"<#(.*?)#>", text, re.S)]
    synopsis = ""
    for _, _, body in blocks:
        m = re.search(r"\.SYNOPSIS\s*\n(.*?)(?:\n\s*\.\w+|\Z)", body, re.S | re.I)
        if m:
            synopsis = " ".join(m.group(1).split())
            break
    head = []
    for ln in lines:
        s = ln.strip()
        if s.startswith("#") and not s.startswith("#Requires") and not s.startswith("#!"):
            head.append(s.lstrip("#").strip())
        elif s == "":
            continue
        else:
            break
    if synopsis:
        f.summary, f.summary_source = first_sentence(synopsis, 300), ".SYNOPSIS"
    elif head:
        f.summary, f.summary_source = first_sentence(" ".join(h for h in head if h), 300), "file comment"
    elif blocks and blocks[0][0] < 5:
        f.summary, f.summary_source = first_sentence(" ".join(blocks[0][2].split()), 300), "file comment"
    in_block = False
    for i, raw in enumerate(lines, 1):
        line = raw
        if in_block:
            if "#>" in line:
                line = line.split("#>", 1)[1]
                in_block = False
            else:
                continue
        if "<#" in line:
            before, _, after = line.partition("<#")
            if "#>" in after:
                line = before + after.split("#>", 1)[1]
            else:
                line = before
                in_block = True
        line = _strip_comment(line)
        if not line.strip():
            continue
        for m in re.finditer(r"\$env:(\w+)\s*=(?!=)\s*(['\"]?)([^'\";}\n]*)\2", line, re.I):
            facts.append(Fact("env_write", f.path, i, {"name": m.group(1), "value": m.group(3).strip()}))
        writes = {m.start() for m in re.finditer(r"\$env:(\w+)\s*=(?!=)", line, re.I)}
        for m in re.finditer(r"\$env:(\w+)", line, re.I):
            if m.start() not in writes:
                facts.append(Fact("env_read", f.path, i, {"name": m.group(1), "default": ""}))
        for m in re.finditer(r"Join-Path\s+\S+\s+(['\"])([^'\"]+)\1", line, re.I):
            facts.append(Fact("path_literal", f.path, i, {"parts": [m.group(2)]}))
        for m in re.finditer(r"(['\"])((?:[^'\"\n])*?)\1", line):
            f.strings.append((m.group(2), i))
        _launches(f, facts, i, line)
    m = re.search(r"(?im)^\s*param\s*\(", text)
    if m:
        depth, j = 0, m.end() - 1
        while j < len(text):
            if text[j] == "(":
                depth += 1
            elif text[j] == ")":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        params = re.findall(r"\$(\w+)", text[m.end():j])
        if params:
            facts.append(Fact("script_params", f.path, text.count("\n", 0, m.start()) + 1, {"params": params}))


def analyze_shell(f: FileInfo, facts: list[Fact]) -> None:
    lines = f.text.split("\n")
    head = []
    for ln in lines:
        s = ln.strip()
        if s.startswith("#!"):
            continue
        if s.startswith("#"):
            head.append(s.lstrip("#").strip())
        elif s:
            break
    if head and any(head):
        f.summary, f.summary_source = first_sentence(" ".join(h for h in head if h), 300), "file comment"
    for i, raw in enumerate(lines, 1):
        line = _strip_comment(raw)
        if not line.strip() or line.lstrip().startswith("#!"):
            continue
        for m in re.finditer(r"\bexport\s+(\w+)=(['\"]?)([^'\"\s;]*)", line):
            facts.append(Fact("env_write", f.path, i, {"name": m.group(1), "value": m.group(3)}))
        for m in re.finditer(r"\$\{(\w+)(?::?-([^}]*))?\}", line):
            if not m.group(1).isdigit() and m.group(1) not in ("BASH_SOURCE",):
                facts.append(Fact("env_read", f.path, i, {"name": m.group(1), "default": (m.group(2) or "").strip("\"'")}))
        for m in re.finditer(r"(['\"])((?:[^'\"\n])*?)\1", line):
            f.strings.append((m.group(2), i))
        _launches(f, facts, i, line)


def analyze_batch(f: FileInfo, facts: list[Fact]) -> None:
    lines = f.text.split("\n")
    head = []
    for ln in lines:
        s = ln.strip()
        low = s.lower()
        if low.startswith("@echo") or not s:
            continue
        if low.startswith("rem ") or s.startswith("::"):
            head.append(s[3:].strip() if low.startswith("rem ") else s[2:].strip())
        else:
            break
    if head:
        f.summary, f.summary_source = first_sentence(" ".join(head), 300), "file comment"
    for i, raw in enumerate(lines, 1):
        s = raw.strip()
        low = s.lower()
        if not s or low.startswith(("rem ", "::", "@echo")) or low == "rem":
            continue
        m = re.match(r'(?i)set\s+"?(\w+)=([^"\n]*)"?', s)
        if m:
            facts.append(Fact("env_write", f.path, i, {"name": m.group(1), "value": m.group(2)}))
        for m in re.finditer(r"%(\w+)%", s):
            if not m.group(1).isdigit():
                facts.append(Fact("env_read", f.path, i, {"name": m.group(1), "default": ""}))
        for m in re.finditer(r"\"([^\"\n]*)\"", s):
            f.strings.append((m.group(1), i))
        _launches(f, facts, i, s)
