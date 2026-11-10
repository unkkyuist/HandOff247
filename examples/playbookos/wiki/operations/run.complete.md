---
generator: HandOff247
id: "op:run.complete"
type: Operation
source: "Operations.cs"
---

# `run.complete`

> handled by `Orchestration.Heartbeat`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Orchestration.Heartbeat`
- **Expression in the table:** `orchestration.Heartbeat(args, true)`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:72](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L72)

**is handled by** →

- [`Orchestration.cs`](../files/Orchestration.cs.md) (Orchestration.Heartbeat) · [Operations.cs:72](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L72)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:72](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L72)

**is called from** ←

- [`AgentWorker.cs`](../files/AgentWorker.cs.md) (Execute(), in-process) · [AgentWorker.cs:177](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs#L177)
- [`scripts/harness-smoke.py`](../files/scripts__harness-smoke.py.md) (cli(), by starting a process) · [scripts/harness-smoke.py:56](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L56)
- [`scripts/ontology-smoke.py`](../files/scripts__ontology-smoke.py.md) (cli(), by starting a process) · [scripts/ontology-smoke.py:169](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L169)
