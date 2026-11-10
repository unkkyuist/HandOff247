---
generator: HandOff247
id: "op:ontology.connections"
type: Operation
source: "Operations.cs"
---

# `ontology.connections`

> handled by `Ontology.Connections`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Ontology.Connections`
- **Expression in the table:** `ontology.Connections(args)`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:47](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L47)

**is handled by** →

- [`Ontology.cs`](../files/Ontology.cs.md) (Ontology.Connections) · [Operations.cs:47](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L47)

**is documented in** ←

- [`docs/ONTOLOGY.md`](../files/docs__ONTOLOGY.md.md) (cli ontology.connections) · [docs/ONTOLOGY.md:155](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/ONTOLOGY.md#L155)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:47](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L47)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:24](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L24)
- [`scripts/graphify-playbook.py`](../files/scripts__graphify-playbook.py.md) (playbook(), by starting a process) · [scripts/graphify-playbook.py:232](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L232)
- [`scripts/ontology-smoke.py`](../files/scripts__ontology-smoke.py.md) (cli(), by starting a process) · [scripts/ontology-smoke.py:371](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L371)
- [`wwwroot/ontology.js`](../files/wwwroot__ontology.js.md) (api(), over HTTP) · [wwwroot/ontology.js:235](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js#L235) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*

**is invoked by** ←

- [`ontology_connections`](../tools/ontology_connections.md) · [McpTools.cs:24](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L24)
