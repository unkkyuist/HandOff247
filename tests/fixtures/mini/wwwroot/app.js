// Browser client: every call goes through api(), which posts to /api/<operation>.
import { renderPanel } from './panel.js';

async function api(op, args = {}) {
  const r = await fetch('/api/' + op, { method: 'POST', body: JSON.stringify(args) });
  return r.json();
}

const pattern = /api\('fake'\)/g; // a regex literal must not confuse the scanner
export async function start() {
  const items = await api('list');
  await api('notes.add', { text: `hello ${items.length}` });
  renderPanel(document.getElementById('root'), api);
}
