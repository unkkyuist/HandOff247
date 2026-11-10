---
generator: HandOff247
id: "file:handoff247/mcp.py"
type: File
source: "handoff247/mcp.py"
---

# `handoff247/mcp.py`

> The MCP server (`handoff247 mcp`): newline-delimited JSON-RPC on stdin/stdout, with `sys.stdout` pointed at stderr so stray prints cannot corrupt the protocol. Six tools; only `handoff_write_note` and `handoff_build` wr…

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 311
- **Source:** [handoff247/mcp.py](../../../../handoff247/mcp.py)

**Notes from the previous owner**

> The MCP server (`handoff247 mcp`): newline-delimited JSON-RPC on stdin/stdout, with `sys.stdout` pointed at stderr so stray prints cannot corrupt the protocol. Six tools; only `handoff_write_note` and `handoff_build` write. `handoff_write_note` accepts only skeleton headings (plus `Op:` for real operations), never overwrites filled text without `replace`, rejects key-like text and appends the agent mark. The analysed project is cached per folder and dropped after every write.

**defines** →

- [`handoff247/mcp.py:250`](../operations.md) · [handoff247/mcp.py:250](../../../../handoff247/mcp.py#L250)
- `Server` · [handoff247/mcp.py:86](../../../../handoff247/mcp.py#L86)
- `ToolError` · [handoff247/mcp.py:82](../../../../handoff247/mcp.py#L82)

**imports** →

- [`handoff247/__init__.py`](handoff247____init__.py.md) · [handoff247/mcp.py:22](../../../../handoff247/mcp.py#L22)
- [`handoff247/cli.py`](handoff247__cli.py.md) · [handoff247/mcp.py:119](../../../../handoff247/mcp.py#L119)
- [`handoff247/leaving.py`](handoff247__leaving.py.md) · [handoff247/mcp.py:22](../../../../handoff247/mcp.py#L22)
- [`handoff247/notes.py`](handoff247__notes.py.md) · [handoff247/mcp.py:23](../../../../handoff247/mcp.py#L23)
- [`handoff247/ontology.py`](handoff247__ontology.py.md) · [handoff247/mcp.py:22](../../../../handoff247/mcp.py#L22)
- [`handoff247/pipeline.py`](handoff247__pipeline.py.md) · [handoff247/mcp.py:24](../../../../handoff247/mcp.py#L24)
- [`handoff247/render_md.py`](handoff247__render_md.py.md) · [handoff247/mcp.py:131](../../../../handoff247/mcp.py#L131)
- [`handoff247/summarize.py`](handoff247__summarize.py.md) · [handoff247/mcp.py:22](../../../../handoff247/mcp.py#L22)
- [`handoff247/translate.py`](handoff247__translate.py.md) · [handoff247/mcp.py:22](../../../../handoff247/mcp.py#L22)

**is part of** ←

- [`handoff247`](../areas/handoff247.md)

**is imported by** ←

- [`handoff247/cli.py`](handoff247__cli.py.md) · [handoff247/cli.py:150](../../../../handoff247/cli.py#L150)

## Comment in the file

MCP server (stdio, JSON-RPC 2.0, one message per line) so an AI agent can work on a handoff: build the pack, see what is still undocumented, read the ontology and the source, and write notes under the right heading. *(module docstring)*

## Defined here

- `ToolError` — class, [line 82](../../../../handoff247/mcp.py#L82)
- `Server` — class, [line 86](../../../../handoff247/mcp.py#L86)
- `Server.root` — method, [line 92](../../../../handoff247/mcp.py#L92)
- `Server.model` — method, [line 101](../../../../handoff247/mcp.py#L101)
- `Server.forget` — method, [line 113](../../../../handoff247/mcp.py#L113)
- `Server.handoff_build` — method, [line 117](../../../../handoff247/mcp.py#L117)
- `Server.handoff_todo` — method, [line 127](../../../../handoff247/mcp.py#L127)
- `Server.handoff_search` — method, [line 151](../../../../handoff247/mcp.py#L151)
- `Server.handoff_entity` — method, [line 164](../../../../handoff247/mcp.py#L164)
- `Server.handoff_source` — method, [line 188](../../../../handoff247/mcp.py#L188)
- `Server.handoff_write_note` — method, [line 205](../../../../handoff247/mcp.py#L205)
- `Server.handle` — method, [line 245](../../../../handoff247/mcp.py#L245)
- `serve` — function, [line 290](../../../../handoff247/mcp.py#L290)
