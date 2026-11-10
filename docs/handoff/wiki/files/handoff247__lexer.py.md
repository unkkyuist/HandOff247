---
generator: HandOff247
id: "file:handoff247/lexer.py"
type: File
source: "handoff247/lexer.py"
---

# `handoff247/lexer.py`

> Produces two views of C-like source with identical offsets: strings+comments blanked (for identifiers) and comments blanked (for literal patterns). Handles C# verbatim, interpolated and raw strings and JS template and r…

- **Class:** File — A file of the project (images and other assets are left out).
- **Language:** Python
- **Kind of file:** code
- **Lines:** 311
- **Source:** [handoff247/lexer.py](../../../../handoff247/lexer.py)

**Notes from the previous owner**

> Produces two views of C-like source with identical offsets: strings+comments blanked (for identifiers) and comments blanked (for literal patterns). Handles C# verbatim, interpolated and raw strings and JS template and regex literals. If a regex in an analyzer misbehaves, check the lexer view first.

**defines** →

- `Comment` · [handoff247/lexer.py:22](../../../../handoff247/lexer.py#L22)
- `Lexed` · [handoff247/lexer.py:30](../../../../handoff247/lexer.py#L30)

**is part of** ←

- [`handoff247`](../areas/handoff247.md)

**is imported by** ←

- [`handoff247/analyzers/csharp.py`](handoff247__analyzers__csharp.py.md) · [handoff247/analyzers/csharp.py:7](../../../../handoff247/analyzers/csharp.py#L7)
- [`handoff247/analyzers/docs.py`](handoff247__analyzers__docs.py.md) · [handoff247/analyzers/docs.py:8](../../../../handoff247/analyzers/docs.py#L8)
- [`handoff247/analyzers/python.py`](handoff247__analyzers__python.py.md) · [handoff247/analyzers/python.py:9](../../../../handoff247/analyzers/python.py#L9)
- [`handoff247/analyzers/shell.py`](handoff247__analyzers__shell.py.md) · [handoff247/analyzers/shell.py:6](../../../../handoff247/analyzers/shell.py#L6)
- [`handoff247/analyzers/web.py`](handoff247__analyzers__web.py.md) · [handoff247/analyzers/web.py:6](../../../../handoff247/analyzers/web.py#L6)
- [`tests/test_handoff.py`](tests__test_handoff.py.md) · [tests/test_handoff.py:18](../../../../tests/test_handoff.py#L18)

## Comment in the file

Comment/string aware scanning for C-like languages (C#, JavaScript/TypeScript, CSS). *(module docstring)*

## Defined here

- `Comment` — class, [line 22](../../../../handoff247/lexer.py#L22)
- `Lexed` — class, [line 30](../../../../handoff247/lexer.py#L30)
- `Lexed.line_of` — method, [line 37](../../../../handoff247/lexer.py#L37)
- `newline_index` — function, [line 41](../../../../handoff247/lexer.py#L41)
- `line_at` — function, [line 45](../../../../handoff247/lexer.py#L45)
- `lex` — function, [line 49](../../../../handoff247/lexer.py#L49)
- `match_brace` — function, [line 271](../../../../handoff247/lexer.py#L271) — Index of the bracket matching ``code[open_index]`` (code must be comment/string-blanked).
- `clean_comment` — function, [line 285](../../../../handoff247/lexer.py#L285) — Strip comment markers and XML doc tags; collapse whitespace.
- `first_sentence` — function, [line 303](../../../../handoff247/lexer.py#L303)
