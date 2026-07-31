# Project Status

*Last updated: 2026-07-31 · Everything merged to `main` · Site work landed at `f053768` · PRs #1, #2, #3 all merged · No open PRs*

> Maintained by the `/sa-wrap-up` skill. If this file and the repo disagree, the repo is right — fix this file.

## Where This Stands

**Ten pages now, structurally complete.** The competitor research at `docs/market-research.md` was worked into the site: three new pages (`bell-service-center.html`, `platforms.html`, `careers.html`), a repeated Request-a-Quote CTA, certifications in the footer sitewide, an airport-identifier slot on Contact, and the placeholder pricing table replaced with a "How Pricing Works" section — MRO shops quote per job rather than publish rates.

So there is now a *place* for everything the category expects. What's in most of those places is still placeholder text, flagged in amber on the page. The gap is content, not structure.

Nothing has been shown to Mike yet. The site isn't deployed anywhere — there's no live URL, so the only way to view it is locally or via the repo.

## Next Up

Things that can move without waiting on anyone:

1. **Wire the contact form to a real handler** (Formspree / Netlify Forms / similar). Right now a customer who fills it in reaches nobody. Highest-severity item on the site.
2. **Turn on GitHub Pages** so there's a shareable preview link — Settings → Pages → deploy from the working branch. This is a repo-owner action; Claude can't do it. Once live, everyone can watch progress by refreshing one URL.
3. **Draft the questionnaire for Mike and the office manager** — one page covering everything in *Waiting On The Client* below, so it can be answered in a single sitting rather than in fragments.
4. **Send Mike the logo board** for sign-off: https://claude.ai/code/artifact/55ef4406-1569-4a12-9bd7-e744d1ad8683
5. **Decide whether Careers ships.** It's built, but a careers page with no listed openings can read as a dead site. Either get openings (or an explicit "nothing right now") from the office manager, or hold the page back until launch.
6. **Lean into the personal/small-shop angle** in About and the homepage hero — named-owner warmth is the one thing neither Arrow Aviation nor Summit Aviation has. Needs Mike's story, so it's half-blocked, but the *structure* for it is there now.

## Waiting On The Client

**Mike (owner / president)**
- Sign-off on the logo. The user approved it; Mike has not seen it.
- Exact scope of the NASA relationship, ideally in writing — which center or program, and what South Air actually does for them. See the standing warning on `nasa-partnership.html` before writing a word of this.
- Confirmed founding year. "1997 or so" is what we have. Every reference to it is now flagged as a placeholder, so this blocks more of the site than it used to — the homepage hero eyebrow, the years stat, and the History page all wait on it.
- **Which airframes the shop is rated on**, and what work is authorized per model. `platforms.html` is entirely empty until this lands, by design.
- What the Bell Customer Service Facility certification actually covers, what ratings are on Repair Station certificate #XRIR622K, plus the Bell badge artwork and written permission to use it.
- Confirmed service list. The current six services are generic helicopter-shop categories, not a confirmed offering.
- How quoting actually works — what he needs from a customer to quote, how the quote comes back, and typical turnaround. Fills the three cards on `services.html`.
- The airport identifier and heliport coordinates for Pearland Regional Airport.
- How public the recent change of ownership should be.

