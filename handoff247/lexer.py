"""Comment/string aware scanning for C-like languages (C#, JavaScript/TypeScript, CSS).

``lex`` returns two views of the source with identical offsets and line breaks:

* ``code``     comments and string *contents* replaced by spaces (safe for identifier search)
* ``code_str`` comments replaced by spaces, strings kept (safe for literal-pattern search)

plus the string literals and comments it found. Keeping offsets identical means a regex
match in either view maps straight back to a line number in the original file.
"""
from __future__ import annotations

import bisect
from dataclasses import dataclass

_JS_REGEX_PREV = set("(,=:[!&|?{};+-*%<>~^")
_JS_REGEX_KEYWORDS = {"return", "typeof", "case", "do", "else", "in", "of", "new", "delete",
                      "void", "throw", "yield", "await"}


@dataclass
class Comment:
    text: str
    line: int
    end_line: int
    doc: bool


@dataclass
class Lexed:
    code: str
    code_str: str
    strings: list[tuple[str, int, int]]   # (value, line, offset)
    comments: list[Comment]
    newlines: list[int]

    def line_of(self, offset: int) -> int:
        return line_at(self.newlines, offset)


def newline_index(text: str) -> list[int]:
    return [i for i, c in enumerate(text) if c == "\n"]


def line_at(newlines: list[int], offset: int) -> int:
    return bisect.bisect_left(newlines, offset) + 1


def lex(text: str, lang: str) -> Lexed:
    n = len(text)
    code = list(text)
    code_str = list(text)
    strings: list[tuple[str, int, int]] = []
    comments: list[Comment] = []
    nl = newline_index(text)

    def blank(arr: list[str], a: int, b: int) -> None:
        for k in range(a, min(b, n)):
            if arr[k] != "\n":
                arr[k] = " "

    def skip_simple_string(j: int, quote: str) -> int:
        """j points just after the opening quote; returns index after closing quote."""
        while j < n:
            c = text[j]
            if c == "\\":
                j += 2
                continue
            if c == quote:
                return j + 1
            if c == "\n" and quote != "`":
                return j            # unterminated; stop at end of line
            j += 1
        return n

    def skip_hole(j: int) -> int:
        """j points just after '{' (or '${'); returns index after matching '}'."""
        depth = 1
        while j < n and depth:
            c = text[j]
            if c in "\"'":
                j = skip_simple_string(j + 1, c)
                continue
            if c == "`":
                j = skip_template(j + 1)
                continue
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
            j += 1
        return j

    def skip_template(j: int) -> int:
        while j < n:
            c = text[j]
            if c == "\\":
                j += 2
                continue
            if c == "`":
                return j + 1
            if c == "$" and j + 1 < n and text[j + 1] == "{":
                j = skip_hole(j + 2)
                continue
            j += 1
        return n

    def record_string(start: int, body_start: int, body_end: int, end: int) -> None:
        strings.append((text[body_start:body_end], line_at(nl, start), start))
        blank(code, body_start, body_end)

    prev_sig = ""      # previous significant char in code (for JS regex detection)
    prev_word = ""
    i = 0
    csharp = lang == "csharp"
    js = lang in ("javascript", "typescript")
    while i < n:
        c = text[i]
        nxt = text[i + 1] if i + 1 < n else ""
        # comments
        if c == "/" and nxt == "/":
            j = text.find("\n", i)
            j = n if j < 0 else j
            body = text[i:j]
            doc = csharp and body.startswith("///")
            comments.append(Comment(body, line_at(nl, i), line_at(nl, i), doc))
            blank(code, i, j)
            blank(code_str, i, j)
            i = j
            continue
        if c == "/" and nxt == "*":
            j = text.find("*/", i + 2)
            j = n if j < 0 else j + 2
            body = text[i:j]
            comments.append(Comment(body, line_at(nl, i), line_at(nl, j - 1), body.startswith("/**")))
            blank(code, i, j)
            blank(code_str, i, j)
            i = j
            continue
        if lang == "css":
            if c in "\"'":
                j = skip_simple_string(i + 1, c)
                record_string(i, i + 1, max(i + 1, j - 1), j)
                i = j
                continue
            i += 1
            continue
        # C# string forms
        if csharp:
            if c == '"' and text.startswith('"""', i):
                q = 3
                while i + q < n and text[i + q] == '"':
                    q += 1
                close = text.find('"' * q, i + q)
                j = n if close < 0 else close + q
                record_string(i, i + q, max(i + q, j - q), j)
                i = j
                prev_sig = '"'
                continue
            prefix = ""
            k = i
            while k < n and text[k] in "@$" and len(prefix) < 3:
                prefix += text[k]
                k += 1
            if k < n and text[k] == '"' and (prefix or c == '"'):
                if text.startswith('"""', k):
                    # interpolated raw string: treat like raw
                    q = 3
                    while k + q < n and text[k + q] == '"':
                        q += 1
                    close = text.find('"' * q, k + q)
                    j = n if close < 0 else close + q
                    record_string(i, k + q, max(k + q, j - q), j)
                    i = j
                    continue
                verbatim = "@" in prefix
                interp = "$" in prefix
                j = k + 1
                while j < n:
                    ch = text[j]
                    if verbatim and ch == '"' and j + 1 < n and text[j + 1] == '"':
                        j += 2
                        continue
                    if not verbatim and ch == "\\":
                        j += 2
                        continue
                    if interp and ch == "{":
                        if j + 1 < n and text[j + 1] == "{":
                            j += 2
                            continue
                        j = skip_hole(j + 1)
                        continue
                    if ch == '"':
                        j += 1
                        break
                    if ch == "\n" and not verbatim:
                        break
                    j += 1
                record_string(i, k + 1, max(k + 1, j - 1), j)
                i = j
                prev_sig = '"'
                continue
            if c == "'":
                j = i + 1
                if j < n and text[j] == "\\":
                    j += 2
                else:
                    j += 1
                while j < n and text[j] != "'" and text[j] != "\n" and j - i < 12:
                    j += 1
                j = min(n, j + 1)
                blank(code, i + 1, j - 1)
                i = j
                continue
        # JS string forms
        if js:
            if c in "\"'":
                j = skip_simple_string(i + 1, c)
                record_string(i, i + 1, max(i + 1, j - 1), j)
                i = j
                prev_sig = c
                continue
            if c == "`":
                j = skip_template(i + 1)
                record_string(i, i + 1, max(i + 1, j - 1), j)
                i = j
                prev_sig = "`"
                continue
            if c == "/" and (prev_sig == "" or prev_sig in _JS_REGEX_PREV or prev_word in _JS_REGEX_KEYWORDS):
                j = i + 1
                in_class = False
                ok = False
                while j < n:
                    ch = text[j]
                    if ch == "\n":
                        break
                    if ch == "\\":
                        j += 2
                        continue
                    if ch == "[":
                        in_class = True
                    elif ch == "]":
                        in_class = False
                    elif ch == "/" and not in_class:
                        ok = True
                        j += 1
                        break
                    j += 1
                if ok:
                    while j < n and text[j].isalpha():
                        j += 1
                    blank(code, i + 1, j)
                    i = j
                    prev_sig = "/"
                    continue
        if not c.isspace():
            if c.isalnum() or c in "_$":
                k = i
                while k < n and (text[k].isalnum() or text[k] in "_$"):
                    k += 1
                prev_word = text[i:k]
                prev_sig = "a"
                i = k
                continue
            prev_sig = c
            prev_word = ""
        i += 1
    return Lexed("".join(code), "".join(code_str), strings, comments, nl)


