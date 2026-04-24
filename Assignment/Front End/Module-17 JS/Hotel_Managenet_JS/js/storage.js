// storage.js — small utility for localStorage CRUD + import/export
const KEY = 'hotel_submissions_v1';

export function getItem(key = KEY) {
  try {
    const raw = localStorage.getItem(key);
    return raw ? JSON.parse(raw) : [];
  } catch (e) {
    console.error('getItem error', e);
    return [];
  }
}

export function setItem(data, key = KEY) {
  try {
    localStorage.setItem(key, JSON.stringify(data));
  } catch (e) {
    console.error('setItem error', e);
  }
}

export function loadSubmissions() {
  return getItem(KEY);
}

export function saveSubmissions(arr) {
  setItem(arr, KEY);
}

export function exportSubmissions() {
  const data = loadSubmissions();
  const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'submissions.json';
  a.click();
  URL.revokeObjectURL(url);
}

export function importSubmissions(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = () => {
      try {
        const parsed = JSON.parse(reader.result);
        if (!Array.isArray(parsed)) throw new Error('Invalid JSON format');
        saveSubmissions(parsed);
        resolve(parsed);
      } catch (e) {
        reject(e);
      }
    };
    reader.onerror = reject;
    reader.readAsText(file);
  });
}
