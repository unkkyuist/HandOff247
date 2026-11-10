---
generator: HandOff247
id: "file:scripts/ontology-smoke.py"
type: File
source: "scripts/ontology-smoke.py"
---

# `scripts/ontology-smoke.py`

> Ontology integration checks using a temporary DB, local fixture and real transports.

**Written by a language model (codex, 2026-11-10); not checked by a person.** Check it against the source before relying on it.

> This script runs ontology integration checks against a temporary database and local fixtures, using the PlayBook CLI and real transports. The shown checks cover record projections, search, run usage and provenance, ingestion, revisions, and rollback; the excerpt does not show the rest of the checks.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** test
- **Lines:** 541
- **Source:** [scripts/ontology-smoke.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py)

**runs** →

- [`PlayBook.csproj`](PlayBook.csproj.md) (build output) · [scripts/ontology-smoke.py:25](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L25)

**calls** →

- [`agent.register`](../operations/agent.register.md) (cli(), by starting a process) · [scripts/ontology-smoke.py:140](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L140)
- [`context`](../operations/context.md) (cli(), by starting a process) · [scripts/ontology-smoke.py:316](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L316)
- [`events`](../operations/events.md) (cli(), by starting a process) · [scripts/ontology-smoke.py:270](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L270)
- [`get`](../operations/get.md) (cli(), by starting a process) · [scripts/ontology-smoke.py:255](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L255)
- [`list`](../operations/list.md) (cli(), by starting a process) · [scripts/ontology-smoke.py:100](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L100)
- [`ontology.connect`](../operations/ontology.connect.md) (cli(), by starting a process) · [scripts/ontology-smoke.py:362](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L362)
- [`ontology.connections`](../operations/ontology.connections.md) (cli(), by starting a process) · [scripts/ontology-smoke.py:371](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L371)
- [`ontology.ingest`](../operations/ontology.ingest.md) (cli(), by starting a process) · [scripts/ontology-smoke.py:195](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L195)
- [`ontology.rebuild`](../operations/ontology.rebuild.md) (cli(), by starting a process) · [scripts/ontology-smoke.py:304](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L304)
- [`ontology.reference`](../operations/ontology.reference.md) (cli(), by starting a process) · [scripts/ontology-smoke.py:163](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L163)
- [`ontology.search`](../operations/ontology.search.md) (cli(), by starting a process) · [scripts/ontology-smoke.py:97](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L97)
- [`ontology.sync`](../operations/ontology.sync.md) (cli(), by starting a process) · [scripts/ontology-smoke.py:366](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L366)
- [`ontology.usage`](../operations/ontology.usage.md) (cli(), by starting a process) · [scripts/ontology-smoke.py:233](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L233)
- [`run.claim`](../operations/run.claim.md) (cli(), by starting a process) · [scripts/ontology-smoke.py:147](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L147)
- [`run.complete`](../operations/run.complete.md) (cli(), by starting a process) · [scripts/ontology-smoke.py:169](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L169)
- [`run.enqueue`](../operations/run.enqueue.md) (cli(), by starting a process) · [scripts/ontology-smoke.py:142](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L142)
- [`run.heartbeat`](../operations/run.heartbeat.md) (cli(), by starting a process) · [scripts/ontology-smoke.py:160](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L160)
- [`save`](../operations/save.md) (cli(), by starting a process) · [scripts/ontology-smoke.py:105](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L105)

**reads** →

- [`PLAYBOOK_TEST_DLL`](../environment.md) · [scripts/ontology-smoke.py:25](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L25)

**is part of** ←

- [`scripts`](../areas/scripts.md)

**is referred to by** ←

- [`scripts/prepare-public-source.py`](scripts__prepare-public-source.py.md) · [scripts/prepare-public-source.py:17](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py#L17)

## Defined here

- `check` — function, [line 32](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L32)
- `free_port` — function, [line 39](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L39)
- `tool_result` — function, [line 45](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L45) — The official SDK returns a JSON string inside MCP text content.
- `http_rpc_message` — function, [line 55](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L55)
