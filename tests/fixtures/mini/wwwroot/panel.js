/** Side panel. Receives api() from app.js as a parameter. */
export function renderPanel(root, api) {
  api('get', { id: 1 });
  api('notes.count');
}