def match_brace(code: str, open_index: int, open_ch: str = "{", close_ch: str = "}") -> int:
    """Index of the bracket matching ``code[open_index]`` (code must be comment/string-blanked)."""
    depth = 0
    for k in range(open_index, len(code)):
        ch = code[k]
        if ch == open_ch:
            depth += 1
        elif ch == close_ch:
            depth -= 1
            if depth == 0:
                return k
    return len(code) - 1


def clean_comment(text: str) -> str:
    """Strip comment markers and XML doc tags; collapse whitespace."""
    import re
    lines = []
    for raw in text.splitlines():
        s = raw.strip()
        for mark in ("///", "//", "/**", "/*", "*/", "*", "#", "REM ", "rem ", "::"):
            if s.startswith(mark):
                s = s[len(mark):]
                break
        s = s.removesuffix("*/").strip()
        lines.append(s)
    out = " ".join(l for l in lines if l)
    out = re.sub(r"<see\s+cref=\"([^\"]+)\"\s*/>", r"\1", out)
    out = re.sub(r"</?\w+[^>]*>", "", out)
    return re.sub(r"\s+", " ", out).strip()


def first_sentence(text: str, limit: int = 220) -> str:
    text = text.strip()
    if not text:
        return ""
    for sep in (". ", "。", "! ", "? "):
        idx = text.find(sep)
        if 0 < idx < limit:
            return text[: idx + 1].strip()
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"
