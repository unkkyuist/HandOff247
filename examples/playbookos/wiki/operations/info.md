---
generator: HandOff247
id: "op:info"
type: Operation
source: "Operations.cs"
---

# `info`

> handled by `OSVersion.ToString`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `OSVersion.ToString`
- **Expression in the table:** `new { name = "PlayBook OS", version = "0.2.0", home = store.Home, machine = Environment.MachineName, platform = Environment.OSVersion.ToString(), schema = 1, co`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:98](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L98)

**is documented in** ←

- [`README.en.md`](../files/README.en.md.md) (cli info) · [README.en.md:21](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.en.md#L21)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:98](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L98)

**is called from** ←

- [`portable/oz/install.py`](../files/portable__oz__install.py.md) (playbook()) · [portable/oz/install.py:145](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L145)
- [`scripts/check-package.py`](../files/scripts__check-package.py.md) (cli(), by starting a process) · [scripts/check-package.py:42](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/check-package.py#L42)
- [`wwwroot/app.js`](../files/wwwroot__app.js.md) (api(), over HTTP) · [wwwroot/app.js:91](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L91)
- [`wwwroot/workspace-ui.js`](../files/wwwroot__workspace-ui.js.md) (api(), over HTTP) · [wwwroot/workspace-ui.js:111](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L111) · *inferred: api is a parameter here; same-name function in wwwroot/app.js, which imports this file*
