---
generator: HandOff247
id: "file:handoff247/workspace.py"
type: File
source: "handoff247/workspace.py"
---

# `handoff247/workspace.py`

> The folder-of-projects mode: finds projects one or two levels down, builds a pack for each, and writes the index (README.md, index.html, workspace.json, workspace.mmd). It does not write into the projects: notes for a p…

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 345
- **Source:** [handoff247/workspace.py](../../../../handoff247/workspace.py)

**Notes from the previous owner**

> The folder-of-projects mode: finds projects one or two levels down, builds a pack for each, and writes the index (README.md, index.html, workspace.json, workspace.mmd). It does not write into the projects: notes for a project without its own notes file go to `<out>/notes/`. One failing project is listed as failed and the rest continue. Cross-project arrows come only from paths that resolve into another project's folder.

**imports** →

- [`handoff247/__init__.py`](handoff247____init__.py.md) · [handoff247/workspace.py:16](../../../../handoff247/workspace.py#L16)
- [`handoff247/build.py`](handoff247__build.py.md) · [handoff247/workspace.py:17](../../../../handoff247/workspace.py#L17)
- [`handoff247/inventory.py`](handoff247__inventory.py.md) · [handoff247/workspace.py:18](../../../../handoff247/workspace.py#L18)
- [`handoff247/leaving.py`](handoff247__leaving.py.md) · [handoff247/workspace.py:16](../../../../handoff247/workspace.py#L16)
- [`handoff247/mermaid.py`](handoff247__mermaid.py.md) · [handoff247/workspace.py:19](../../../../handoff247/workspace.py#L19)
- [`handoff247/notes.py`](handoff247__notes.py.md) · [handoff247/workspace.py:20](../../../../handoff247/workspace.py#L20)
- [`handoff247/pipeline.py`](handoff247__pipeline.py.md) · [handoff247/workspace.py:21](../../../../handoff247/workspace.py#L21)
- [`handoff247/render_html.py`](handoff247__render_html.py.md) · [handoff247/workspace.py:22](../../../../handoff247/workspace.py#L22)
- [`handoff247/render_md.py`](handoff247__render_md.py.md) · [handoff247/workspace.py:23](../../../../handoff247/workspace.py#L23)

**refers to** →

- [`README.md`](README.md.md) · [handoff247/workspace.py:340](../../../../handoff247/workspace.py#L340)
- [`pyproject.toml`](pyproject.toml.md) · [handoff247/workspace.py:25](../../../../handoff247/workspace.py#L25)

**is part of** ←

- [`handoff247`](../areas/handoff247.md)

**is imported by** ←

- [`handoff247/cli.py`](handoff247__cli.py.md) · [handoff247/cli.py:9](../../../../handoff247/cli.py#L9)

## Comment in the file

A folder that holds several projects: one pack per project plus an index of all of them. *(module docstring)*

## Defined here

- `project_reason` — function, [line 32](../../../../handoff247/workspace.py#L32) — Why a folder counts as a project ('' when it does not).
- `find_projects` — function, [line 66](../../../../handoff247/workspace.py#L66) — Projects one or two levels below ``root`` and the folders where none was recognised.
- `is_workspace` — function, [line 84](../../../../handoff247/workspace.py#L84) — True when ``root`` holds projects rather than being one: it has no manifest of its own or at least two sub-folders that are their own Git repositories.
- `slug` — function, [line 94](../../../../handoff247/workspace.py#L94)
- `cross_refs` — function, [line 102](../../../../handoff247/workspace.py#L102) — Paths in this project's files that point into another project's folder.
- `attention` — function, [line 169](../../../../handoff247/workspace.py#L169) — What must not be lost when the computer goes away, most serious first.
- `summarize` — function, [line 191](../../../../handoff247/workspace.py#L191)
- `diagram` — function, [line 210](../../../../handoff247/workspace.py#L210)
- `index_md` — function, [line 226](../../../../handoff247/workspace.py#L226)
- `index_html` — function, [line 290](../../../../handoff247/workspace.py#L290)
- `build_workspace` — function, [line 304](../../../../handoff247/workspace.py#L304)
