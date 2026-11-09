# 파일 카드

<sub>HandOff247 0.1.0이 2026-11-09에 https://github.com/unkkyuist/PlayBookOS@7153e47 기준으로 생성했습니다. 이 페이지를 직접 고치지 말고 노트 파일을 고친 뒤 다시 생성하세요.</sub>

[← 처음으로](README.md)


[(root)](#root) · [Properties](#properties) · [docs](#docs) · [examples](#examples) · [portable](#portable) · [scripts](#scripts) · [wwwroot](#wwwroot)


## (root)

### .gitattributes

`ignore` · 2 줄 · config · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/.gitattributes)

### .gitignore

`ignore` · 13 줄 · config · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/.gitignore)

### AGENTS.md

`Markdown` · 24 줄 · docs · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AGENTS.md)

> Read README.md and docs/PLAN.md.  
> <sub>출처: first paragraph</sub>

**심볼**

- [PlayBook development](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AGENTS.md#L1) · h1
- [Development knowledge loop](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AGENTS.md#L11) · h2

**들어오는 연결:** refers ← [AgentWorker.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs), [ProjectScanner.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ProjectScanner.cs), [Workspace.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs), [central-smoke.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/central-smoke.py), [harness-smoke.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py), [prepare-public-source.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py) … 외 1개

### Access.cs

`C#` · 61 줄 · code · namespace `PlayBook` · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Access.cs)

**심볼**

- [ServerIdentity](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Access.cs#L6) · record
- [ServerSession](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Access.cs#L7) · record
- [Access](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Access.cs#L9) · class
- [Access.Setup](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Access.cs#L16) · method
- [Access.Login](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Access.cs#L33) · method
- [Access.Valid](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Access.cs#L54) · method
- [Access.Logout](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Access.cs#L60) · method

**나가는 연결:** uses → [Domain.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Domain.cs)

**들어오는 연결:** dispatches ← [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); injects ← [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); mode:serve ← [Program.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs); mode:server ← [Program.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs); uses ← [Program.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs)

### AgentWorker.cs

`C#` · 196 줄 · code · namespace `PlayBook` · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs)

**심볼**

- [AgentWorker](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs#L8) · class
- [AgentWorker.Status](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs#L12) · method
- [AgentWorker.Configure](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs#L13) · method

**나가는 연결:** calls-op → [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); injects → [Connection.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Connection.cs), [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs), [Providers.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Providers.cs), [Store.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs), [Workspace.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs); refers → [AGENTS.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AGENTS.md); uses → [Domain.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Domain.cs), [ProjectScanner.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ProjectScanner.cs), [ToolRunner.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ToolRunner.cs)

**들어오는 연결:** dispatches ← [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); mode:agent ← [Program.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs); mode:serve ← [Program.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs); mode:server ← [Program.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs); uses ← [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs), [Program.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs)

### Connection.cs

`C#` · 78 줄 · code · namespace `PlayBook` · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Connection.cs)

**심볼**

- [ClientSettings](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Connection.cs#L7) · record
- [Connection](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Connection.cs#L10) · class — This file contains device configuration, never a second project ledger.
- [Connection.Status](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Connection.cs#L22) · method
- [Connection.Configure](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Connection.cs#L23) · method
- [Connection.ServerUri](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Connection.cs#L34) · method
- [Connection.Connect](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Connection.cs#L41) · method
- [Connection.Disconnect](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Connection.cs#L51) · method
- [Connection.Request](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Connection.cs#L58) · method

**나가는 연결:** uses → [Domain.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Domain.cs)

**들어오는 연결:** dispatches ← [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); injects ← [AgentWorker.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs), [Library.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs), [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs), [ProjectScanner.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ProjectScanner.cs); mode:agent ← [Program.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs); mode:serve ← [Program.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs); mode:server ← [Program.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs); uses ← [Program.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs), [Store.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs)

### Desktop.cs

`C#` · 20 줄 · code · namespace `PlayBook` · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Desktop.cs)

**심볼**

- [Desktop](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Desktop.cs#L6) · class
- [Desktop.PickFolder](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Desktop.cs#L8) · method

**나가는 연결:** uses → [Domain.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Domain.cs)

**들어오는 연결:** dispatches ← [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); uses ← [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs)

### Domain.cs

`C#` · 23 줄 · code · namespace `PlayBook` · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Domain.cs)

**심볼**

- [Entry](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Domain.cs#L6) · record
- [WriteEntry](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Domain.cs#L8) · record
- [Change](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Domain.cs#L10) · record
- [DomainError](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Domain.cs#L12) · class
- [Json](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Domain.cs#L16) · class
- [Json.Print](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Domain.cs#L20) · method
- [Json.Read](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Domain.cs#L21) · method
- [Json.Text](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Domain.cs#L22) · method

**들어오는 연결:** injects ← [Folders.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs), [Ontology.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Ontology.cs); mode:cli ← [Program.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs); mode:serve ← [Program.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs); mode:server ← [Program.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs); uses ← [Access.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Access.cs), [AgentWorker.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs), [Connection.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Connection.cs), [Desktop.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Desktop.cs), [Folders.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs), [Harnesses.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs) … 외 11개

### Folders.cs

`C#` · 259 줄 · code · namespace `PlayBook` · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs)

**심볼**

- [FolderPlan](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs#L7) · record
- [ProjectFileEntry](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs#L9) · record
- [Folders](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs#L12) · class — Project-internal file operations.
- [in](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs#L167) · record
- [Folders.List](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs#L68) · method
- [Folders.Files](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs#L80) · method
- [Folders.Create](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs#L120) · method
- [Folders.Plan](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs#L198) · method
- [Folders.Apply](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs#L210) · method
- [Folders.Recover](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs#L238) · method

**나가는 연결:** injects → [Domain.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Domain.cs), [Store.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs), [ToolRunner.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ToolRunner.cs), [Workspace.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs); uses → [Domain.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Domain.cs)

**들어오는 연결:** dispatches ← [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); uses ← [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs)

### Harnesses.cs

`C#` · 181 줄 · code · namespace `PlayBook` · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs)

**심볼**

- [Harnesses](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs#L10) · class — A bounded, native adaptation of Harness²'s propose/probe/compose/reflection loop.
- [Harnesses.Active](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs#L30) · method
- [Harnesses.Snapshot](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs#L38) · method
- [Harnesses.Validate](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs#L43) · method
- [Harnesses.State](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs#L60) · method
- [Harnesses.Propose](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs#L69) · method
- [Harnesses.Probe](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs#L87) · method
- [Harnesses.Compare](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs#L129) · method
- [Harnesses.Adopt](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs#L137) · method
- [Harnesses.Disable](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs#L174) · method

**나가는 연결:** injects → [Store.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs), [Workspace.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs); uses → [Domain.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Domain.cs), [Orchestration.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Orchestration.cs)

**들어오는 연결:** dispatches ← [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); uses ← [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs), [Orchestration.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Orchestration.cs), [Store.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs)

### Library.cs

`C#` · 108 줄 · code · namespace `PlayBook` · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs)

**심볼**

- [Library](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs#L7) · class — Immutable, content-addressed shared references.
- [Library.List](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs#L11) · method
- [Library.Register](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs#L12) · method
- [Library.Put](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs#L21) · method
- [Library.Download](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs#L62) · method
- [Library.Resolve](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs#L76) · method
- [Library.Preview](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs#L95) · method
- [Library.Text](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs#L101) · method

**나가는 연결:** calls-op → [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); injects → [Connection.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Connection.cs), [Store.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs), [Workspace.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs); uses → [Domain.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Domain.cs), [Workspace.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs)

**들어오는 연결:** dispatches ← [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); mode:serve ← [Program.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs); mode:server ← [Program.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs); uses ← [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs), [Program.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs)

### McpTools.cs

`C#` · 102 줄 · code · mcp-tool-type · namespace `PlayBook` · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs)

**심볼**

- [McpTools](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L6) · class
- [McpTools.List](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L10) · method — List/search records.
- [McpTools.Get](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L12) · method — Read a record and revision before modifying it.
- [McpTools.Context](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L14) · method — Start here: project plan, next tasks, evidence, assets, decisions, inherited preferences and accepted canon, ontology and recent changes.
- [McpTools.OntologyIngest](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L16) · method — Ingest development messages, research or documents with provenance.
- [McpTools.OntologySearch](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L18) · method — Search this project's development ontology by Korean/English keywords.
- [McpTools.OntologyReference](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L20) · method — Resolve ontology IDs or search terms into source-backed references and relation neighborhoods.
- [McpTools.OntologyUsage](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L22) · method — Record which ontology references were used and why.
- [McpTools.OntologyConnections](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L24) · method — List registered read-only external ontology connections and import status for a project.
- [McpTools.OntologyConnect](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L26) · method — Register/update a user-selected external ontology JSON endpoint.
- [McpTools.OntologySync](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L28) · method — Fetch a registered external ontology via bounded read-only HTTP GET and atomically import its sources.
- [McpTools.OntologyRebuild](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L30) · method — Backfill existing PlayBook project/task/note/research/message/decision/asset/run records into the ontology.
- [McpTools.Save](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L32) · method — Create/update JSON: {id:null|existing,kind,projectId:null|id,title,status,body:{...},expectedRevision:0|current,actor,reason}.
- [McpTools.Changes](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L34) · method — Immutable change events after sequence cursor; max 1000, use last sequence to continue.
- [McpTools.ApproveCanon](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L36) · method — Explicit reviewer action: promote proposed change into accepted canon of its own/ancestor project, atomic and revision checked.
- [McpTools.Git](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs#L38) · method — Read live Git status, HEAD and recent commits; no Git mutations.
- … 외 31개

**여기서 정의한 인터페이스:** MCP `list`, MCP `get`, MCP `context`, MCP `ontology_ingest`, MCP `ontology_search`, MCP `ontology_reference`, MCP `ontology_usage`, MCP `ontology_connections` … 외 38개

**나가는 연결:** calls-op → [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); injects → [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); uses → [Domain.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Domain.cs)

**들어오는 연결:** mode:mcp ← [Program.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs); mode:serve ← [Program.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs); mode:server ← [Program.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs); uses ← [Program.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs)

### Ontology.cs

`C#` · 505 줄 · code · namespace `PlayBook` · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Ontology.cs)

**심볼**

- [Ontology](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Ontology.cs#L11) · class — Ontology is a projection and a source ledger inside Store, never a second database.
- [Ontology.Validate](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Ontology.cs#L56) · method
- [Ontology.CompactEntry](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Ontology.cs#L134) · method
- [Ontology.CompactReference](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Ontology.cs#L171) · method — Prompt references are excerpts.
- [Ontology.ProjectRecord](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Ontology.cs#L221) · method
- [Ontology.Ingest](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Ontology.cs#L317) · method
- [Ontology.Search](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Ontology.cs#L361) · method
- [Ontology.Reference](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Ontology.cs#L369) · method
- [Ontology.Usage](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Ontology.cs#L390) · method
- [Ontology.Connections](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Ontology.cs#L426) · method
- [Ontology.Connect](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Ontology.cs#L432) · method
- [Ontology.Sync](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Ontology.cs#L444) · method
- [Ontology.Rebuild](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Ontology.cs#L492) · method

**나가는 연결:** injects → [Domain.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Domain.cs), [Store.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs); uses → [Domain.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Domain.cs)

**들어오는 연결:** dispatches ← [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); uses ← [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs), [Orchestration.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Orchestration.cs), [Store.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs), [Workspace.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs)

### Operations.cs

`C#` · 113 줄 · code · namespace `PlayBook` · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs)

> **노트**
>
> 새 기능이 붙는 단 한 곳입니다. AGENTS.md: CLI·GUI·MCP 기능은 이 공용 Operations 서비스를 쓰고, 두 번째 데이터 권한을 만들지 않습니다.

**심볼**

- [Operations](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L4) · class
- [Operations.LocalOperation](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L8) · method
- [Operations.Execute](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs#L11) · method

**여기서 정의한 인터페이스:** dispatch `Operations.Execute` (65 ops, L33)

**나가는 연결:** dispatches → [Access.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Access.cs), [AgentWorker.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs), [Connection.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Connection.cs), [Desktop.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Desktop.cs), [Folders.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs), [Harnesses.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs) … 외 8개; injects → [Access.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Access.cs), [Connection.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Connection.cs), [Providers.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Providers.cs), [Store.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs), [ToolRunner.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ToolRunner.cs), [Workspace.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs); refers → [API.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/API.md); uses → [AgentWorker.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs), [Desktop.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Desktop.cs), [Domain.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Domain.cs), [Folders.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs), [Harnesses.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs), [Library.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs) … 외 3개

**들어오는 연결:** calls-op ← [AgentWorker.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs), [Library.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs), [McpTools.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs), [install.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py), [oz_graphify_mcp.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_graphify_mcp.py), [check-package.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/check-package.py) … 외 15개; injects ← [AgentWorker.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs), [McpTools.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs); mode:agent ← [Program.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs); mode:cli ← [Program.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs); mode:serve ← [Program.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs); mode:server ← [Program.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs); uses ← [Program.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs)

### Orchestration.cs

`C#` · 196 줄 · code · namespace `PlayBook` · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Orchestration.cs)

**심볼**

- [Orchestration](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Orchestration.cs#L8) · class — Queue, leases and results live in the same revisioned, audited ledger as projects.
- [Orchestration.Register](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Orchestration.cs#L22) · method
- [Orchestration.Enqueue](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Orchestration.cs#L37) · method
- [Orchestration.Enqueue](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Orchestration.cs#L42) · method
- [Orchestration.State](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Orchestration.cs#L103) · method
- [Orchestration.Claim](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Orchestration.cs#L110) · method
- [Orchestration.Heartbeat](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Orchestration.cs#L152) · method
- [Orchestration.Cancel](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Orchestration.cs#L187) · method

**나가는 연결:** injects → [Store.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs), [Workspace.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs); uses → [Domain.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Domain.cs), [Harnesses.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs), [Ontology.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Ontology.cs)

**들어오는 연결:** dispatches ← [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); uses ← [Harnesses.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs), [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs)

### PlayBook.csproj

`MSBuild` · 19 줄 · config · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/PlayBook.csproj)

> PlayBook: Microsoft.NET.Sdk.Web, net10.0, v0.2.0  
> <sub>출처: project file</sub>

**들어오는 연결:** refers ← [Start-PlayBook-Desktop.ps1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Start-PlayBook-Desktop.ps1), [playbook-harness.ps1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/playbook-harness.ps1), [playbook.ps1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/playbook.ps1), [playbook.sh](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/playbook.sh), [prepare-public-source.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py); runs ← [Start-PlayBook-Desktop.ps1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Start-PlayBook-Desktop.ps1), [codex-mcp.toml](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/examples/codex-mcp.toml), [mcp.json](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/examples/mcp.json), [playbook-harness.ps1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/playbook-harness.ps1), [playbook.ps1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/playbook.ps1), [playbook.sh](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/playbook.sh) … 외 11개

### Program.cs

`C#` · 111 줄 · code · entry · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs)

**여기서 정의한 인터페이스:** mode `worker` (L19–19), mode `cli` (L20–32), mode `mcp` (L33–40), mode `agent` (L41–48), mode `serve` (L49–112), mode `server` (L49–112), route `GET /session` (L98), route `POST /auth/login` (L99) … 외 4개

**나가는 연결:** mode:agent → [AgentWorker.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs), [Connection.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Connection.cs), [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); mode:cli → [Domain.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Domain.cs), [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); mode:mcp → [McpTools.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs); mode:serve → [Access.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Access.cs), [AgentWorker.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs), [Connection.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Connection.cs), [Domain.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Domain.cs), [Library.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs), [McpTools.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs) … 외 3개; mode:server → [Access.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Access.cs), [AgentWorker.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs), [Connection.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Connection.cs), [Domain.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Domain.cs), [Library.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs), [McpTools.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs) … 외 3개; mode:worker → [ToolRunner.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ToolRunner.cs); refers → [PORTABLE-AND-AGENTS.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/PORTABLE-AND-AGENTS.md); uses → [Access.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Access.cs), [AgentWorker.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs), [Connection.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Connection.cs), [Domain.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Domain.cs), [Library.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs), [McpTools.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/McpTools.cs) … 외 5개

### ProjectScanner.cs

`C#` · 84 줄 · code · namespace `PlayBook` · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ProjectScanner.cs)

**심볼**

- [ProjectCandidate](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ProjectScanner.cs#L7) · record
- [ProjectScan](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ProjectScanner.cs#L8) · record
- [ProjectScanner](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ProjectScanner.cs#L10) · class
- [ProjectScanner.Scan](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ProjectScanner.cs#L16) · method
- [ProjectScanner.Import](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ProjectScanner.cs#L54) · method
- [ProjectScanner.CheckLinks](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ProjectScanner.cs#L79) · method

**나가는 연결:** injects → [Connection.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Connection.cs), [Store.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs), [Workspace.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs); refers → [AGENTS.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AGENTS.md); uses → [Domain.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Domain.cs)

**들어오는 연결:** dispatches ← [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); uses ← [AgentWorker.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs), [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs)

### Providers.cs

`C#` · 124 줄 · code · namespace `PlayBook` · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Providers.cs)

**심볼**

- [ProviderCommand](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Providers.cs#L8) · record
- [ProviderStatus](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Providers.cs#L9) · record
- [Providers](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Providers.cs#L11) · class
- [Providers.Self](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Providers.cs#L13) · method
- [Providers.Find](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Providers.cs#L19) · method
- [Providers.StartInfo](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Providers.cs#L39) · method
- [Providers.Status](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Providers.cs#L57) · method
- [Providers.All](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Providers.cs#L71) · method
- [Providers.Login](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Providers.cs#L72) · method
- [Providers.McpConfig](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Providers.cs#L84) · method
- [Providers.Run](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Providers.cs#L90) · method

**나가는 연결:** injects → [Store.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs); refers → [mcp.json](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/examples/mcp.json); uses → [Domain.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Domain.cs)

**들어오는 연결:** dispatches ← [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); injects ← [AgentWorker.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs), [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); uses ← [Program.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs)

### README.en.md

`Markdown` · 39 줄 · docs · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.en.md)

> Manage projects, shared references and AI work through one revisioned ledger.  
> <sub>출처: first paragraph</sub>

**심볼**

- [PlayBook OS](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.en.md#L1) · h1
- [Install on Windows](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.en.md#L5) · h2
- [CLI and MCP](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.en.md#L18) · h2
- [Verification and scope](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.en.md#L33) · h2

**나가는 연결:** documents → [README.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.md), [API.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/API.md), [ONTOLOGY.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/ONTOLOGY.md), [PORTABLE-AND-AGENTS.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/PORTABLE-AND-AGENTS.md), [RELEASE-0.2.0.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/RELEASE-0.2.0.md)

**들어오는 연결:** documents ← [README.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.md); refers ← [package.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/package.py), [prepare-public-source.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py)

### README.md

`Markdown` · 184 줄 · docs · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.md)

> 프로젝트와 AI 작업을 관리하는 공통 원장.  
> <sub>출처: first paragraph</sub>

**심볼**

- [PlayBook OS](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.md#L1) · h1
- [시작](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.md#L8) · h2
- [사용 순서](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.md#L40) · h2
- [Headless 예시](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.md#L59) · h2
- [MCP 연결](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.md#L76) · h2
- [도구/서버](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.md#L108) · h2
- [데이터와 이식](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.md#L130) · h2
- [현재 구현 범위](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.md#L143) · h2
- [개발 온톨로지](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.md#L158) · h2
- [검증/설계](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.md#L170) · h2

**나가는 연결:** documents → [README.en.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.en.md), [API.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/API.md), [CLAUDE-AND-FOLDERS.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/CLAUDE-AND-FOLDERS.md), [GRAPHIFY-OZ-MAC.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/GRAPHIFY-OZ-MAC.md), [GRAPHIFY.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/GRAPHIFY.md), [HARNESS.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/HARNESS.md) … 외 5개

**들어오는 연결:** documents ← [README.en.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.en.md); refers ← [Workspace.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs), [package.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/package.py), [prepare-public-source.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py), [real-provider-smoke.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/real-provider-smoke.py)

### START_GRAPHIFY.cmd

`Batch` · 5 줄 · script · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/START_GRAPHIFY.cmd)

**나가는 연결:** refers → [graphify.ps1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/graphify.ps1); runs → [graphify.ps1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/graphify.ps1)

### START_PLAYBOOK.cmd

`Batch` · 3 줄 · script · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/START_PLAYBOOK.cmd)

**나가는 연결:** refers → [playbook.ps1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/playbook.ps1); runs → [playbook.ps1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/playbook.ps1)

**들어오는 연결:** refers ← [prepare-public-source.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py)

### Start-PlayBook-Desktop.ps1

`PowerShell` · 34 줄 · script · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Start-PlayBook-Desktop.ps1)

> 바탕화면 바로가기용: 서버가 꺼져 있으면 켜고, 화면을 엽니다.  
> <sub>출처: file comment</sub>

**나가는 연결:** refers → [PlayBook.csproj](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/PlayBook.csproj); runs → [PlayBook.csproj](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/PlayBook.csproj)

### Store.cs

`C#` · 183 줄 · code · namespace `PlayBook` · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs)

> **노트**
>
> 모든 기록 변경은 여기서 검증을 통과하고 같은 트랜잭션 안에서 감사 이벤트를 남겨야 합니다 (AGENTS.md).

**심볼**

- [Store](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs#L6) · class
- [Store.Open](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs#L32) · method
- [Store.List](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs#L40) · method
- [Store.Get](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs#L56) · method
- [Store.Get](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs#L62) · method
- [Store.Save](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs#L68) · method
- [Store.Save](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs#L74) · method
- [Store.Approve](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs#L141) · method
- [Store.Events](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs#L167) · method
- [Store.Backup](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs#L176) · method

**나가는 연결:** uses → [Connection.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Connection.cs), [Domain.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Domain.cs), [Harnesses.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs), [Ontology.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Ontology.cs)

**들어오는 연결:** dispatches ← [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); injects ← [AgentWorker.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs), [Folders.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs), [Harnesses.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs), [Library.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs), [Ontology.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Ontology.cs), [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs) … 외 5개; mode:serve ← [Program.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs); mode:server ← [Program.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs); uses ← [Program.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs)

### ToolRunner.cs

`C#` · 132 줄 · code · namespace `PlayBook` · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ToolRunner.cs)

**심볼**

- [ToolDefinition](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ToolRunner.cs#L6) · record
- [RunState](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ToolRunner.cs#L9) · record
- [ToolRunner](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ToolRunner.cs#L11) · class
- [ToolRunner.Definitions](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ToolRunner.cs#L13) · method
- [ToolRunner.RunsList](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ToolRunner.cs#L18) · method
- [ToolRunner.Status](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ToolRunner.cs#L25) · method
- [ToolRunner.Start](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ToolRunner.cs#L43) · method
- [ToolRunner.Stop](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ToolRunner.cs#L85) · method
- [ToolRunner.Logs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ToolRunner.cs#L102) · method
- [ToolRunner.Worker](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/ToolRunner.cs#L111) · method

**나가는 연결:** injects → [Store.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs); uses → [Domain.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Domain.cs)

**들어오는 연결:** dispatches ← [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); injects ← [Folders.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs), [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); mode:worker ← [Program.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs); uses ← [AgentWorker.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs), [Program.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs)

### Workspace.cs

`C#` · 264 줄 · code · namespace `PlayBook` · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs)

**심볼**

- [Workspace](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L8) · class
- [MediaFile](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L19) · record
- [Workspace.IsPreviewableImage](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L20) · method
- [Workspace.FilePath](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L21) · method
- [Workspace.MediaType](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L22) · method
- [Workspace.Preview](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L50) · method
- [Workspace.ReadText](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L61) · method
- [Workspace.ShareAsset](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L68) · method
- [Workspace.Context](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L136) · method
- [Workspace.PathFor](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L167) · method
- [Workspace.Discover](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L173) · method
- [Workspace.Git](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L191) · method
- [Workspace.Run](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L200) · method
- [Workspace.Export](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L213) · method
- [Workspace.VerifyAsset](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Workspace.cs#L252) · method

**나가는 연결:** injects → [Store.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Store.cs); refers → [AGENTS.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AGENTS.md), [README.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.md); uses → [Domain.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Domain.cs), [Ontology.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Ontology.cs)

**들어오는 연결:** dispatches ← [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); injects ← [AgentWorker.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AgentWorker.cs), [Folders.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Folders.cs), [Harnesses.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Harnesses.cs), [Library.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs), [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs), [Orchestration.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Orchestration.cs) … 외 1개; mode:serve ← [Program.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs); mode:server ← [Program.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs); uses ← [Library.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Library.cs), [Program.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs)

### appsettings.Development.json

`JSON` · 8 줄 · config · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/appsettings.Development.json)

> keys: Logging  
> <sub>출처: json keys</sub>

**들어오는 연결:** refers ← [prepare-public-source.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py)

### appsettings.json

`JSON` · 9 줄 · config · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/appsettings.json)

> keys: Logging, AllowedHosts  
> <sub>출처: json keys</sub>

**들어오는 연결:** refers ← [prepare-public-source.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py)

### graphify.ps1

`PowerShell` · 6 줄 · script · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/graphify.ps1)

**나가는 연결:** refers → [graphify-playbook.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py); runs → [graphify-playbook.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py)

**들어오는 연결:** refers ← [START_GRAPHIFY.cmd](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/START_GRAPHIFY.cmd); runs ← [START_GRAPHIFY.cmd](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/START_GRAPHIFY.cmd)

### packages.lock.json

`JSON` · 104 줄 · config · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/packages.lock.json)

> keys: version, dependencies  
> <sub>출처: json keys</sub>

**들어오는 연결:** refers ← [prepare-public-source.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py)

### playbook-harness.ps1

`PowerShell` · 12 줄 · script · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/playbook-harness.ps1)

**나가는 연결:** refers → [PlayBook.csproj](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/PlayBook.csproj); runs → [PlayBook.csproj](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/PlayBook.csproj)

### playbook.ps1

`PowerShell` · 10 줄 · script · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/playbook.ps1)

**나가는 연결:** refers → [PlayBook.csproj](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/PlayBook.csproj); runs → [PlayBook.csproj](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/PlayBook.csproj)

**들어오는 연결:** refers ← [START_PLAYBOOK.cmd](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/START_PLAYBOOK.cmd), [prepare-public-source.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py); runs ← [START_PLAYBOOK.cmd](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/START_PLAYBOOK.cmd)

### playbook.sh

`Shell` · 9 줄 · script · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/playbook.sh)

**나가는 연결:** refers → [PlayBook.csproj](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/PlayBook.csproj); runs → [PlayBook.csproj](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/PlayBook.csproj)

**들어오는 연결:** refers ← [prepare-public-source.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py)


## Properties

### Properties/launchSettings.json

`JSON` · 23 줄 · config · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Properties/launchSettings.json)

> keys: $schema, profiles  
> <sub>출처: json keys</sub>

**들어오는 연결:** refers ← [prepare-public-source.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py)


## docs

### docs/API.md

`Markdown` · 153 줄 · docs · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/API.md)

> 모든 진입점이 Operations.Execute(operation, arguments)를 공유한다.  
> <sub>출처: first paragraph</sub>

**심볼**

- [PlayBook API / 데이터 계약](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/API.md#L1) · h1
- [WriteEntry](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/API.md#L72) · h2
- [ToolDefinition (`PLAYBOOK_HOME/tools.json`)](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/API.md#L120) · h2
- [오류](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/API.md#L145) · h2
- [작업 지침 개선 API](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/API.md#L149) · h2

**나가는 연결:** documents → [CLAUDE-AND-FOLDERS.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/CLAUDE-AND-FOLDERS.md), [HARNESS.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/HARNESS.md), [ONTOLOGY.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/ONTOLOGY.md)

**들어오는 연결:** documents ← [README.en.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.en.md), [README.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.md), [CENTRAL-SERVER-PLAN.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/CENTRAL-SERVER-PLAN.md), [PORTABLE-AND-AGENTS.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/PORTABLE-AND-AGENTS.md); refers ← [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs), [package.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/package.py), [prepare-public-source.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py)

### docs/CENTRAL-SERVER-PLAN.md

`Markdown` · 195 줄 · docs · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/CENTRAL-SERVER-PLAN.md)

> PlayBook 서버가 프로젝트 지침, 목적, 파일 목록, 작업과 검증 기록의 공통 원장을 관리하고, 로그인한 각 컴퓨터의 클라이언트가 로컬 AI와 도구를 실행한다.  
> <sub>출처: first paragraph</sub>

**심볼**

- [PlayBook 중앙 서버와 기기 간 AI 오케스트레이션 설계안](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/CENTRAL-SERVER-PLAN.md#L1) · h1
- [사용 흐름](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/CENTRAL-SERVER-PLAN.md#L12) · h2
- [현재 구현과 확장 지점](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/CENTRAL-SERVER-PLAN.md#L34) · h2
- [서버와 클라이언트의 책임](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/CENTRAL-SERVER-PLAN.md#L53) · h2
- [로그인과 실시간 공유](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/CENTRAL-SERVER-PLAN.md#L73) · h2
- [파일 목록과 기기별 작업 폴더](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/CENTRAL-SERVER-PLAN.md#L90) · h2
- [AI 하네스와 지침 반영](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/CENTRAL-SERVER-PLAN.md#L108) · h2
- [다른 기기의 여러 AI 작업 조정](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/CENTRAL-SERVER-PLAN.md#L130) · h2
- [구현 순서와 확인할 결과](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/CENTRAL-SERVER-PLAN.md#L171) · h2
- [이번 설계의 확인 범위](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/CENTRAL-SERVER-PLAN.md#L190) · h2

**나가는 연결:** documents → [API.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/API.md), [PORTABLE-AND-AGENTS.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/PORTABLE-AND-AGENTS.md)

**들어오는 연결:** documents ← [PLAN.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/PLAN.md); refers ← [prepare-public-source.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py)

### docs/CLAUDE-AND-FOLDERS.md

`Markdown` · 61 줄 · docs · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/CLAUDE-AND-FOLDERS.md)

> DevWork 전체에서 같은 PlayBook을 사용하려면 사용자 범위 MCP에 등록한다:  
> <sub>출처: first paragraph</sub>

**심볼**

- [Claude 연결과 폴더 관리](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/CLAUDE-AND-FOLDERS.md#L1) · h1
- [Claude Code](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/CLAUDE-AND-FOLDERS.md#L3) · h2
- [Claude Desktop](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/CLAUDE-AND-FOLDERS.md#L16) · h2
- [프로젝트 내부 폴더 정리](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/CLAUDE-AND-FOLDERS.md#L28) · h2

**나가는 연결:** documents → [PORTABLE-AND-AGENTS.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/PORTABLE-AND-AGENTS.md)

**들어오는 연결:** documents ← [README.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.md), [API.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/API.md); refers ← [prepare-public-source.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py)

### docs/GRAPHIFY-OZ-MAC.md

`Markdown` · 86 줄 · docs · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/GRAPHIFY-OZ-MAC.md)

> 오즈는 Mac의 Claude Code 앱을 사용한다는 사용자 정정을 반영했습니다.  
> <sub>출처: first paragraph</sub>

**심볼**

- [오즈용 Mac 배포본](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/GRAPHIFY-OZ-MAC.md#L1) · h1
- [전달 파일](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/GRAPHIFY-OZ-MAC.md#L8) · h2
- [설치와 구성](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/GRAPHIFY-OZ-MAC.md#L20) · h2
- [Claude가 사용하는 도구](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/GRAPHIFY-OZ-MAC.md#L35) · h2
- [빌드와 검증](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/GRAPHIFY-OZ-MAC.md#L57) · h2

**나가는 연결:** documents → [OZ-LOGGING.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/OZ-LOGGING.md)

**들어오는 연결:** documents ← [README.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.md)

### docs/GRAPHIFY.md

`Markdown` · 131 줄 · docs · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/GRAPHIFY.md)

> 공식 Graphify를 로컬 코드 분석 도구로 연결했습니다.  
> <sub>출처: first paragraph</sub>

**심볼**

- [Graphify와 PlayBook 함께 사용하기](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/GRAPHIFY.md#L1) · h1
- [화면 사용](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/GRAPHIFY.md#L6) · h2
- [CLI](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/GRAPHIFY.md#L19) · h2
- [AI / MCP](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/GRAPHIFY.md#L36) · h2
- [연결 범위와 출처](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/GRAPHIFY.md#L66) · h2
- [설치 위치와 현재 실행본](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/GRAPHIFY.md#L85) · h2
- [검증](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/GRAPHIFY.md#L121) · h2

**들어오는 연결:** documents ← [README.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.md)

### docs/HARNESS.md

`Markdown` · 101 줄 · docs · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/HARNESS.md)

> Harness²의 제안 → 시험 → 비교·조합 → 검토 후 채택 → 교훈 재사용 절차 중 현재 PlayBook에 맞는 부분을 .NET 엔진에 구현했다.  
> <sub>출처: first paragraph</sub>

**심볼**

- [작업 지침 개선](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/HARNESS.md#L1) · h1
- [화면에서 사용](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/HARNESS.md#L8) · h2
- [실행 경계](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/HARNESS.md#L21) · h2
- [공통 API](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/HARNESS.md#L32) · h2
- [원장과 검증](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/HARNESS.md#L63) · h2

**들어오는 연결:** documents ← [README.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.md), [API.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/API.md), [PLAN.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/PLAN.md)

### docs/ONTOLOGY.md

`Markdown` · 210 줄 · docs · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/ONTOLOGY.md)

> PlayBook에 기록된 대화, 연구 결과와 개발 상태를 출처가 있는 개발 지식으로 모으고 검색·참조합니다.  
> <sub>출처: first paragraph</sub>

**심볼**

- [개발 온톨로지](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/ONTOLOGY.md#L1) · h1
- [자동 갱신이 일어나는 범위](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/ONTOLOGY.md#L7) · h2
- [동작과 인터페이스](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/ONTOLOGY.md#L38) · h2
- [대화·연구 수집](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/ONTOLOGY.md#L58) · h2
- [검색·참조·사용 이력](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/ONTOLOGY.md#L111) · h2
- [외부 온톨로지 연결](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/ONTOLOGY.md#L147) · h2
- [검증](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/ONTOLOGY.md#L198) · h2

**나가는 연결:** documents → [ontology-feed.json](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/examples/ontology-feed.json), [ontology-research.json](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/examples/ontology-research.json)

**들어오는 연결:** documents ← [README.en.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.en.md), [README.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.md), [API.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/API.md), [PLAN.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/PLAN.md), [PORTABLE-AND-AGENTS.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/PORTABLE-AND-AGENTS.md); refers ← [package.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/package.py), [prepare-public-source.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py)

### docs/OZ-LOGGING.md

`Markdown` · 44 줄 · docs · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/OZ-LOGGING.md)

> 0.1.1은 Claude Code가 oz-playbook, oz-graphify 두 stdio 연결을 사용하도록 설치합니다.  
> <sub>출처: first paragraph</sub>

**심볼**

- [오즈의 AI 대화 중심 운영과 로그](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/OZ-LOGGING.md#L1) · h1
- [자동 기록](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/OZ-LOGGING.md#L7) · h2
- [오즈와 담당자의 사용법](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/OZ-LOGGING.md#L21) · h2
- [기존 설치와 검증](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/OZ-LOGGING.md#L35) · h2

**들어오는 연결:** documents ← [README.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.md), [GRAPHIFY-OZ-MAC.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/GRAPHIFY-OZ-MAC.md)

### docs/PLAN.md

`Markdown` · 59 줄 · docs · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/PLAN.md)

> DevWork의 프로젝트 기획, 실행, 변경, 검증, 인수인계를 한 원장에서 관리한다.  
> <sub>출처: first paragraph</sub>

**심볼**

- [Project PlayBook — 설계와 구현 계획](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/PLAN.md#L1) · h1
- [목적](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/PLAN.md#L3) · h2
- [구현 단위와 검증](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/PLAN.md#L8) · h2
- [데이터 모델](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/PLAN.md#L15) · h2
- [경계](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/PLAN.md#L25) · h2
- [후속 확장](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/PLAN.md#L35) · h2
- [개발 온톨로지 확장 (2026-10-07)](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/PLAN.md#L45) · h2
- [작업 지침 개선 (2026-10-18)](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/PLAN.md#L54) · h2

**나가는 연결:** documents → [CENTRAL-SERVER-PLAN.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/CENTRAL-SERVER-PLAN.md), [HARNESS.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/HARNESS.md), [ONTOLOGY.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/ONTOLOGY.md), [PORTABLE-AND-AGENTS.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/PORTABLE-AND-AGENTS.md)

**들어오는 연결:** documents ← [README.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.md); refers ← [prepare-public-source.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py)

### docs/PORTABLE-AND-AGENTS.md

`Markdown` · 64 줄 · docs · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/PORTABLE-AND-AGENTS.md)

> Extract the complete release ZIP and double-click INSTALLPLAYBOOK.cmd.  
> <sub>출처: first paragraph</sub>

**심볼**

- [Installation, central server and AI agents](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/PORTABLE-AND-AGENTS.md#L1) · h1
- [Windows portable installation](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/PORTABLE-AND-AGENTS.md#L3) · h2
- [Select projects and references](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/PORTABLE-AND-AGENTS.md#L15) · h2
- [Connect Codex and Claude](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/PORTABLE-AND-AGENTS.md#L21) · h2
- [Central server](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/PORTABLE-AND-AGENTS.md#L33) · h2
- [Current boundaries](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/PORTABLE-AND-AGENTS.md#L56) · h2

**나가는 연결:** documents → [API.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/API.md), [ONTOLOGY.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/ONTOLOGY.md)

**들어오는 연결:** documents ← [README.en.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.en.md), [README.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.md), [CENTRAL-SERVER-PLAN.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/CENTRAL-SERVER-PLAN.md), [CLAUDE-AND-FOLDERS.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/CLAUDE-AND-FOLDERS.md), [PLAN.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/PLAN.md), [RELEASE-0.2.0.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/RELEASE-0.2.0.md); refers ← [Program.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Program.cs), [package.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/package.py), [prepare-public-source.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py)

### docs/RELEASE-0.2.0.md

`Markdown` · 21 줄 · docs · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/RELEASE-0.2.0.md)

> This release adds a Windows portable installer, Korean/English UI, recursive folder selection, shared reference copies, central workspace login, and a leased AI queue for installed Codex and Claude Code clients.  
> <sub>출처: first paragraph</sub>

**심볼**

- [PlayBook OS 0.2.0](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/RELEASE-0.2.0.md#L1) · h1
- [Verification](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/RELEASE-0.2.0.md#L7) · h2
- [Limits](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/RELEASE-0.2.0.md#L17) · h2

**나가는 연결:** documents → [PORTABLE-AND-AGENTS.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/PORTABLE-AND-AGENTS.md)

**들어오는 연결:** documents ← [README.en.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.en.md), [README.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.md); refers ← [package.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/package.py), [prepare-public-source.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py)


## examples

### examples/codex-mcp.toml

`TOML` · 7 줄 · config · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/examples/codex-mcp.toml)

> Paste into the MCP client configuration after building.  
> <sub>출처: file comment</sub>

**나가는 연결:** runs → [PlayBook.csproj](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/PlayBook.csproj)

### examples/mcp.json

`JSON` · 9 줄 · config · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/examples/mcp.json)

> keys: mcpServers  
> <sub>출처: json keys</sub>

**나가는 연결:** runs → [PlayBook.csproj](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/PlayBook.csproj)

**들어오는 연결:** refers ← [Providers.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Providers.cs), [graphify-playbook.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py)

### examples/ontology-feed.json

`JSON` · 15 줄 · config · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/examples/ontology-feed.json)

> keys: sources  
> <sub>출처: json keys</sub>

**들어오는 연결:** documents ← [ONTOLOGY.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/ONTOLOGY.md)

### examples/ontology-research.json

`JSON` · 17 줄 · config · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/examples/ontology-research.json)

> keys: projectId, sourceId, sourceType, title, content, sourceUri, actor, reason, entities, relations  
> <sub>출처: json keys</sub>

**들어오는 연결:** documents ← [ONTOLOGY.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/ONTOLOGY.md)


## portable

### portable/INSTALL_PLAYBOOK.cmd

`Batch` · 3 줄 · script · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/INSTALL_PLAYBOOK.cmd)

**나가는 연결:** refers → [Install-PlayBook.ps1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/Install-PlayBook.ps1); runs → [Install-PlayBook.ps1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/Install-PlayBook.ps1)

### portable/Install-PlayBook.ps1

`PowerShell` · 81 줄 · script · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/Install-PlayBook.ps1)

**나가는 연결:** refers → [Start-PlayBook.ps1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/Start-PlayBook.ps1); runs → [PlayBook.csproj](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/PlayBook.csproj), [Start-PlayBook.ps1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/Start-PlayBook.ps1)

**들어오는 연결:** refers ← [INSTALL_PLAYBOOK.cmd](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/INSTALL_PLAYBOOK.cmd), [check-package.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/check-package.py); runs ← [INSTALL_PLAYBOOK.cmd](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/INSTALL_PLAYBOOK.cmd)

### portable/START_PLAYBOOK.cmd

`Batch` · 3 줄 · script · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/START_PLAYBOOK.cmd)

**나가는 연결:** refers → [Start-PlayBook.ps1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/Start-PlayBook.ps1); runs → [Start-PlayBook.ps1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/Start-PlayBook.ps1)

### portable/STOP_PLAYBOOK.cmd

`Batch` · 3 줄 · script · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/STOP_PLAYBOOK.cmd)

**나가는 연결:** refers → [Stop-PlayBook.ps1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/Stop-PlayBook.ps1); runs → [Stop-PlayBook.ps1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/Stop-PlayBook.ps1)

### portable/Start-PlayBook.ps1

`PowerShell` · 40 줄 · script · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/Start-PlayBook.ps1)

**나가는 연결:** runs → [PlayBook.csproj](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/PlayBook.csproj)

**들어오는 연결:** refers ← [Install-PlayBook.ps1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/Install-PlayBook.ps1), [START_PLAYBOOK.cmd](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/START_PLAYBOOK.cmd), [check-package.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/check-package.py); runs ← [Install-PlayBook.ps1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/Install-PlayBook.ps1), [START_PLAYBOOK.cmd](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/START_PLAYBOOK.cmd)

### portable/Stop-PlayBook.ps1

`PowerShell` · 11 줄 · script · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/Stop-PlayBook.ps1)

**들어오는 연결:** refers ← [STOP_PLAYBOOK.cmd](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/STOP_PLAYBOOK.cmd), [check-package.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/check-package.py); runs ← [STOP_PLAYBOOK.cmd](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/STOP_PLAYBOOK.cmd)

### portable/oz/00_먼저읽기.txt

`text` · 89 줄 · docs · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/00_먼저읽기.txt)

> 오즈용 PlayBook + Graphify — Mac / Claude Code 앱  
> <sub>출처: first line</sub>

### portable/oz/install.py

`Python` · 445 줄 · code · entry · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py)

> Oz's offline Mac installer and launch/repair/diagnostic actions.  
> <sub>출처: module docstring</sub>

**심볼**

- [read](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L30) · function
- [write](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L34) · function
- [digest](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L48) · function
- [verify](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L52) · function
- [extract_runtime](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L63) · function
- [merge_claude](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L78) · function
- [load_bridge](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L102) · function
- [choose_port](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L110) · function
- [configure](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L132) · function
- [mcp_definitions](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L169) · function
- [upgrade_logging](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L179) · function — One bounded 0.1.0 -> 0.1.1 script-only update; never replace the ledger/runtimes.
- [install](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L247) · function
- [start](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L292) · function
- [check_mcp](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L318) · function
- [diagnose](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L342) · function
- [main](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py#L366) · function

**나가는 연결:** calls-op → [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); refers → [oz_graphify_mcp.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_graphify_mcp.py), [oz_mcp_proxy.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_mcp_proxy.py), [oz_support.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_support.py), [graphify-playbook.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py), [index.html](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify/index.html)

**들어오는 연결:** refers ← [oz-logging-smoke.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-logging-smoke.py), [oz-package-smoke.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-package-smoke.py), [package-oz-mac.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/package-oz-mac.py)

### portable/oz/oz_graphify_mcp.py

`Python` · 149 줄 · code · entry · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_graphify_mcp.py)

> Project-aware Graphify MCP.  
> <sub>출처: module docstring</sub>

**심볼**

- [schema](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_graphify_mcp.py#L39) · function
- [register_project](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_graphify_mcp.py#L57) · function
- [ensure_companion](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_graphify_mcp.py#L75) · function
- [call](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_graphify_mcp.py#L90) · function
- [list_tools](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_graphify_mcp.py#L130) · function
- [call_tool](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_graphify_mcp.py#L134) · function
- [main](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_graphify_mcp.py#L142) · function

**나가는 연결:** calls-op → [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); imports → [oz_support.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_support.py); refers → [graphify-playbook.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py)

**들어오는 연결:** refers ← [install.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py), [oz-package-smoke.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-package-smoke.py), [package-oz-mac.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/package-oz-mac.py)

### portable/oz/oz_mcp_proxy.py

`Python` · 141 줄 · code · entry · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_mcp_proxy.py)

> Transparent stdio MCP proxy.  
> <sub>출처: module docstring</sub>

**심볼**

- [run](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_mcp_proxy.py#L17) · function

**나가는 연결:** imports → [oz_support.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_support.py)

**들어오는 연결:** refers ← [install.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py), [oz-logging-smoke.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-logging-smoke.py), [oz-package-smoke.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-package-smoke.py), [package-oz-mac.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/package-oz-mac.py)

### portable/oz/oz_support.py

`Python` · 201 줄 · code · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_support.py)

> Bounded, content-free local audit journal and opt-in troubleshooting exports.  
> <sub>출처: module docstring</sub>

**심볼**

- [ref](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_support.py#L28) · function — Correlate IDs without recording paths, names, prompts or user supplied RPC IDs.
- [category](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_support.py#L33) · function
- [clean](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_support.py#L52) · function — Allowlist fields and values again on export; never trust text in local log files.
- [locked](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_support.py#L77) · function
- [emit](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_support.py#L111) · function
- [snapshot](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_support.py#L135) · function
- [summarize](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_support.py#L153) · function
- [status](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_support.py#L168) · function
- [create_bundle](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_support.py#L172) · function

**들어오는 연결:** imports ← [oz_graphify_mcp.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_graphify_mcp.py), [oz_mcp_proxy.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_mcp_proxy.py); refers ← [install.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py), [graphify-playbook.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py), [oz-logging-smoke.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-logging-smoke.py), [oz-package-smoke.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-package-smoke.py), [package-oz-mac.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/package-oz-mac.py)

### portable/oz/templates/봇_정리양식.md

`Markdown` · 20 줄 · docs · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/templates/봇_정리양식.md)

> 비밀번호·토큰·인증 코드는 이 문서에 적지 않습니다.  
> <sub>출처: first paragraph</sub>

**심볼**

- [{{BOT_NAME}} 봇](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/templates/봇_정리양식.md#L1) · h1

### portable/oz/templates/사람과_봇_업무흐름.md

`Markdown` · 18 줄 · docs · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/templates/사람과_봇_업무흐름.md)

> 시작 조건: {{TRIGGER}} 끝났다는 기준: {{COMPLETIONCRITERIA}} 전체 담당자: {{WORKFLOWOWNER}}  
> <sub>출처: first paragraph</sub>

**심볼**

- [{{WORKFLOW_NAME}}](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/templates/사람과_봇_업무흐름.md#L1) · h1

### portable/oz/오즈에게_전달.txt

`text` · 25 줄 · docs · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/오즈에게_전달.txt)

> 오즈야, 맥에서 쓰는 PlayBook + Graphify 설치본이야.  
> <sub>출처: first line</sub>

### portable/oz/클로드에_처음_붙여넣기.txt

`text` · 17 줄 · docs · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/클로드에_처음_붙여넣기.txt)

> 나는 오즈고 컴퓨터 설명을 어렵게 하면 잘 모른다.  
> <sub>출처: first line</sub>


## scripts

### scripts/central-smoke.py

`Python` · 184 줄 · test · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/central-smoke.py)

> Isolated recursive scanning, authentication, queue/lease and two real device-client processes.  
> <sub>출처: module docstring</sub>

**심볼**

- [check](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/central-smoke.py#L22) · function
- [port](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/central-smoke.py#L26) · function
- [call](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/central-smoke.py#L29) · function
- [request](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/central-smoke.py#L35) · function

**나가는 연결:** refers → [AGENTS.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AGENTS.md), [provider.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/fixtures/provider.py); runs → [PlayBook.csproj](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/PlayBook.csproj)

**들어오는 연결:** refers ← [prepare-public-source.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py)

### scripts/check-package.py

`Python` · 77 줄 · code · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/check-package.py)

> Install the Windows package into an isolated folder and exercise its own launcher.  
> <sub>출처: module docstring</sub>

**심볼**

- [check](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/check-package.py#L14) · function
- [powershell](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/check-package.py#L18) · function

**나가는 연결:** calls-op → [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); refers → [Install-PlayBook.ps1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/Install-PlayBook.ps1), [Start-PlayBook.ps1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/Start-PlayBook.ps1), [Stop-PlayBook.ps1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/Stop-PlayBook.ps1); runs → [PlayBook.csproj](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/PlayBook.csproj)

**들어오는 연결:** refers ← [prepare-public-source.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py)

### scripts/fixtures/harness-provider.py

`Python` · 34 줄 · code · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/fixtures/harness-provider.py)

> A deterministic provider process for harness wiring tests; never calls a model.  
> <sub>출처: module docstring</sub>

**들어오는 연결:** refers ← [harness-smoke.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py)

### scripts/fixtures/provider.py

`Python` · 28 줄 · code · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/fixtures/provider.py)

> Deterministic CLI fixture; not a real model/authentication test.  
> <sub>출처: module docstring</sub>

**들어오는 연결:** refers ← [central-smoke.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/central-smoke.py), [prepare-public-source.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py)

### scripts/folders-smoke.py

`Python` · 83 줄 · test · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/folders-smoke.py)

> Real, isolated filesystem + SQLite tests for folder organization.  
> <sub>출처: module docstring</sub>

**심볼**

- [check](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/folders-smoke.py#L11) · function

**나가는 연결:** calls-op → [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); runs → [PlayBook.csproj](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/PlayBook.csproj)

**들어오는 연결:** refers ← [prepare-public-source.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py)

### scripts/graphify-playbook.py

`Python` · 398 줄 · code · entry · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py)

> Local Graphify companion using PlayBook's existing tool and ontology APIs.  
> <sub>출처: module docstring</sub>

**심볼**

- [audit_event](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L40) · function
- [read_json](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L45) · function
- [write_json](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L49) · function
- [playbook](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L62) · function
- [project_dir](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L71) · function
- [project](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L77) · function
- [local_path](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L85) · function
- [project_lock](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L95) · function
- [make_feed](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L115) · function — Bounded overview; the complete graph stays available to Graphify queries.
- [analyze](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L173) · function
- [current](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L221) · function
- [sync](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L228) · function
- [query](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L243) · function
- [projects](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L253) · function
- [serve](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L268) · function
- [main](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py#L355) · function

**나가는 연결:** calls-op → [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); refers → [mcp.json](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/examples/mcp.json), [oz_support.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_support.py), [index.html](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify/index.html); runs → [PlayBook.csproj](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/PlayBook.csproj)

**들어오는 연결:** refers ← [graphify.ps1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/graphify.ps1), [install.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py), [oz_graphify_mcp.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_graphify_mcp.py), [graphify-smoke.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-smoke.py), [oz-package-smoke.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-package-smoke.py), [package-oz-mac.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/package-oz-mac.py); runs ← [graphify.ps1](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/graphify.ps1)

### scripts/graphify-smoke.py

`Python` · 157 줄 · test · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-smoke.py)

> Real Graphify/PlayBook integration checks, using an isolated ledger and source.  
> <sub>출처: module docstring</sub>

**심볼**

- [check](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-smoke.py#L22) · function
- [request](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-smoke.py#L28) · function
- [rejected](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-smoke.py#L39) · function
- [mcp_checks](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-smoke.py#L47) · function

**나가는 연결:** calls-op → [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); refers → [graphify-playbook.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py)

### scripts/graphify/index.html

`HTML` · 32 줄 · web · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify/index.html)

> Graphify · PlayBook  
> <sub>출처: <title></sub>

**심볼**

- [api](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify/index.html#L22) · function
- [show](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify/index.html#L23) · function
- [refresh](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify/index.html#L24) · function
- [poll](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify/index.html#L25) · function

**들어오는 연결:** refers ← [install.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py), [graphify-playbook.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py), [package-oz-mac.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/package-oz-mac.py)

### scripts/harness-smoke.py

`Python` · 216 줄 · test · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py)

> Harness proposal/trial/adoption tests on isolated SQLite and real worker/provider processes.  
> <sub>출처: module docstring</sub>

**심볼**

- [check](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py#L22) · function

**나가는 연결:** calls-op → [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); refers → [AGENTS.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AGENTS.md), [harness-provider.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/fixtures/harness-provider.py), [harness.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/harness.js); runs → [PlayBook.csproj](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/PlayBook.csproj)

### scripts/ontology-smoke.py

`Python` · 541 줄 · test · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py)

> Ontology integration checks using a temporary DB, local fixture and real transports.  
> <sub>출처: module docstring</sub>

**심볼**

- [check](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L32) · function
- [free_port](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L39) · function
- [tool_result](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L45) · function — The official SDK returns a JSON string inside MCP text content.
- [http_rpc_message](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/ontology-smoke.py#L55) · function

**나가는 연결:** calls-op → [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); runs → [PlayBook.csproj](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/PlayBook.csproj)

**들어오는 연결:** refers ← [prepare-public-source.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py)

### scripts/oz-logging-smoke.py

`Python` · 139 줄 · test · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-logging-smoke.py)

> Real-process failure/privacy/concurrency tests for Oz's content-free audit boundary.  
> <sub>출처: module docstring</sub>

**심볼**

- [check](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-logging-smoke.py#L19) · function
- [load](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-logging-smoke.py#L25) · function

**나가는 연결:** refers → [install.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py), [oz_mcp_proxy.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_mcp_proxy.py), [oz_support.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_support.py)

### scripts/oz-package-smoke.py

`Python` · 243 줄 · test · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-package-smoke.py)

> Audit real Mac payloads and exercise their installer/MCP logic on Windows.  
> <sub>출처: module docstring</sub>

**심볼**

- [check](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-package-smoke.py#L21) · function
- [import_file](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-package-smoke.py#L27) · function
- [arches](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-package-smoke.py#L34) · function
- [check_installed_mcp](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/oz-package-smoke.py#L68) · function

**나가는 연결:** calls-op → [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); refers → [install.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py), [oz_graphify_mcp.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_graphify_mcp.py), [oz_mcp_proxy.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_mcp_proxy.py), [oz_support.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_support.py), [graphify-playbook.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py); runs → [PlayBook.csproj](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/PlayBook.csproj)

### scripts/package-oz-mac.py

`Python` · 197 줄 · code · entry · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/package-oz-mac.py)

> Build offline Mac handoff ZIPs from explicit native runtime directories.  
> <sub>출처: module docstring</sub>

**심볼**

- [sha](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/package-oz-mac.py#L21) · function
- [command](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/package-oz-mac.py#L25) · function
- [stage](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/package-oz-mac.py#L68) · function
- [archive](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/package-oz-mac.py#L155) · function

**나가는 연결:** refers → [install.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/install.py), [oz_graphify_mcp.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_graphify_mcp.py), [oz_mcp_proxy.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_mcp_proxy.py), [oz_support.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/portable/oz/oz_support.py), [graphify-playbook.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify-playbook.py), [index.html](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/graphify/index.html)

### scripts/package.py

`Python` · 44 줄 · code · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/package.py)

> Package an explicit self-contained publish directory, without any live data.  
> <sub>출처: module docstring</sub>

**나가는 연결:** refers → [README.en.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.en.md), [README.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.md), [API.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/API.md), [ONTOLOGY.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/ONTOLOGY.md), [PORTABLE-AND-AGENTS.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/PORTABLE-AND-AGENTS.md), [RELEASE-0.2.0.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/docs/RELEASE-0.2.0.md)

**들어오는 연결:** refers ← [prepare-public-source.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py)

### scripts/prepare-public-source.py

`Python` · 27 줄 · code · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py)

> Copy an explicit public source snapshot; never copy the private local Git history.  
> <sub>출처: module docstring</sub>

**나가는 연결:** refers → [AGENTS.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AGENTS.md), [PlayBook.csproj](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/PlayBook.csproj), [launchSettings.json](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Properties/launchSettings.json), [README.en.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.en.md), [README.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.md), [START_PLAYBOOK.cmd](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/START_PLAYBOOK.cmd) … 외 20개

### scripts/real-provider-smoke.py

`Python` · 82 줄 · test · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/real-provider-smoke.py)

> Explicit, small read-only smoke against installed, already signed-in Codex and Claude.  
> <sub>출처: module docstring</sub>

**심볼**

- [cli](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/real-provider-smoke.py#L21) · function
- [request](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/real-provider-smoke.py#L35) · function

**나가는 연결:** calls-op → [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); refers → [README.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/README.md); runs → [PlayBook.csproj](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/PlayBook.csproj)

**들어오는 연결:** refers ← [prepare-public-source.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py)

### scripts/smoke.py

`Python` · 173 줄 · test · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/smoke.py)

> End-to-end tests against a fresh SQLite database, real CLI, HTTP and MCP transports.  
> <sub>출처: module docstring</sub>

**심볼**

- [check](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/smoke.py#L22) · function
- [port](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/smoke.py#L28) · function

**나가는 연결:** calls-op → [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); runs → [PlayBook.csproj](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/PlayBook.csproj)

**들어오는 연결:** refers ← [prepare-public-source.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/prepare-public-source.py)


## wwwroot

### wwwroot/app.js

`JavaScript` · 91 줄 · code · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js)

**심볼**

- [api](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L18) · function
- [toast](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L19) · function
- [action](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L20) · function
- [badge](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L21) · function
- [date](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L22) · function
- [view](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L23) · function
- [section](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L24) · function
- [heading](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L25) · function
- [stats](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L26) · function
- [sidebar](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L27) · function
- [refresh](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L53) · function
- [select](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L54) · function
- [render](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L55) · function
- [dashboard](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L70) · function
- [recordList](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L77) · function
- [timeline](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js#L78) · function
- … 외 7개

**나가는 연결:** calls-op → [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); imports → [assets.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/assets.js), [context-menu.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/context-menu.js), [flowchart.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/flowchart.js), [folders.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/folders.js), [harness.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/harness.js), [i18n.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/i18n.js) … 외 4개; refers → [assets.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/assets.js), [context-menu.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/context-menu.js), [flowchart.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/flowchart.js), [folders.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/folders.js), [harness.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/harness.js), [i18n.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/i18n.js) … 외 4개

**들어오는 연결:** loads ← [index.html](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/index.html)

### wwwroot/assets.js

`JavaScript` · 118 줄 · code · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/assets.js)

**심볼**

- [renderAssets](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/assets.js#L5) · export
- [filePreview](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/assets.js#L97) · function
- [categoryLabel](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/assets.js#L105) · function
- [extension](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/assets.js#L106) · function
- [categoryFromPath](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/assets.js#L107) · function
- [joinPath](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/assets.js#L108) · function
- [formatSize](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/assets.js#L109) · function
- [sameProjectPath](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/assets.js#L110) · function
- [assetRecords](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/assets.js#L111) · function
- [action](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/assets.js#L118) · function

**나가는 연결:** calls-op → [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); imports → [context-menu.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/context-menu.js), [i18n.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/i18n.js), [media.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/media.js); refers → [context-menu.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/context-menu.js), [i18n.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/i18n.js), [media.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/media.js)

**들어오는 연결:** imports ← [app.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js); refers ← [app.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js)

### wwwroot/context-menu.js

`JavaScript` · 39 줄 · code · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/context-menu.js)

**심볼**

- [showContextMenu](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/context-menu.js#L4) · export
- [contextMenuKey](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/context-menu.js#L37) · export

**나가는 연결:** imports → [i18n.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/i18n.js); refers → [i18n.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/i18n.js)

**들어오는 연결:** imports ← [app.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js), [assets.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/assets.js), [folders.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/folders.js); refers ← [app.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js), [assets.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/assets.js), [folders.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/folders.js)

### wwwroot/flowchart.js

`JavaScript` · 50 줄 · code · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/flowchart.js)

**심볼**

- [renderFlowchart](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/flowchart.js#L30) · export — Shows body.flowchart (Mermaid source) of a project.
- [loadMermaid](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/flowchart.js#L10) · function
- [node](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/flowchart.js#L4) · function — Mermaid is vendored under /vendor/mermaid (pinned version) and loaded on first use.

**나가는 연결:** imports → [i18n.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/i18n.js); refers → [i18n.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/i18n.js), [mermaid.min.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/vendor/mermaid/mermaid.min.js)

**들어오는 연결:** imports ← [app.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js); refers ← [app.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js)

### wwwroot/folders.js

`JavaScript` · 103 줄 · code · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/folders.js)

**심볼**

- [renderFolders](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/folders.js#L5) · export

**나가는 연결:** calls-op → [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); imports → [context-menu.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/context-menu.js), [i18n.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/i18n.js), [media.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/media.js); refers → [context-menu.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/context-menu.js), [i18n.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/i18n.js), [media.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/media.js)

**들어오는 연결:** imports ← [app.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js); refers ← [app.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js)

### wwwroot/harness.js

`JavaScript` · 71 줄 · code · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/harness.js)

**심볼**

- [renderHarnesses](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/harness.js#L36) · export
- [field](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/harness.js#L26) · function
- [select](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/harness.js#L32) · function
- [node](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/harness.js#L25) · function

**나가는 연결:** calls-op → [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); imports → [i18n.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/i18n.js); refers → [i18n.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/i18n.js)

**들어오는 연결:** imports ← [app.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js); refers ← [harness-smoke.py](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/scripts/harness-smoke.py), [app.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js)

### wwwroot/i18n.js

`JavaScript` · 259 줄 · code · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/i18n.js)

**심볼**

- [t](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/i18n.js#L239) · export
- [setLanguage](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/i18n.js#L244) · export
- [translatePage](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/i18n.js#L253) · export
- [getLanguage](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/i18n.js#L236) · export
- [locale](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/i18n.js#L237) · export
- [registerTranslations](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/i18n.js#L238) · export

**들어오는 연결:** imports ← [app.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js), [assets.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/assets.js), [context-menu.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/context-menu.js), [flowchart.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/flowchart.js), [folders.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/folders.js), [harness.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/harness.js) … 외 4개; refers ← [app.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js), [assets.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/assets.js), [context-menu.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/context-menu.js), [flowchart.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/flowchart.js), [folders.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/folders.js), [harness.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/harness.js) … 외 4개

### wwwroot/index.html

`HTML` · 9 줄 · web · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/index.html)

> Project PlayBook  
> <sub>출처: <title></sub>

**나가는 연결:** loads → [app.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js), [style.css](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/style.css)

### wwwroot/inventory.js

`JavaScript` · 45 줄 · code · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/inventory.js)

**심볼**

- [renderReview](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/inventory.js#L4) · export
- [renderCatalog](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/inventory.js#L18) · export
- [node](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/inventory.js#L2) · function

**나가는 연결:** imports → [i18n.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/i18n.js); refers → [i18n.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/i18n.js)

**들어오는 연결:** imports ← [app.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js); refers ← [app.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js)

### wwwroot/media.js

`JavaScript` · 112 줄 · code · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/media.js)

**심볼**

- [showProjectImage](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/media.js#L2) · export
- [imageThumbnail](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/media.js#L9) · export
- [mediaPlayer](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/media.js#L30) · export
- [pdfPreview](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/media.js#L45) · export
- [showTextFile](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/media.js#L67) · export
- [clearImageThumbnails](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/media.js#L78) · export
- [setMediaSessionKey](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/media.js#L111) · export
- [fetchProjectImage](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/media.js#L83) · function
- [showImageDialog](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/media.js#L97) · function

**나가는 연결:** calls-op → [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); imports → [i18n.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/i18n.js); refers → [i18n.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/i18n.js)

**들어오는 연결:** imports ← [app.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js), [assets.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/assets.js), [folders.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/folders.js), [workspace-ui.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js); refers ← [app.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js), [assets.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/assets.js), [folders.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/folders.js), [workspace-ui.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js)

### wwwroot/ontology.js

`JavaScript` · 246 줄 · code · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js)

**심볼**

- [renderOntology](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js#L88) · export
- [inputField](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js#L62) · function
- [selectField](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js#L69) · function
- [message](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js#L74) · function
- [showMessage](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js#L75) · function
- [button](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js#L76) · function
- [when](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js#L81) · function
- [uriNode](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js#L82) · function
- [node](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js#L57) · function
- [textOf](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js#L60) · function
- [asList](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/ontology.js#L61) · function

**나가는 연결:** calls-op → [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); imports → [i18n.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/i18n.js); refers → [i18n.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/i18n.js)

**들어오는 연결:** imports ← [app.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js); refers ← [app.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js)

### wwwroot/style.css

`CSS` · 47 줄 · web · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/style.css)

**들어오는 연결:** loads ← [index.html](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/index.html)

### wwwroot/vendor/mermaid/README.md

`Markdown` · 8 줄 · docs · vendored · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/vendor/mermaid/README.md)

> - Package: mermaid 11.17.2 (published 2026-08-25), MIT license.  
> <sub>출처: first paragraph</sub>

**심볼**

- [Mermaid (vendored)](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/vendor/mermaid/README.md#L1) · h1

### wwwroot/workspace-ui.js

`JavaScript` · 149 줄 · code · [source](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js)

**심볼**

- [renderSetup](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L46) · export
- [renderAgents](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L79) · export
- [renderLibrary](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L120) · export
- [loginSession](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L142) · export
- [button](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L33) · function
- [field](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L37) · function
- [choice](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L40) · function
- [heading](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L44) · function
- [node](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/workspace-ui.js#L32) · function

**나가는 연결:** calls-op → [Operations.cs](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/Operations.cs); imports → [i18n.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/i18n.js), [media.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/media.js); refers → [AGENTS.md](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/AGENTS.md), [i18n.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/i18n.js), [media.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/media.js)

**들어오는 연결:** imports ← [app.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js); refers ← [app.js](https://github.com/unkkyuist/PlayBookOS/blob/7153e47ec28a0b1933c24404db08a43a468b6c14/wwwroot/app.js)

