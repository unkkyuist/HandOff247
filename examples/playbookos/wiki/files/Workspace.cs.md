---
generator: HandOff247
id: "file:Workspace.cs"
type: File
source: "Workspace.cs"
---

# `Workspace.cs`

**Written by a language model (codex, 2026-11-10); not checked by a person.** Check it against the source before relying on it.

> Workspace resolves project files within registered project roots, provides text and media previews, and copies supported files into a shared asset directory with hash checks. It also builds project context, discovers project folders, and retrieves Git status, revision, and recent commit information; the excerpt ends as its command-running method begins.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** C#
- **Kind of file:** code
- **Lines:** 264
- **Source:** [Workspace.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs)

**defines** →

- `MediaFile` · [Workspace.cs:19](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L19)
- `Workspace` · [Workspace.cs:8](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L8)

**uses** →

- [`Domain.cs`](Domain.cs.md) (Json, DomainError, Entry) · [Workspace.cs:4](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L4)
- [`Ontology.cs`](Ontology.cs.md) (Ontology) · [Workspace.cs:156](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L156)

**takes as a dependency** →

- [`Store.cs`](Store.cs.md) (Store) · [Workspace.cs:8](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L8)

**refers to** →

- [`AGENTS.md`](AGENTS.md.md) · [Workspace.cs:184](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L184)
- [`README.md`](README.md.md) · [Workspace.cs:184](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L184)

**is part of** ←

- [PlayBookOS](../overview.md)

**is used by** ←

- [`Library.cs`](Library.cs.md) (MediaFile) · [Library.cs:95](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs#L95)
- [`Program.cs`](Program.cs.md) (Workspace) · [Program.cs:8](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs#L8)

**is a dependency of** ←

- [`AgentWorker.cs`](AgentWorker.cs.md) (Workspace) · [AgentWorker.cs:8](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs#L8)
- [`Folders.cs`](Folders.cs.md) (Workspace) · [Folders.cs:12](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs#L12)
- [`Harnesses.cs`](Harnesses.cs.md) (Workspace) · [Harnesses.cs:10](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs#L10)
- [`Library.cs`](Library.cs.md) (Workspace) · [Library.cs:7](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs#L7)
- [`Operations.cs`](Operations.cs.md) (Workspace) · [Operations.cs:4](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L4)
- [`Orchestration.cs`](Orchestration.cs.md) (Workspace) · [Orchestration.cs:8](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Orchestration.cs#L8)
- [`ProjectScanner.cs`](ProjectScanner.cs.md) (Workspace) · [ProjectScanner.cs:10](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ProjectScanner.cs#L10)

**handles** ←

- [`asset.readText`](../operations/asset.readText.md) (Workspace.ReadText) · [Operations.cs:84](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L84)
- [`asset.shareCopy`](../operations/asset.shareCopy.md) (Workspace.ShareAsset) · [Operations.cs:85](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L85)
- [`asset.verify`](../operations/asset.verify.md) (Workspace.VerifyAsset) · [Operations.cs:82](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L82)
- [`context`](../operations/context.md) (Workspace.Context) · [Operations.cs:51](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L51)
- [`discover`](../operations/discover.md) (Workspace.Discover) · [Operations.cs:54](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L54)
- [`export`](../operations/export.md) (Workspace.Export) · [Operations.cs:86](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L86)
- [`git`](../operations/git.md) (Workspace.Git) · [Operations.cs:81](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L81)

## Defined here

- `Workspace` — class, [line 8](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L8)
- `MediaFile` — record, [line 19](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L19)
- `Workspace.IsPreviewableImage` — method, [line 20](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L20)
- `Workspace.FilePath` — method, [line 21](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L21)
- `Workspace.MediaType` — method, [line 22](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L22)
- `Workspace.Preview` — method, [line 50](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L50)
- `Workspace.ReadText` — method, [line 61](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L61)
- `Workspace.ShareAsset` — method, [line 68](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L68)
- `Workspace.Context` — method, [line 136](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L136)
- `Workspace.PathFor` — method, [line 167](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L167)
- `Workspace.Discover` — method, [line 173](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L173)
- `Workspace.Git` — method, [line 191](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L191)
- `Workspace.Run` — method, [line 200](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L200)
- `Workspace.Export` — method, [line 213](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L213)
- `Workspace.VerifyAsset` — method, [line 252](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L252)
