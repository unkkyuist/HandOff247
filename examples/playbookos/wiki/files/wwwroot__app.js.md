---
generator: HandOff247
id: "file:wwwroot/app.js"
type: File
source: "wwwroot/app.js"
---

# `wwwroot/app.js`

**Written by a language model (codex, 2026-11-10); not checked by a person.** Check it against the source before relying on it.

> Implements the browser interface for PlayBook OS, loading modules for folders, assets, agents, ontology, media, and other project views. It fetches project and record data from the API, renders navigation and project tabs, and provides actions for viewing, editing, approving, and verifying records.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** JavaScript
- **Kind of file:** code
- **Lines:** 91
- **Source:** [wwwroot/app.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js)

**imports** →

- [`wwwroot/assets.js`](wwwroot__assets.js.md) · [wwwroot/app.js:7](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L7)
- [`wwwroot/context-menu.js`](wwwroot__context-menu.js.md) · [wwwroot/app.js:6](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L6)
- [`wwwroot/flowchart.js`](wwwroot__flowchart.js.md) · [wwwroot/app.js:4](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L4)
- [`wwwroot/folders.js`](wwwroot__folders.js.md) · [wwwroot/app.js:2](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L2)
- [`wwwroot/harness.js`](wwwroot__harness.js.md) · [wwwroot/app.js:10](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L10)
- [`wwwroot/i18n.js`](wwwroot__i18n.js.md) · [wwwroot/app.js:1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L1)
- [`wwwroot/inventory.js`](wwwroot__inventory.js.md) · [wwwroot/app.js:3](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L3)
- [`wwwroot/media.js`](wwwroot__media.js.md) · [wwwroot/app.js:5](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L5)
- [`wwwroot/ontology.js`](wwwroot__ontology.js.md) · [wwwroot/app.js:9](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L9)
- [`wwwroot/workspace-ui.js`](wwwroot__workspace-ui.js.md) · [wwwroot/app.js:8](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L8)

**refers to** →

- [`wwwroot/assets.js`](wwwroot__assets.js.md) · [wwwroot/app.js:7](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L7)
- [`wwwroot/context-menu.js`](wwwroot__context-menu.js.md) · [wwwroot/app.js:6](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L6)
- [`wwwroot/flowchart.js`](wwwroot__flowchart.js.md) · [wwwroot/app.js:4](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L4)
- [`wwwroot/folders.js`](wwwroot__folders.js.md) · [wwwroot/app.js:2](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L2)
- [`wwwroot/harness.js`](wwwroot__harness.js.md) · [wwwroot/app.js:10](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L10)
- [`wwwroot/i18n.js`](wwwroot__i18n.js.md) · [wwwroot/app.js:1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L1)
- [`wwwroot/inventory.js`](wwwroot__inventory.js.md) · [wwwroot/app.js:3](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L3)
- [`wwwroot/media.js`](wwwroot__media.js.md) · [wwwroot/app.js:5](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L5)
- [`wwwroot/ontology.js`](wwwroot__ontology.js.md) · [wwwroot/app.js:9](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L9)
- [`wwwroot/workspace-ui.js`](wwwroot__workspace-ui.js.md) · [wwwroot/app.js:8](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L8)

**calls** →

- [`asset.verify`](../operations/asset.verify.md) (api(), over HTTP) · [wwwroot/app.js:77](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L77)
- [`backup`](../operations/backup.md) (api(), over HTTP) · [wwwroot/app.js:88](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L88)
- [`canon.approve`](../operations/canon.approve.md) (api(), over HTTP) · [wwwroot/app.js:85](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L85)
- [`context`](../operations/context.md) (api(), over HTTP) · [wwwroot/app.js:61](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L61)
- [`discover`](../operations/discover.md) (api(), over HTTP) · [wwwroot/app.js:86](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L86)
- [`events`](../operations/events.md) (api(), over HTTP) · [wwwroot/app.js:64](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L64)
- [`export`](../operations/export.md) (api(), over HTTP) · [wwwroot/app.js:63](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L63)
- [`git`](../operations/git.md) (api(), over HTTP) · [wwwroot/app.js:63](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L63)
- [`info`](../operations/info.md) (api(), over HTTP) · [wwwroot/app.js:91](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L91)
- [`library.register`](../operations/library.register.md) (api(), over HTTP) · [wwwroot/app.js:64](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L64)
- [`list`](../operations/list.md) (api(), over HTTP) · [wwwroot/app.js:53](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L53)
- [`save`](../operations/save.md) (api(), over HTTP) · [wwwroot/app.js:84](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L84)
- [`tool.logs`](../operations/tool.logs.md) (exec()) · [wwwroot/app.js:79](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L79)
- [`tool.start`](../operations/tool.start.md) (exec()) · [wwwroot/app.js:79](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L79)
- [`tool.status`](../operations/tool.status.md) (exec()) · [wwwroot/app.js:79](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L79)
- [`tool.stop`](../operations/tool.stop.md) (exec()) · [wwwroot/app.js:79](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L79)
- [`tools`](../operations/tools.md) (api(), over HTTP) · [wwwroot/app.js:53](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L53)

**is part of** ←

- [`wwwroot`](../areas/wwwroot.md)

**is loaded by** ←

- [`wwwroot/index.html`](wwwroot__index.html.md) · [wwwroot/index.html:9](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/index.html#L9)

## Defined here

- `api` — function, [line 18](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L18)
- `toast` — function, [line 19](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L19)
- `action` — function, [line 20](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L20)
- `badge` — function, [line 21](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L21)
- `date` — function, [line 22](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L22)
- `view` — function, [line 23](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L23)
- `section` — function, [line 24](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L24)
- `heading` — function, [line 25](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L25)
- `stats` — function, [line 26](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L26)
- `sidebar` — function, [line 27](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L27)
- `refresh` — function, [line 53](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L53)
- `select` — function, [line 54](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L54)
- `render` — function, [line 55](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L55)
- `dashboard` — function, [line 70](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L70)
- `recordList` — function, [line 77](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L77)
- `timeline` — function, [line 78](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L78)
- `renderTools` — function, [line 79](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L79)
- `toolDisplay` — function, [line 80](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L80)
- `bodyFields` — function, [line 81](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L81)
- `edit` — function, [line 82](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L82)
- `approve` — function, [line 85](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L85)
- `discover` — function, [line 86](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L86)
- `$` — function, [line 11](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L11)
