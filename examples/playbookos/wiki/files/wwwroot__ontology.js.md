---
generator: HandOff247
id: "file:wwwroot/ontology.js"
type: File
source: "wwwroot/ontology.js"
---

# `wwwroot/ontology.js`

**Written by a language model (codex, 2026-11-10); not checked by a person.** Check it against the source before relying on it.

> Renders the ontology workbench for searching knowledge, collecting and viewing references, recording how references are used, and editing entities and relations. It builds the interface with translated labels and calls the supplied API for ontology operations; the displayed code also handles search results and reference selection.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** JavaScript
- **Kind of file:** code
- **Lines:** 246
- **Source:** [wwwroot/ontology.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js)

**imports** →

- [`wwwroot/i18n.js`](wwwroot__i18n.js.md) · [wwwroot/ontology.js:1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js#L1)

**refers to** →

- [`wwwroot/i18n.js`](wwwroot__i18n.js.md) · [wwwroot/ontology.js:1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js#L1)

**calls** →

- [`ontology.connect`](../operations/ontology.connect.md) (api(), over HTTP) · [wwwroot/ontology.js:229](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js#L229) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*
- [`ontology.connections`](../operations/ontology.connections.md) (api(), over HTTP) · [wwwroot/ontology.js:235](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js#L235) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*
- [`ontology.ingest`](../operations/ontology.ingest.md) (api(), over HTTP) · [wwwroot/ontology.js:217](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js#L217) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*
- [`ontology.rebuild`](../operations/ontology.rebuild.md) (api(), over HTTP) · [wwwroot/ontology.js:94](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js#L94) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*
- [`ontology.reference`](../operations/ontology.reference.md) (api(), over HTTP) · [wwwroot/ontology.js:111](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js#L111) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*
- [`ontology.search`](../operations/ontology.search.md) (api(), over HTTP) · [wwwroot/ontology.js:159](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js#L159) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*
- [`ontology.sync`](../operations/ontology.sync.md) (api(), over HTTP) · [wwwroot/ontology.js:240](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js#L240) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*
- [`ontology.usage`](../operations/ontology.usage.md) (api(), over HTTP) · [wwwroot/ontology.js:118](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js#L118) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*

**is part of** ←

- [`wwwroot`](../areas/wwwroot.md)

**is imported by** ←

- [`wwwroot/app.js`](wwwroot__app.js.md) · [wwwroot/app.js:9](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L9)

**is referred to by** ←

- [`wwwroot/app.js`](wwwroot__app.js.md) · [wwwroot/app.js:9](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L9)

## Defined here

- `renderOntology` — export, [line 88](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js#L88)
- `inputField` — function, [line 62](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js#L62)
- `selectField` — function, [line 69](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js#L69)
- `message` — function, [line 74](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js#L74)
- `showMessage` — function, [line 75](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js#L75)
- `button` — function, [line 76](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js#L76)
- `when` — function, [line 81](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js#L81)
- `uriNode` — function, [line 82](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js#L82)
- `node` — function, [line 57](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js#L57)
- `textOf` — function, [line 60](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js#L60)
- `asList` — function, [line 61](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js#L61)