**Office manager (the user's mother)**
- Business hours.
- Company overview and mission statement for the About page.
- Which inbox is the public "general inquiries" one, and whether other staff should appear on the team page.
- Whether there are any current job openings — and if not, that's fine, `careers.html` should just say so.
- Whether resumes should go to a separate inbox rather than the general one, plus the EEO statement wording.
- Photos: hangar, aircraft, team, anything historical.

**Either**
- Domain name once purchased, and the Google Workspace email addresses that follow.
- Any news or stories worth featuring.

## Content: Real vs Placeholder

| Page | Real | Still placeholder |
| --- | --- | --- |
| `index.html` | Logo, nav, footer contact block, quote CTAs | Hero positioning line, all three service blurbs, the stat strip (**"100%" and "24/7" still invented**; the years figure is now flagged), history and NASA teasers |
| `about.html` | Mike Pike as President; Bell Customer Service Facility + Repair Station #XRIR622K; Pearland Regional Airport | Company overview, mission, all three values, Mike's bio, two other team slots, every photo |
| `services.html` | Bell certification line; quote-only framing | The entire six-service list, all three "How Pricing Works" steps, the testimonial |
| `bell-service-center.html` | Repair Station #XRIR622K; Bell CSF status (business-card wording) | What the certification covers, how long it's been held, the ratings on the certificate. Page carries a standing trademark warning and an empty reserved badge slot |
| `platforms.html` | — | **Everything.** No aircraft model is named anywhere. Page carries a standing warning that the model list is unconfirmed |
| `history.html` | — | Every timeline entry including the founding year; the longer origin story |
| `nasa-partnership.html` | — | Everything. Page carries a standing pre-publication warning |
| `news.html` | — | All three article cards are format demos, not stories |
| `careers.html` | Phone and general email as the apply-to contact | Why-work-here cards, all openings (incl. whether there are any), resume inbox, EEO statement |
| `contact.html` | Address, phone, both emails, Google map embed | Airport identifier/coordinates; business hours; **the form doesn't submit anywhere** |

## Decisions Locked

- **Static HTML/CSS/JS, no framework** — a marketing site with no backend; keeps hosting free and hand-editing possible later.
- **Company name is plural: "South Air Helicopters, Inc."** — confirmed on Mike's business card. The repo name `SouthAirHelicopter` is singular and misleading; ignore it.
- **Logo is a two-mark system**, not one logo — a stacked badge for formal use, a three-blade rotor icon for small sizes, both from one shared blade profile. Approved by the user, *not yet by Mike*.
- **Wordmark carries the legal name** — "SOUTH AIR / HELICOPTERS, INC.", second line letter-spaced flush to the first.
- **Palette: navy `#0b2545`, steel blue `#2f7fb8`, amber `#f2a71b`** — carried from the user's original sketch. Amber appears once, on the hub rivet.
- **Placeholders stay visibly flagged** — dashed amber blocks, not plausible filler. Invented content reaching a real customer is the failure mode worth engineering against.
- **Nav is 8 items; History and Careers are footer-only** — 10 top-level links don't fit, and dropdowns aren't worth the CSS+JS+ARIA cost across 10 hand-copied files. History still has three inbound paths (homepage teaser, About's closing CTA, footer).
- **Nav collapses to the hamburger at 940px, not 860px** — the 8-item nav wraps below ~940px. If nav items are added or renamed, re-check where the wrap actually starts.
- **No published pricing** — quote-only is the category norm; both competitors do it. The old placeholder pricing table is gone, replaced by "How Pricing Works".
- **No aircraft model is named anywhere on the site** — until Mike confirms which airframes the shop is rated on, naming one is a claim a customer could make a maintenance decision on. There's an automated check for this (see below).
- **Structure follows `docs/market-research.md`** — the Bell page, the repeated quote CTA, footer certifications, and the airport identifier slot all exist because the competitor analysis says the category expects them.

## Constraints That Bite

- **Bell trademark.** South Air is an authorized Bell Customer Service Facility, but the Bell logo cannot appear without permission, and the copy must not imply Bell endorses the company. The badge sits *beside* the South Air logo, never merged into it.
- **NASA trademark and endorsement rules.** Same shape, stricter. NASA has explicit guidelines about vendors and contractors implying endorsement. Do not use the NASA logo. Get the relationship's wording confirmed in writing before that page goes live.
- **The founding year is unconfirmed and was asserted in ~14 places.** All in-page references are now wrapped in `[PLACEHOLDER Year]`, and the year was removed from `<title>`/`<meta>` tags entirely (placeholder styling can't reach those, and they leak into search results and link previews). Derived age claims — "27+ years", "nearly three decades" — went with it. **Don't put any age claim back until Mike confirms the year.**
- **Unverified claims on the homepage.** The stat strip still asserts "100% safety-first culture" and "24/7 support availability." Both were design filler, both are marked for verification, and both should be confirmed or removed before launch.
- **The repo is public.** Anything committed here is world-readable, including the client's contact details (already public on a business card) and any draft copy.

## Verification

There's no build step or test suite, so correctness lives in one script. Run it after any change touching the shared header/footer — copy-paste drift across 10 hand-edited files is this architecture's main failure mode.

`python3 tools/verify.py` checks: header and footer byte-identical across all 10 pages, 8 nav items each, every internal link resolves, **no aircraft model names anywhere**, no dead `.pricing-table` CSS, no Bell-branded image assets, every page carries placeholders, and no `.quote-strip` inside a `.section-alt` (where its fill would vanish).

## In Flight

Nothing half-finished, nothing open. Everything is merged to `main`, working tree clean, `tools/verify.py` green across all 10 pages.

Screenshots of all 10 pages at 1280px were reviewed on 2026-07-31 and are current as of `f053768`. Mobile (390px) has been spot-checked but not reviewed page by page.
