"""Single-file interactive viewer (index.html). It embeds the Markdown pages, the diagram
sources and the file cards; marked, DOMPurify and Mermaid are loaded from jsDelivr with
pinned versions. Without network access the pages fall back to plain text."""
from __future__ import annotations

import html
import json

from . import __version__

MARKED = "https://cdn.jsdelivr.net/npm/marked@12.0.2/marked.min.js"
PURIFY = "https://cdn.jsdelivr.net/npm/dompurify@3.1.6/dist/purify.min.js"
MERMAID = "https://cdn.jsdelivr.net/npm/mermaid@11.4.1/dist/mermaid.min.js"

TEMPLATE = r"""<!doctype html>
<html lang="__LANG__">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="generator" content="HandOff247 __VERSION__">
<title>__TITLE__</title>
<style>
:root{--bg:#f7f7f5;--panel:#ffffff;--ink:#1d2330;--muted:#5d6675;--line:#e2e4e8;--accent:#2f5bd3;--accent-soft:#e8eefc;--chip:#f0f1f4;--code:#f3f4f6;--shadow:0 1px 2px rgba(16,24,40,.06),0 4px 16px rgba(16,24,40,.06)}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#11141a;--panel:#181c24;--ink:#e6e8ec;--muted:#9aa3b2;--line:#2a303b;--accent:#8fb0ff;--accent-soft:#1f2a44;--chip:#222833;--code:#1e232c;--shadow:none}}
:root[data-theme="dark"]{--bg:#11141a;--panel:#181c24;--ink:#e6e8ec;--muted:#9aa3b2;--line:#2a303b;--accent:#8fb0ff;--accent-soft:#1f2a44;--chip:#222833;--code:#1e232c;--shadow:none}
*{box-sizing:border-box}
html,body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.6 system-ui,-apple-system,"Segoe UI","Malgun Gothic","Apple SD Gothic Neo",sans-serif}
header{position:sticky;top:0;z-index:5;background:var(--panel);border-bottom:1px solid var(--line);padding:10px 16px;display:flex;gap:12px;align-items:center;flex-wrap:wrap}
header h1{font-size:16px;margin:0;font-weight:650;letter-spacing:-.01em}
header .meta{color:var(--muted);font-size:12px}
nav{display:flex;gap:4px;flex-wrap:wrap;margin-left:auto}
nav button{border:1px solid var(--line);background:transparent;color:var(--ink);border-radius:8px;padding:5px 10px;font:inherit;font-size:13px;cursor:pointer}
nav button[aria-selected="true"]{background:var(--accent-soft);border-color:var(--accent);color:var(--accent)}
input[type=search]{border:1px solid var(--line);background:var(--bg);color:var(--ink);border-radius:8px;padding:6px 10px;font:inherit;font-size:13px;min-width:180px}
main{max-width:1180px;margin:0 auto;padding:20px 16px 80px}
article{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:8px 28px 28px;box-shadow:var(--shadow);overflow-wrap:anywhere}
article h1{font-size:24px;letter-spacing:-.02em}
article h2{font-size:19px;margin-top:2em;padding-bottom:.3em;border-bottom:1px solid var(--line)}
article h3{font-size:16px;margin-top:1.6em}
article a{color:var(--accent);text-decoration:none}
article a:hover{text-decoration:underline}
article code{background:var(--code);padding:.1em .35em;border-radius:5px;font-size:.88em}
article pre{background:var(--code);padding:12px;border-radius:8px;overflow:auto}
article blockquote{margin:1em 0;padding:.4em 1em;border-left:3px solid var(--accent);background:var(--accent-soft);border-radius:0 8px 8px 0}
article table{border-collapse:collapse;display:block;overflow-x:auto;max-width:100%;font-size:13.5px;margin:1em 0}
article th,article td{border:1px solid var(--line);padding:6px 9px;text-align:left;vertical-align:top}
article th{background:var(--chip);font-weight:600}
.diagram{overflow:auto;border:1px solid var(--line);border-radius:10px;padding:12px;background:#fff;margin:1em 0}
.diagram svg{max-width:none;height:auto}
.diagram .node{cursor:pointer}
.diagram .tools{display:flex;gap:6px;justify-content:flex-end;margin-bottom:6px}
.diagram .tools button{border:1px solid #d0d4da;background:#fff;color:#1d2330;border-radius:6px;font-size:12px;padding:2px 8px;cursor:pointer}
#drawer{position:fixed;top:0;right:0;bottom:0;width:min(520px,100vw);background:var(--panel);border-left:1px solid var(--line);box-shadow:-8px 0 24px rgba(0,0,0,.12);transform:translateX(105%);transition:transform .18s ease;z-index:10;overflow:auto;padding:18px 20px 40px}
#drawer.open{transform:none}
#drawer h2{font-size:17px;margin:.2em 0 .4em;overflow-wrap:anywhere}
#drawer a{color:var(--accent);text-decoration:none}
#drawer a:hover{text-decoration:underline}
#drawer .close{position:sticky;top:0;float:right;border:1px solid var(--line);background:var(--panel);color:var(--ink);border-radius:8px;padding:2px 10px;cursor:pointer}
.chip{display:inline-block;background:var(--chip);border-radius:999px;padding:1px 9px;font-size:12px;margin:0 4px 4px 0;color:var(--muted)}
.muted{color:var(--muted)}
.list{list-style:none;padding:0;margin:0}
.list li{padding:4px 0;border-bottom:1px dashed var(--line)}
.filehit{display:block;padding:8px 10px;border:1px solid var(--line);border-radius:8px;margin:6px 0;cursor:pointer;background:var(--panel)}
.filehit:hover{border-color:var(--accent)}
.note{border-left:3px solid #d97706;background:rgba(217,119,6,.08);padding:.4em .9em;border-radius:0 8px 8px 0;white-space:pre-wrap}
@media (max-width:640px){article{padding:4px 14px 18px}header{gap:8px}nav{margin-left:0}input[type=search]{min-width:0;width:100%}}
</style>
</head>
<body>
<header>
  <div><h1>__TITLE__</h1><div class="meta">HandOff247 __VERSION__ · __DATE__</div></div>
  <nav id="tabs" role="tablist"></nav>
  <input id="q" type="search" placeholder="__SEARCH__" aria-label="__SEARCH__">
</header>
<main><article id="page"></article></main>
<aside id="drawer" aria-hidden="true"><button class="close" type="button" onclick="closeDrawer()">✕</button><div id="card"></div></aside>
<script id="data" type="application/json">__DATA__</script>
<script src="__MARKED__"></script>
<script src="__PURIFY__"></script>
<script src="__MERMAID__"></script>
<script>
const DATA = JSON.parse(document.getElementById('data').textContent);
const ko = DATA.lang === 'ko';
const TABS = [['README.md', ko ? '개요' : 'Overview'], ['RUNNING.md', ko ? '실행' : 'Running'],
  ['CONNECTIONS.md', ko ? '연결' : 'Connections'], ['CODEMAP.md', ko ? '코드 지도' : 'Code map'],
  ['FILES.md', ko ? '파일' : 'Files'], ['@search', ko ? '찾기' : 'Search']];
const filesByPath = Object.fromEntries(DATA.files.map(f => [f.path, f]));
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
let current = 'README.md', mermaidSeq = 0;
if (window.mermaid) mermaid.initialize({startOnLoad: false, securityLevel: 'strict', theme: 'default', flowchart: {htmlLabels: true, useMaxWidth: false, wrappingWidth: 320}});

function tabs() {
  const nav = document.getElementById('tabs'); nav.innerHTML = '';
  for (const [id, label] of TABS) {
    const b = document.createElement('button'); b.type = 'button'; b.textContent = label; b.setAttribute('role', 'tab');
    b.setAttribute('aria-selected', id === current); b.onclick = () => show(id); nav.append(b);
  }
}
function md(text) {
  if (!window.marked) return '<pre>' + esc(text) + '</pre>';
  const raw = marked.parse(text, {gfm: true});
  return window.DOMPurify ? DOMPurify.sanitize(raw, {ADD_ATTR: ['target']}) : '<pre>' + esc(text) + '</pre>';
}
async function show(id, anchor) {
  current = id; tabs();
  const page = document.getElementById('page');
  if (id === '@search') { searchPage(document.getElementById('q').value); return; }
  page.innerHTML = md(DATA.pages[id] || '');
  wireLinks(page);
  await drawDiagrams(page);
  if (anchor) document.getElementById(anchor)?.scrollIntoView(); else window.scrollTo(0, 0);
  try { history.replaceState(null, '', '#' + id); } catch (e) {}
}
function wireLinks(root) {
  root.querySelectorAll('h2,h3').forEach(h => { if (!h.id) h.id = h.textContent.trim().toLowerCase().replace(/[^\w가-힣]+/g, '-'); });
  root.querySelectorAll('a[href]').forEach(a => {
    const href = a.getAttribute('href');
    if (DATA.pages[href]) { a.onclick = e => { e.preventDefault(); show(href); }; return; }
    if (href.startsWith('#')) return;
    const path = toProjectPath(href);
    if (path && filesByPath[path]) {
      a.onclick = e => { if (e.ctrlKey || e.metaKey) return; e.preventDefault(); openCard(path, lineOf(href)); };
    } else { a.target = '_blank'; a.rel = 'noopener'; }
  });
}
function lineOf(href) { const m = href.match(/#L(\d+)$/); return m ? +m[1] : 0; }
function toProjectPath(href) {
  let h = decodeURIComponent(href.split('#')[0]);
  if (DATA.linkBase && h.startsWith(DATA.linkBase)) return h.slice(DATA.linkBase.length);
  if (DATA.relPrefix && h.startsWith(DATA.relPrefix)) return h.slice(DATA.relPrefix.length);
  return filesByPath[h] ? h : null;
}
async function drawDiagrams(root) {
  const blocks = [...root.querySelectorAll('pre > code.language-mermaid')];
  for (const code of blocks) {
    const src = code.textContent;
    const diagram = Object.values(DATA.diagrams).find(d => d.source.trim() === src.trim());
    const box = document.createElement('div'); box.className = 'diagram';
    const tools = document.createElement('div'); tools.className = 'tools';
    let zoom = 1;
    const mk = (label, fn) => { const b = document.createElement('button'); b.type = 'button'; b.textContent = label; b.onclick = fn; tools.append(b); };
    const canvas = document.createElement('div');
    const fit = () => { const svg = canvas.querySelector('svg'); if (!svg) return;
      zoom = Math.min(1, (box.clientWidth - 26) / (svg.getBoundingClientRect().width / zoom)); canvas.style.zoom = zoom; };
    mk('−', () => { zoom = Math.max(.2, zoom - .15); canvas.style.zoom = zoom; });
    mk('+', () => { zoom = Math.min(3, zoom + .15); canvas.style.zoom = zoom; });
    mk(ko ? '맞춤' : 'Fit', fit);
    mk('1:1', () => { zoom = 1; canvas.style.zoom = 1; });
    box.append(tools, canvas);
    code.parentElement.replaceWith(box);
    if (!window.mermaid) { canvas.innerHTML = '<pre>' + esc(src) + '</pre>'; continue; }
    try {
      const {svg} = await mermaid.render('hf' + (++mermaidSeq), src);
      canvas.innerHTML = svg;
      fit();
      if (diagram) canvas.querySelectorAll('g.node').forEach(g => {
        const m = (g.id || '').match(/flowchart-(n\d+)-/); const path = m && diagram.files[m[1]];
        if (path && filesByPath[path]) { g.addEventListener('click', () => openCard(path)); g.setAttribute('tabindex', '0'); g.setAttribute('role', 'button'); }
      });
    } catch (e) { canvas.innerHTML = '<pre>' + esc(src) + '\n\n' + esc(e.message || e) + '</pre>'; }
  }
}
function link(path, line, label) {
  const f = filesByPath[path];
  return f ? `<a href="#" data-path="${esc(path)}" data-line="${line || 0}">${esc(label || path)}</a>` : esc(label || path);
}
function openCard(path, line) {
  const f = filesByPath[path]; if (!f) return;
  const L = s => ko ? s[1] : s[0];
  let h = `<h2>${esc(f.path)}${line ? ' <span class="muted">:' + line + '</span>' : ''}</h2>`;
  h += `<div><span class="chip">${esc(f.lang)}</span><span class="chip">${f.lines} ${L(['lines','줄'])}</span><span class="chip">${esc(f.category)}</span>${f.tags.filter(t => !t.startsWith('ns:')).map(t => `<span class="chip">${esc(t)}</span>`).join('')}</div>`;
  if (f.source_url) h += `<p><a href="${esc(f.source_url)}${line ? '#L' + line : ''}" target="_blank" rel="noopener">${L(['Open source ↗','원본 열기 ↗'])}</a></p>`;
  if (f.note) h += `<h3>${L(['Notes','노트'])}</h3><div class="note">${esc(f.note)}</div>`;
  if (f.summary) h += `<h3>${L(['Comment','주석'])}</h3><p>${esc(f.summary)} <span class="muted">(${esc(f.summary_source)})</span></p>`;
  if (f.symbols.length) h += `<h3>${L(['Symbols','심볼'])}</h3><ul class="list">` + f.symbols.slice(0, 60).map(s => `<li><code>${esc((s.parent && s.kind === 'method' ? s.parent + '.' : '') + s.name)}</code> <span class="muted">${esc(s.kind)} · L${s.line}</span>${s.doc ? '<br>' + esc(s.doc) : ''}</li>`).join('') + '</ul>';
  for (const [title, list, arrow] of [[L(['Links out','나가는 연결']), f.out, '→'], [L(['Links in','들어오는 연결']), f.in, '←']]) {
    if (!list.length) continue;
    h += `<h3>${title}</h3><ul class="list">` + list.map(e => `<li><span class="chip">${esc(e.kind)}</span>${arrow} ${link(e.other, 0, e.other)}${e.label ? ' <span class="muted">' + esc(e.label) + '</span>' : ''}</li>`).join('') + '</ul>';
  }
  const card = document.getElementById('card'); card.innerHTML = h;
  card.querySelectorAll('a[data-path]').forEach(a => a.onclick = e => { e.preventDefault(); openCard(a.dataset.path, +a.dataset.line); });
  const d = document.getElementById('drawer'); d.classList.add('open'); d.setAttribute('aria-hidden', 'false'); d.scrollTop = 0;
}
function closeDrawer() { const d = document.getElementById('drawer'); d.classList.remove('open'); d.setAttribute('aria-hidden', 'true'); }
document.addEventListener('keydown', e => { if (e.key === 'Escape') closeDrawer(); });
function searchPage(q) {
  current = '@search'; tabs();
  const page = document.getElementById('page');
  const words = q.toLowerCase().split(/\s+/).filter(Boolean);
  const hits = DATA.files.filter(f => {
    const hay = (f.path + ' ' + f.summary + ' ' + f.note + ' ' + f.symbols.map(s => s.name + ' ' + s.doc).join(' ')).toLowerCase();
    return words.every(w => hay.includes(w));
  });
  page.innerHTML = `<h1>${ko ? '찾기' : 'Search'}</h1><p class="muted">${hits.length} / ${DATA.files.length}</p>` +
    hits.slice(0, 300).map(f => `<div class="filehit" data-path="${esc(f.path)}"><strong>${esc(f.path)}</strong> <span class="chip">${esc(f.lang)}</span><br><span class="muted">${esc(f.note || f.summary || '')}</span></div>`).join('');
  page.querySelectorAll('.filehit').forEach(el => el.onclick = () => openCard(el.dataset.path));
}
document.getElementById('q').addEventListener('input', e => searchPage(e.target.value));
const start = decodeURIComponent(location.hash.slice(1));
show(DATA.pages[start] ? start : 'README.md');
</script>
</body>
</html>
"""


