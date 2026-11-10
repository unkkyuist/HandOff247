---
generator: HandOff247
id: "file:Connection.cs"
type: File
source: "Connection.cs"
---

# `Connection.cs`

**Written by a language model (codex, 2026-11-10); not checked by a person.** Check it against the source before relying on it.

> Stores device and server connection settings in client.json and provides connection status, configuration, connect, disconnect, and API request methods. It validates server URLs, sends JSON over HTTP, and converts request failures into domain errors.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** C#
- **Kind of file:** code
- **Lines:** 78
- **Source:** [Connection.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Connection.cs)

**defines** →

- `ClientSettings` · [Connection.cs:7](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Connection.cs#L7)
- `Connection` · [Connection.cs:10](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Connection.cs#L10)

**uses** →

- [`Domain.cs`](Domain.cs.md) (Json, DomainError) · [Connection.cs:3](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Connection.cs#L3)

**is part of** ←

- [PlayBookOS](../overview.md)

**is used by** ←

- [`Program.cs`](Program.cs.md) (Connection) · [Program.cs:11](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L11)
- [`Store.cs`](Store.cs.md) (Connection) · [Store.cs:9](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs#L9)

**is a dependency of** ←

- [`AgentWorker.cs`](AgentWorker.cs.md) (Connection) · [AgentWorker.cs:8](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs#L8)
- [`Library.cs`](Library.cs.md) (Connection) · [Library.cs:7](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs#L7)
- [`Operations.cs`](Operations.cs.md) (Connection) · [Operations.cs:4](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L4)
- [`ProjectScanner.cs`](ProjectScanner.cs.md) (Connection) · [ProjectScanner.cs:10](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ProjectScanner.cs#L10)

**handles** ←

- [`connection.connect`](../operations/connection.connect.md) (Connection.Connect) · [Operations.cs:58](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L58)
- [`connection.disconnect`](../operations/connection.disconnect.md) (Connection.Disconnect) · [Operations.cs:59](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L59)
- [`connection.status`](../operations/connection.status.md) (Connection.Status) · [Operations.cs:57](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L57)

## Defined here

- `ClientSettings` — record, [line 7](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Connection.cs#L7)
- `Connection` — class, [line 10](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Connection.cs#L10) — This file contains device configuration, never a second project ledger.
- `Connection.Status` — method, [line 22](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Connection.cs#L22)
- `Connection.Configure` — method, [line 23](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Connection.cs#L23)
- `Connection.ServerUri` — method, [line 34](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Connection.cs#L34)
- `Connection.Connect` — method, [line 41](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Connection.cs#L41)
- `Connection.Disconnect` — method, [line 51](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Connection.cs#L51)
- `Connection.Request` — method, [line 58](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Connection.cs#L58)
