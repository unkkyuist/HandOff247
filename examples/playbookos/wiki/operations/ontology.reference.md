---
generator: HandOff247
id: "op:ontology.reference"
type: Operation
source: "Operations.cs"
---

# `ontology.reference`

> handled by `Ontology.Reference`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Ontology.Reference`
- **Expression in the table:** `ontology.Reference(args)`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:45](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L45)

**is handled by** →

- [`Ontology.cs`](../files/Ontology.cs.md) (Ontology.Reference) · [Operations.cs:45](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L45)

**is documented in** ←

- [`docs/ONTOLOGY.md`](../files/docs__ONTOLOGY.md.md) (cli ontology.reference) · [docs/ONTOLOGY.md:115](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/ONTOLOGY.md#L115)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:45](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L45)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:20](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L20)
- [`scripts/ontology-smoke.py`](../files/scripts__ontology-smoke.py.md) (cli(), by starting a process) · [scripts/ontology-smoke.py:163](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L163)
- [`wwwroot/ontology.js`](../files/wwwroot__ontology.js.md) (api(), over HTTP) · [wwwroot/ontology.js:111](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js#L111) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*

**is invoked by** ←

- [`ontology_reference`](../tools/ontology_reference.md) · [McpTools.cs:20](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L20)
