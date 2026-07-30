# South Air Helicopters, Inc. — Website

A static marketing website for South Air Helicopters, Inc. (est. 1997). Plain HTML/CSS/JS — no build step, no framework, no dependencies.

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
- **GitHub Pages** — push this repo, enable Pages on the `main` branch.
- **Netlify / Vercel** — drag-and-drop the folder or connect the repo, zero config needed.
- A traditional web host that serves static files also works fine.

## Content still needed

This site is fully built out structurally, but a lot of the actual copy is placeholder text (marked with `[PLACEHOLDER: ...]` and a dashed amber box in the rendered page, so it's obvious what's real vs. not). Before launch, replace:

- [ ] Real company overview, mission statement, and team bios (`about.html`) — Mike Pike (President) is in as the first leadership card, two more team slots still open
- [ ] Confirmed list of services and real pricing (`services.html`) — the current list/table is a generic starting point, not confirmed offerings
- [ ] Verified founding year and real history timeline entries (`history.html`) — "1997 or so" needs to be confirmed
- [ ] NASA partnership details — **read the notice on `nasa-partnership.html` before publishing.** Get exact wording about the relationship confirmed in writing, and don't use NASA's logo/branding without permission (NASA has strict guidelines about contractors implying endorsement)
- [ ] Bell Helicopter Service Center logo — `about.html` and `services.html` now list the real facts (Bell Helicopter Customer Service Facility, Certified Repair Station #XRIR622K) from Mike's business card, but still need the actual Bell logo file + permission to use it (Bell, like NASA, has brand guidelines for authorized service centers — confirm usage rules before publishing the logo)
- [ ] Real news/story posts (`news.html`)
- [x] Address, phone, email — filled in from Mike Pike's business card: 17402 C.R. 127, Pearland, TX 77581 / 281.648.5187 / general email sahinc@sbcglobal.net / Mike Pike (President) direct email mpikesahinc@att.net, both shown on `contact.html`. **These emails are temporary** — the company plans to buy a domain and move to a matching Google Workspace address; update `contact.html` and the site footer once that happens. Business hours still needed.
- [ ] Real photos throughout (currently placeholder boxes in `images/`)
- [ ] Wire up the contact form to an actual email/form handler (it currently doesn't send anywhere — see the note on `contact.html`)
- [ ] Domain name + Google Workspace email — company is purchasing a Google domain and will get matching email addresses; once set up, swap the temporary sbcglobal/att.net emails everywhere and point the domain at wherever the site ends up hosted
- [x] **Company name** — resolved. The site had used the singular "South Air Helicopter" (a guess from the repo name); the business card confirms the real name is plural. All page copy, titles, and headings now read "South Air Helicopters", with the full legal "South Air Helicopters, Inc." in the logo wordmark, the footer copyright, and the Bell/repair-station line.

## Design

- Navy/steel blue + amber accent, aviation-inspired
- Fully responsive (mobile nav collapses to a hamburger menu)
- No external dependencies — everything is self-contained in `css/style.css` and `js/main.js`
