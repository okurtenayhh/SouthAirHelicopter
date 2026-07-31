# Project Status

*Last updated: 2026-07-31 · Branch `claude/new-session-cymw5g` · Commit `0de7416` · [PR #2](https://github.com/okurtenayhh/SouthAirHelicopter/pull/2) (draft, open) · PR #1 merged 2026-07-30*

> Maintained by the `/sa-wrap-up` skill. If this file and the repo disagree, the repo is right — fix this file.

## Where This Stands

PR #1 merged — the seven-page prototype is on `main`. All seven pages are built and styled, the logo family is done and wired in, and the real contact details are in. What the site does **not** have is real content: services, pricing, company history, the NASA and Bell specifics, and every photo are still placeholder text, clearly flagged in amber on the page.

The user also handed over a market research summary (competitor analysis of Arrow Aviation and Summit Aviation, plus category standards and differentiation angles) — now saved at `docs/market-research.md`. It's reference material for copywriting and structure, not yet worked into any page.

Nothing has been shown to Mike yet. The site isn't deployed anywhere — there's no live URL, so the only way to view it is locally or via the repo.

## Next Up

Things that can move without waiting on anyone:

1. **Wire the contact form to a real handler** (Formspree / Netlify Forms / similar). Right now a customer who fills it in reaches nobody. Highest-severity item on the site.
2. **Turn on GitHub Pages** so there's a shareable preview link — Settings → Pages → deploy from the working branch. This is a repo-owner action; Claude can't do it. Once live, everyone can watch progress by refreshing one URL.
3. **Draft the questionnaire for Mike and the office manager** — one page covering everything in *Waiting On The Client* below, so it can be answered in a single sitting rather than in fragments.
4. **Send Mike the logo board** for sign-off: https://claude.ai/code/artifact/55ef4406-1569-4a12-9bd7-e744d1ad8683
5. **Work the market research (`docs/market-research.md`) into the site**, once there's real copy to write against:
   - Add a repeated "Request a Quote" CTA — both competitors treat this as the norm instead of published pricing.
   - Consider a short Bell-authorization page/section separate from the general Services list — competitors give manufacturer certification its own page because it's the biggest trust signal in this industry. Mind the Bell trademark constraint below.
   - Lean into the personal/small-shop angle in About and the homepage hero — named-owner warmth is the one thing neither Arrow Aviation nor Summit Aviation has.

## Waiting On The Client

**Mike (owner / president)**
- Sign-off on the logo. The user approved it; Mike has not seen it.
- Exact scope of the NASA relationship, ideally in writing — which center or program, and what South Air actually does for them. See the standing warning on `nasa-partnership.html` before writing a word of this.
- Confirmed founding year. "1997 or so" is what we have; the timeline can't be published on a guess.
- What the Bell Customer Service Facility certification actually covers, plus the Bell logo file and permission to use it.
- Confirmed service list and real pricing. The current six services are generic helicopter-shop categories, not a confirmed offering.
- How public the recent change of ownership should be.

**Office manager (the user's mother)**
- Business hours.
- Company overview and mission statement for the About page.
- Which inbox is the public "general inquiries" one, and whether other staff should appear on the team page.
- Photos: hangar, aircraft, team, anything historical.

**Either**
- Domain name once purchased, and the Google Workspace email addresses that follow.
- Any news or stories worth featuring.

## Content: Real vs Placeholder

| Page | Real | Still placeholder |
| --- | --- | --- |
| `index.html` | Logo, nav, footer contact block | Hero positioning line, all three service blurbs, the "27+ / 100% / 24-7" stat strip (**invented — verify or delete**), history and NASA teasers |
| `about.html` | Mike Pike as President; Bell Customer Service Facility + Repair Station #XRIR622K; Pearland Regional Airport | Company overview, mission, all three values, Mike's bio, two other team slots, every photo |
| `services.html` | Bell certification line | The entire six-service list, the whole pricing table, the testimonial |
| `history.html` | — | Every timeline entry including the founding year; the longer origin story |
| `nasa-partnership.html` | — | Everything. Page carries a standing pre-publication warning |
| `news.html` | — | All three article cards are format demos, not stories |
| `contact.html` | Address, phone, both emails, Google map embed | Business hours; **the form doesn't submit anywhere** |

## Decisions Locked

- **Static HTML/CSS/JS, no framework** — a marketing site with no backend; keeps hosting free and hand-editing possible later.
- **Company name is plural: "South Air Helicopters, Inc."** — confirmed on Mike's business card. The repo name `SouthAirHelicopter` is singular and misleading; ignore it.
- **Logo is a two-mark system**, not one logo — a stacked badge for formal use, a three-blade rotor icon for small sizes, both from one shared blade profile. Approved by the user, *not yet by Mike*.
- **Wordmark carries the legal name** — "SOUTH AIR / HELICOPTERS, INC.", second line letter-spaced flush to the first.
- **Palette: navy `#0b2545`, steel blue `#2f7fb8`, amber `#f2a71b`** — carried from the user's original sketch. Amber appears once, on the hub rivet.
- **Placeholders stay visibly flagged** — dashed amber blocks, not plausible filler. Invented content reaching a real customer is the failure mode worth engineering against.

## Constraints That Bite

- **Bell trademark.** South Air is an authorized Bell Customer Service Facility, but the Bell logo cannot appear without permission, and the copy must not imply Bell endorses the company. The badge sits *beside* the South Air logo, never merged into it.
- **NASA trademark and endorsement rules.** Same shape, stricter. NASA has explicit guidelines about vendors and contractors implying endorsement. Do not use the NASA logo. Get the relationship's wording confirmed in writing before that page goes live.
- **Unverified claims on the homepage.** The stat strip currently asserts "27+ years", "100% safety-first culture", and "24/7 support availability." These were written as design filler. Two of them are marked for verification; all three should be confirmed or removed before launch — they're the kind of claim a customer could reasonably rely on.
- **The repo is public.** Anything committed here is world-readable, including the client's contact details (already public on a business card) and any draft copy.

## In Flight

Nothing half-finished. Working tree clean, all work pushed to the branch.
