# Page Counter & Guestbook System

## Overview

Custom page view counter and guestbook system for coaiexist.wtf, designed to work with **Neocities** static hosting and **GitHub** as the backend.

### Why This Approach?

- **No Bravenet**: Replaced third-party guestbook with custom solution
- **GitHub as Backend**: Uses GitHub repo + Actions for data storage and processing
- **Neocities API**: Automated deployment via GitHub Actions
- **Privacy-Focused**: All data stored in your repo, no tracking scripts

---

## Architecture

```
┌─────────────────┐
│  Static Pages   │  ← Users visit pages
│  (Neocities)    │
└────────┬────────┘
         │
         ├─── Read pageviews.json (display counts)
         ├─── Read guestbook.json (show entries)
         └─── Store pending data in localStorage
                    │
                    │
         ┌──────────▼───────────┐
         │  Admin Portal        │  ← You review & approve
         │  /admin/index.html   │
         └──────────┬───────────┘
                    │
                    ├─── Export updated JSON files
                    │
         ┌──────────▼───────────┐
         │  GitHub Repo         │  ← Commit JSON files
         │  /data/*.json        │
         └──────────┬───────────┘
                    │
         ┌──────────▼───────────┐
         │  GitHub Actions      │  ← Auto-deploy to Neocities
         │  (every 6 hours)     │
         └──────────────────────┘
```

---

## File Structure

```
coaiexist.wtf/
├── data/
│   ├── pageviews.json          # Page view counts
│   └── guestbook.json          # Guestbook entries
├── js/
│   ├── pageCounter.js          # Frontend: track & display views
│   └── guestbook.js            # Frontend: guestbook widget
├── css/
│   └── counter-guestbook.css   # Styles for both features
├── admin/
│   └── index.html              # Admin portal to manage data
├── .github/workflows/
│   └── sync-to-neocities.yml   # Deployment automation
└── guestbook.html              # Main guestbook page
```

---

## How It Works

### Page View Counter

1. **Display**: Each page fetches `/data/pageviews.json` and shows the count
2. **Track**: On page load, increments count locally (localStorage)
3. **Store**: Saves pending views in `localStorage` queue
4. **Process**: Admin reviews pending views and exports updated JSON
5. **Deploy**: GitHub Actions pushes updated JSON to Neocities

### Guestbook

1. **Display**: Loads entries from `/data/guestbook.json`
2. **Submit**: User fills form, entry saved to `localStorage` queue
3. **Review**: Admin portal shows pending entries
4. **Approve/Reject**: Admin curates entries
5. **Export**: Approved entries merged into `guestbook.json`
6. **Deploy**: GitHub Actions deploys to Neocities

---

## Setup Instructions

### 1. Configure GitHub Secrets

Add these secrets to your GitHub repo settings:

```
NEOCITIES_API_KEY     # Your Neocities API key
NEOCITIES_SITENAME    # Your site name (e.g., "coaiexist")
```

**Get your Neocities API key:**
- Go to https://neocities.org/settings
- Scroll to "API Key"
- Copy the key

### 2. Enable GitHub Actions

The workflow file is at `.github/workflows/sync-to-neocities.yml`

**It runs:**
- Every 6 hours (automatic)
- When you push changes to `/data/`
- Manually via "Actions" tab

### 3. Add Counter to Pages

Add this snippet before `</body>` tag:

```html
<!-- Page View Counter -->
<div style="position: fixed; bottom: 50px; right: 20px; z-index: 9999;">
    <div id="page-counter"></div>
</div>
<link rel="stylesheet" href="/css/counter-guestbook.css">
<script src="/js/pageCounter.js"></script>
```

### 4. Add Guestbook to a Page

```html
<!-- Guestbook Widget -->
<div id="guestbook-container"></div>

<link rel="stylesheet" href="/css/counter-guestbook.css">
<script src="/js/guestbook.js"></script>
```

---

## Admin Workflow

### Processing Pending Data

1. **Visit Admin Portal**: Open `/admin/index.html` locally or on your site
2. **Review Pending Items**:
   - Page views are auto-approved
   - Guestbook entries need manual approval/rejection
