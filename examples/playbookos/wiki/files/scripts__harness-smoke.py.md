---
generator: HandOff247
id: "file:scripts/harness-smoke.py"
type: File
source: "scripts/harness-smoke.py"
---

# `scripts/harness-smoke.py`

> Harness proposal/trial/adoption tests on isolated SQLite and real worker/provider processes.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** test
- **Lines:** 216
- **Source:** [scripts/harness-smoke.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py)

**runs** →

- [`PlayBook.csproj`](PlayBook.csproj.md) (build output) · [scripts/harness-smoke.py:20](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L20)

**refers to** →

- [`AGENTS.md`](AGENTS.md.md) · [scripts/harness-smoke.py:29](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L29)
- [`scripts/fixtures/harness-provider.py`](scripts__fixtures__harness-provider.py.md) · [scripts/harness-smoke.py:97](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L97)
- [`wwwroot/harness.js`](wwwroot__harness.js.md) · [scripts/harness-smoke.py:114](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L114)

**calls** →

- [`agent.register`](../operations/agent.register.md) (atomic_cli(), by starting a process) · [scripts/harness-smoke.py:204](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L204)
- [`asset.readText`](../operations/asset.readText.md) (cli(), by starting a process) · [scripts/harness-smoke.py:73](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L73)
- [`events`](../operations/events.md) (atomic_cli(), by starting a process) · [scripts/harness-smoke.py:209](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L209)
- [`get`](../operations/get.md) (cli(), by starting a process) · [scripts/harness-smoke.py:72](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L72)
- [`harness.adopt`](../operations/harness.adopt.md) (cli(), by starting a process) · [scripts/harness-smoke.py:69](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L69)
- [`harness.compare`](../operations/harness.compare.md) (cli(), by starting a process) · [scripts/harness-smoke.py:80](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L80)
- [`harness.probe`](../operations/harness.probe.md) (atomic_cli(), by starting a process) · [scripts/harness-smoke.py:210](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L210)
- [`harness.propose`](../operations/harness.propose.md) (atomic_cli(), by starting a process) · [scripts/harness-smoke.py:208](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L208)
- [`harness.state`](../operations/harness.state.md) (cli(), by starting a process) · [scripts/harness-smoke.py:88](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L88)
- [`list`](../operations/list.md) (atomic_cli(), by starting a process) · [scripts/harness-smoke.py:211](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L211)
- [`ontology.search`](../operations/ontology.search.md) (cli(), by starting a process) · [scripts/harness-smoke.py:89](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L89)
- [`orchestration.state`](../operations/orchestration.state.md) (cli(), by starting a process) · [scripts/harness-smoke.py:149](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L149)
- [`run.cancel`](../operations/run.cancel.md) (cli(), by starting a process) · [scripts/harness-smoke.py:94](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L94)
- [`run.claim`](../operations/run.claim.md) (atomic_cli(), by starting a process) · [scripts/harness-smoke.py:206](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L206)
- [`run.complete`](../operations/run.complete.md) (cli(), by starting a process) · [scripts/harness-smoke.py:56](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L56)
- [`run.enqueue`](../operations/run.enqueue.md) (atomic_cli(), by starting a process) · [scripts/harness-smoke.py:205](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L205)
- [`save`](../operations/save.md) (atomic_cli(), by starting a process) · [scripts/harness-smoke.py:203](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L203)

**reads** →

- [`PLAYBOOK_TEST_DLL`](../environment.md) · [scripts/harness-smoke.py:20](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L20)

**is part of** ←

- [`scripts`](../areas/scripts.md)

## Defined here

- `check` — function, [line 22](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L22)
