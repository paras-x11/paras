// utils.js — general helpers and message UI
export function $(selector, root = document) { return root.querySelector(selector); }
export function $all(selector, root = document) { return [...root.querySelectorAll(selector)]; }

export function formatDateISO(d) {
  const dt = (d instanceof Date) ? d : new Date(d);
  const pad = (n) => String(n).padStart(2, '0');
  return `${dt.getFullYear()}-${pad(dt.getMonth()+1)}-${pad(dt.getDate())}`;
}

export function showMessage(message, type = 'success') {
  const container = document.getElementById('toastContainer');
  if (!container) return alert(message);
  const id = `toast-${Date.now()}`;
  const div = document.createElement('div');
  div.className = `toast align-items-center text-bg-${type} show`;
  div.id = id;
  div.role = 'alert';
  div.ariaLive = 'assertive';
  div.ariaAtomic = 'true';
  div.innerHTML = `
    <div class="d-flex">
      <div class="toast-body">${message}</div>
      <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
    </div>`;
  container.appendChild(div);
  setTimeout(() => div.remove(), 4000);
}

export function sanitizeText(value){
  return String(value ?? '').trim();
}
