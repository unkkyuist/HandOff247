---
generator: HandOff247
id: "op:agent.register"
type: Operation
source: "Operations.cs"
---

# `agent.register`

> handled by `Orchestration.Register`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Orchestration.Register`
- **Expression in the table:** `orchestration.Register(args)`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:67](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L67)

**is handled by** →

- [`Orchestration.cs`](../files/Orchestration.cs.md) (Orchestration.Register) · [Operations.cs:67](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L67)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:67](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L67)

**is called from** ←

- [`AgentWorker.cs`](../files/AgentWorker.cs.md) (Execute(), in-process) · [AgentWorker.cs:41](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs#L41)
- [`scripts/harness-smoke.py`](../files/scripts__harness-smoke.py.md) (atomic_cli(), by starting a process) · [scripts/harness-smoke.py:204](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L204)
- [`scripts/ontology-smoke.py`](../files/scripts__ontology-smoke.py.md) (cli(), by starting a process) · [scripts/ontology-smoke.py:140](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L140)
