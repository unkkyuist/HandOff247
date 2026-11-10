---
generator: HandOff247
id: "op:context"
type: Operation
source: "Operations.cs"
---

# `context`

> handled by `Workspace.Context`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Workspace.Context`
- **Expression in the table:** `workspace.Context(args.Text("projectId"))`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:51](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L51)

**is handled by** →

- [`Workspace.cs`](../files/Workspace.cs.md) (Workspace.Context) · [Operations.cs:51](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L51)

**is documented in** ←

- [`README.en.md`](../files/README.en.md.md) (cli context) · [README.en.md:23](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.en.md#L23)
- [`README.md`](../files/README.md.md) (cli context) · [README.md:63](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.md#L63)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:51](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L51)

**is called from** ←

- [`McpTools.cs`](../files/McpTools.cs.md) (Call(), in-process) · [McpTools.cs:14](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L14)
- [`scripts/graphify-playbook.py`](../files/scripts__graphify-playbook.py.md) (playbook(), by starting a process) · [scripts/graphify-playbook.py:182](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L182)
- [`scripts/ontology-smoke.py`](../files/scripts__ontology-smoke.py.md) (cli(), by starting a process) · [scripts/ontology-smoke.py:316](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L316)
- [`scripts/smoke.py`](../files/scripts__smoke.py.md) (cli(), by starting a process) · [scripts/smoke.py:75](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/smoke.py#L75)
- [`wwwroot/app.js`](../files/wwwroot__app.js.md) (api(), over HTTP) · [wwwroot/app.js:61](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L61)

**is invoked by** ←

- [`context`](../tools/context.md) · [McpTools.cs:14](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L14)
