---
generator: HandOff247
id: "file:Access.cs"
type: File
source: "Access.cs"
---

# `Access.cs`

**Written by a language model (codex, 2026-11-10); not checked by a person.** Check it against the source before relying on it.

> Stores server account identity data and session records under the configured home directory. It provides account setup, login, token validation, and logout, with password-derived hashes, expiring sessions, and login-attempt limits.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** C#
- **Kind of file:** code
- **Lines:** 61
- **Source:** [Access.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Access.cs)

**defines** →

- `Access` · [Access.cs:9](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Access.cs#L9)
- `ServerIdentity` · [Access.cs:6](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Access.cs#L6)
- `ServerSession` · [Access.cs:7](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Access.cs#L7)

**uses** →

- [`Domain.cs`](Domain.cs.md) (DomainError, Json) · [Access.cs:20](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Access.cs#L20)

**is part of** ←

- [PlayBookOS](../overview.md)

**is used by** ←

- [`Program.cs`](Program.cs.md) (Access) · [Program.cs:12](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L12)

**is a dependency of** ←

- [`Operations.cs`](Operations.cs.md) (Access) · [Operations.cs:4](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L4)

**handles** ←

- [`server.setup`](../operations/server.setup.md) (Access.Setup) · [Operations.cs:61](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L61)

## Defined here

- `ServerIdentity` — record, [line 6](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Access.cs#L6)
- `ServerSession` — record, [line 7](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Access.cs#L7)
- `Access` — class, [line 9](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Access.cs#L9)
- `Access.Setup` — method, [line 16](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Access.cs#L16)
- `Access.Login` — method, [line 33](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Access.cs#L33)
- `Access.Valid` — method, [line 54](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Access.cs#L54)
- `Access.Logout` — method, [line 60](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Access.cs#L60)
