---
generator: HandOff247
id: "file:wwwroot/assets.js"
type: File
source: "wwwroot/assets.js"
---

# `wwwroot/assets.js`

**Written by a language model (codex, 2026-11-10); not checked by a person.** Check it against the source before relying on it.

> Renders a project file inventory with search, type filters, previews, file actions, registered asset records, and shared assets. It also formats file metadata and compares project paths to identify registered files.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** JavaScript
- **Kind of file:** code
- **Lines:** 118
- **Source:** [wwwroot/assets.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/assets.js)

**imports** →

- [`wwwroot/context-menu.js`](wwwroot__context-menu.js.md) · [wwwroot/assets.js:3](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/assets.js#L3)
- [`wwwroot/i18n.js`](wwwroot__i18n.js.md) · [wwwroot/assets.js:1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/assets.js#L1)
- [`wwwroot/media.js`](wwwroot__media.js.md) · [wwwroot/assets.js:2](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/assets.js#L2)

**refers to** →

- [`wwwroot/context-menu.js`](wwwroot__context-menu.js.md) · [wwwroot/assets.js:3](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/assets.js#L3)
- [`wwwroot/i18n.js`](wwwroot__i18n.js.md) · [wwwroot/assets.js:1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/assets.js#L1)
- [`wwwroot/media.js`](wwwroot__media.js.md) · [wwwroot/assets.js:2](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/assets.js#L2)

**calls** →

- [`asset.files`](../operations/asset.files.md) (api(), over HTTP) · [wwwroot/assets.js:22](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/assets.js#L22) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*

**is part of** ←

- [`wwwroot`](../areas/wwwroot.md)

**is imported by** ←

- [`wwwroot/app.js`](wwwroot__app.js.md) · [wwwroot/app.js:7](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L7)

**is referred to by** ←

- [`wwwroot/app.js`](wwwroot__app.js.md) · [wwwroot/app.js:7](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L7)

## Defined here

- `renderAssets` — export, [line 5](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/assets.js#L5)
- `filePreview` — function, [line 97](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/assets.js#L97)
- `categoryLabel` — function, [line 105](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/assets.js#L105)
- `extension` — function, [line 106](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/assets.js#L106)
- `categoryFromPath` — function, [line 107](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/assets.js#L107)
- `joinPath` — function, [line 108](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/assets.js#L108)
- `formatSize` — function, [line 109](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/assets.js#L109)
- `sameProjectPath` — function, [line 110](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/assets.js#L110)
- `assetRecords` — function, [line 111](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/assets.js#L111)
- `action` — function, [line 118](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/assets.js#L118)