def render(project, pages: dict[str, str], diagrams: dict, notes, lang: str, date: str, linker) -> str:
    out_edges, in_edges = {}, {}
    for e in project.edges:
        out_edges.setdefault(e.src, []).append({"kind": e.kind, "other": e.dst, "label": e.label})
        in_edges.setdefault(e.dst, []).append({"kind": e.kind, "other": e.src, "label": e.label})
    files = []
    for f in project.files:
        if f.category == "asset" and not f.symbols:
            continue
        src_url = ""
        if linker.mode == "url":
            src_url = linker.base + f.path.replace(" ", "%20")
        elif linker.mode == "relative":
            src_url = linker.rel_prefix + f.path.replace(" ", "%20")
        files.append({"path": f.path, "lang": f.lang, "category": f.category, "lines": f.lines, "tags": f.tags,
                      "summary": f.summary, "summary_source": f.summary_source, "note": notes.get(f"File: {f.path}"),
                      "source_url": src_url,
                      "symbols": [{"name": s.name, "kind": s.kind, "line": s.line, "doc": s.doc, "parent": s.parent}
                                  for s in f.symbols if s.public][:120],
                      "out": out_edges.get(f.path, [])[:80], "in": in_edges.get(f.path, [])[:80]})
    data = {"lang": lang, "pages": pages, "files": files,
            "diagrams": {k: {"source": v.render(), "files": v.files} for k, v in diagrams.items()},
            "linkBase": linker.base if linker.mode == "url" else "",
            "relPrefix": linker.rel_prefix if linker.mode == "relative" else ""}
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    title = f"Handoff · {project.name}" if lang != "ko" else f"인수인계 · {project.name}"
    page = (TEMPLATE.replace("__TITLE__", html.escape(title))
            .replace("__LANG__", "ko" if lang == "ko" else "en")
            .replace("__VERSION__", __version__)
            .replace("__DATE__", date)
            .replace("__SEARCH__", "파일·심볼 찾기" if lang == "ko" else "Find a file or symbol")
            .replace("__MARKED__", MARKED).replace("__PURIFY__", PURIFY).replace("__MERMAID__", MERMAID))
    return page.replace("__DATA__", payload, 1)   # last, so project text can never hit a placeholder
