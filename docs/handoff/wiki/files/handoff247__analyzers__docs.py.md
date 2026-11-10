---
generator: HandOff247
id: "file:handoff247/analyzers/docs.py"
type: File
source: "handoff247/analyzers/docs.py"
---

# `handoff247/analyzers/docs.py`

> Markdown (summary, headings, relative links, code blocks for `<mode> <op>` usage), plus config formats: .csproj, package.json, pyproject, requirements, MCP client configs (`mcpServers` / `[mcp_servers]`), Dockerfile, Gi…

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 211
- **Source:** [handoff247/analyzers/docs.py](../../../../handoff247/analyzers/docs.py)

**Notes from the previous owner**

> Markdown (summary, headings, relative links, code blocks for `<mode> <op>` usage), plus config formats: .csproj, package.json, pyproject, requirements, MCP client configs (`mcpServers` / `[mcp_servers]`), Dockerfile, GitHub workflows.

**imports** →

- [`handoff247/lexer.py`](handoff247__lexer.py.md) · [handoff247/analyzers/docs.py:8](../../../../handoff247/analyzers/docs.py#L8)
- [`handoff247/model.py`](handoff247__model.py.md) · [handoff247/analyzers/docs.py:9](../../../../handoff247/analyzers/docs.py#L9)

**is part of** ←

- [`handoff247`](../areas/handoff247.md)

**is imported by** ←

- [`handoff247/analyzers/__init__.py`](handoff247__analyzers____init__.py.md) · [handoff247/analyzers/__init__.py:5](../../../../handoff247/analyzers/__init__.py#L5)

**handles** ←

- [`dockerfile`](../operations/dockerfile.md) (docs.analyze_dockerfile) · [handoff247/analyzers/__init__.py:23](../../../../handoff247/analyzers/__init__.py#L23)
- [`json`](../operations/json.md) (docs.analyze_json) · [handoff247/analyzers/__init__.py:19](../../../../handoff247/analyzers/__init__.py#L19)
- [`markdown`](../operations/markdown.md) (docs.analyze_markdown) · [handoff247/analyzers/__init__.py:17](../../../../handoff247/analyzers/__init__.py#L17)
- [`msbuild`](../operations/msbuild.md) (docs.analyze_msbuild) · [handoff247/analyzers/__init__.py:22](../../../../handoff247/analyzers/__init__.py#L22)
- [`requirements`](../operations/requirements.md) (docs.analyze_requirements) · [handoff247/analyzers/__init__.py:21](../../../../handoff247/analyzers/__init__.py#L21)
- [`text`](../operations/text.md) (docs.analyze_text) · [handoff247/analyzers/__init__.py:18](../../../../handoff247/analyzers/__init__.py#L18)
- [`toml`](../operations/toml.md) (docs.analyze_toml) · [handoff247/analyzers/__init__.py:20](../../../../handoff247/analyzers/__init__.py#L20)
- [`yaml`](../operations/yaml.md) (docs.analyze_yaml) · [handoff247/analyzers/__init__.py:24](../../../../handoff247/analyzers/__init__.py#L24)

## Comment in the file

Markdown/text documents and configuration files (MSBuild, package.json, pyproject, requirements, MCP client configs, Dockerfile, GitHub workflows). *(module docstring)*

## Defined here

- `analyze_markdown` — function, [line 17](../../../../handoff247/analyzers/docs.py#L17)
- `analyze_text` — function, [line 69](../../../../handoff247/analyzers/docs.py#L69)
- `analyze_json` — function, [line 94](../../../../handoff247/analyzers/docs.py#L94)
- `analyze_toml` — function, [line 131](../../../../handoff247/analyzers/docs.py#L131)
- `analyze_requirements` — function, [line 155](../../../../handoff247/analyzers/docs.py#L155)
- `analyze_msbuild` — function, [line 164](../../../../handoff247/analyzers/docs.py#L164)
- `analyze_dockerfile` — function, [line 187](../../../../handoff247/analyzers/docs.py#L187)
- `analyze_yaml` — function, [line 202](../../../../handoff247/analyzers/docs.py#L202)
