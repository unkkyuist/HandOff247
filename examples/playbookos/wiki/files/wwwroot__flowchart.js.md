---
generator: HandOff247
id: "file:wwwroot/flowchart.js"
type: File
source: "wwwroot/flowchart.js"
---

# `wwwroot/flowchart.js`

**Written by a language model (codex, 2026-11-10); not checked by a person.** Check it against the source before relying on it.

> Displays a project's Mermaid flowchart source, loads the vendored Mermaid script on first use, and renders the diagram. If rendering fails, it shows an error message and the source remains available in a details section.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** JavaScript
- **Kind of file:** code
- **Lines:** 50
- **Source:** [wwwroot/flowchart.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/flowchart.js)

**imports** →

- [`wwwroot/i18n.js`](wwwroot__i18n.js.md) · [wwwroot/flowchart.js:1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/flowchart.js#L1)

**refers to** →

- [`wwwroot/i18n.js`](wwwroot__i18n.js.md) · [wwwroot/flowchart.js:1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/flowchart.js#L1)

**is part of** ←

- [`wwwroot`](../areas/wwwroot.md)

**is imported by** ←

- [`wwwroot/app.js`](wwwroot__app.js.md) · [wwwroot/app.js:4](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L4)

**is referred to by** ←

- [`wwwroot/app.js`](wwwroot__app.js.md) · [wwwroot/app.js:4](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L4)

## Defined here

- `renderFlowchart` — export, [line 30](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/flowchart.js#L30) — Shows body.flowchart (Mermaid source) of a project.
- `loadMermaid` — function, [line 10](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/flowchart.js#L10)
- `node` — function, [line 4](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/flowchart.js#L4) — Mermaid is vendored under /vendor/mermaid (pinned version) and loaded on first use.
