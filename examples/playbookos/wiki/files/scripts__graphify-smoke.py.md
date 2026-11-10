---
generator: HandOff247
id: "file:scripts/graphify-smoke.py"
type: File
source: "scripts/graphify-smoke.py"
---

# `scripts/graphify-smoke.py`

> Real Graphify/PlayBook integration checks, using an isolated ledger and source.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** test
- **Lines:** 157
- **Source:** [scripts/graphify-smoke.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-smoke.py)

**refers to** →

- [`scripts/graphify-playbook.py`](scripts__graphify-playbook.py.md) · [scripts/graphify-smoke.py:82](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-smoke.py#L82)

**calls** →

- [`ontology.search`](../operations/ontology.search.md) (playbook()) · [scripts/graphify-smoke.py:134](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-smoke.py#L134)
- [`save`](../operations/save.md) (playbook()) · [scripts/graphify-smoke.py:85](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-smoke.py#L85)

**sets** →

- [`PLAYBOOK_HOME`](../environment.md) · [scripts/graphify-smoke.py:81](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-smoke.py#L81)

**depends on** →

- [`mcp`](../packages.md) (imported) · [scripts/graphify-smoke.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-smoke.py)

**is part of** ←

- [`scripts`](../areas/scripts.md)

## Defined here

- `check` — function, [line 22](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-smoke.py#L22)
- `request` — function, [line 28](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-smoke.py#L28)
- `rejected` — function, [line 39](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-smoke.py#L39)
- `mcp_checks` — function, [line 47](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-smoke.py#L47)
