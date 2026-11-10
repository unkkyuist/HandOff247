---
generator: HandOff247
id: "file:scripts/prepare-public-source.py"
type: File
source: "scripts/prepare-public-source.py"
---

# `scripts/prepare-public-source.py`

> Copy an explicit public source snapshot; never copy the private local Git history.

**Written by a language model (codex, 2026-11-10); not checked by a person.** Check it against the source before relying on it.

> Copies an explicit set of source, documentation, web, portable, example, and script files into a fresh public-source snapshot directory. It rejects private data and selected generated files, records hashes for the copied files, and writes a manifest indicating that private Git history was not included.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 27
- **Source:** [scripts/prepare-public-source.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py)

**refers to** →

- [`AGENTS.md`](AGENTS.md.md) · [scripts/prepare-public-source.py:11](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py#L11)
- [`PlayBook.csproj`](PlayBook.csproj.md) · [scripts/prepare-public-source.py:11](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py#L11)
- [`Properties/launchSettings.json`](Properties__launchSettings.json.md) · [scripts/prepare-public-source.py:13](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py#L13)
- [`README.en.md`](README.en.md.md) · [scripts/prepare-public-source.py:11](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py#L11)
- [`README.md`](README.md.md) · [scripts/prepare-public-source.py:11](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py#L11)
- [`START_PLAYBOOK.cmd`](START_PLAYBOOK.cmd.md) · [scripts/prepare-public-source.py:12](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py#L12)
- [`appsettings.Development.json`](appsettings.Development.json.md) · [scripts/prepare-public-source.py:12](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py#L12)
- [`appsettings.json`](appsettings.json.md) · [scripts/prepare-public-source.py:12](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py#L12)
- [`docs/API.md`](docs__API.md.md) · [scripts/prepare-public-source.py:16](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py#L16)
- [`docs/CENTRAL-SERVER-PLAN.md`](docs__CENTRAL-SERVER-PLAN.md.md) · [scripts/prepare-public-source.py:16](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py#L16)
- [`docs/CLAUDE-AND-FOLDERS.md`](docs__CLAUDE-AND-FOLDERS.md.md) · [scripts/prepare-public-source.py:16](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py#L16)
- [`docs/ONTOLOGY.md`](docs__ONTOLOGY.md.md) · [scripts/prepare-public-source.py:16](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py#L16)
- [`docs/PLAN.md`](docs__PLAN.md.md) · [scripts/prepare-public-source.py:16](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py#L16)
- [`docs/PORTABLE-AND-AGENTS.md`](docs__PORTABLE-AND-AGENTS.md.md) · [scripts/prepare-public-source.py:16](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py#L16)
- [`docs/RELEASE-0.2.0.md`](docs__RELEASE-0.2.0.md.md) · [scripts/prepare-public-source.py:16](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py#L16)
- [`packages.lock.json`](packages.lock.json.md) · [scripts/prepare-public-source.py:11](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py#L11)
- [`playbook.ps1`](playbook.ps1.md) · [scripts/prepare-public-source.py:12](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py#L12)
- [`playbook.sh`](playbook.sh.md) · [scripts/prepare-public-source.py:12](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py#L12)
- [`scripts/central-smoke.py`](scripts__central-smoke.py.md) · [scripts/prepare-public-source.py:17](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py#L17)
- [`scripts/check-package.py`](scripts__check-package.py.md) · [scripts/prepare-public-source.py:17](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py#L17)
- [`scripts/fixtures/provider.py`](scripts__fixtures__provider.py.md) · [scripts/prepare-public-source.py:17](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py#L17)
- [`scripts/folders-smoke.py`](scripts__folders-smoke.py.md) · [scripts/prepare-public-source.py:17](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py#L17)
- [`scripts/ontology-smoke.py`](scripts__ontology-smoke.py.md) · [scripts/prepare-public-source.py:17](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py#L17)
- [`scripts/package.py`](scripts__package.py.md) · [scripts/prepare-public-source.py:17](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py#L17)
- [`scripts/real-provider-smoke.py`](scripts__real-provider-smoke.py.md) · [scripts/prepare-public-source.py:17](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py#L17)
- [`scripts/smoke.py`](scripts__smoke.py.md) · [scripts/prepare-public-source.py:17](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py#L17)

**is part of** ←

- [`scripts`](../areas/scripts.md)
