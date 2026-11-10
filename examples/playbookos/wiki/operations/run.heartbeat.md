---
generator: HandOff247
id: "op:run.heartbeat"
type: Operation
source: "Operations.cs"
---

# `run.heartbeat`

> handled by `Orchestration.Heartbeat`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Orchestration.Heartbeat`
- **Expression in the table:** `orchestration.Heartbeat(args)`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:71](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L71)

**is handled by** →

- [`Orchestration.cs`](../files/Orchestration.cs.md) (Orchestration.Heartbeat) · [Operations.cs:71](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L71)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:71](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L71)

**is called from** ←

- [`AgentWorker.cs`](../files/AgentWorker.cs.md) (Execute(), in-process) · [AgentWorker.cs:155](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs#L155)
- [`scripts/ontology-smoke.py`](../files/scripts__ontology-smoke.py.md) (cli(), by starting a process) · [scripts/ontology-smoke.py:160](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L160)
