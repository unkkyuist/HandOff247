---
generator: HandOff247
id: "file:handoff247/render_html.py"
type: File
source: "handoff247/render_html.py"
---

# `handoff247/render_html.py`

> The single-file viewer. It embeds the Markdown pages and loads marked, DOMPurify and Mermaid from jsDelivr at pinned versions. Diagram nodes are matched back to files through the `flowchart-nN-` element ids, so clicking…

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 527
- **Source:** [handoff247/render_html.py](../../../../handoff247/render_html.py)

**Notes from the previous owner**

> The single-file viewer. It embeds the Markdown pages and loads marked, DOMPurify and Mermaid from jsDelivr at pinned versions. Diagram nodes are matched back to files through the `flowchart-nN-` element ids, so clicking a node opens that file's card. The Graph tab is hand-written canvas code with no library: a force layout with a fixed seed (the same picture every run), hit testing, and names drawn most-connected first without overlap. The eight colours are the `--g1`…`--g8` variables; do not add a ninth, give a new class a shape inside an existing group. Wiki pages are embedded too, and `resolveHref` turns their page-relative links into pack-relative ones.

**imports** →

- [`handoff247/__init__.py`](handoff247____init__.py.md) · [handoff247/render_html.py:9](../../../../handoff247/render_html.py#L9)

**mentions** →

- [`cdn.jsdelivr.net`](../hosts.md) · [handoff247/render_html.py:11](../../../../handoff247/render_html.py#L11)

**is part of** ←

- [`handoff247`](../areas/handoff247.md)

**is imported by** ←

- [`handoff247/build.py`](handoff247__build.py.md) · [handoff247/build.py:13](../../../../handoff247/build.py#L13)
- [`handoff247/workspace.py`](handoff247__workspace.py.md) · [handoff247/workspace.py:22](../../../../handoff247/workspace.py#L22)

## Comment in the file

Single-file interactive viewer (index.html). *(module docstring)*

## Defined here

- `render` — function, [line 491](../../../../handoff247/render_html.py#L491)
