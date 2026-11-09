# HandOff247

**Hand Off 24-7은 지금 하던 프로젝트를 다음 사람에게 넘기기 위한 작별 프로젝트입니다.**
프로젝트 폴더를 지정하면 *인수인계 묶음*을 만듭니다. 다이어그램, 구조, 코드에 이미 있는 주석,
그리고 프로젝트 안의 도구들이 서로 어떻게 연결되는지가 들어 있습니다.
후임자는 페이지 하나만 열어도 프로그램이 어떻게 시작되는지, 실행 모드가 무엇인지, 누가 무엇을 호출하는지,
어디부터 읽으면 되는지 알 수 있습니다.

[English →](README.md)

- **추측하지 않습니다.** 묶음의 모든 내용은 파일에서 찾은 것이고 정확한 줄로 연결됩니다. 추론일 뿐인 연결은
  "추론"이라고 표시하고 점선으로 그립니다. 애매한 것은 아예 넣지 않습니다.
- **아무것도 실행하지 않습니다.** 파일을 읽기만 하고, 대상 프로젝트를 import·빌드·실행하지 않습니다.
- **설치할 것이 없습니다.** Python 3.10 이상 표준 라이브러리만 씁니다.
- **코드가 말하지 못하는 것은 사람이 적습니다.** 평범한 Markdown 노트 파일에 프로젝트 목적, 후임자가 먼저 할 일,
  알려진 위험, 인증 정보 보관 위치(값은 쓰지 않음)를 적습니다. 노트는 모든 페이지에 합쳐지고, 다시 생성해도 사라지지 않습니다.

## 예시

