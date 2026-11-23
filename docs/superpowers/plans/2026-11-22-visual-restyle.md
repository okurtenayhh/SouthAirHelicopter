# Visual Restyle (2b) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restyle the four launch pages to the approved 2b look: navy leading, gunmetal plate details, slab and mono type, square corners.

**Architecture:** Nearly all of the change is in `css/style.css` (tokens first, then components). The markup changes are small: a call link in the shared header (byte-identical on all four pages) and a data plate replacing the Home stats strip. The fonts are self-hosted woff2 files in `fonts/`.

**Tech Stack:** Static HTML/CSS/JS, no build. Python `tools/verify.py` for checks; Playwright for the visual pass; Netlify CLI for the review deploy.

**Spec:** `docs/superpowers/specs/2026-11-22-visual-restyle-design.md`

## Global Constraints

- Colors: navy `#1e3a5f`, deep navy `#14283f`, gunmetal `#3d4854`→`#2b333d`, orange `#f26722` (header call button and one accent rule per view). No navy→sky gradients.
- Fonts: Zilla Slab 500/600 (headings), Inter Tight variable (body), IBM Plex Mono 500 (numbers and labels). Self-hosted, SIL OFL; no font or style URL outside the site.
- Square corners; thin rules instead of shadowed cards.
- No copy changes. The real logo stays. Header and footer stay byte-identical across pages.
- Text contrast at least 4.5:1 (existing `--color-*-on-*` tints stay).

## Review Focus

- Mobile header (390px): logo, call link and hamburger fit on one row with no sideways scroll.
- Fonts fail to load (blocked, slow): fallbacks are set so the page still reads. `font-display: swap`.
- Data plate on Home at 390px: stacks to two columns or one, with no overflow.
- Orange text on navy or white below 4.5:1: only the on-dark/on-light tints are used for small text.
- verify.py nav-count check: the call link must sit outside `<ul class="nav-links">` so the count stays 4.

---

### Task 1: Self-hosted fonts + type tokens

**Files:** Create `fonts/*.woff2`, `fonts/OFL.txt`; Modify `css/style.css` (top of file, `:root`); Modify `tools/verify.py`.

- [ ] Add verify check `no external font or stylesheet URLs`: fail if any launch page has `<link rel="stylesheet" href="http` or `fonts.googleapis`, or if `style.css` contains `url(http`. Run it: it passes today, then the scratch-copy test with an injected Google Fonts link fails.
- [ ] Fetch the latin woff2 files: Zilla Slab 500 and 600, Inter Tight variable (wght), IBM Plex Mono 500, plus the OFL text. Download into a fresh scratch directory, confirm each file is `font/woff2` (magic `wOF2`), then copy into `fonts/`.
- [ ] `@font-face` blocks with `font-display: swap`; tokens `--font-heading: "Zilla Slab", Rockwell, Georgia, serif`, `--font-body: "Inter Tight", "Segoe UI", Arial, sans-serif`, `--font-mono: "IBM Plex Mono", Consolas, monospace`.
- [ ] verify.py green. Commit.

### Task 2: Palette and component restyle

**Files:** Modify `css/style.css`.

- [ ] Tokens: `--radius: 0`; shadows reduced to the plate only; add `--color-gunmetal-dark: #2b333d`.
- [ ] Header deep navy. Hero flat navy (gradient and orange glow removed), 4px deep-navy bottom rule. Headings in slab 500/600. Eyebrows in mono, letter-spaced.
- [ ] Cards: no shadow, 2px navy top rule. Card icons in navy. Callout and quote-strip: square, with one orange rule.
- [ ] `.fact-panel` becomes the riveted gunmetal plate: rivets via `::before`/`::after` on the panel plus `.rivets` spans, mono values.
- [ ] `.cta-band` gunmetal with 3px orange top rule; footer deep navy.
- [ ] Buttons square; primary stays orange with ink text.
- [ ] verify.py green. Commit.

### Task 3: Header call link

**Files:** Modify all four pages' `<header>` (identical edit); `css/style.css`.

- [ ] Insert `<a class="nav-call" href="tel:+12816485187">281.648.5187</a>` inside `.nav-bar`, after `<ul class="nav-links">`. Mono, orange outline. On mobile it shows beside the hamburger.
- [ ] verify.py: header byte-identical, 4 nav items. 390px header has no overflow. Commit.

### Task 4: Home data plate

**Files:** Modify `index.html` (the `.stats-band` block); `css/style.css`.

- [ ] Replace the stats band with `<div class="plate-wrap"><dl class="data-plate">`. Entries: Established 1979 · Bell CSF 1981 · Repair Station XRIR622K · No maint.-related accident 45+ yrs. It overlaps the hero bottom by about 32px. 4 columns, 2 below 700px.
- [ ] verify.py (age check) green. 390px has no overflow. Commit.

### Task 5: Visual pass and review deploy

- [ ] Playwright at 1280 and 390 on all four pages: screenshots read, no overflow, no console errors.
- [ ] Contrast spot-check of new pairs (mono labels on gunmetal, eyebrows on navy).
- [ ] Push; redeploy `phase-1-ready` from a clean worktree; curl 200s and the `private/` 404.
