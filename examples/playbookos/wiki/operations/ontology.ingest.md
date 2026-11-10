---
generator: HandOff247
id: "op:ontology.ingest"
type: Operation
source: "Operations.cs"
---

# `ontology.ingest`

> handled by `Ontology.Ingest`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Ontology.Ingest`
- **Expression in the table:** `ontology.Ingest(args)`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:43](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L43)

**is handled by** →

- [`Ontology.cs`](../files/Ontology.cs.md) (Ontology.Ingest) · [Operations.cs:43](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L43)

**is documented in** ←

- [`docs/ONTOLOGY.md`](../files/docs__ONTOLOGY.md.md) (cli ontology.ingest) · [docs/ONTOLOGY.md:63](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/ONTOLOGY.md#L63)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:43](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L43)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Execute(), in-process) · [McpTools.cs:16](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L16)
- [`scripts/ontology-smoke.py`](../files/scripts__ontology-smoke.py.md) (cli(), by starting a process) · [scripts/ontology-smoke.py:195](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L195)
- [`wwwroot/ontology.js`](../files/wwwroot__ontology.js.md) (api(), over HTTP) · [wwwroot/ontology.js:217](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js#L217) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*

**is invoked by** ←

- [`ontology_ingest`](../tools/ontology_ingest.md) · [McpTools.cs:16](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L16)
