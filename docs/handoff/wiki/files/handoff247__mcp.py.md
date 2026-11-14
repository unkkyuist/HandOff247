---
generator: HandOff247
id: "file:handoff247/mcp.py"
type: File
source: "handoff247/mcp.py"
---

# `handoff247/mcp.py`

> The MCP server (`handoff247 mcp`): newline-delimited JSON-RPC on stdin/stdout, with `sys.stdout` pointed at stderr so stray prints cannot corrupt the protocol. Thirteen tools; only `handoff_write_note` and `handoff_buil…

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 496
- **Source:** [handoff247/mcp.py](../../../../handoff247/mcp.py)

**Notes from the previous owner**

> The MCP server (`handoff247 mcp`): newline-delimited JSON-RPC on stdin/stdout, with `sys.stdout` pointed at stderr so stray prints cannot corrupt the protocol. Thirteen tools; only `handoff_write_note` and `handoff_build` write. `handoff_overview` is the briefing an agent starts with; `handoff_users`, `handoff_request`, `handoff_feature`, `handoff_asset` and `handoff_impact` are thin wrappers over `explore.Explorer`; `handoff_page` renders any page of the pack in memory, and the same pages are offered as MCP resources when the server was started with a project folder. `handoff_write_note` accepts only skeleton headings (plus `Op:` for real operations), never overwrites filled text without `replace`, rejects key-like text and appends the agent mark. The analysed project is cached per folder and dropped after every write.

**defines** →

- [`handoff247/mcp.py:421`](../operations.md) · [handoff247/mcp.py:421](../../../../handoff247/mcp.py#L421)
- `Server` · [handoff247/mcp.py:165](../../../../handoff247/mcp.py#L165)
- `ToolError` · [handoff247/mcp.py:161](../../../../handoff247/mcp.py#L161)

**imports** →

- [`handoff247/__init__.py`](handoff247____init__.py.md) · [handoff247/mcp.py:27](../../../../handoff247/mcp.py#L27)
- [`handoff247/cli.py`](handoff247__cli.py.md) · [handoff247/mcp.py:290](../../../../handoff247/mcp.py#L290)
- [`handoff247/explore.py`](handoff247__explore.py.md) · [handoff247/mcp.py:28](../../../../handoff247/mcp.py#L28)
- [`handoff247/leaving.py`](handoff247__leaving.py.md) · [handoff247/mcp.py:27](../../../../handoff247/mcp.py#L27)
- [`handoff247/mermaid.py`](handoff247__mermaid.py.md) · [handoff247/mcp.py:207](../../../../handoff247/mcp.py#L207)
- [`handoff247/notes.py`](handoff247__notes.py.md) · [handoff247/mcp.py:29](../../../../handoff247/mcp.py#L29)
- [`handoff247/ontology.py`](handoff247__ontology.py.md) · [handoff247/mcp.py:27](../../../../handoff247/mcp.py#L27)
- [`handoff247/pipeline.py`](handoff247__pipeline.py.md) · [handoff247/mcp.py:30](../../../../handoff247/mcp.py#L30)
- [`handoff247/render_md.py`](handoff247__render_md.py.md) · [handoff247/mcp.py:302](../../../../handoff247/mcp.py#L302)
- [`handoff247/summarize.py`](handoff247__summarize.py.md) · [handoff247/mcp.py:27](../../../../handoff247/mcp.py#L27)
- [`handoff247/translate.py`](handoff247__translate.py.md) · [handoff247/mcp.py:27](../../../../handoff247/mcp.py#L27)
- [`handoff247/wiki.py`](handoff247__wiki.py.md) · [handoff247/mcp.py:27](../../../../handoff247/mcp.py#L27)

**refers to** →

- [`README.md`](README.md.md) · [handoff247/mcp.py:214](../../../../handoff247/mcp.py#L214)

**is part of** ←

- [`handoff247`](../areas/handoff247.md)

**is imported by** ←

- [`handoff247/cli.py`](handoff247__cli.py.md) · [handoff247/cli.py:207](../../../../handoff247/cli.py#L207)

## Comment in the file

MCP server (stdio, JSON-RPC 2.0, one message per line) so an AI agent can work with a project it has never seen: get a briefing of the whole project, follow what each kind of user sees and does, trace a user's request from their own words to the code, read any page of the pack, the ontology and the… *(module docstring)*

## Defined here

- `ToolError` — class, [line 161](../../../../handoff247/mcp.py#L161)
- `Server` — class, [line 165](../../../../handoff247/mcp.py#L165)
- `Server.root` — method, [line 172](../../../../handoff247/mcp.py#L172)
- `Server.model` — method, [line 181](../../../../handoff247/mcp.py#L181)
- `Server.forget` — method, [line 194](../../../../handoff247/mcp.py#L194)
- `Server.explorer` — method, [line 198](../../../../handoff247/mcp.py#L198)
- `Server.pages` — method, [line 202](../../../../handoff247/mcp.py#L202) — Every page of the pack as text, rendered once per project and kept until a note changes.
- `Server.handoff_overview` — method, [line 226](../../../../handoff247/mcp.py#L226)
- `Server.handoff_users` — method, [line 233](../../../../handoff247/mcp.py#L233)
- `Server.handoff_request` — method, [line 240](../../../../handoff247/mcp.py#L240)
- `Server.handoff_feature` — method, [line 247](../../../../handoff247/mcp.py#L247)
- `Server.handoff_asset` — method, [line 253](../../../../handoff247/mcp.py#L253)
- `Server.handoff_impact` — method, [line 259](../../../../handoff247/mcp.py#L259)
- `Server.handoff_page` — method, [line 266](../../../../handoff247/mcp.py#L266)
- `Server.handoff_build` — method, [line 288](../../../../handoff247/mcp.py#L288)
- `Server.handoff_todo` — method, [line 298](../../../../handoff247/mcp.py#L298)
- `Server.handoff_search` — method, [line 322](../../../../handoff247/mcp.py#L322)
- `Server.handoff_entity` — method, [line 335](../../../../handoff247/mcp.py#L335)
- `Server.handoff_source` — method, [line 359](../../../../handoff247/mcp.py#L359)
- `Server.handoff_write_note` — method, [line 376](../../../../handoff247/mcp.py#L376)
- `Server.handle` — method, [line 416](../../../../handoff247/mcp.py#L416)
- `serve` — function, [line 475](../../../../handoff247/mcp.py#L475)
