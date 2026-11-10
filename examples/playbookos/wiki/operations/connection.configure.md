---
generator: HandOff247
id: "op:connection.configure"
type: Operation
source: "Operations.cs"
---

# `connection.configure`

> handled by `Operations.Configure`

- **Class:** Operation — One named operation of a dispatch table.
- **Handler:** `Operations.Configure`
- **Expression in the table:** `Configure(args)`
- **Reachable through:** POST /api/{operation}
- **Source:** [Operations.cs:60](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L60)

**is handled by** →

- [`Operations.cs`](../files/Operations.cs.md) (Operations.Configure) · [Operations.cs:60](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L60)

**is an operation of** ←

- [`Operations.Execute`](../operations.md) · [Operations.cs:60](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L60)

**is called from** ←

- [`portable/Install-PlayBook.ps1`](../files/portable__Install-PlayBook.ps1.md) (cli connection.configure, by starting a process) · [portable/Install-PlayBook.ps1:67](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/Install-PlayBook.ps1#L67)
- [`portable/oz/install.py`](../files/portable__oz__install.py.md) (playbook()) · [portable/oz/install.py:146](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L146)
