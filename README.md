# Kiro IDE Documentation Hub

A premium, standalone single-page website that pulls the latest documentation from [kiro.dev/docs](https://kiro.dev/docs/), compiles it into a single, offline-friendly Markdown file, and renders it with a beautiful, fast UI.

## Features
- **Visual Design**: Sleek dark mode with radial neon accents, clean typography (Inter & Outfit), responsive double-column grid layout.
- **Dynamic Sidebar TOC**: Dynamic table of contents that matches reading progression (Scroll Spy).
- **Fuzzy Search**: Instant header filtering from the search bar.
- **Code Copy**: Hover and click copy button on code blocks.
- **One-click Download**: Download the combined `kiro_docs.md` file locally via a button in the header.
- **Self-Contained Markdown**: Scraper rewrites all relative links and image references to absolute `kiro.dev` URLs so the downloaded file functions offline and inside any markdown editor.

---

## Getting Started

### 1. Requirements
Ensure you have Python 3 and Node.js installed. Install the Python dependencies for parsing:
```bash
pip install beautifulsoup4
```

### 2. Update/Regenerate Documentation
To crawl the live `kiro.dev` site and compile the newest version of the documentation:
```bash
npm run update
```
*This executes `python3 update_docs.py`, generating `kiro_docs.md` and `metadata.json`.*

### 3. Local Development Preview
To spin up a local preview server:
```bash
npm run dev
```
Then navigate to `http://localhost:8000` in your web browser.

---

## File Structure
- `update_docs.py` — Python scraper and markup compiler.
- `kiro_docs.md` — The compiled Markdown output containing all 12 sections.
- `metadata.json` — Scraping metadata (timestamp, word counts).
- `index.html` — Main website template layout.
- `style.css` — Custom premium Vanilla CSS styles.
- `app.js` — Client controller for rendering, search, TOC, and downloading.
- `package.json` — Commands management.
