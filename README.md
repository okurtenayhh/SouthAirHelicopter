# South Air Helicopters, Inc. — Website

A static marketing website for South Air Helicopters, Inc. (est. 1997). Plain HTML/CSS/JS — no build step, no framework, no dependencies.

> **Picking this project back up?** Read [`PROJECT-STATUS.md`](PROJECT-STATUS.md) — it tracks what's real vs. placeholder, what's waiting on the client, and what's next. Run `/sa-wrap-up` to refresh it at the end of a work session.

## Structure

```
index.html               Home
about.html                About the company
services.html              Services & general pricing
history.html                Company history / timeline
nasa-partnership.html         NASA collaboration page
news.html                  News & stories
contact.html                Contact form + info
css/style.css              Shared styles (design tokens at the top)
js/main.js                Mobile nav toggle, contact form UX, active-nav highlighting
images/                   Logo files (below) — put real photos here too
tools/generate-logos.py       Regenerates the logo SVGs; not needed to use them
PROJECT-STATUS.md          Between-session state: real vs placeholder, blockers, decisions
.claude/skills/sa-wrap-up/     `/sa-wrap-up` — wrap up or pick up a work session
```

Every page shares the same header/nav and footer markup (copy-pasted, since there's no templating layer). If you change the nav or footer, update it in all 7 HTML files.

## Logo files

All type is converted to outlines, so these render identically everywhere with no font dependency. `-light` variants are for dark backgrounds.

| File | Use |
| --- | --- |
| `logo-horizontal.svg` / `-light` | **Site header, letterhead, email signature.** The default lockup — currently in the nav bar. |
| `logo-primary.svg` / `-light` | Full stacked signature. Best where there's vertical room: print, signage, a title slide. |
| `logo-badge.svg` | Badge with no wordmark. For when the company name already appears nearby. |
| `logo-icon.svg` / `-light` | Rotor mark alone. Social avatars, patches, decals — anywhere too small for type. |
| `favicon.svg` | The icon on a navy ground, for browser tabs. |

The badge and the rotor icon are built from one shared blade profile so they read as a family. To regenerate (new colour, new lockup), see the header comment in `tools/generate-logos.py`.

**Status:** approved by you, not yet by Mike. Not final until he signs off. The wordmark uses the legal name — "SOUTH AIR / HELICOPTERS, INC." — with the second line tracked to sit flush under the first.

## Running locally

No build step needed. Either:

- Open `index.html` directly in a browser, or
- Serve it locally so relative links behave exactly like production:
  ```
  python3 -m http.server 8000
  ```
  then visit `http://localhost:8000`.

## Deploying

Since this is plain static HTML/CSS/JS, it can be hosted almost anywhere for free or very cheap:
- **GitHub Pages** — Settings → Pages → deploy from a branch. Point it at the working branch (`claude/south-air-helicopter-site-1fyg5b`) to get a live preview link that updates on every push, without waiting for a merge.
- **Netlify / Vercel** — drag-and-drop the folder or connect the repo, zero config needed.
- A traditional web host that serves static files also works fine.

## Content still needed

Most page copy is still placeholder — marked `[PLACEHOLDER: ...]` and rendered in a dashed amber box, so it's obvious on the page what's real and what isn't.

**The tracked list lives in [`PROJECT-STATUS.md`](PROJECT-STATUS.md)**, per page, alongside what's blocked on Mike or the office manager. Keeping it in one file stops the two lists drifting apart. Run `/sa-wrap-up` at the end of a session to refresh it.

## Design

- Navy/steel blue + amber accent, aviation-inspired
- Fully responsive (mobile nav collapses to a hamburger menu)
- No external dependencies — everything is self-contained in `css/style.css` and `js/main.js`
