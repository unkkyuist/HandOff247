---
generator: HandOff247
id: "file:handoff247/leaving.py"
type: File
source: "handoff247/leaving.py"
---

# `handoff247/leaving.py`

> The handover findings: Git state (uncommitted, commits on no remote, stashes, authors), files Git ignores that are present, absolute paths, hosts in URLs, TODO comments, key and token patterns, declared tool versions, a…

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 383
- **Source:** [handoff247/leaving.py](../../../../handoff247/leaving.py)

**Notes from the previous owner**

> The handover findings: Git state (uncommitted, commits on no remote, stashes, authors), files Git ignores that are present, absolute paths, hosts in URLs, TODO comments, key and token patterns, declared tool versions, and the readiness rows. Two rules to keep: a secret hit records file, line and kind but never the value, and anything that cannot be known is left out (no history figures for shallow clones, no "pushed" row without a remote). `JUNK_DIRS` decides which ignored folders are build output; add to it when a pack lists noise.

**defines** →

- [`handoff247/leaving.py:257`](../operations.md) · [handoff247/leaving.py:257](../../../../handoff247/leaving.py#L257)

**imports** →

- [`handoff247/inventory.py`](handoff247__inventory.py.md) · [handoff247/leaving.py:15](../../../../handoff247/leaving.py#L15)
- [`handoff247/model.py`](handoff247__model.py.md) · [handoff247/leaving.py:16](../../../../handoff247/leaving.py#L16)

**refers to** →

- [`HANDOFF.notes.md`](HANDOFF.notes.md.md) · [handoff247/leaving.py:18](../../../../handoff247/leaving.py#L18)
- [`README.md`](README.md.md) · [handoff247/leaving.py:66](../../../../handoff247/leaving.py#L66)
- [`pyproject.toml`](pyproject.toml.md) · [handoff247/leaving.py:239](../../../../handoff247/leaving.py#L239)

**starts** →

- [`git`](../commands.md) · [handoff247/leaving.py:73](../../../../handoff247/leaving.py#L73)

**is part of** ←

- [`handoff247`](../areas/handoff247.md)

**is imported by** ←

- [`handoff247/cli.py`](handoff247__cli.py.md) · [handoff247/cli.py:9](../../../../handoff247/cli.py#L9)
- [`handoff247/mcp.py`](handoff247__mcp.py.md) · [handoff247/mcp.py:22](../../../../handoff247/mcp.py#L22)
- [`handoff247/pipeline.py`](handoff247__pipeline.py.md) · [handoff247/pipeline.py:6](../../../../handoff247/pipeline.py#L6)
- [`handoff247/render_md.py`](handoff247__render_md.py.md) · [handoff247/render_md.py:7](../../../../handoff247/render_md.py#L7)
- [`handoff247/summarize.py`](handoff247__summarize.py.md) · [handoff247/summarize.py:27](../../../../handoff247/summarize.py#L27)
- [`handoff247/workspace.py`](handoff247__workspace.py.md) · [handoff247/workspace.py:16](../../../../handoff247/workspace.py#L16)

## Comment in the file

What the code alone cannot hand over: unfinished work, things that exist only on the computer the pack was generated on, accounts and services, tools to install, people. *(module docstring)*

## Defined here

- `git_state` — function, [line 80](../../../../handoff247/leaving.py#L80) — State of the checkout the pack is generated from.
- `local_only` — function, [line 127](../../../../handoff247/leaving.py#L127) — Files and folders Git ignores that are present in this checkout: the successor will not get them through the repository.
- `prerequisites` — function, [line 228](../../../../handoff247/leaving.py#L228) — Runtimes and tool versions the project declares.
- `commands_used` — function, [line 279](../../../../handoff247/leaving.py#L279) — Well-known command-line tools the project's scripts and configs start.
- `secret_env` — function, [line 292](../../../../handoff247/leaving.py#L292)
- `collect` — function, [line 300](../../../../handoff247/leaving.py#L300) — Fill ``project.links['leaving']``.
- `start_known` — function, [line 319](../../../../handoff247/leaving.py#L319)
- `readiness` — function, [line 325](../../../../handoff247/leaving.py#L325) — The handover checklist: one row per check, state 'ok', 'todo' or 'na' (cannot be known).
- `score` — function, [line 381](../../../../handoff247/leaving.py#L381)
