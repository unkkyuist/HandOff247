"""Markdown/text documents and configuration files (MSBuild, package.json, pyproject,
requirements, MCP client configs, Dockerfile, GitHub workflows)."""
from __future__ import annotations

import json
import re

from ..lexer import first_sentence
from ..model import Fact, FileInfo, Symbol

try:  # Python 3.11+
    import tomllib
except ImportError:  # pragma: no cover
    tomllib = None


def analyze_markdown(f: FileInfo, facts: list[Fact]) -> None:
    text = f.text
    in_code = False
    para: list[str] = []
    first_para = ""
    title = ""
    code_lines = []
    for i, line in enumerate(text.split("\n"), 1):
        s = line.strip()
        if s.startswith("```") or s.startswith("~~~"):
            in_code = not in_code
            continue
        if in_code:
            code_lines.append((i, line))
            continue
        m = re.match(r"(#{1,6})\s+(.*?)\s*#*$", s)
        if m:
            level = len(m.group(1))
            if not title and level == 1:
                title = m.group(2)
            if level <= 3:
                f.symbols.append(Symbol(m.group(2)[:120], f"h{level}", i))
            if para and not first_para:
                first_para = " ".join(para)
            para = []
            continue
        if not s:
            if para and not first_para:
                first_para = " ".join(para)
            para = []
            continue
        if not first_para and not s.startswith(("|", "<", "!", "[!", "---", "- [", ">")):
            para.append(s)
    if para and not first_para:
        first_para = " ".join(para)
    clean = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", first_para)
    clean = re.sub(r"[*_`]{1,3}", "", clean)
    if clean:
        f.summary, f.summary_source = first_sentence(clean, 300), "first paragraph"
    elif title:
        f.summary, f.summary_source = title, "title"
    for m in re.finditer(r"(?<!!)\[[^\]]*\]\(([^)\s#]+)(?:#[^)]*)?\)", text):
        target = m.group(1)
        if not re.match(r"[a-z]+:", target):
            f.imports.append((target, text.count("\n", 0, m.start()) + 1))
    for i, line in code_lines:
        for m in re.finditer(r"(['\"])((?:[^'\"\n])*?)\1", line):
            f.strings.append((m.group(2), i))
    if code_lines:
        facts.append(Fact("doc_code", f.path, code_lines[0][0], {"lines": [[i, l[:300]] for i, l in code_lines[:400]]}))


def analyze_text(f: FileInfo, facts: list[Fact]) -> None:
    for line in f.text.split("\n"):
        s = line.strip()
        if s:
            f.summary, f.summary_source = first_sentence(s, 200), "first line"
            break


def _mcp_clients(f: FileInfo, facts: list[Fact], servers: dict) -> None:
    for name, cfg in servers.items():
        if not isinstance(cfg, dict):
            continue
        args = cfg.get("args") or []
        if not isinstance(args, list):
            args = [str(args)]
        facts.append(Fact("mcp_client", f.path, _line_of(f.text, name), {
            "server": name, "command": str(cfg.get("command", "")), "args": [str(a) for a in args],
            "url": str(cfg.get("url", cfg.get("serverUrl", ""))), "env": sorted((cfg.get("env") or {}).keys())}))


def _line_of(text: str, needle: str) -> int:
    idx = text.find(needle)
    return text.count("\n", 0, idx) + 1 if idx >= 0 else 1


def analyze_json(f: FileInfo, facts: list[Fact]) -> None:
    try:
        data = json.loads(re.sub(r"(?m)^\s*//.*$", "", f.text)) if f.text.strip() else None
    except (json.JSONDecodeError, ValueError):
        return
    name = f.path.rsplit("/", 1)[-1].lower()
    if isinstance(data, dict):
        if isinstance(data.get("mcpServers"), dict):
            _mcp_clients(f, facts, data["mcpServers"])
        if isinstance(data.get("servers"), dict) and name.endswith("mcp.json"):
            _mcp_clients(f, facts, data["servers"])
        if name == "package.json":
            f.summary = str(data.get("description") or data.get("name") or "")
            f.summary_source = "package.json"
            for script, cmd in (data.get("scripts") or {}).items():
                facts.append(Fact("launch", f.path, _line_of(f.text, f'"{script}"'), {
                    "cmd": str(cmd).split(" ", 1)[0], "text": str(cmd)[:220], "script": script}))
                f.symbols.append(Symbol(f"npm run {script}", "script", _line_of(f.text, f'"{script}"'), str(cmd)[:160]))
            for section in ("dependencies", "devDependencies", "peerDependencies"):
                for dep, ver in (data.get(section) or {}).items():
                    facts.append(Fact("package", f.path, _line_of(f.text, f'"{dep}"'), {
                        "name": dep, "version": str(ver), "ecosystem": "npm", "dev": section != "dependencies"}))
            bins = data.get("bin")
            if isinstance(bins, dict):
                for b, target in bins.items():
                    facts.append(Fact("entry", f.path, _line_of(f.text, b), {"style": f"npm bin {b} -> {target}"}))
            if data.get("main"):
                f.imports.append((str(data["main"]), _line_of(f.text, '"main"')))
        if name == "launchsettings.json" and isinstance(data.get("profiles"), dict):
            for prof, cfg in data["profiles"].items():
                if isinstance(cfg, dict) and cfg.get("applicationUrl"):
                    facts.append(Fact("listen", f.path, _line_of(f.text, prof), {"value": str(cfg["applicationUrl"]), "profile": prof}))
        top = [k for k in data.keys()][:20]
        if top and not f.summary:
            f.summary, f.summary_source = "keys: " + ", ".join(map(str, top)), "json keys"


