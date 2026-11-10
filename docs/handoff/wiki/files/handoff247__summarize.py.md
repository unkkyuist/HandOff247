---
generator: HandOff247
id: "file:handoff247/summarize.py"
type: File
source: "handoff247/summarize.py"
---

# `handoff247/summarize.py`

> The optional `--summarize` step. It shells out to `codex exec` (read-only sandbox, empty temporary folder, `--ephemeral`, an output schema) with batches of files and their analysis facts, and keeps the answers in `<note…

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 325
- **Source:** [handoff247/summarize.py](../../../../handoff247/summarize.py)

**Notes from the previous owner**

> The optional `--summarize` step. It shells out to `codex exec` (read-only sandbox, empty temporary folder, `--ephemeral`, an output schema) with batches of files and their analysis facts, and keeps the answers in `<notes>.summaries.json` keyed by path with a content hash. Rules to keep: a file with a note is never sent; key-like lines are replaced with `[removed]` before sending (`redact`); answers for ids that were not asked for are dropped; a summary whose file hash no longer matches is ignored. `prepare()` is what the CLI and the workspace call before writing a pack.

**defines** →

- `EngineError` · [handoff247/summarize.py:57](../../../../handoff247/summarize.py#L57)

**imports** →

- [`handoff247/__init__.py`](handoff247____init__.py.md) · [handoff247/summarize.py:27](../../../../handoff247/summarize.py#L27)
- [`handoff247/leaving.py`](handoff247__leaving.py.md) · [handoff247/summarize.py:27](../../../../handoff247/summarize.py#L27)
- [`handoff247/model.py`](handoff247__model.py.md) · [handoff247/summarize.py:28](../../../../handoff247/summarize.py#L28)

**is part of** ←

- [`handoff247`](../areas/handoff247.md)

**is imported by** ←

- [`handoff247/cli.py`](handoff247__cli.py.md) · [handoff247/cli.py:9](../../../../handoff247/cli.py#L9)
- [`handoff247/mcp.py`](handoff247__mcp.py.md) · [handoff247/mcp.py:22](../../../../handoff247/mcp.py#L22)
- [`handoff247/workspace.py`](handoff247__workspace.py.md) · [handoff247/workspace.py:17](../../../../handoff247/workspace.py#L17)

## Comment in the file

Optional: short descriptions of files, written by a language model through a command-line tool the user is already signed in to (today: the Codex CLI). *(module docstring)*

## Defined here

- `EngineError` — class, [line 57](../../../../handoff247/summarize.py#L57)
- `cache_path` — function, [line 62](../../../../handoff247/summarize.py#L62)
- `digest` — function, [line 68](../../../../handoff247/summarize.py#L68)
- `load_cache` — function, [line 72](../../../../handoff247/summarize.py#L72)
- `save_cache` — function, [line 80](../../../../handoff247/summarize.py#L80)
- `fresh` — function, [line 91](../../../../handoff247/summarize.py#L91) — Cache entries whose file still has the content they were written for.
- `attach` — function, [line 101](../../../../handoff247/summarize.py#L101) — Put the fresh summaries into ``project.links['model_summaries']``; returns how many.
- `redact` — function, [line 109](../../../../handoff247/summarize.py#L109)
- `targets` — function, [line 165](../../../../handoff247/summarize.py#L165)
- `batches` — function, [line 175](../../../../handoff247/summarize.py#L175)
- `parse_answer` — function, [line 189](../../../../handoff247/summarize.py#L189) — id -> summary, keeping only ids that were asked for and non-empty text.
- `codex_status` — function, [line 208](../../../../handoff247/summarize.py#L208)
- `codex_call` — function, [line 224](../../../../handoff247/summarize.py#L224)
- `prepare` — function, [line 254](../../../../handoff247/summarize.py#L254) — What every command does before writing a pack: load the cached summaries and, when ``args.summarize`` is set, write the missing ones first.
- `run` — function, [line 276](../../../../handoff247/summarize.py#L276) — Summarize every code file that has no note and no fresh summary yet.
