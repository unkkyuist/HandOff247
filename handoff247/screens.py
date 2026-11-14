"""What a person sees: screens (templates and HTML pages) and the words on them.

A template is read as text, never rendered. For each one this module records the visible
terms (links, buttons, field labels, headings), where each of them leads (a link target or
the form it submits), the template condition it sits inside, the layout it extends, and
the files it shows (images, scripts, stylesheets). Translation keys are resolved through
the project's locale files, so a term is found by the word the user reads on the screen
even when the template only holds a key.

Nothing here decides who sees a screen or what a route does; ``journeys.py`` joins these
observations with the routes and their handlers.
"""
from __future__ import annotations

import json
import posixpath
import re

from .model import FileInfo

TEMPLATE_EXT = (".html", ".htm", ".jinja", ".jinja2", ".j2", ".njk", ".twig", ".hbs", ".handlebars", ".mustache")
ASSET_EXT = (".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".ico", ".bmp", ".avif", ".mp4", ".webm", ".mov", ".mp3",
             ".wav", ".ogg", ".pdf", ".woff", ".woff2", ".ttf", ".otf", ".csv", ".zip", ".docx", ".xlsx")
LOCALE_DIRS = {"locales", "locale", "i18n", "lang", "langs", "languages", "translations", "messages"}
ENGLISH = ("en", "en-us", "en_us", "en-gb", "en_gb", "english")

TOKEN = re.compile(
    r"<!--.*?-->|\{#.*?#\}"                                   # comments
    r"|\{%-?\s*(?P<stmt>.*?)\s*-?%\}"                         # {% statement %}
    r"|\{\{-?\s*(?P<expr>.*?)\s*-?\}\}"                       # {{ expression }}
    r"|<(?P<close>/?)(?P<tag>[A-Za-z][\w:-]*)(?P<attrs>(?:\"[^\"]*\"|'[^']*'|[^<>\"'])*)>",
    re.S)
ATTR = re.compile(r"([A-Za-z_:@][\w:.@-]*)\s*(?:=\s*(?:\"([^\"]*)\"|'([^']*)'|([^\s\"'>]+)))?")
HOLE = re.compile(r"\{\{.*?\}\}|\{%.*?%\}|\$\{[^}]*\}", re.S)
URL_FOR = re.compile(r"url_for\(\s*['\"]([\w.]+)['\"](?P<rest>[^)]*)\)")
FILENAME_ARG = re.compile(r"\b(?:filename|path)\s*=\s*['\"]([^'\"]+)['\"]")
DJANGO_STATIC = re.compile(r"^static\s+['\"]([^'\"]+)['\"]")
I18N_CALL = re.compile(r"^(?:[\w$]+\.)?(t|_|gettext|translate|trans|\$t|__)\(\s*(['\"])(.+?)\2")
STRING_ONLY = re.compile(r"^(['\"])(.*)\1$", re.S)
CSS_URL = re.compile(r"url\(\s*['\"]?([^'\")\s]+)['\"]?\s*\)")

# elements whose text is something a user would name when describing the screen
TERM_TAGS = {"a": "link", "button": "button", "label": "field", "h1": "heading", "h2": "heading", "h3": "heading",
             "h4": "heading", "th": "column", "legend": "heading", "summary": "heading", "title": "title",
             "option": "choice"}
VOID = {"input", "img", "br", "hr", "meta", "link", "source", "area", "base", "col", "embed", "track", "wbr"}
# who-is-it tests inside a template condition
ROLE_COMPARE = re.compile(r"[\w.\[\]'\"()]*(?:role|user_?type|account_?type|group)[\w.\[\]'\"()]*\s*(==|===|\bin\b)\s*"
                          r"(\(?\s*(?:['\"][^'\"]+['\"]\s*,?\s*)+\)?|\[\s*(?:['\"][^'\"]+['\"]\s*,?\s*)+\])", re.I)
