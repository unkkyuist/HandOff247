---
generator: HandOff247
id: "op:run.claim"
type: Operation
source: "Operations.cs"
---

# `run.claim`

> handled by `Orchestration.Claim`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Orchestration.Claim`
- **Expression in the table:** `await orchestration.Claim(args)`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:70](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L70)

**is handled by** →

- [`Orchestration.cs`](../files/Orchestration.cs.md) (Orchestration.Claim) · [Operations.cs:70](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L70)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:70](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L70)

**is called from** ←

- [`AgentWorker.cs`](../files/AgentWorker.cs.md) (Execute(), in-process) · [AgentWorker.cs:47](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs#L47)
- [`scripts/harness-smoke.py`](../files/scripts__harness-smoke.py.md) (atomic_cli(), by starting a process) · [scripts/harness-smoke.py:206](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L206)
- [`scripts/ontology-smoke.py`](../files/scripts__ontology-smoke.py.md) (cli(), by starting a process) · [scripts/ontology-smoke.py:147](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L147)
