// main.js — bootstraps the form page & wire up import/export
import { CustomerFormHandler } from './formHandler.js';
import { exportSubmissions, importSubmissions } from './storage.js';
import { $ , showMessage } from './utils.js';

const form = document.getElementById('guestForm');
const handler = new CustomerFormHandler(form);

// Export / Import controls
$('#exportBtn')?.addEventListener('click', () => exportSubmissions());
$('#importFile')?.addEventListener('change', async (e) => {
  const file = e.target.files?.[0];
  if (!file) return;
  try{
    await importSubmissions(file);
    showMessage('Import successful!');
  }catch(err){
    showMessage('Import failed: ' + err.message, 'danger');
  } finally {
    e.target.value = '';
  }
});