ROLE_CALL = re.compile(r"\b(?:has_?role|is_?in_?role|hasRole|IsInRole|has_any_role)\(\s*((?:['\"][^'\"]+['\"]\s*,?\s*)+)\)")
ROLE_FLAG = re.compile(r"(?<![\w])(?:[\w.]+\.)?is_(admin|staff|superuser|moderator|editor|owner|manager)\b")
QUOTED = re.compile(r"['\"]([^'\"]+)['\"]")


def is_template(f: FileInfo) -> bool:
    return bool(f.text) and not f.skipped and f.path.lower().endswith(TEMPLATE_EXT) and "vendored" not in f.tags


def roles_in(condition: str) -> list[str]:
    """Role names a template condition tests for with ==, ``in`` or a has-role call. A negated
    test (``!=``, ``not``) names a role without saying who passes, so it yields nothing."""
    if condition.startswith("not ("):                   # the else branch of a test
        return []

    def negated(start: int) -> bool:
        return bool(re.search(r"(?:\bnot\s+|!)\(?\s*$", condition[:start]))

    found: list[str] = []
    for m in ROLE_COMPARE.finditer(condition):
        if not negated(m.start()):
            found += QUOTED.findall(m.group(2))
    for m in ROLE_CALL.finditer(condition):
        if not negated(m.start()):
            found += QUOTED.findall(m.group(1))
    for m in ROLE_FLAG.finditer(condition):
        if not negated(m.start()):
            found.append(m.group(1))
    out = []
    for r in found:
        if r not in out:
            out.append(r)
    return out


# ---------------------------------------------------------------------------- locale files

class Locales:
    """Translation resources: flat ``key -> text`` per language, with the line of each key."""

    def __init__(self, files: list[FileInfo]):
        self.langs: dict[str, dict[str, tuple[str, str, int]]] = {}        # lang -> key -> (text, file, line)
        for f in files:
            if f.lang != "json" or not f.text or f.skipped:
                continue
            parts = f.path.lower().split("/")
            stem = parts[-1].rsplit(".", 1)[0]
            in_dir = any(p in LOCALE_DIRS for p in parts[:-1])
            if in_dir:
                lang = stem if re.fullmatch(r"[a-z]{2,3}(?:[-_][a-z]{2,4})?", stem) else \
                    (parts[-2] if re.fullmatch(r"[a-z]{2,3}(?:[-_][a-z]{2,4})?", parts[-2]) else "")
            else:
                lang = ""
            if not lang:
                continue
            try:
                data = json.loads(f.text)
            except ValueError:
                continue
            if not isinstance(data, dict):
                continue
            flat: dict[str, str] = {}
            self._flatten(data, "", flat)
            table = self.langs.setdefault(lang, {})
            lines = f.text.split("\n")
            for key, text in flat.items():
                leaf = json.dumps(key.rsplit(".", 1)[-1])
                line = next((i for i, l in enumerate(lines, 1) if leaf in l), 0)
                table.setdefault(key, (text, f.path, line))

    @staticmethod
    def _flatten(node: dict, prefix: str, out: dict[str, str]) -> None:
        for k, v in node.items():
            key = f"{prefix}.{k}" if prefix else str(k)
            if isinstance(v, dict):
                Locales._flatten(v, key, out)
            elif isinstance(v, str):
                out[key] = v

    def lookup(self, key: str) -> dict | None:
        """English text first; the same key in other languages is kept as alternatives, so a
        term can be found by the word a user of another language reads."""
        hits = [(lang, table[key]) for lang, table in sorted(self.langs.items()) if key in table]
        if not hits:
            return None
        hits.sort(key=lambda h: (h[0] not in ENGLISH, h[0]))
        lang, (text, file, line) = hits[0]
        return {"key": key, "text": text, "lang": lang, "file": file, "line": line,
                "other": [{"lang": l, "text": t, "file": fl, "line": ln} for l, (t, fl, ln) in hits[1:]]}


# ---------------------------------------------------------------------------- one template

def _attrs(raw: str) -> dict[str, str]:
    out = {}
    for m in ATTR.finditer(raw or ""):
        name = m.group(1).lower()
        value = next((g for g in m.groups()[1:] if g is not None), "")
        out.setdefault(name, value)
    return out


