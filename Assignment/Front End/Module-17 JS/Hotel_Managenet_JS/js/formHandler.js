// formHandler.js — CustomerFormHandler class per requirements
import { saveSubmissions, loadSubmissions } from './storage.js';
import { $, showMessage, formatDateISO, sanitizeText } from './utils.js';

export class CustomerFormHandler {
  constructor(form) {
    this.form = form;
    this.state = {};
    this.bindEvents();
    this.setMinDates();
  }

  bindEvents() {
    // Event delegation: handle input/blur on the form
    this.form.addEventListener('input', (e) => this.handleRealtimeValidation(e));
    this.form.addEventListener('blur', (e) => this.handleRealtimeValidation(e), true);
    this.form.addEventListener('submit', (e) => this.onSubmit(e));

    // Clear form button
    const clearBtn = document.getElementById('clearBtn');
    if (clearBtn) clearBtn.addEventListener('click', () => this.clearForm());
  }

  setMinDates(){
    const todayISO = formatDateISO(new Date());
    this.form.checkIn.min = todayISO;
    this.form.checkOut.min = todayISO;
  }

  // Core validation rules
  validateForm() {
    const fd = new FormData(this.form);
    const data = Object.fromEntries(fd.entries());

    // sanitize
    data.fullName = sanitizeText(data.fullName);
    data.phone = sanitizeText(data.phone);
    data.email = sanitizeText(data.email);
    data.address = sanitizeText(data.address);
    data.aadhar = sanitizeText(data.aadhar);
    data.checkIn = sanitizeText(data.checkIn);
    data.checkOut = sanitizeText(data.checkOut);
    data.adults = sanitizeText(data.adults);
    data.purpose = sanitizeText(data.purpose);

    let valid = true;

    // Name: ≥ 3 chars
    valid &= this.toggleValidity('fullName', data.fullName.length >= 3);

    // Phone: exactly 10 digits
    valid &= this.toggleValidity('phone', /^\d{10}$/.test(data.phone));

    // Email: regex basic
    valid &= this.toggleValidity('email', /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(data.email));

    // Address: not empty
    valid &= this.toggleValidity('address', data.address.length > 0);

    // Aadhar: 12 digits
    valid &= this.toggleValidity('aadhar', /^\d{12}$/.test(data.aadhar));

    // Dates
    const today = new Date(formatDateISO(new Date()));
    const inDate = data.checkIn ? new Date(data.checkIn) : null;
    const outDate = data.checkOut ? new Date(data.checkOut) : null;
    const checkInOk = inDate && inDate >= today;
    const checkOutOk = outDate && inDate && outDate > inDate;

    valid &= this.toggleValidity('checkIn', !!checkInOk);
    valid &= this.toggleValidity('checkOut', !!checkOutOk);

    // Adults: number >=1
    const adultsNum = Number.parseInt(data.adults, 10);
    const adultsOk = Number.isFinite(adultsNum) && adultsNum >= 1;
    valid &= this.toggleValidity('adults', adultsOk);

    // Purpose: required
    valid &= this.toggleValidity('purpose', data.purpose.length > 0);

    return { valid: !!valid, data: { ...data, createdAt: new Date().toISOString() } };
  }

  toggleValidity(fieldId, isValid){
    const el = this.form[fieldId];
    if (!el) return true;
    if (isValid) {
      el.classList.remove('is-invalid');
    } else {
      el.classList.add('is-invalid');
    }
    return isValid;
  }

  handleRealtimeValidation(e){
    const field = e.target;
    if (!('id' in field)) return;
    // Re-run validate only for this field by simple rules
    const { data } = this.validateForm();
    // optional: could be optimized per-field
  }

  saveToLocalStorage(record) {
    const arr = loadSubmissions();
    arr.push(record);
    saveSubmissions(arr);
  }

  clearForm() {
    this.form.reset();
    this.setMinDates();
    // remove invalid markers
    ['fullName','phone','email','address','aadhar','checkIn','checkOut','adults','purpose']
      .forEach(id => this.form[id]?.classList.remove('is-invalid'));
    showMessage('Form cleared.', 'secondary');
  }

  onSubmit(e) {
    e.preventDefault();
    const { valid, data } = this.validateForm();
    if (!valid) {
      showMessage('Please correct highlighted fields.', 'danger');
      return;
    }
    this.saveToLocalStorage(data);
    this.showMessage('Submission saved successfully.');
    this.clearForm();
  }

  showMessage(message, type='success'){
    showMessage(message, type);
  }
}
