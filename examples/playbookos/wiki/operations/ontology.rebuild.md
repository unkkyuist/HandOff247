---
generator: HandOff247
id: "op:ontology.rebuild"
type: Operation
source: "Operations.cs"
---

# `ontology.rebuild`

> handled by `Ontology.Rebuild`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Ontology.Rebuild`
- **Expression in the table:** `ontology.Rebuild(args)`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:50](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L50)

**is handled by** →

- [`Ontology.cs`](../files/Ontology.cs.md) (Ontology.Rebuild) · [Operations.cs:50](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L50)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:50](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L50)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:30](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L30)
- [`scripts/ontology-smoke.py`](../files/scripts__ontology-smoke.py.md) (cli(), by starting a process) · [scripts/ontology-smoke.py:304](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L304)
- [`wwwroot/ontology.js`](../files/wwwroot__ontology.js.md) (api(), over HTTP) · [wwwroot/ontology.js:94](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js#L94) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*

**is invoked by** ←

- [`ontology_rebuild`](../tools/ontology_rebuild.md) · [McpTools.cs:30](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L30)
