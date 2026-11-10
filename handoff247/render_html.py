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
<html lang="en">
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
:root{--g1:#2a78d6;--g2:#eb6834;--g3:#1baf7a;--g4:#eda100;--g5:#e87ba4;--g6:#008300;--g7:#6250d6;--g8:#e34948;--edge:#b9bec8}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--g1:#3987e5;--g2:#d95926;--g3:#199e70;--g4:#c98500;--g5:#d55181;--g6:#008300;--g7:#9085e9;--g8:#e66767;--edge:#4a5261}}
:root[data-theme="dark"]{--g1:#3987e5;--g2:#d95926;--g3:#199e70;--g4:#c98500;--g5:#d55181;--g6:#008300;--g7:#9085e9;--g8:#e66767;--edge:#4a5261}
.gbar{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin:10px 0 8px}
.gbar button,.legend button,#card button.act{border:1px solid var(--line);background:var(--panel);color:var(--ink);border-radius:8px;padding:4px 10px;font:inherit;font-size:13px;cursor:pointer}
.gbar label{font-size:13px;color:var(--muted);display:flex;gap:5px;align-items:center}
.legend{display:flex;gap:6px;flex-wrap:wrap;margin:0 0 10px}
.legend button{display:inline-flex;gap:6px;align-items:center;padding:3px 9px;font-size:12.5px}
.legend button[aria-pressed="false"]{opacity:.45;text-decoration:line-through}
.legend svg{flex:none}
.gwrap{position:relative;border:1px solid var(--line);border-radius:10px;overflow:hidden;background:var(--panel)}
#gcanvas{display:block;width:100%;height:min(72vh,760px);min-height:420px;touch-action:none;cursor:grab}
#gtip{position:absolute;pointer-events:none;max-width:320px;background:var(--panel);color:var(--ink);border:1px solid var(--line);border-radius:8px;padding:6px 10px;font-size:12.5px;line-height:1.45;box-shadow:var(--shadow);display:none;overflow-wrap:anywhere}
#card button.act{margin:0 6px 6px 0}
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
const TABS = [['README.md', 'Overview'], ['HANDOVER.md', 'Handover'], ['RUNNING.md', 'Running'], ['CONNECTIONS.md', 'Connections'],
  ['CODEMAP.md', 'Code map'], ['FILES.md', 'Files'], ['@graph', 'Graph'], ['wiki/index.md', 'Wiki'], ['@search', 'Search']];
const filesByPath = Object.fromEntries(DATA.files.map(f => [f.path, f]));
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
let current = 'README.md', mermaidSeq = 0;
if (window.mermaid) mermaid.initialize({startOnLoad: false, securityLevel: 'strict', theme: 'default', flowchart: {htmlLabels: true, useMaxWidth: false, wrappingWidth: 320}});

function tabs() {
  const nav = document.getElementById('tabs'); nav.innerHTML = '';
  for (const [id, label] of TABS) {
    const b = document.createElement('button'); b.type = 'button'; b.textContent = label; b.setAttribute('role', 'tab');
    b.setAttribute('aria-selected', id === current || (id === 'wiki/index.md' && current.startsWith('wiki/')));
    b.onclick = () => show(id); nav.append(b);
  }
}
// a link written inside wiki/…/page.md is relative to that page; the viewer sits at the pack root
function resolveHref(href) {
  if (/^[a-z][a-z0-9+.-]*:|^#|^\//i.test(href) || current.startsWith('@') || !current.includes('/')) return href;
  const [path, frag] = href.split('#');
  const parts = current.split('/').slice(0, -1);
  for (const seg of path.split('/')) {
    if (seg === '..') { if (parts.length && parts[parts.length - 1] !== '..') parts.pop(); else parts.push('..'); }
    else if (seg && seg !== '.') parts.push(seg);
  }
  return parts.join('/') + (path.endsWith('/') ? '/' : '') + (frag ? '#' + frag : '');
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
  if (id === '@graph') { graphPage(); return; }
  page.innerHTML = md((DATA.pages[id] || '').replace(/^---\n[\s\S]*?\n---\n/, ''));
  wireLinks(page);
  await drawDiagrams(page);
  if (anchor) document.getElementById(anchor)?.scrollIntoView(); else window.scrollTo(0, 0);
  try { history.replaceState(null, '', '#' + id); } catch (e) {}
}
function wireLinks(root) {
  root.querySelectorAll('h2,h3').forEach(h => { if (!h.id) h.id = h.textContent.trim().toLowerCase().replace(/[^\p{L}\p{N}_]+/gu, '-'); });
  root.querySelectorAll('a[href]').forEach(a => {
    const raw = a.getAttribute('href');
    if (raw.startsWith('#')) return;
    const href = resolveHref(raw);
    if (href !== raw) a.setAttribute('href', href);
    const target = href.split('#')[0];
    if (DATA.pages[target]) { a.onclick = e => { e.preventDefault(); show(target); }; return; }
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
    mk('Fit', fit);
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
  let h = `<h2>${esc(f.path)}${line ? ' <span class="muted">:' + line + '</span>' : ''}</h2>`;
  h += `<div><span class="chip">${esc(f.lang)}</span><span class="chip">${f.lines} lines</span><span class="chip">${esc(f.category)}</span>${f.tags.filter(t => !t.startsWith('ns:')).map(t => `<span class="chip">${esc(t)}</span>`).join('')}</div>`;
  if (f.source_url) h += `<p><a href="${esc(f.source_url)}${line ? '#L' + line : ''}" target="_blank" rel="noopener">Open source ↗</a></p>`;
  if (G.byId['file:' + f.path]) h += `<p><button class="act" type="button" data-rel="1">Relations and wiki page</button></p>`;
  if (f.note) h += `<h3>Notes</h3><div class="note">${esc(f.note)}</div>`;
  if (f.summary) h += `<h3>Comment</h3><p>${esc(f.summary)} <span class="muted">(${esc(f.summary_source)})</span></p>`;
  if (f.translated) h += `<p class="muted">${f.translated} heading(s) or comment(s) here are English versions from the notes file; the originals are in handoff.json.</p>`;
  if (f.symbols.length) h += `<h3>Symbols</h3><ul class="list">` + f.symbols.slice(0, 60).map(s => `<li><code>${esc((s.parent && s.kind === 'method' ? s.parent + '.' : '') + s.name)}</code> <span class="muted">${esc(s.kind)} · L${s.line}</span>${s.doc ? '<br>' + esc(s.doc) : ''}</li>`).join('') + '</ul>';
  for (const [title, list, arrow] of [['Links out', f.out, '→'], ['Links in', f.in, '←']]) {
    if (!list.length) continue;
    h += `<h3>${title}</h3><ul class="list">` + list.map(e => `<li><span class="chip">${esc(e.kind)}</span>${arrow} ${link(e.other, 0, e.other)}${e.label ? ' <span class="muted">' + esc(e.label) + '</span>' : ''}</li>`).join('') + '</ul>';
  }
  const card = document.getElementById('card'); card.innerHTML = h;
  card.querySelectorAll('a[data-path]').forEach(a => a.onclick = e => { e.preventDefault(); openCard(a.dataset.path, +a.dataset.line); });
  card.querySelector('[data-rel]')?.addEventListener('click', () => openEntity('file:' + f.path));
  const d = document.getElementById('drawer'); d.classList.add('open'); d.setAttribute('aria-hidden', 'false'); d.scrollTop = 0;
}
function closeDrawer() { const d = document.getElementById('drawer'); d.classList.remove('open'); d.setAttribute('aria-hidden', 'true'); }
document.addEventListener('keydown', e => { if (e.key === 'Escape') closeDrawer(); });

// ---------------------------------------------------------------- ontology: entity cards and the graph
const ONT = DATA.ontology || {classes: [], relations: [], entities: [], triples: []};
const CLS = Object.fromEntries(ONT.classes.map(c => [c.id, c]));
const REL = Object.fromEntries(ONT.relations.map(r => [r.id, r]));
const GROUPS = ['file', 'structure', 'type', 'run', 'operation', 'interface', 'config', 'outside'];   // colour slot 1..8, fixed
const G = {nodes: [], links: [], vis: [], vlinks: [], byId: {}, hidden: new Set(), sel: null, hover: null, drag: null, match: null,
  k: 1, tx: 0, ty: 0, alpha: 0, auto: true, labels: true, dirty: false, raf: 0, started: false, col: {}};
(function () {
  for (const e of ONT.entities) { const n = {e, c: CLS[e.type], deg: 0, out: [], in: [], x: 0, y: 0, vx: 0, vy: 0}; G.nodes.push(n); G.byId[e.id] = n; }
  for (const r of ONT.triples) {
    const s = G.byId[r.s], o = G.byId[r.o]; if (!s || !o) continue;
    const l = {s, o, r}; s.deg++; o.deg++; s.out.push(l); o.in.push(l); G.links.push(l);
  }
  let seed = 7; const rnd = () => (seed = seed * 16807 % 2147483647) / 2147483647;   // fixed seed: the same picture every time
  for (const n of G.nodes) {
    const a = GROUPS.indexOf(n.c.group) / GROUPS.length * 6.2832 + rnd() * .8, d = 60 + rnd() * 320;
    n.x = Math.cos(a) * d; n.y = Math.sin(a) * d;
    n.r = n.e.type === 'Project' ? 13 : Math.min(12, 3.5 + Math.sqrt(n.deg) * 1.2);
  }
  if (G.nodes.length > 1200) for (const id of ['Type', 'Package', 'EnvVar', 'Port', 'Host', 'Command']) G.hidden.add(id);
})();
const entLabel = e => { const s = e.type === 'File' ? e.name.split('/').pop() : e.name; return s.length > 34 ? s.slice(0, 33) + '…' : s; };
function entLink(id) {
  const n = G.byId[id];
  return n ? `<a href="#" data-ent="${esc(id)}">${esc(n.e.name)}</a> <span class="muted">${esc(n.c.label)}</span>` : esc(id);
}
function openEntity(id) {
  const n = G.byId[id]; if (!n) return; const e = n.e;
  let h = `<h2>${esc(e.name)}</h2><div><span class="chip">${esc(n.c.label)}</span><span class="chip">${n.deg} relation(s)</span></div>`;
  if (e.summary) h += `<p>${esc(e.summary)}</p>`;
  h += '<p>';
  if (e.page && DATA.pages[e.page]) h += `<button class="act" type="button" data-page="1">Wiki page</button>`;
  if (e.type === 'File' && filesByPath[e.name]) h += `<button class="act" type="button" data-file="1">File card</button>`;
  if (current !== '@graph') h += `<button class="act" type="button" data-show="1">Show in graph</button>`;
  h += '</p>';
  for (const [list, end, word, arrow] of [[n.out, 'o', 'label', '→'], [n.in, 's', 'inverse', '←']]) {
    const by = {}; for (const l of list) (by[l.r.p] ||= []).push(l);
    for (const p of Object.keys(by)) {
      h += `<h3>${esc(REL[p] ? REL[p][word] : p)} ${arrow}</h3><ul class="list">` + by[p].slice(0, 80).map(l =>
        `<li>${entLink(l[end].e.id)}${l.r.label ? ' <span class="muted">(' + esc(l.r.label) + ')</span>' : ''}` +
        `${l.r.file ? ' <span class="muted">· ' + esc(l.r.file) + (l.r.line ? ':' + l.r.line : '') + '</span>' : ''}` +
        `${l.r.inferred ? ' <span class="chip" title="' + esc(l.r.inferred) + '">inferred</span>' : ''}</li>`).join('') +
        (by[p].length > 80 ? `<li class="muted">… ${by[p].length - 80} more</li>` : '') + '</ul>';
    }
  }
  const card = document.getElementById('card'); card.innerHTML = h;
  card.querySelectorAll('a[data-ent]').forEach(a => a.onclick = ev => { ev.preventDefault(); focusEntity(a.dataset.ent); });
  card.querySelector('[data-page]')?.addEventListener('click', () => { closeDrawer(); show(e.page); });
  card.querySelector('[data-file]')?.addEventListener('click', () => openCard(e.name));
  card.querySelector('[data-show]')?.addEventListener('click', async () => { await show('@graph'); focusEntity(id); });
  const d = document.getElementById('drawer'); d.classList.add('open'); d.setAttribute('aria-hidden', 'false'); d.scrollTop = 0;
}
function focusEntity(id) {
  const n = G.byId[id]; if (!n) return;
  if (current === '@graph') {
    if (G.hidden.has(n.e.type)) { G.hidden.delete(n.e.type); glegend(); gvisible(); }
    // the card opens over the right side, so the mark is centred in what stays visible
    G.sel = n; G.auto = false; G.tx = -n.x * G.k - (window.innerWidth > 1100 ? 220 : 0); G.ty = -n.y * G.k; G.dirty = true;
  }
  openEntity(id);
}
function gcolors() {
  const css = getComputedStyle(document.documentElement), v = k => css.getPropertyValue(k).trim();
  G.col = {ink: v('--ink'), muted: v('--muted'), panel: v('--panel'), edge: v('--edge'), accent: v('--accent'), g: GROUPS.map((_, i) => v('--g' + (i + 1)))};
}
function gvisible() {
  G.vis = G.nodes.filter(n => !G.hidden.has(n.e.type));
  G.vlinks = G.links.filter(l => !G.hidden.has(l.s.e.type) && !G.hidden.has(l.o.e.type));
  G.top = new Set([...G.vis].sort((a, b) => b.deg - a.deg).slice(0, 28));   // always named, however far zoomed out
  G.alpha = Math.max(G.alpha, .5); G.dirty = true; gcount();
}
function gcount() {
  const c = document.getElementById('gcount'); if (!c) return;
  c.textContent = `${G.vis.length} of ${G.nodes.length} things, ${G.vlinks.length} relations` + (G.match ? ` · ${G.match.size} match` : '');
}
function shapePath(ctx, shape, x, y, r) {
  ctx.beginPath();
  if (shape === 'square') ctx.rect(x - r * .86, y - r * .86, r * 1.72, r * 1.72);
  else if (shape === 'diamond') { ctx.moveTo(x, y - r * 1.2); ctx.lineTo(x + r * 1.2, y); ctx.lineTo(x, y + r * 1.2); ctx.lineTo(x - r * 1.2, y); ctx.closePath(); }
  else if (shape === 'triangle') { ctx.moveTo(x, y - r * 1.25); ctx.lineTo(x + r * 1.15, y + r * .85); ctx.lineTo(x - r * 1.15, y + r * .85); ctx.closePath(); }
  else ctx.arc(x, y, r, 0, 6.2832);
}
function swatch(c) {
  const s = {square: '<rect x="2" y="2" width="10" height="10"/>', diamond: '<path d="M7 .5 13.5 7 7 13.5 .5 7z"/>',
    triangle: '<path d="M7 1 13.5 12.5H.5z"/>'}[c.shape] || '<circle cx="7" cy="7" r="5.5"/>';
  return `<svg width="14" height="14" viewBox="0 0 14 14" style="fill:var(--g${GROUPS.indexOf(c.group) + 1})" aria-hidden="true">${s}</svg>`;
}
function glegend() {
  const box = document.getElementById('glegend'); if (!box) return; box.innerHTML = '';
  for (const c of ONT.classes) {
    const n = G.nodes.filter(x => x.e.type === c.id).length; if (!n) continue;
    const b = document.createElement('button'); b.type = 'button'; b.title = c.description; b.setAttribute('aria-pressed', !G.hidden.has(c.id));
    b.innerHTML = swatch(c) + esc(c.plural) + ' <span class="muted">' + n + '</span>';
    b.onclick = () => { if (G.hidden.has(c.id)) G.hidden.delete(c.id); else G.hidden.add(c.id); glegend(); gvisible(); };
    box.append(b);
  }
}
function graphPage() {
  const page = document.getElementById('page');
  page.innerHTML = `<h1>Graph</h1>
<p class="muted">Every mark is something the analysis found; every line is a relation that has a file and line behind it (dashed: inferred). Colour is the kind of thing and the shape tells kinds of one colour apart. Click a mark for its relations, drag to move, scroll to zoom. The same content as text is on the Wiki tab, as data in <a href="ontology.json" target="_blank" rel="noopener">ontology.json</a>.</p>
<div class="gbar"><input id="gq" type="search" placeholder="Find in the graph" aria-label="Find in the graph"><button id="gfit" type="button">Fit</button><label><input id="glab" type="checkbox"${G.labels ? ' checked' : ''}> Names</label><span id="gcount" class="muted"></span></div>
<div class="legend" id="glegend"></div>
<div class="gwrap"><canvas id="gcanvas" role="img" aria-label="Graph of the project ontology"></canvas><div id="gtip"></div></div>`;
  G.cv = document.getElementById('gcanvas'); G.ctx = G.cv.getContext('2d'); G.match = null; G.hover = null;
  gcolors(); glegend(); gvisible(); gwire();
  if (!G.started) { G.started = true; G.alpha = 1; }
  G.dirty = true; if (!G.raf) G.raf = requestAnimationFrame(gloop);
  window.scrollTo(0, 0);
  try { history.replaceState(null, '', '#@graph'); } catch (e) {}
}
function gloop() {
  if (current !== '@graph' || !document.body.contains(G.cv)) { G.raf = 0; return; }
  if (G.alpha > .02) { gtick(); if (G.vis.length < 700) gtick(); if (G.auto) gfit(); G.dirty = true; }
  if (G.dirty) { G.dirty = false; gdraw(); }
  G.raf = requestAnimationFrame(gloop);
}
function gtick() {
  const ns = G.vis, a = G.alpha;
  for (let i = 0; i < ns.length; i++) {
    const p = ns[i];
    for (let j = i + 1; j < ns.length; j++) {
      const q = ns[j]; let dx = q.x - p.x, dy = q.y - p.y, d2 = dx * dx + dy * dy;
      if (d2 > 160000) continue;
      if (d2 < 1) { dx = (i % 7) - 3.5; dy = (j % 5) - 2.5; d2 = dx * dx + dy * dy; }
      const f = 150 * a / d2; dx *= f; dy *= f; p.vx -= dx; p.vy -= dy; q.vx += dx; q.vy += dy;
    }
  }
  for (const l of G.vlinks) {
    const dx = l.o.x - l.s.x, dy = l.o.y - l.s.y, d = Math.sqrt(dx * dx + dy * dy) || 1;
    const f = (d - (26 + l.s.r + l.o.r)) / d * .22 * a / Math.sqrt(Math.min(l.s.deg, l.o.deg));
    l.s.vx += dx * f; l.s.vy += dy * f; l.o.vx -= dx * f; l.o.vy -= dy * f;
  }
  for (const n of ns) {
    if (n === G.drag) { n.vx = n.vy = 0; continue; }
    n.vx = Math.max(-40, Math.min(40, (n.vx - n.x * .035 * a) * .82)); n.vy = Math.max(-40, Math.min(40, (n.vy - n.y * .035 * a) * .82));
    n.x += n.vx; n.y += n.vy;
  }
  G.alpha *= .99;
}
function gfit() {
  const ns = G.vis; if (!ns.length || !G.cv) return;
  let x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9;
  for (const n of ns) { x0 = Math.min(x0, n.x); x1 = Math.max(x1, n.x); y0 = Math.min(y0, n.y); y1 = Math.max(y1, n.y); }
  const k = Math.min(2, (G.cv.clientWidth - 80) / Math.max(1, x1 - x0), (G.cv.clientHeight - 60) / Math.max(1, y1 - y0));
  G.k = Math.max(.05, k); G.tx = -(x0 + x1) / 2 * G.k; G.ty = -(y0 + y1) / 2 * G.k; G.dirty = true;
}
function gdraw() {
  const cv = G.cv, ctx = G.ctx, w = cv.clientWidth, h = cv.clientHeight, dpr = window.devicePixelRatio || 1, C = G.col, k = G.k;
  if (cv.width !== Math.round(w * dpr) || cv.height !== Math.round(h * dpr)) { cv.width = Math.round(w * dpr); cv.height = Math.round(h * dpr); }
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0); ctx.clearRect(0, 0, w, h);
  ctx.translate(w / 2 + G.tx, h / 2 + G.ty); ctx.scale(k, k);
  const focus = G.hover || G.sel, near = new Set();
  if (focus) { near.add(focus); for (const l of focus.out) near.add(l.o); for (const l of focus.in) near.add(l.s); }
  const dim = n => (focus && !near.has(n)) || (G.match && !G.match.has(n) && !near.has(n));
  for (const dashed of [false, true]) {
    ctx.beginPath();
    for (const l of G.vlinks) {
      if (!!l.r.inferred !== dashed || (focus && (l.s === focus || l.o === focus))) continue;
      ctx.moveTo(l.s.x, l.s.y); ctx.lineTo(l.o.x, l.o.y);
    }
    ctx.setLineDash(dashed ? [4 / k, 3 / k] : []); ctx.strokeStyle = C.edge; ctx.globalAlpha = focus || G.match ? .2 : .65; ctx.lineWidth = 1 / k; ctx.stroke();
  }
  ctx.globalAlpha = 1;
  const hot = focus ? G.vlinks.filter(l => l.s === focus || l.o === focus) : [];
  for (const l of hot) {
    const dx = l.o.x - l.s.x, dy = l.o.y - l.s.y, d = Math.sqrt(dx * dx + dy * dy) || 1, ux = dx / d, uy = dy / d;
    const ex = l.o.x - ux * (l.o.r + 2 / k), ey = l.o.y - uy * (l.o.r + 2 / k), a = 7 / k;
    ctx.setLineDash(l.r.inferred ? [4 / k, 3 / k] : []); ctx.strokeStyle = C.accent; ctx.lineWidth = 1.6 / k;
    ctx.beginPath(); ctx.moveTo(l.s.x, l.s.y); ctx.lineTo(ex, ey); ctx.stroke();
    ctx.setLineDash([]); ctx.fillStyle = C.accent; ctx.beginPath(); ctx.moveTo(ex, ey);
    ctx.lineTo(ex - ux * a - uy * a * .45, ey - uy * a + ux * a * .45); ctx.lineTo(ex - ux * a + uy * a * .45, ey - uy * a - ux * a * .45); ctx.closePath(); ctx.fill();
  }
  ctx.setLineDash([]);
  for (const n of G.vis) {
    ctx.globalAlpha = dim(n) ? .16 : 1;
    shapePath(ctx, n.c.shape, n.x, n.y, n.r); ctx.fillStyle = C.g[GROUPS.indexOf(n.c.group)]; ctx.fill();
    ctx.lineWidth = 1.5 / k; ctx.strokeStyle = C.panel; ctx.stroke();
    if (n === G.sel) { shapePath(ctx, n.c.shape, n.x, n.y, n.r + 3 / k); ctx.lineWidth = 2 / k; ctx.strokeStyle = C.ink; ctx.stroke(); }
  }
  ctx.globalAlpha = 1;
  // names and relation words are drawn in screen pixels, most connected first, skipping any that would overlap
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  const sx = n => w / 2 + G.tx + n.x * k, sy = n => h / 2 + G.ty + n.y * k, placed = [];
  const put = (text, x, y, color, font, centered) => {
    ctx.font = font; const tw = ctx.measureText(text).width, bx = centered ? x - tw / 2 : x, box = [bx - 2, y - 11, bx + tw + 2, y + 4];
    if (box[2] < 0 || box[0] > w || box[3] < 0 || box[1] > h) return;
    for (const p of placed) if (box[0] < p[2] && box[2] > p[0] && box[1] < p[3] && box[3] > p[1]) return;
    placed.push(box); ctx.lineWidth = 3; ctx.strokeStyle = C.panel; ctx.lineJoin = 'round'; ctx.strokeText(text, bx, y); ctx.fillStyle = color; ctx.fillText(text, bx, y);
  };
  const named = G.vis.filter(n => !dim(n) && (near.has(n) || (G.labels && ((G.match && G.match.size <= 60) || n.r * k >= 7.5 || G.top.has(n)))));
  named.sort((a, b) => (b === focus) - (a === focus) || near.has(b) - near.has(a) || b.deg - a.deg);
  for (const n of named.slice(0, 260)) put(entLabel(n.e), sx(n) + n.r * k + 4, sy(n) + 4, C.ink, (n === focus ? '600 ' : '') + '12px system-ui,sans-serif', false);
  if (hot.length <= 16) for (const l of hot) put(REL[l.r.p] ? REL[l.r.p].label : l.r.p, (sx(l.s) + sx(l.o)) / 2, (sy(l.s) + sy(l.o)) / 2 + 4, C.muted, '11px system-ui,sans-serif', true);
}
function gwire() {
  const cv = G.cv, tip = document.getElementById('gtip');
  const world = ev => { const r = cv.getBoundingClientRect(); return [(ev.clientX - r.left - r.width / 2 - G.tx) / G.k, (ev.clientY - r.top - r.height / 2 - G.ty) / G.k]; };
  const hit = ev => {
    const [x, y] = world(ev); let best = null, bd = 1e9;
    for (const n of G.vis) { const d = Math.hypot(n.x - x, n.y - y) - n.r; if (d < 6 / G.k && d < bd) { bd = d; best = n; } }
    return best;
  };
  let down = null;
  cv.onpointerdown = ev => {
    try { cv.setPointerCapture(ev.pointerId); } catch (e) {}
    const n = hit(ev); down = {n, x: ev.clientX, y: ev.clientY, lx: ev.clientX, ly: ev.clientY, moved: false};
    cv.style.cursor = 'grabbing'; tip.style.display = 'none';
  };
  cv.onpointermove = ev => {
    if (down) {
      if (Math.abs(ev.clientX - down.x) + Math.abs(ev.clientY - down.y) > 3) down.moved = true;
      if (!down.moved) return;
      G.auto = false;
      if (down.n) { G.drag = down.n; [down.n.x, down.n.y] = world(ev); G.alpha = Math.max(G.alpha, .25); }
      else { G.tx += ev.clientX - down.lx; G.ty += ev.clientY - down.ly; }
      down.lx = ev.clientX; down.ly = ev.clientY; G.dirty = true; return;
    }
    const n = hit(ev); if (n !== G.hover) { G.hover = n; G.dirty = true; }
    cv.style.cursor = n ? 'pointer' : 'grab';
    if (!n) { tip.style.display = 'none'; return; }
    tip.innerHTML = `<strong>${esc(n.e.name)}</strong><br><span class="muted">${esc(n.c.label)} · ${n.deg} relation(s)</span>${n.e.summary ? '<br>' + esc(n.e.summary) : ''}`;
    tip.style.display = 'block';
    const r = cv.getBoundingClientRect(), x = ev.clientX - r.left, y = ev.clientY - r.top;
    tip.style.left = Math.max(0, Math.min(x + 14, r.width - tip.offsetWidth - 6)) + 'px';
    tip.style.top = (y + 18 + tip.offsetHeight > r.height ? Math.max(0, y - tip.offsetHeight - 10) : y + 18) + 'px';
  };
  cv.onpointerup = () => {
    const d = down; down = null; G.drag = null; cv.style.cursor = 'grab';
    if (!d || d.moved) return;
    if (d.n) { G.sel = d.n; openEntity(d.n.e.id); } else { G.sel = null; closeDrawer(); }
    G.dirty = true;
  };
  cv.onpointercancel = () => { down = null; G.drag = null; };
  cv.onpointerleave = () => { if (G.hover) { G.hover = null; G.dirty = true; } tip.style.display = 'none'; };
  cv.addEventListener('wheel', ev => {
    ev.preventDefault();
    const r = cv.getBoundingClientRect(), px = ev.clientX - r.left - r.width / 2, py = ev.clientY - r.top - r.height / 2;
    const k = Math.min(6, Math.max(.05, G.k * Math.exp(-ev.deltaY * .0015)));
    G.tx = px - (px - G.tx) / G.k * k; G.ty = py - (py - G.ty) / G.k * k; G.k = k; G.auto = false; G.dirty = true;
  }, {passive: false});
  document.getElementById('gfit').onclick = () => { G.auto = G.alpha > .02; gfit(); };
  document.getElementById('glab').onchange = ev => { G.labels = ev.target.checked; G.dirty = true; };
  const q = document.getElementById('gq');
  q.oninput = () => {
    const words = q.value.toLowerCase().split(/\s+/).filter(Boolean);
    G.match = words.length ? new Set(G.vis.filter(n => { const hay = (n.e.name + ' ' + n.c.label + ' ' + (n.e.summary || '')).toLowerCase(); return words.every(x => hay.includes(x)); })) : null;
    G.dirty = true; gcount();
  };
  q.onkeydown = ev => { if (ev.key === 'Enter' && G.match && G.match.size) focusEntity([...G.match].sort((a, b) => b.deg - a.deg)[0].e.id); };
}
window.addEventListener('resize', () => { G.dirty = true; });
if (window.matchMedia) matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => { gcolors(); G.dirty = true; });
function searchPage(q) {
  current = '@search'; tabs();
  const page = document.getElementById('page');
  const words = q.toLowerCase().split(/\s+/).filter(Boolean);
  const hits = DATA.files.filter(f => {
    const hay = (f.path + ' ' + f.summary + ' ' + f.note + ' ' + f.symbols.map(s => s.name + ' ' + s.doc).join(' ')).toLowerCase();
    return words.every(w => hay.includes(w));
  });
  page.innerHTML = `<h1>Search</h1><p class="muted">${hits.length} / ${DATA.files.length}</p>` +
    hits.slice(0, 300).map(f => `<div class="filehit" data-path="${esc(f.path)}"><strong>${esc(f.path)}</strong> <span class="chip">${esc(f.lang)}</span><br><span class="muted">${esc(f.note || f.summary || '')}</span></div>`).join('');
  page.querySelectorAll('.filehit').forEach(el => el.onclick = () => openCard(el.dataset.path));
}
document.getElementById('q').addEventListener('input', e => searchPage(e.target.value));
const start = decodeURIComponent(location.hash.slice(1));
show(DATA.pages[start] || start === '@graph' ? start : 'README.md');
</script>
</body>
</html>
"""


def render(project, pages: dict[str, str], diagrams: dict, notes, date: str, linker, onto: dict | None = None) -> str:
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
                      "source_url": src_url, "translated": len(f.translated),
                      "symbols": [{"name": s.name, "kind": s.kind, "line": s.line, "doc": s.doc, "parent": s.parent}
                                  for s in f.symbols if s.public][:120],
                      "out": out_edges.get(f.path, [])[:80], "in": in_edges.get(f.path, [])[:80]})
    data = {"pages": pages, "files": files,
            "diagrams": {k: {"source": v.render(), "files": v.files} for k, v in diagrams.items()},
            "linkBase": linker.base if linker.mode == "url" else "",
            "relPrefix": linker.rel_prefix if linker.mode == "relative" else ""}
    if onto:
        keep = ("id", "type", "name", "summary", "page")
        data["ontology"] = {"classes": onto["schema"]["classes"], "relations": onto["schema"]["relations"],
                            "entities": [{k: e[k] for k in keep if k in e} for e in onto["entities"]],
                            "triples": onto["relations"]}
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    title = f"Handoff · {project.name}"
    page = (TEMPLATE.replace("__TITLE__", html.escape(title))
            .replace("__VERSION__", __version__)
            .replace("__DATE__", date)
            .replace("__SEARCH__", "Find a file or symbol")
            .replace("__MARKED__", MARKED).replace("__PURIFY__", PURIFY).replace("__MERMAID__", MERMAID))
    return page.replace("__DATA__", payload, 1)   # last, so project text can never hit a placeholder
