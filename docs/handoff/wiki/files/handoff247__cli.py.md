---
generator: HandOff247
id: "file:handoff247/cli.py"
type: File
source: "handoff247/cli.py"
---

# `handoff247/cli.py`

> Six commands: `go`, `build`, `notes`, `check`, `mcp`, `trace`. `trace` answers a question from the user's side (a request in words, a user type, a feature, an asset, a code file) without writing a pack. A first argument…

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 276
- **Source:** [handoff247/cli.py](../../../../handoff247/cli.py)

**Notes from the previous owner**

> Six commands: `go`, `build`, `notes`, `check`, `mcp`, `trace`. `trace` answers a question from the user's side (a request in words, a user type, a feature, an asset, a code file) without writing a pack. A first argument that is not a command is taken as a folder for `go`. `go` decides between one project and a folder of projects (`workspace.is_workspace`), then does notes + build + report. `check --min N` exits 1 when fewer than N% of files have notes, which is how CI can enforce documentation.

**defines** →

- [`build`](../subcommands.md) · [handoff247/cli.py:172](../../../../handoff247/cli.py#L172)
- [`check`](../subcommands.md) · [handoff247/cli.py:182](../../../../handoff247/cli.py#L182)
- [`go`](../subcommands.md) · [handoff247/cli.py:162](../../../../handoff247/cli.py#L162)
- [`mcp`](../subcommands.md) · [handoff247/cli.py:185](../../../../handoff247/cli.py#L185)
- [`notes`](../subcommands.md) · [handoff247/cli.py:180](../../../../handoff247/cli.py#L180)
- [`trace`](../subcommands.md) · [handoff247/cli.py:188](../../../../handoff247/cli.py#L188)

**imports** →

- [`handoff247/__init__.py`](handoff247____init__.py.md) · [handoff247/cli.py:9](../../../../handoff247/cli.py#L9)
- [`handoff247/build.py`](handoff247__build.py.md) · [handoff247/cli.py:10](../../../../handoff247/cli.py#L10)
- [`handoff247/explore.py`](handoff247__explore.py.md) · [handoff247/cli.py:113](../../../../handoff247/cli.py#L113)
- [`handoff247/leaving.py`](handoff247__leaving.py.md) · [handoff247/cli.py:9](../../../../handoff247/cli.py#L9)
- [`handoff247/mcp.py`](handoff247__mcp.py.md) · [handoff247/cli.py:207](../../../../handoff247/cli.py#L207)
- [`handoff247/notes.py`](handoff247__notes.py.md) · [handoff247/cli.py:11](../../../../handoff247/cli.py#L11)
- [`handoff247/pipeline.py`](handoff247__pipeline.py.md) · [handoff247/cli.py:12](../../../../handoff247/cli.py#L12)
- [`handoff247/render_md.py`](handoff247__render_md.py.md) · [handoff247/cli.py:262](../../../../handoff247/cli.py#L262)
- [`handoff247/summarize.py`](handoff247__summarize.py.md) · [handoff247/cli.py:9](../../../../handoff247/cli.py#L9)
- [`handoff247/translate.py`](handoff247__translate.py.md) · [handoff247/cli.py:9](../../../../handoff247/cli.py#L9)
- [`handoff247/workspace.py`](handoff247__workspace.py.md) · [handoff247/cli.py:9](../../../../handoff247/cli.py#L9)

**mentions** →

- [`github.com`](../hosts.md) · [handoff247/cli.py:177](../../../../handoff247/cli.py#L177)

**is part of** ←

- [`handoff247`](../areas/handoff247.md)

**is imported by** ←

- [`handoff247/__main__.py`](handoff247____main__.py.md) · [handoff247/__main__.py:1](../../../../handoff247/__main__.py#L1)
- [`handoff247/mcp.py`](handoff247__mcp.py.md) · [handoff247/mcp.py:290](../../../../handoff247/mcp.py#L290)
- [`tests/test_handoff.py`](tests__test_handoff.py.md) · [tests/test_handoff.py:17](../../../../tests/test_handoff.py#L17)

## Comment in the file

Command line: build a pack, create/extend the notes file, check documentation coverage. *(module docstring)*

## Defined here

- `main` — function, [line 148](../../../../handoff247/cli.py#L148)
