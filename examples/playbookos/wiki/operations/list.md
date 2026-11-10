---
generator: HandOff247
id: "op:list"
type: Operation
source: "Operations.cs"
---

# `list`

> handled by `Store.List`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Store.List`
- **Expression in the table:** `store.List(Optional("kind"), Optional("projectId"), Optional("query"))`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:34](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L34)

**is handled by** →

- [`Store.cs`](../files/Store.cs.md) (Store.List) · [Operations.cs:34](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L34)

**is documented in** ←

- [`README.en.md`](../files/README.en.md.md) (cli list) · [README.en.md:22](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.en.md#L22)
- [`README.md`](../files/README.md.md) (cli list) · [README.md:29](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.md#L29)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:34](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L34)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:10](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L10)
- [`portable/oz/install.py`](../files/portable__oz__install.py.md) (playbook()) · [portable/oz/install.py:162](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L162)
- [`portable/oz/oz_graphify_mcp.py`](../files/portable__oz__oz_graphify_mcp.py.md) (playbook()) · [portable/oz/oz_graphify_mcp.py:63](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_graphify_mcp.py#L63)
- [`scripts/folders-smoke.py`](../files/scripts__folders-smoke.py.md) (call(), by starting a process) · [scripts/folders-smoke.py:40](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/folders-smoke.py#L40)
- [`scripts/graphify-playbook.py`](../files/scripts__graphify-playbook.py.md) (playbook(), by starting a process) · [scripts/graphify-playbook.py:255](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L255)
- [`scripts/harness-smoke.py`](../files/scripts__harness-smoke.py.md) (atomic_cli(), by starting a process) · [scripts/harness-smoke.py:211](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L211)
- [`scripts/ontology-smoke.py`](../files/scripts__ontology-smoke.py.md) (cli(), by starting a process) · [scripts/ontology-smoke.py:100](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L100)
- [`wwwroot/app.js`](../files/wwwroot__app.js.md) (api(), over HTTP) · [wwwroot/app.js:53](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L53)

**is invoked by** ←

- [`list`](../tools/list.md) · [McpTools.cs:10](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L10)
