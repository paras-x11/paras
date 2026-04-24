// viewer.js — SubmissionViewer to render, search, delete
import { loadSubmissions, saveSubmissions, exportSubmissions, importSubmissions } from './storage.js';
import { $, $all, showMessage, formatDateISO } from './utils.js';

class SubmissionViewer {
  constructor() {
    this.tableBody = $('#tableBody');
    this.searchInput = $('#searchInput');
    this.dateFilter = $('#dateFilter');
    this.resetBtn = $('#resetFilters');
    this.bindEvents();
    this.render();
  }

  bindEvents(){
    // Event delegation for delete buttons
    this.tableBody.addEventListener('click', (e) => {
      const btn = e.target.closest('[data-action="delete"]');
      if (!btn) return;
      const idx = Number(btn.dataset.index);
      this.deleteAt(idx);
    });

    // Search & filter
    this.searchInput.addEventListener('input', () => this.render());
    this.dateFilter.addEventListener('input', () => this.render());
    this.resetBtn.addEventListener('click', () => {
      this.searchInput.value = '';
      this.dateFilter.value = '';
      this.render();
    });

    // Export / Import
    $('#exportBtn')?.addEventListener('click', () => exportSubmissions());
    $('#importFile')?.addEventListener('change', async (e) => {
      const file = e.target.files?.[0];
      if (!file) return;
      try{
        await importSubmissions(file);
        showMessage('Import successful!');
        this.render();
      }catch(err){
        showMessage('Import failed: ' + err.message, 'danger');
      } finally {
        e.target.value = '';
      }
    });
  }

  getFiltered(){
    const q = (this.searchInput.value || '').toLowerCase();
    const dateQ = this.dateFilter.value || '';
    let data = loadSubmissions();
    if (q) {
      data = data.filter(r =>
        (r.fullName && r.fullName.toLowerCase().includes(q)) ||
        (r.email && r.email.toLowerCase().includes(q))
      );
    }
    if (dateQ) {
      data = data.filter(r => (r.checkIn || '').startsWith(dateQ) || (r.checkOut || '').startsWith(dateQ));
    }
    return data;
  }

  deleteAt(index){
    const data = loadSubmissions();
    if (index < 0 || index >= data.length) return;
    if (!confirm('Delete this record?')) return;
    data.splice(index, 1);
    saveSubmissions(data);
    showMessage('Record deleted.', 'warning');
    this.render();
  }

  render(){
    const data = this.getFiltered();
    this.tableBody.innerHTML = '';
    if (!data.length){
      this.tableBody.innerHTML = '<tr><td colspan="12" class="text-center text-secondary py-4">No data found</td></tr>';
      return;
    }
    data.forEach((r, i) => {
      const tr = document.createElement('tr');
      tr.innerHTML = `
        <td>${i+1}</td>
        <td>${r.fullName ?? ''}</td>
        <td>${r.phone ?? ''}</td>
        <td>${r.email ?? ''}</td>
        <td>${r.aadhar ?? ''}</td>
        <td style="max-width:220px; word-break:break-word;">${r.address ?? ''}</td>
        <td>${r.checkIn ?? ''}</td>
        <td>${r.checkOut ?? ''}</td>
        <td>${r.adults ?? ''}</td>
        <td style="max-width:220px; word-break:break-word;">${r.purpose ?? ''}</td>
        <td>${(r.createdAt ? r.createdAt.replace('T',' ').slice(0,16) : '')}</td>
        <td class="text-end">
          <button class="btn btn-sm btn-outline-danger" data-action="delete" data-index="${i}">
            <i class="bi bi-trash"></i>
          </button>
        </td>
      `;
      this.tableBody.appendChild(tr);
    });
  }
}

new SubmissionViewer();