def classify_url(raw: str) -> dict:
    """What a link, form action or src points at, as far as the text says.

    kinds: endpoint (a route named by its handler), static (a file under the static folder),
    path (a URL path, template holes shown as ``*``), external (another host), none.
    """
    raw = (raw or "").strip()
    if not raw or raw.startswith(("#", "javascript:", "mailto:", "tel:", "data:")):
        return {"kind": "none", "raw": raw}
    m = URL_FOR.search(raw)
    if m:
        if m.group(1) == "static" or m.group(1).endswith(".static"):
            fn = FILENAME_ARG.search(m.group("rest"))
            return {"kind": "static", "raw": raw, "file": fn.group(1) if fn else ""}
        return {"kind": "endpoint", "raw": raw, "endpoint": m.group(1).rsplit(".", 1)[-1]}
    inner = re.match(r"\{%-?\s*(.*?)\s*-?%\}$", raw, re.S)
    if inner:
        st = DJANGO_STATIC.match(inner.group(1))
        if st:
            return {"kind": "static", "raw": raw, "file": st.group(1)}
        return {"kind": "none", "raw": raw}
    if re.match(r"(?:https?:)?//", raw):
        host = re.sub(r"^(?:https?:)?//", "", raw).split("/", 1)[0]
        return {"kind": "external", "raw": raw, "host": host}
    path = HOLE.sub("*", raw).split("#", 1)[0].split("?", 1)[0]
    if not path or path == "*":
        return {"kind": "none", "raw": raw}
    return {"kind": "path", "raw": raw, "path": path}


class _Capture:
    def __init__(self, tag: str, attrs: dict, line: int, conditions: list[str], form: int | None, cond_lines: list[int]):
        self.tag, self.attrs, self.line, self.conditions, self.form = tag, attrs, line, conditions, form
        self.cond_lines = cond_lines
        self.parts: list[str] = []
        self.i18n: dict | None = None
        self.unresolved_key = ""
        self.holes = False
        self.field = ""