3. **Approve/Reject Entries**: Click buttons to curate guestbook
4. **Export JSON**: Click "Export" buttons to generate updated files
5. **Update Files**: Copy JSON and paste into `/data/pageviews.json` or `/data/guestbook.json`
6. **Commit & Push**: Push changes to GitHub
7. **Auto-Deploy**: GitHub Actions will deploy to Neocities

### Example Workflow

```bash
# 1. Open admin portal in browser
open admin/index.html

# 2. Approve entries and export JSON

# 3. Update data files
# (Copy exported JSON from admin portal)
nano data/guestbook.json  # Paste new JSON

# 4. Commit and push
git add data/
git commit -m "Update guestbook entries and page views"
git push

# 5. GitHub Actions automatically deploys to Neocities
```

---

## Data Formats

### pageviews.json

```json
{
  "/": 0,
  "/index.html": 42,
  "/hex.html": 15,
  "/guestbook.html": 8
}
```

### guestbook.json

```json
{
  "entries": [
    {
      "id": "abc123",
      "name": "Cosmic Traveler",
      "message": "Amazing site! Love the aesthetic.",
      "website": "https://example.com",
      "timestamp": "2025-10-27T12:00:00.000Z"
    }
  ]
}
```

---

## Customization

### Styling

Edit `/css/counter-guestbook.css` to match your aesthetic:

```css
:root {
    --magenta: #f312af;
    --cyan: #00ffcc;
    --yellow: #fffb01;
    --purple: #bf5fff;
}
```

### Counter Position

Change the inline style in your HTML:

```html
<!-- Example: Top right corner -->
<div style="position: fixed; top: 20px; right: 20px; z-index: 9999;">
    <div id="page-counter"></div>
</div>
```

### Form Validation

Edit `/js/guestbook.js`:

```javascript
this.maxNameLength = 50;
this.maxMessageLength = 500;
```

---

## Privacy & Security

### What's Tracked

- **Page Views**: Only page URLs, timestamps, user agent (stored locally)
- **Guestbook**: Name, message, optional website, timestamp

### What's NOT Tracked

- No IP addresses
- No cookies
- No third-party analytics
- No cross-site tracking

### Security Features

- XSS protection (HTML escaping)
- Manual approval for guestbook entries
- No database injections (static JSON files)
- All data in your control (GitHub repo)

---

## Troubleshooting

### Counter not showing?

1. Check browser console for errors
2. Ensure `/data/pageviews.json` exists
3. Verify CSS/JS files are loading

### Guestbook form not working?

1. Check `localStorage` is enabled in browser
2. Ensure `/data/guestbook.json` exists
3. Check `/js/guestbook.js` is loaded

### GitHub Actions failing?

1. Verify secrets are set correctly
2. Check Neocities API key is valid
3. Review Actions logs in GitHub

### Data not syncing to Neocities?

1. Check GitHub Actions ran successfully
2. Verify Neocities API key has write permissions
3. Manually trigger workflow from Actions tab

---

## Future Enhancements

### Possible Additions

- [ ] Real-time sync via webhook
- [ ] Spam protection (honeypot field)
- [ ] Export guestbook to HTML
- [ ] Guestbook pagination
- [ ] View stats dashboard
- [ ] Comment threads/replies
- [ ] Email notifications for new entries
- [ ] RSS feed for guestbook

### Advanced: Auto-Approval

Edit the admin portal to auto-approve entries:

```javascript
// Auto-approve entries matching criteria
const autoApprove = (entry) => {
  if (entry.message.length < 500 && !containsSpam(entry.message)) {
    approveEntry(entry.id);
  }
};
```

---

## Credits

- **System Design**: Custom built for coaiexist.wtf
- **Hosting**: Neocities (static files)
- **Backend**: GitHub (data storage + Actions)
- **Aesthetic**: Y2K/Medieval/Vaporwave vibes ✨

---

## Support

Issues? Questions?

1. Check this documentation
2. Review browser console logs
3. Check GitHub Actions logs
4. Review pending data in admin portal

Made with 💜 for the digital cosmos.
