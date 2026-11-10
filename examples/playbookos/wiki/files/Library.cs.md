---
generator: HandOff247
id: "file:Library.cs"
type: File
source: "Library.cs"
---

# `Library.cs`

**Written by a language model (codex, 2026-11-10); not checked by a person.** Check it against the source before relying on it.

> Stores shared asset copies by SHA-256 hash, records their metadata, and provides listing, download, local resolution, preview, and TXT-reading operations. Registration accepts selected project files with supported extensions up to 32 MiB; the original files are not moved or rewritten.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** C#
- **Kind of file:** code
- **Lines:** 108
- **Source:** [Library.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs)

**defines** →

- `Library` · [Library.cs:7](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs#L7)

**uses** →

- [`Domain.cs`](Domain.cs.md) (Json, DomainError, Entry) · [Library.cs:2](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs#L2)
- [`Workspace.cs`](Workspace.cs.md) (MediaFile) · [Library.cs:95](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs#L95)

**takes as a dependency** →

- [`Connection.cs`](Connection.cs.md) (Connection) · [Library.cs:7](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs#L7)
- [`Store.cs`](Store.cs.md) (Store) · [Library.cs:7](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs#L7)
- [`Workspace.cs`](Workspace.cs.md) (Workspace) · [Library.cs:7](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs#L7)

**calls** →

- [`library.download`](../operations/library.download.md) (Request()) · [Library.cs:83](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs#L83)
- [`library.put`](../operations/library.put.md) (Request()) · [Library.cs:19](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs#L19)

**is part of** ←

- [PlayBookOS](../overview.md)

**is used by** ←

- [`Operations.cs`](Operations.cs.md) (Library) · [Operations.cs:23](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L23)
- [`Program.cs`](Program.cs.md) (Library) · [Program.cs:105](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L105)

**handles** ←

- [`library.download`](../operations/library.download.md) (Library.Download) · [Operations.cs:77](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L77)
- [`library.list`](../operations/library.list.md) (Library.List) · [Operations.cs:74](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L74)
- [`library.put`](../operations/library.put.md) (Library.Put) · [Operations.cs:76](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L76)
- [`library.register`](../operations/library.register.md) (Library.Register) · [Operations.cs:75](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L75)
- [`library.resolve`](../operations/library.resolve.md) (Library.Resolve) · [Operations.cs:78](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L78)
- [`library.text`](../operations/library.text.md) (Library.Text) · [Operations.cs:79](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L79)

## Defined here

- `Library` — class, [line 7](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs#L7) — Immutable, content-addressed shared references.
- `Library.List` — method, [line 11](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs#L11)
- `Library.Register` — method, [line 12](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs#L12)
- `Library.Put` — method, [line 21](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs#L21)
- `Library.Download` — method, [line 62](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs#L62)
- `Library.Resolve` — method, [line 76](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs#L76)
- `Library.Preview` — method, [line 95](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs#L95)
- `Library.Text` — method, [line 101](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs#L101)