| 예시 | 내용 |
|---|---|
| [examples/playbookos-ko](examples/playbookos-ko/README.md) | [PlayBookOS](https://github.com/unkkyuist/PlayBookOS) 인수인계 묶음 (C# + JS + Python + PowerShell), 한국어 |
| [examples/playbookos](examples/playbookos/README.md) | 같은 묶음, 영어 |
| [docs/handoff](docs/handoff/README.md) | HandOff247이 자기 자신을 설명한 묶음 |

GitHub에서는 다이어그램이 바로 그려집니다. 대화형으로 보려면 묶음 폴더를 내려받아 `index.html`을 여세요
(다이어그램의 상자를 누르면 그 파일 카드가 열립니다. Mermaid는 jsDelivr에서 불러옵니다).

PlayBookOS에 대해 아무 설명 없이 찾아낸 것:

- `Program.cs`의 실행 모드 6개 (`serve` 기본, `server`, `cli`, `mcp`, `agent`, `worker`)
- 분기표 `Operations.Execute` 하나와 operation 65개, 그리고 각 operation을 처리하는 파일
- HTTP 라우트 6개, 그중 `POST /api/{operation}`이 그 분기표로 넘긴다는 것
- MCP 도구 46개와 각각이 부르는 operation
- 분기표를 부르는 쪽: `wwwroot/app.js`는 `api()` → `fetch('/api/…')`로 (`api`를 인자로 받는 UI 파일 6개는 *추론*으로 표시),
  Python 스크립트 7개는 `dotnet PlayBook.dll cli <op>`로, MCP 도구는 프로세스 안에서 직접
- 실행 순서 `START_PLAYBOOK.cmd → playbook.ps1 (serve) → PlayBook.csproj`, `mcp` 모드를 띄우는 MCP 클라이언트 설정,
  환경변수(`PLAYBOOK_HOME`, `PLAYBOOK_PORT` 등)를 읽는 곳과 설정하는 곳, 포트, SQLite 파일 `playbook.db`

## 빠른 시작

```bash
git clone https://github.com/unkkyuist/HandOff247
cd HandOff247
python -m handoff247 notes /path/to/project --lang ko     # /path/to/project/HANDOFF.notes.md 생성
python -m handoff247 build /path/to/project -o /path/to/project/docs/handoff --lang ko
python -m handoff247 check /path/to/project                # 아직 설명이 없는 곳
```

명령으로 설치하려면 `pip install .` 후 `handoff247 build …`.

## 묶음에 들어 있는 것

| 파일 | 내용 |
|---|---|
| `README.md` | 시작 페이지: 한눈에 보기, **전체 구조도**, 추천 읽기 순서, 후임자 체크리스트, 위험, 아직 설명 없는 곳, 최근 커밋 |
| `RUNNING.md` | **실행 순서**(누가 누구를 띄우는지), 실행 모드, 실행 명령, 환경변수(읽는 곳·설정하는 곳), 포트, 실행 중 경로, 빌드 대상, 패키지, 테스트 |
| `CONNECTIONS.md` | **인터페이스 지도**: 호출하는 쪽 → HTTP / CLI 프로세스 / MCP / 프로세스 내부 → 분기표 → 처리 파일. 라우트·MCP 도구·MCP 클라이언트·operation 표 |
| `CODEMAP.md` | 폴더별 파일 의존 관계도, 공통 기반, 구성 요소 표(요약, 의존, 사용하는 곳) |
| `FILES.md` | 파일마다 카드 하나: 추출한 주석, 노트, 공개 심볼과 문서 주석, 들어오고 나가는 연결 |
| `diagrams/*.mmd` | 모든 다이어그램의 Mermaid 원문 (PlayBook 프로젝트의 `body.flowchart`에도 그대로 붙일 수 있음) |
| `handoff.json` | 위 내용 전체를 데이터로 — 스크립트와 AI 에이전트용 |
| `index.html` | 탭·검색·누를 수 있는 다이어그램이 있는 단일 파일 뷰어 |

## "도구가 어떻게 연결되는지"를 찾는 방법

대부분의 프로그램은 일을 몇 군데로 모읍니다. HandOff247은 그곳을 찾아 따라갑니다.

1. **진입점과 모드.** 진입 파일(`Program.cs` 최상위 문장, `static Main`, `if __name__ == "__main__"`, 패키지 bin)에서
   첫 인자를 문자열과 비교하는 곳(`if (mode == "cli")`)을 실행 모드로 봅니다. 모드마다 맡은 줄 범위, 쓰는 타입,
   여는 것(HTTP 서버, stdio/HTTP MCP, 백그라운드 서비스)을 기록합니다.
2. **분기표.** 문자열 키로 나누는 `switch`(C#, JS), 함수를 값으로 갖는 Python dict, 키 3개 이상의 `if/elif` 사슬이나 `match`.
   분기마다 처리 함수를 파일까지 찾아갑니다 (`store.List()` → `Store` → `Store.cs`).
3. **호출하는 쪽.** 그 키를 넘기는 모든 호출(`api('list')`, `cli('save', …)`, `Call("ontology.search")`,
   README 코드 블록의 `playbook.ps1 cli list`)을 감싼 함수까지 따라가서 경로를 구분합니다.
   `fetch`를 부르면 HTTP(서버 라우트와 맞춤), 모드 인자로 프로세스를 띄우면 CLI, 분기표를 바로 부르면 프로세스 내부입니다.
   감싼 함수가 인자로 전달된 경우는 *추론*으로 보고합니다.
4. **인터페이스.** ASP.NET 미니멀 API 라우트와 `[Http*]` 속성, Flask/FastAPI/Express 라우트, `[McpServerTool]` 메서드,
   Python/TypeScript MCP 도구 등록, MCP 클라이언트 설정(`mcpServers` JSON, Codex `[mcp_servers]` TOML).
5. **실행 순서.** `.cmd`/`.ps1`/`.sh`의 명령 줄, `subprocess`/`Process.Start` 호출, `package.json` 스크립트, Dockerfile, CI 단계를
   실제로 띄우는 프로젝트 파일과 빌드 결과물(`PlayBook.dll` → `PlayBook.csproj`)로 연결합니다.
6. **코드 지도.** C# 타입 참조와 생성자 주입, Python·JS import, HTML `<script src>`, Markdown 링크.

## 노트 파일

`handoff247 notes <프로젝트>`가 항목마다 제목이 하나씩 있는 `HANDOFF.notes.md`를 만듭니다.

```markdown
## Project
하는 일, 쓰는 사람, 지금 상태.

## Topic: 후임자 체크리스트
## Topic: 알려진 문제와 위험
## Topic: 인증 정보와 계정            ← 보관 위치만, 값은 절대 쓰지 않기
## Mode: serve
## Area: scripts
## File: Program.cs
## Op: ontology.search              ← 선택, operation 표에 표시됨
```

아무 제목 아래에나 쓰면 됩니다. 아직 `TODO`로 시작하는 줄은 설명이 없는 것으로 셉니다.
`notes`를 다시 실행하면 새 파일·모드·폴더의 제목만 **추가**하고 기존 글은 바꾸지 않습니다.
없어진 파일의 제목은 지우지 않고 목록으로 알려 줍니다.

## 늘 최신으로 (24/7)

이 저장소를 GitHub Action으로 쓰면 push할 때마다 묶음을 다시 만듭니다. 설정 예시는 [영어 README](README.md#keep-it-current-the-247-part)에 있습니다.
Action은 마지막 커밋 날짜를 찍기 때문에 프로젝트가 바뀌지 않으면 묶음도 똑같이 나오고 커밋도 생기지 않습니다.
`min-notes`를 올리면 설명이 부족할 때 빌드를 실패시킬 수 있습니다.

## 명령

```text
handoff247 build  [PROJECT] [-o OUT] [--lang en|ko] [--notes FILE] [--name NAME]
                  [--links auto|relative|url|plain] [--link-base URL] [--date YYYY-MM-DD] [--exclude GLOB]
handoff247 notes  [PROJECT] [--lang en|ko] [--notes FILE]
handoff247 check  [PROJECT] [--notes FILE] [--min PERCENT]
```

- `--links auto`: 묶음이 프로젝트 안에 있으면 상대 경로로, 밖에 있고 GitHub 저장소면 정확한 커밋의 GitHub 주소로, 그 밖에는 글자로만 연결합니다.
- 프로젝트 루트의 `.handoffignore`(또는 `--exclude`)로 경로를 뺍니다: `tests/fixtures/`, `*.min.js` 등.
  Git이 무시하는 파일과 이전 묶음이 든 폴더는 자동으로 건너뜁니다.
- 기본 출력 폴더는 `./handoff/<프로젝트 이름>`입니다.

## 한계

- Python은 `ast`로, 나머지 언어는 주석·문자열을 구분하는 렉서와 패턴으로 분석합니다. 실행 중에 이름을 만드는 코드
  (리플렉션, DI 컨테이너, 문자열 이어 붙이기)는 따라가지 않습니다.
- 분석기가 없는 언어(Go, Rust, Java 등)는 줄 수와 함께 목록에만 나옵니다.
- C# SDK의 MCP 도구 이름은 메서드 이름에서 만든 것이라 `*`로 표시합니다. 실제 이름은 클라이언트의 `tools/list`로 확인하세요.
- 다이어그램은 읽기 쉽게 크기를 제한합니다 (큰 폴더는 상자 하나로 접고, 공통 기반은 들어오는 화살표를 생략).

## 개발

```bash
python -m unittest discover -s tests
python -m handoff247 build . -o docs/handoff        # HandOff247 자신의 묶음
```

`tests/fixtures/mini`는 PlayBookOS처럼 연결된 작은 가짜 앱입니다. 이 도구가 찾는다고 주장하는 연결 종류마다
`tests/test_handoff.py`에 검증이 있습니다. 코드 구성은 [docs/handoff](docs/handoff/README.md)를 보세요.