def parse_template(f: FileInfo, locales: Locales) -> dict:
    text = f.text
    line_starts = [0] + [m.end() for m in re.finditer("\n", text)]

    def line_of(offset: int) -> int:
        lo, hi = 0, len(line_starts) - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if line_starts[mid] <= offset:
                lo = mid
            else:
                hi = mid - 1
        return lo + 1

    out = {"file": f.path, "title": "", "extends": "", "includes": [], "terms": [], "forms": [], "refs": [],
           "inputs": {}, "blocks": []}
    conditions: list[str] = []          # verbatim, innermost last
    cond_lines: list[int] = []          # the line each of them was written on
    captures: list[_Capture] = []
    forms: list[int] = []
    pos = 0

    def add_text(s: str) -> None:
        if s and captures:
            for c in captures:
                c.parts.append(s)

    def expression(expr: str) -> None:
        """A {{ … }} inside an element: a translated string, a literal, or a value only known at run time."""
        if not captures:
            return
        m = I18N_CALL.match(expr)
        if m:
            arg = m.group(3)
            hit = locales.lookup(arg)
            for c in captures:
                if hit:
                    c.parts.append(hit["text"])
                    c.i18n = c.i18n or hit
                elif m.group(1) in ("_", "gettext", "trans", "__"):
                    c.parts.append(arg)                 # gettext style: the argument is the text itself
                else:
                    c.unresolved_key = c.unresolved_key or arg
            return
        s = STRING_ONLY.match(expr)
        if s:
            add_text(s.group(2))
            return
        for c in captures:
            c.holes = True
            c.parts.append(" … ")

    def finish(c: _Capture) -> None:
        txt = " ".join("".join(c.parts).split())
        kind = TERM_TAGS[c.tag]
        if c.tag == "button" and c.attrs.get("type", "").lower() == "reset":
            return
        term = {"text": txt.strip(" …").strip() if txt.replace("…", "").strip() else "", "kind": kind, "line": c.line,
                "conditions": list(c.conditions), "condition_lines": list(c.cond_lines)}
        if not term["text"]:
            if c.unresolved_key:
                term["text"], term["unresolved_key"] = c.unresolved_key, True
            elif c.tag == "a" and c.attrs.get("href") and c.holes:
                term["text"], term["dynamic"] = "", True         # e.g. a list row whose text is a record's title
            else:
                return
        if c.holes and term["text"]:
            term["partly_dynamic"] = True
        if c.i18n:
            term["i18n"] = c.i18n
        if c.tag == "a":
            term["url"] = classify_url(c.attrs.get("href", ""))
        elif c.tag == "button":
            if c.form is not None:
                term["form"] = c.form
            for a in ("onclick", "@click", "data-action", "hx-post", "hx-get", "hx-put", "hx-delete", "formaction"):
                if c.attrs.get(a):
                    term["attr"] = {a: c.attrs[a]}
                    if a.startswith("hx-") or a == "formaction":
                        term["url"] = classify_url(c.attrs[a])
                        term["method"] = a[3:].upper() if a.startswith("hx-") else ""
                    break
        elif c.tag == "label":
            term["for"] = c.attrs.get("for", "")
            term["field"] = c.field
            if c.form is not None:
                term["form"] = c.form
        elif c.tag == "title":
            out["title"] = out["title"] or term["text"]
        if c.tag in ("h1",) and not out["title"]:
            out["title"] = term["text"]
        out["terms"].append(term)

    for m in TOKEN.finditer(text):
        add_text(text[pos:m.start()])
        pos = m.end()
        line = line_of(m.start())
        stmt, expr, tag = m.group("stmt"), m.group("expr"), m.group("tag")
        if stmt is not None:
            word, _, rest = stmt.partition(" ")
            rest = " ".join(rest.split())
            if word == "if":
                conditions.append(rest)
                cond_lines.append(line)
            elif word in ("elif", "elseif") and conditions:
                conditions[-1], cond_lines[-1] = rest, line
            elif word == "else" and conditions:
                conditions[-1] = f"not ({conditions[-1]})"
            elif word == "endif" and conditions:
                conditions.pop()
                cond_lines.pop()
            elif word == "extends":
                q = QUOTED.search(rest)
                if q:
                    out["extends"] = q.group(1)
            elif word in ("include", "import", "from"):
                q = QUOTED.search(rest)
                if q:
                    out["includes"].append({"name": q.group(1), "line": line})
            elif word == "block":
                out["blocks"].append(rest.split(" ")[0])
            elif word in ("trans", "translate"):
                q = QUOTED.search(rest)
                if q:
                    add_text(q.group(1))
            continue
        if expr is not None:
            if expr.startswith("#if "):
                conditions.append(expr[4:].strip())
                cond_lines.append(line)
            elif expr.startswith("#unless "):
                conditions.append(f"not ({expr[8:].strip()})")
                cond_lines.append(line)
            elif expr in ("else", "^") and conditions:
                conditions[-1] = f"not ({conditions[-1]})"
            elif expr in ("/if", "/unless") and conditions:
                conditions.pop()
                cond_lines.pop()
            elif not expr.startswith(("#", "/", ">", "!")):
                expression(expr)
            continue
        if tag is None:
            continue                                    # a comment
        tag = tag.lower()
        attrs = _attrs(m.group("attrs"))
        if m.group("close"):
            if tag == "form" and forms:
                forms.pop()
            for i in range(len(captures) - 1, -1, -1):
                if captures[i].tag == tag:
                    finish(captures.pop(i))
                    break
            continue
        if tag == "form":
            out["forms"].append({"line": line, "action": classify_url(attrs.get("action", "")),
                                 "action_raw": attrs.get("action", ""), "method": (attrs.get("method") or "GET").upper(),
                                 "upload": "multipart" in attrs.get("enctype", "").lower(), "fields": [],
                                 "conditions": list(conditions)})
            forms.append(len(out["forms"]) - 1)
        elif tag in ("input", "textarea", "select"):
            name, itype = attrs.get("name", ""), attrs.get("type", "text").lower() if tag == "input" else tag
            if itype in ("submit", "button") and tag == "input":
                if attrs.get("value"):
                    term = {"text": attrs["value"], "kind": "button", "line": line, "conditions": list(conditions)}
                    if forms:
                        term["form"] = forms[-1]
                    out["terms"].append(term)
            elif name:
                field = {"name": name, "type": itype, "line": line, "id": attrs.get("id", "")}
                if forms:
                    out["forms"][forms[-1]]["fields"].append(field)
                    field["form"] = forms[-1]
                out["inputs"][attrs.get("id") or name] = field
                for c in captures:
                    if c.tag == "label" and not c.field:
                        c.field = name                  # <label>Text <input name=…></label>
                if attrs.get("placeholder") and itype not in ("hidden",):
                    term = {"text": attrs["placeholder"], "kind": "field", "line": line, "conditions": list(conditions),
                            "field": name, "placeholder": True}
                    if forms:
                        term["form"] = forms[-1]
                    out["terms"].append(term)
        if tag in ("img", "script", "source", "video", "audio", "embed", "iframe") and attrs.get("src"):
            out["refs"].append({"tag": tag, "url": classify_url(attrs["src"]), "line": line, "conditions": list(conditions),
                                "alt": attrs.get("alt", "")})
        elif tag == "link" and attrs.get("href"):
            out["refs"].append({"tag": "link", "url": classify_url(attrs["href"]), "line": line, "conditions": list(conditions)})
        elif tag == "a" and attrs.get("href") and attrs["href"].lower().split("?")[0].endswith(ASSET_EXT):
            out["refs"].append({"tag": "a", "url": classify_url(attrs["href"]), "line": line, "conditions": list(conditions)})
        if attrs.get("style") and "url(" in attrs["style"]:
            for u in CSS_URL.findall(attrs["style"]):
                out["refs"].append({"tag": "style", "url": classify_url(u), "line": line, "conditions": list(conditions)})
        if tag in TERM_TAGS and tag not in VOID and not m.group("attrs").rstrip().endswith("/"):
            cap = _Capture(tag, attrs, line, list(conditions), forms[-1] if forms else None, list(cond_lines))
            key = attrs.get("data-i18n") or attrs.get("data-i18n-key") or attrs.get("i18n")
            if key:
                hit = locales.lookup(key)
                if hit:
                    cap.i18n = hit
                    cap.parts.append(hit["text"] + " ")
                else:
                    cap.unresolved_key = key
            captures.append(cap)
    for c in captures:                                  # unclosed elements still count
        finish(c)
    # a label names its field through for="id"
    for term in out["terms"]:
        if term["kind"] == "field" and not term.get("field") and term.get("for"):
            inp = out["inputs"].get(term["for"])
            if inp:
                term["field"] = inp["name"]
                term["field_type"] = inp["type"]
                if "form" in inp:
                    term.setdefault("form", inp["form"])
        if term["kind"] == "field" and term.get("field") and "field_type" not in term:
            inp = next((i for i in out["inputs"].values() if i["name"] == term["field"]), None)
            if inp:
                term["field_type"] = inp["type"]
    return out


def css_refs(f: FileInfo) -> list[dict]:
    """url(…) references of a stylesheet, with their lines."""
    out = []
    for i, line in enumerate(f.text.split("\n"), 1):
        for u in CSS_URL.findall(line):
            if not u.startswith(("data:", "#")):
                out.append({"raw": u, "line": i})
    return out


def resolve_template(name: str, from_file: str, paths: set[str]) -> str:
    """The project file a template name such as ``admin/list.html`` refers to: next to the
    file that names it, or the one file whose path ends with the name. Ambiguous: ''."""
    name = name.lstrip("/")
    here = posixpath.dirname(from_file)
    for cand in (posixpath.normpath(posixpath.join(here, name)), name):
        if cand in paths:
            return cand
    hits = [p for p in paths if p.endswith("/" + name)]
    if len(hits) == 1:
        return hits[0]
    if not posixpath.splitext(name)[1]:                 # Express style: render('review') -> views/review.ejs
        hits = [p for p in paths if posixpath.splitext(p)[0].endswith("/" + name) or posixpath.splitext(p)[0] == name]
        if len(hits) == 1:
            return hits[0]
    return ""
