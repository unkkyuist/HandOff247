---
generator: HandOff247
id: "file:handoff247/analyzers/web.py"
type: File
source: "handoff247/analyzers/web.py"
---

# `handoff247/analyzers/web.py`

> JavaScript/TypeScript (imports, exported functions with spans, `fetch` calls, Express routes, MCP registrations, `case` tables), HTML (`<script src>`, `<link>`, inline scripts) and CSS imports.

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 138
- **Source:** [handoff247/analyzers/web.py](../../../../handoff247/analyzers/web.py)

**Notes from the previous owner**

> JavaScript/TypeScript (imports, exported functions with spans, `fetch` calls, Express routes, MCP registrations, `case` tables), HTML (`<script src>`, `<link>`, inline scripts) and CSS imports.

**imports** →

- [`handoff247/lexer.py`](handoff247__lexer.py.md) · [handoff247/analyzers/web.py:6](../../../../handoff247/analyzers/web.py#L6)
- [`handoff247/model.py`](handoff247__model.py.md) · [handoff247/analyzers/web.py:7](../../../../handoff247/analyzers/web.py#L7)

**is part of** ←

- [`handoff247`](../areas/handoff247.md)

**is imported by** ←

- [`handoff247/analyzers/__init__.py`](handoff247__analyzers____init__.py.md) · [handoff247/analyzers/__init__.py:5](../../../../handoff247/analyzers/__init__.py#L5)

**handles** ←

- [`css`](../operations/css.md) (web.analyze_css) · [handoff247/analyzers/__init__.py:13](../../../../handoff247/analyzers/__init__.py#L13)
- [`html`](../operations/html.md) (web.analyze_html) · [handoff247/analyzers/__init__.py:12](../../../../handoff247/analyzers/__init__.py#L12)
- [`javascript`](../operations/javascript.md) (web.analyze_js) · [handoff247/analyzers/__init__.py:10](../../../../handoff247/analyzers/__init__.py#L10)
- [`typescript`](../operations/typescript.md) (web.analyze_js) · [handoff247/analyzers/__init__.py:11](../../../../handoff247/analyzers/__init__.py#L11)

## Comment in the file

JavaScript/TypeScript, HTML and CSS analyzers. *(module docstring)*

## Defined here

- `analyze_js_text` — function, [line 39](../../../../handoff247/analyzers/web.py#L39)
- `analyze_js` — function, [line 113](../../../../handoff247/analyzers/web.py#L113)
- `analyze_html` — function, [line 117](../../../../handoff247/analyzers/web.py#L117)
- `analyze_css` — function, [line 133](../../../../handoff247/analyzers/web.py#L133)
