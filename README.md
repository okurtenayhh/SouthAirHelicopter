# South Air Helicopter — Website

A static marketing website for South Air Helicopter (est. 1997). Plain HTML/CSS/JS — no build step, no framework, no dependencies.

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
images/                   Put real photos here
```

Every page shares the same header/nav and footer markup (copy-pasted, since there's no templating layer). If you change the nav or footer, update it in all 7 HTML files.

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

- [ ] Real company overview, mission statement, and team bios (`about.html`)
- [ ] Confirmed list of services and real pricing (`services.html`) — the current list/table is a generic starting point, not confirmed offerings
- [ ] Verified founding year and real history timeline entries (`history.html`) — "1997 or so" needs to be confirmed
- [ ] NASA partnership details — **read the notice on `nasa-partnership.html` before publishing.** Get exact wording about the relationship confirmed in writing, and don't use NASA's logo/branding without permission (NASA has strict guidelines about contractors implying endorsement)
- [ ] Bell Helicopter Service Center status — confirmed on `about.html` and `services.html` as a `[PLACEHOLDER]`. Need: exact certification/authorization level, and the Bell logo file + permission to use it (Bell, like NASA, has brand guidelines for authorized service centers — confirm usage rules before publishing the logo)
- [ ] Real news/story posts (`news.html`)
- [ ] Address, phone, email, hours (`contact.html` and site footer)
- [ ] Real photos throughout (currently placeholder boxes in `images/`)
- [ ] Wire up the contact form to an actual email/form handler (it currently doesn't send anywhere — see the note on `contact.html`)
- [ ] Domain name — once purchased, note it here and point it at wherever the site ends up hosted

## Design

- Navy/steel blue + amber accent, aviation-inspired
- Fully responsive (mobile nav collapses to a hamburger menu)
- No external dependencies — everything is self-contained in `css/style.css` and `js/main.js`
