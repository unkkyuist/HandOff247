# HandOff247 notes · PlayBookOS

<!--
Example notes for the PlayBookOS demo pack. They were written while building HandOff247 and only
restate what PlayBookOS's own README.en.md and AGENTS.md (commit 7153e47) say, so the demo shows
how notes appear next to the generated facts. In a real handoff the outgoing owner writes these.
-->

## Project
PlayBook OS is a shared ledger for projects, references and AI work. The web UI, the JSON CLI and MCP (stdio and HTTP) all go through the same operations and the same SQLite records (README.en.md).
It is a trusted-owner workspace service: there are no per-user roles or tenant isolation (README.en.md, "Verification and scope").

## Topic: Successor checklist
1. Install the .NET 10 SDK, run `dotnet build -c Release`, then `dotnet bin/Release/net10.0/PlayBook.dll serve` and open http://127.0.0.1:7331.
2. Point every client (GUI, CLI, MCP) at the same `PLAYBOOK_HOME`, or they will each see a different database.
3. After any business-logic change run `python scripts/smoke.py` (plus folders/ontology/central smokes before a release).
4. Track work for this project in PlayBook itself under project ID `playbook` (AGENTS.md).

## Topic: Known issues and risks
- Every write must send `expectedRevision`; on conflict reread and merge instead of retrying blindly (README.en.md).
- macOS runtime is unverified; cross-publishing does not count as evidence (AGENTS.md).
- Real Claude model execution was not verified in v0.2.0; see docs/RELEASE-0.2.0.md.

## Topic: Credentials and accounts
The HTTP/MCP key lives in `PLAYBOOK_HOME/api-key` (created on first `serve`). Never commit `data/`, tool credentials, logs or API keys (AGENTS.md).

## Mode: serve
What people normally run: web UI, `/api/{operation}`, HTTP MCP at `/mcp`, and the local AI worker.

## Mode: server
Central multi-PC server. Needs its own `PLAYBOOK_HOME` and an account created with `cli server.setup` first.

## Mode: cli
One operation per process: `PlayBook.dll cli <operation> <json | @file | ->`. Errors go to stderr as JSON with exit code 1.

## File: Operations.cs
The single place new features plug into. AGENTS.md: use this shared Operations service for CLI/GUI/MCP features and do not add a second data authority.

## File: Store.cs
All record changes must pass validation here and write an audit event in the same transaction (AGENTS.md).

