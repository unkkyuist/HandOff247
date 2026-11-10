---
generator: HandOff247
id: "op:get"
type: Operation
source: "Operations.cs"
---

# `get`

> handled by `Store.Get`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Store.Get`
- **Expression in the table:** `store.Get(args.Text("id"))`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:35](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L35)

**is handled by** →

- [`Store.cs`](../files/Store.cs.md) (Store.Get) · [Operations.cs:35](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L35)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:35](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L35)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:12](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L12)
- [`scripts/check-package.py`](../files/scripts__check-package.py.md) (cli(), by starting a process) · [scripts/check-package.py:59](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/check-package.py#L59)
- [`scripts/folders-smoke.py`](../files/scripts__folders-smoke.py.md) (call(), by starting a process) · [scripts/folders-smoke.py:39](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/folders-smoke.py#L39)
- [`scripts/graphify-playbook.py`](../files/scripts__graphify-playbook.py.md) (playbook(), by starting a process) · [scripts/graphify-playbook.py:79](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L79)
- [`scripts/harness-smoke.py`](../files/scripts__harness-smoke.py.md) (cli(), by starting a process) · [scripts/harness-smoke.py:72](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L72)
- [`scripts/ontology-smoke.py`](../files/scripts__ontology-smoke.py.md) (cli(), by starting a process) · [scripts/ontology-smoke.py:255](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L255)
- [`scripts/oz-package-smoke.py`](../files/scripts__oz-package-smoke.py.md) (playbook()) · [scripts/oz-package-smoke.py:205](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-package-smoke.py#L205)
- [`scripts/smoke.py`](../files/scripts__smoke.py.md) (cli(), by starting a process) · [scripts/smoke.py:49](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/smoke.py#L49)
- [`wwwroot/workspace-ui.js`](../files/wwwroot__workspace-ui.js.md) (api(), over HTTP) · [wwwroot/workspace-ui.js:111](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L111) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*

**is invoked by** ←

- [`get`](../tools/get.md) · [McpTools.cs:12](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L12)
