---
generator: HandOff247
id: "file:wwwroot/workspace-ui.js"
type: File
source: "wwwroot/workspace-ui.js"
---

# `wwwroot/workspace-ui.js`

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** JavaScript
- **Kind of file:** code
- **Lines:** 149
- **Source:** [wwwroot/workspace-ui.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js)

**imports** →

- [`wwwroot/i18n.js`](wwwroot__i18n.js.md) · [wwwroot/workspace-ui.js:1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L1)
- [`wwwroot/media.js`](wwwroot__media.js.md) · [wwwroot/workspace-ui.js:2](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L2)

**refers to** →

- [`AGENTS.md`](AGENTS.md.md) · [wwwroot/workspace-ui.js:28](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L28)
- [`wwwroot/i18n.js`](wwwroot__i18n.js.md) · [wwwroot/workspace-ui.js:1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L1)
- [`wwwroot/media.js`](wwwroot__media.js.md) · [wwwroot/workspace-ui.js:2](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L2)

**calls** →

- [`connection.connect`](../operations/connection.connect.md) (api(), over HTTP) · [wwwroot/workspace-ui.js:84](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L84) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*
- [`connection.disconnect`](../operations/connection.disconnect.md) (api(), over HTTP) · [wwwroot/workspace-ui.js:85](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L85) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*
- [`connection.status`](../operations/connection.status.md) (api(), over HTTP) · [wwwroot/workspace-ui.js:48](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L48) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*
- [`desktop.pickFolder`](../operations/desktop.pickFolder.md) (api(), over HTTP) · [wwwroot/workspace-ui.js:71](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L71) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*
- [`get`](../operations/get.md) (api(), over HTTP) · [wwwroot/workspace-ui.js:111](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L111) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*
- [`info`](../operations/info.md) (api(), over HTTP) · [wwwroot/workspace-ui.js:111](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L111) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*
- [`library.list`](../operations/library.list.md) (api(), over HTTP) · [wwwroot/workspace-ui.js:133](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L133) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*
- [`library.put`](../operations/library.put.md) (api(), over HTTP) · [wwwroot/workspace-ui.js:129](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L129) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*
- [`library.text`](../operations/library.text.md) (api(), over HTTP) · [wwwroot/workspace-ui.js:138](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L138) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*
- [`orchestration.state`](../operations/orchestration.state.md) (api(), over HTTP) · [wwwroot/workspace-ui.js:97](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L97) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*
- [`provider.login`](../operations/provider.login.md) (api(), over HTTP) · [wwwroot/workspace-ui.js:92](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L92) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*
- [`provider.mcp`](../operations/provider.mcp.md) (api(), over HTTP) · [wwwroot/workspace-ui.js:88](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L88) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*
- [`provider.status`](../operations/provider.status.md) (api(), over HTTP) · [wwwroot/workspace-ui.js:90](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L90) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*
- [`run.cancel`](../operations/run.cancel.md) (api(), over HTTP) · [wwwroot/workspace-ui.js:116](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L116) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*
- [`run.enqueue`](../operations/run.enqueue.md) (api(), over HTTP) · [wwwroot/workspace-ui.js:106](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L106) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*
- [`save`](../operations/save.md) (api(), over HTTP) · [wwwroot/workspace-ui.js:111](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L111) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*
- [`scan`](../operations/scan.md) (api(), over HTTP) · [wwwroot/workspace-ui.js:72](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L72) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*
- [`scan.import`](../operations/scan.import.md) (api(), over HTTP) · [wwwroot/workspace-ui.js:54](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L54) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*
- [`worker.configure`](../operations/worker.configure.md) (api(), over HTTP) · [wwwroot/workspace-ui.js:88](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L88) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*
- [`worker.status`](../operations/worker.status.md) (api(), over HTTP) · [wwwroot/workspace-ui.js:86](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L86) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*

**mentions** →

- [`code.claude.com`](../hosts.md) · [wwwroot/workspace-ui.js:93](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L93)
- [`learn.chatgpt.com`](../hosts.md) · [wwwroot/workspace-ui.js:93](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L93)

**is part of** ←

- [`wwwroot`](../areas/wwwroot.md)

**is imported by** ←

- [`wwwroot/app.js`](wwwroot__app.js.md) · [wwwroot/app.js:8](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L8)

**is referred to by** ←

- [`wwwroot/app.js`](wwwroot__app.js.md) · [wwwroot/app.js:8](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L8)

## Defined here

- `renderSetup` — export, [line 46](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L46)
- `renderAgents` — export, [line 79](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L79)
- `renderLibrary` — export, [line 120](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L120)
- `loginSession` — export, [line 142](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L142)
- `button` — function, [line 33](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L33)
- `field` — function, [line 37](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L37)
- `choice` — function, [line 40](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L40)
- `heading` — function, [line 44](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L44)
- `node` — function, [line 32](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L32)
