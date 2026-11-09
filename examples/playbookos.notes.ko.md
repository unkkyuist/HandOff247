# HandOff247 notes · PlayBookOS

<!--
PlayBookOS 예시 묶음용 노트입니다. HandOff247을 만들면서 PlayBookOS의 README.md·README.en.md·AGENTS.md
(커밋 7153e47)에 적힌 내용만 옮겨 적었습니다. 생성된 사실 옆에 노트가 어떻게 붙는지 보여 주려는 예시이며,
실제 인수인계에서는 넘겨주는 사람이 직접 씁니다.
-->

## Project
PlayBook OS는 프로젝트·레퍼런스·AI 작업을 함께 기록하는 공통 원장입니다. 웹 화면, JSON CLI, MCP(stdio/HTTP)가 모두 같은 operation과 같은 SQLite DB를 씁니다 (README.md).
사용자별 권한이나 테넌트 분리가 없는, 소유자가 신뢰하는 작업 공간용 서비스입니다 (README.en.md "Verification and scope").

## Topic: 후임자 체크리스트
1. .NET 10 SDK를 설치하고 `dotnet build -c Release` 뒤 `.\playbook.ps1 serve`로 띄운 다음 http://127.0.0.1:7331 을 엽니다.
2. GUI·CLI·MCP 모두 같은 `PLAYBOOK_HOME`을 가리켜야 합니다. 다르면 각자 다른 DB를 봅니다.
3. 비즈니스 로직을 바꾸면 `python scripts/smoke.py`를 돌립니다 (릴리스 전에는 folders·ontology·central 스모크도).
4. 이 프로젝트의 작업은 PlayBook 안의 프로젝트 ID `playbook`으로 기록합니다 (AGENTS.md).

## Topic: 알려진 문제와 위험
- 모든 변경은 `expectedRevision`을 보내야 합니다. 충돌하면 무작정 다시 보내지 말고 최신 기록을 읽어 합칩니다 (README.md).
- macOS 실행은 검증되지 않았습니다. 크로스 빌드만으로는 근거가 되지 않습니다 (AGENTS.md).
- v0.2.0에서 Claude 실제 모델 실행은 검증되지 않았습니다. docs/RELEASE-0.2.0.md를 보세요.

## Topic: 인증 정보와 계정
HTTP·MCP 키는 `PLAYBOOK_HOME/api-key`에 있습니다 (`serve`를 처음 실행할 때 만들어짐). `data/`, 도구 인증 정보, 로그, API 키는 커밋하지 않습니다 (AGENTS.md).

## Mode: serve
평소에 쓰는 모드입니다. 웹 화면, `/api/{operation}`, `/mcp`의 HTTP MCP, 로컬 AI 워커가 함께 뜹니다.

## Mode: server
여러 PC가 함께 쓰는 중앙 서버입니다. 별도의 `PLAYBOOK_HOME`이 필요하고, 먼저 `cli server.setup`으로 계정을 만들어야 합니다.

## Mode: cli
프로세스 하나에 operation 하나: `PlayBook.dll cli <operation> <JSON | @파일 | ->`. 오류는 stderr에 JSON으로 나오고 종료 코드는 1입니다.

## File: Operations.cs
새 기능이 붙는 단 한 곳입니다. AGENTS.md: CLI·GUI·MCP 기능은 이 공용 Operations 서비스를 쓰고, 두 번째 데이터 권한을 만들지 않습니다.

## File: Store.cs
모든 기록 변경은 여기서 검증을 통과하고 같은 트랜잭션 안에서 감사 이벤트를 남겨야 합니다 (AGENTS.md).