def analyze_toml(f: FileInfo, facts: list[Fact]) -> None:
    if tomllib is None:
        return
    try:
        data = tomllib.loads(f.text)
    except (tomllib.TOMLDecodeError, ValueError):
        return
    if isinstance(data.get("mcp_servers"), dict):
        _mcp_clients(f, facts, data["mcp_servers"])
    proj = data.get("project") or {}
    if proj:
        f.summary, f.summary_source = str(proj.get("description") or proj.get("name") or ""), "pyproject"
        for dep in proj.get("dependencies") or []:
            nm = re.split(r"[<>=!~ ;\[]", str(dep), 1)[0]
            facts.append(Fact("package", f.path, _line_of(f.text, nm), {"name": nm, "version": str(dep)[len(nm):].strip(),
                                                                       "ecosystem": "pypi", "dev": False}))
        for script, target in (proj.get("scripts") or {}).items():
            facts.append(Fact("entry", f.path, _line_of(f.text, script), {"style": f"console script {script} -> {target}"}))
            f.symbols.append(Symbol(script, "script", _line_of(f.text, script), str(target)))
    lines = [l for l in f.text.split("\n") if l.strip().startswith("#")]
    if lines and not f.summary:
        f.summary, f.summary_source = first_sentence(lines[0].lstrip("# ").strip(), 200), "file comment"


def analyze_requirements(f: FileInfo, facts: list[Fact]) -> None:
    for i, line in enumerate(f.text.split("\n"), 1):
        s = line.split("#", 1)[0].strip()
        if not s or s.startswith("-"):
            continue
        nm = re.split(r"[<>=!~ ;\[]", s, 1)[0]
        facts.append(Fact("package", f.path, i, {"name": nm, "version": s[len(nm):].strip(), "ecosystem": "pypi", "dev": False}))


def analyze_msbuild(f: FileInfo, facts: list[Fact]) -> None:
    text = f.text
    sdk = re.search(r'<Project\s+Sdk="([^"]+)"', text)
    tfm = re.search(r"<TargetFrameworks?>([^<]+)</TargetFrameworks?>", text)
    out = re.search(r"<OutputType>([^<]+)</OutputType>", text)
    asm = re.search(r"<AssemblyName>([^<]+)</AssemblyName>", text)
    ver = re.search(r"<Version>([^<]+)</Version>", text)
    stem = f.path.rsplit("/", 1)[-1].rsplit(".", 1)[0]
    assembly = asm.group(1) if asm else stem
    bits = [b for b in [sdk.group(1) if sdk else "", tfm.group(1) if tfm else "", out.group(1) if out else "",
                        f"v{ver.group(1)}" if ver else ""] if b]
    f.summary, f.summary_source = f"{assembly}: " + ", ".join(bits), "project file"
    facts.append(Fact("build_target", f.path, 1, {"assembly": assembly, "sdk": sdk.group(1) if sdk else "",
                                                  "framework": tfm.group(1) if tfm else "",
                                                  "output": out.group(1) if out else ("Exe" if sdk and "Web" in sdk.group(1) else ""),
                                                  "version": ver.group(1) if ver else ""}))
    for m in re.finditer(r'<PackageReference\s+Include="([^"]+)"(?:\s+Version="([^"]*)")?', text):
        facts.append(Fact("package", f.path, text.count("\n", 0, m.start()) + 1,
                          {"name": m.group(1), "version": m.group(2) or "", "ecosystem": "nuget", "dev": False}))
    for m in re.finditer(r'<ProjectReference\s+Include="([^"]+)"', text):
        f.imports.append((m.group(1).replace("\\", "/"), text.count("\n", 0, m.start()) + 1))


def analyze_dockerfile(f: FileInfo, facts: list[Fact]) -> None:
    for i, line in enumerate(f.text.split("\n"), 1):
        s = line.strip()
        m = re.match(r"(?i)EXPOSE\s+(.+)", s)
        if m:
            for port in re.findall(r"\d{2,5}", m.group(1)):
                facts.append(Fact("listen", f.path, i, {"value": port}))
        m = re.match(r"(?i)(CMD|ENTRYPOINT)\s+(.+)", s)
        if m:
            facts.append(Fact("launch", f.path, i, {"cmd": m.group(1).upper(), "text": m.group(2)[:220]}))
        m = re.match(r"(?i)ENV\s+(\w+)[= ](.*)", s)
        if m:
            facts.append(Fact("env_write", f.path, i, {"name": m.group(1), "value": m.group(2).strip()}))


def analyze_yaml(f: FileInfo, facts: list[Fact]) -> None:
    if "/.github/workflows/" not in "/" + f.path:
        return
    name = re.search(r"(?m)^name:\s*(.+)$", f.text)
    if name:
        f.summary, f.summary_source = "CI workflow: " + name.group(1).strip().strip("'\""), "workflow name"
    for i, line in enumerate(f.text.split("\n"), 1):
        m = re.match(r"\s*(?:-\s*)?run:\s*(.+)", line)
        if m and m.group(1).strip() not in ("|", ">"):
            facts.append(Fact("launch", f.path, i, {"cmd": m.group(1).split()[0], "text": m.group(1).strip()[:220], "ci": True}))
