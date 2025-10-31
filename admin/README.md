# 📁 Admin Folder - All-in-One Package

This folder contains **EVERYTHING** for the custom page counter and guestbook system in one place!

## 🚀 How to Use

### Upload to Neocities:

1. **Download/grab this entire `/admin` folder**
2. **Drag and drop it to Neocities** (keep the folder structure)
3. **Done!**

The folder will be at: `https://coaiexist.wtf/admin/`

---

## 📂 What's Inside

```
/admin/
├── index.html              ← Stats dashboard (manage entries)
├── guestbook.html          ← Main guestbook page (visitor-facing)
├── css/
│   └── counter-guestbook.css
├── js/
│   ├── pageCounter.js
│   └── guestbook.js
├── data/
│   ├── pageviews.json      ← Page view counts
│   └── guestbook.json      ← Guestbook entries (has 7 imported from Bravenet)
└── README.md               ← This file
```

---

## 🌐 Access Your Pages

After uploading to Neocities:

- **Guestbook (public):** `https://coaiexist.wtf/admin/guestbook.html`
- **Admin Portal (private):** `https://coaiexist.wtf/admin/index.html`

---

## ✨ Features

### Guestbook Page
- Sign form for new entries
- Display all entries with timestamps
- Includes 7 imported Bravenet entries
- Links to admin portal

### Admin Portal
- View statistics
- Review pending entries
- Approve/reject guestbook entries
- Export updated JSON files
- Process page views

---

## 📝 How It Works

1. **Visitors sign guestbook** → Entry saves to localStorage
2. **You open admin portal** → See pending entries
3. **Approve entries** → Export updated `guestbook.json`
4. **Upload JSON file** → Replace `data/guestbook.json` on Neocities
5. **Entries appear live!**

---

## 🎨 Styling

Everything uses your site's color scheme:
- Magenta: `#f312af`
- Cyan: `#00ffcc`
- Purple: `#bf5fff`
- Yellow: `#fffb01`

---

## 🔄 Updating Data

When you approve entries or process page views:

1. Open `admin/index.html` in browser
2. Approve/reject entries
3. Click "Export" button
4. Copy the JSON output
5. Save to corresponding file in `admin/data/`
6. Upload `admin/data/` folder to Neocities

---

## 🎯 Everything is Self-Contained

All paths are **relative** - the folder works anywhere you put it!

Move it, rename it, doesn't matter - it just works! 💜

---

Made with love for the digital cosmos ✨
