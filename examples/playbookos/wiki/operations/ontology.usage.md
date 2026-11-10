---
generator: HandOff247
id: "op:ontology.usage"
type: Operation
source: "Operations.cs"
---

# `ontology.usage`

> handled by `Ontology.Usage`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Ontology.Usage`
- **Expression in the table:** `ontology.Usage(args)`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:46](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L46)

**is handled by** →

- [`Ontology.cs`](../files/Ontology.cs.md) (Ontology.Usage) · [Operations.cs:46](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L46)

**is documented in** ←

- [`docs/ONTOLOGY.md`](../files/docs__ONTOLOGY.md.md) (cli ontology.usage) · [docs/ONTOLOGY.md:117](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/ONTOLOGY.md#L117)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:46](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L46)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:22](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L22)
- [`scripts/ontology-smoke.py`](../files/scripts__ontology-smoke.py.md) (cli(), by starting a process) · [scripts/ontology-smoke.py:233](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L233)
- [`wwwroot/ontology.js`](../files/wwwroot__ontology.js.md) (api(), over HTTP) · [wwwroot/ontology.js:118](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js#L118) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*

**is invoked by** ←

- [`ontology_usage`](../tools/ontology_usage.md) · [McpTools.cs:22](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L22)
