---
generator: HandOff247
id: "op:ontology.search"
type: Operation
source: "Operations.cs"
---

# `ontology.search`

> handled by `Ontology.Search`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Ontology.Search`
- **Expression in the table:** `ontology.Search(args)`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:44](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L44)

**is handled by** →

- [`Ontology.cs`](../files/Ontology.cs.md) (Ontology.Search) · [Operations.cs:44](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L44)

**is documented in** ←

- [`docs/GRAPHIFY.md`](../files/docs__GRAPHIFY.md.md) (cli ontology.search) · [docs/GRAPHIFY.md:107](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/GRAPHIFY.md#L107)
- [`docs/ONTOLOGY.md`](../files/docs__ONTOLOGY.md.md) (cli ontology.search) · [docs/ONTOLOGY.md:114](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/ONTOLOGY.md#L114)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:44](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L44)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:18](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L18)
- [`scripts/graphify-smoke.py`](../files/scripts__graphify-smoke.py.md) (playbook()) · [scripts/graphify-smoke.py:134](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-smoke.py#L134)
- [`scripts/harness-smoke.py`](../files/scripts__harness-smoke.py.md) (cli(), by starting a process) · [scripts/harness-smoke.py:89](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L89)
- [`scripts/ontology-smoke.py`](../files/scripts__ontology-smoke.py.md) (cli(), by starting a process) · [scripts/ontology-smoke.py:97](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L97)
- [`wwwroot/ontology.js`](../files/wwwroot__ontology.js.md) (api(), over HTTP) · [wwwroot/ontology.js:159](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js#L159) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*

**is invoked by** ←

- [`ontology_search`](../tools/ontology_search.md) · [McpTools.cs:18](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L18)