## Translations
<!-- PlayBookOS writes most comments and doc headings in Korean. These English versions were written while building HandOff247 (`handoff247 notes` listed the originals); file names stay as they are because they are identifiers. -->
| Original | English |
|---|---|
| 프로젝트와 AI 작업을 관리하는 공통 원장. | A shared ledger for managing projects and AI work. |
| 시작 | Getting started |
| 사용 순서 | Usage steps |
| Headless 예시 | Headless examples |
| MCP 연결 | MCP connection |
| 도구/서버 | Tools / servers |
| 데이터와 이식 | Data and portability |
| 현재 구현 범위 | What is implemented now |
| 개발 온톨로지 | Development ontology |
| 검증/설계 | Verification / design |
| 바탕화면 바로가기용: 서버가 꺼져 있으면 켜고, 화면을 엽니다. | For the desktop shortcut: starts the server if it is not running, then opens the UI. |
| 모든 진입점이 Operations.Execute(operation, arguments)를 공유한다. | Every entry point shares Operations.Execute(operation, arguments). |
| PlayBook API / 데이터 계약 | PlayBook API / data contract |
| 오류 | Errors |
| 작업 지침 개선 API | Work-instruction improvement API |
| PlayBook 서버가 프로젝트 지침, 목적, 파일 목록, 작업과 검증 기록의 공통 원장을 관리하고, 로그인한 각 컴퓨터의 클라이언트가 로컬 AI와 도구를 실행한다. | The PlayBook server keeps the shared ledger of project instructions, goals, file lists, tasks and verification records; a client on each signed-in computer runs the local AI and tools. |
| PlayBook 중앙 서버와 기기 간 AI 오케스트레이션 설계안 | Design: PlayBook central server and AI orchestration across devices |
| 사용 흐름 | Usage flow |
| 현재 구현과 확장 지점 | Current implementation and extension points |
| 서버와 클라이언트의 책임 | Responsibilities of server and client |
| 로그인과 실시간 공유 | Sign-in and live sharing |
| 파일 목록과 기기별 작업 폴더 | File lists and per-device work folders |
| AI 하네스와 지침 반영 | AI harness and applying instructions |
| 다른 기기의 여러 AI 작업 조정 | Coordinating several AI tasks on other devices |
| 구현 순서와 확인할 결과 | Implementation order and results to check |
| 이번 설계의 확인 범위 | What this design has been checked against |
| DevWork 전체에서 같은 PlayBook을 사용하려면 사용자 범위 MCP에 등록한다: | To use the same PlayBook across all of DevWork, register it as a user-scope MCP server: |
| Claude 연결과 폴더 관리 | Connecting Claude and managing folders |
| 프로젝트 내부 폴더 정리 | Organizing folders inside a project |
| 오즈는 Mac의 Claude Code 앱을 사용한다는 사용자 정정을 반영했습니다. | Updated after the user's correction that Oz uses the Claude Code app on a Mac. |
| 오즈용 Mac 배포본 | Mac distribution for Oz |
| 전달 파일 | Files to hand over |
| 설치와 구성 | Installation and setup |
| Claude가 사용하는 도구 | Tools Claude uses |
| 빌드와 검증 | Build and verification |
| 공식 Graphify를 로컬 코드 분석 도구로 연결했습니다. | Connected the official Graphify as a local code-analysis tool. |
| Graphify와 PlayBook 함께 사용하기 | Using Graphify together with PlayBook |
| 화면 사용 | Using the UI |
| 연결 범위와 출처 | Scope of the connection and sources |
| 설치 위치와 현재 실행본 | Install location and the build currently running |
| 검증 | Verification |
| Harness²의 제안 → 시험 → 비교·조합 → 검토 후 채택 → 교훈 재사용 절차 중 현재 PlayBook에 맞는 부분을 .NET 엔진에 구현했다. | Implemented in the .NET engine the parts of Harness²'s propose → trial → compare and combine → adopt after review → reuse lessons procedure that fit PlayBook today. |
| 작업 지침 개선 | Improving work instructions |
| 화면에서 사용 | Using it from the UI |
| 실행 경계 | Execution boundaries |
| 공통 API | Shared API |
| 원장과 검증 | Ledger and verification |
| PlayBook에 기록된 대화, 연구 결과와 개발 상태를 출처가 있는 개발 지식으로 모으고 검색·참조합니다. | Gathers the conversations, research results and development status recorded in PlayBook into sourced development knowledge that can be searched and referenced. |
| 자동 갱신이 일어나는 범위 | Scope of automatic updates |
| 동작과 인터페이스 | Behavior and interfaces |
| 대화·연구 수집 | Collecting conversations and research |
| 검색·참조·사용 이력 | Search, references and usage history |
| 외부 온톨로지 연결 | Connecting external ontologies |
| 0.1.1은 Claude Code가 oz-playbook, oz-graphify 두 stdio 연결을 사용하도록 설치합니다. | Version 0.1.1 sets Claude Code up to use two stdio connections, oz-playbook and oz-graphify. |
| 오즈의 AI 대화 중심 운영과 로그 | Oz's conversation-first AI operation and logs |
| 자동 기록 | Automatic logging |
| 오즈와 담당자의 사용법 | How Oz and the person in charge use it |
| 기존 설치와 검증 | Existing installs and verification |
| DevWork의 프로젝트 기획, 실행, 변경, 검증, 인수인계를 한 원장에서 관리한다. | Manages DevWork's project planning, execution, changes, verification and handoff in one ledger. |
| Project PlayBook — 설계와 구현 계획 | Project PlayBook — design and implementation plan |
| 목적 | Purpose |
| 구현 단위와 검증 | Implementation units and verification |
| 데이터 모델 | Data model |
| 경계 | Boundaries |
| 후속 확장 | Later extensions |
| 개발 온톨로지 확장 (2026-10-07) | Development ontology extension (2026-10-07) |
| 작업 지침 개선 (2026-10-18) | Improving work instructions (2026-10-18) |
| 오즈용 PlayBook + Graphify — Mac / Claude Code 앱 | PlayBook + Graphify for Oz — Mac / Claude Code app |
| 비밀번호·토큰·인증 코드는 이 문서에 적지 않습니다. | Passwords, tokens and verification codes are never written in this document. |
| {{BOT_NAME}} 봇 | {{BOT_NAME}} bot |
| 시작 조건: {{TRIGGER}} 끝났다는 기준: {{COMPLETIONCRITERIA}} 전체 담당자: {{WORKFLOWOWNER}} | Start condition: {{TRIGGER}} Done when: {{COMPLETIONCRITERIA}} Owner of the whole flow: {{WORKFLOWOWNER}} |
| 오즈야, 맥에서 쓰는 PlayBook + Graphify 설치본이야. | Oz, this is the PlayBook + Graphify install for your Mac. |
| 나는 오즈고 컴퓨터 설명을 어렵게 하면 잘 모른다. | I'm Oz; I don't follow computer explanations when they get complicated. |
