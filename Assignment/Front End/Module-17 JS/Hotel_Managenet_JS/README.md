# Hotel Management System — JavaScript (Module 8)

A responsive, elegant web app to capture hotel guest registrations and view submissions. Built with **ES6 classes & modules**, **Bootstrap 5**, **event delegation**, **real-time validation**, and **localStorage** for persistence.

## Features
- **Responsive, mobile-first** form (Bootstrap grid)
- **CustomerFormHandler** (class)
  - `validateForm()` — full validation: name, phone (10 digits), email, address, Aadhar (12 digits), dates (future & logical), adults ≥ 1, purpose required
  - `saveToLocalStorage()` — saves as an array
  - `clearForm()` — resets and cleans validation state
  - `showMessage()` — reusable toast message
- **Event delegation** (form events, table actions)
- **Real-time validation** (on input/blur)
- **Submissions viewer** (search by name/email, filter by date, delete rows)
- **Import/Export** submissions as JSON (utility module)
- Clean, modular code (`type="module"`)

## Files
- `index.html` — Registration form
- `view.html` — Submissions list
- `assets/css/style.css` — Theme & UI polish
- `js/utils.js` — helpers & toast messages
- `js/storage.js` — localStorage CRUD + import/export
- `js/formHandler.js` — main form class
- `js/main.js` — bootstraps form page
- `js/viewer.js` — renders table, search, delete
- `README.md` — this file

## Run
Just open `index.html` or `view.html` in a browser (no build step needed).

> Tip: Use the **Export/Import** buttons to move data between machines/browsers.

## Notes on Validation
- **Phone**: exactly 10 digits (India format, no country code).
- **Aadhar**: exactly 12 digits (format check only; no checksum).
- **Dates**: check-in ≥ today; check-out > check-in.
- **Adults**: integer ≥ 1.

## Reflective Answers (Short)
- **API integration**: Replace localStorage with a REST API (POST/GET) to persist to a backend; add auth & server validation.
- **Better error UX**: Inline hints, debounce validation, disable submit until valid, and per-field help.
- **Security**: localStorage is unencrypted and accessible by any script on the origin; avoid storing sensitive IDs; prefer server-side storage with TLS and proper access controls.
- **PWA**: Add a manifest and service worker to cache assets and enable offline submissions queued for sync.

Enjoy! ✨
