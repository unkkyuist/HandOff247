"""Data model shared by every analyzer and renderer.

Everything HandOff247 reports is either an *observed* fact (found in a file, with a
file:line location) or a *note* written by a person in the notes file. Analyzers never
guess intent; when a pattern is ambiguous it is left out rather than reported wrong.
"""
from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Any


@dataclass
class Symbol:
    name: str
    kind: str                     # class, record, struct, interface, enum, function, method, export
    line: int
    doc: str = ""                 # first sentence of the doc comment / docstring, if any
    parent: str = ""              # enclosing type for methods
    public: bool = True
    end_line: int = 0             # last line of the body when known


@dataclass
class Fact:
    """One observation. ``kind`` decides how ``data`` is interpreted.

    kinds: entry, mode, dispatch, call, route, http_call, mcp_tool, env_read, env_write,
    launch, port, path_literal, cli_usage, mcp_client, package, subcommand
    """
    kind: str
    file: str
    line: int
    data: dict[str, Any] = field(default_factory=dict)


@dataclass
class FileInfo:
    path: str                     # project-relative, forward slashes
    lang: str
    category: str                 # code, script, web, docs, config, test, data, other
    lines: int = 0
    size: int = 0
    summary: str = ""             # leading comment / docstring / first paragraph
    summary_source: str = ""      # where the summary came from (comment, docstring, heading)
    symbols: list[Symbol] = field(default_factory=list)
    imports: list[tuple[str, int]] = field(default_factory=list)   # (raw target, line)
    strings: list[tuple[str, int]] = field(default_factory=list)   # string literals (value, line)
    tags: list[str] = field(default_factory=list)
    skipped: str = ""             # reason the file was not parsed
    translated: list[dict[str, str]] = field(default_factory=list)   # {where, original} replaced by an English version
    # private analyzer state (not serialised)
    text: str = field(default="", repr=False)
    code: str = field(default="", repr=False)        # comments and string contents blanked
    code_str: str = field(default="", repr=False)    # comments blanked, strings kept

    def to_json(self) -> dict[str, Any]:
        d = asdict(self)
        for k in ("text", "code", "code_str", "strings"):
            d.pop(k, None)
        return d


@dataclass
class Edge:
    src: str
    dst: str
    kind: str                     # uses, injects, imports, loads, runs, refers, calls-op, documents
    line: int = 0
    count: int = 1
    label: str = ""


@dataclass
class Project:
    name: str
    root: str                     # absolute path (never written to output)
    files: list[FileInfo] = field(default_factory=list)
    facts: list[Fact] = field(default_factory=list)
    edges: list[Edge] = field(default_factory=list)
    links: dict[str, Any] = field(default_factory=dict)     # resolved cross-file structures
    git: dict[str, Any] = field(default_factory=dict)

    def file(self, path: str) -> FileInfo | None:
        for f in self.files:
            if f.path == path:
                return f
        return None

    def facts_of(self, kind: str) -> list[Fact]:
        return [f for f in self.facts if f.kind == kind]
