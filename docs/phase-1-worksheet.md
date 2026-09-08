# Phase 1 Worksheet — Home · Services · Contact

*Started 2026-09-08. This is the working document for Phase 1 and is meant to be
worked through together over several sessions, section by section, not executed in one
pass. `docs/launch-plan.md` says what the phases are; this says what actually has to
happen inside Phase 1.*

**Nothing here is implemented.** Every page is untouched.

How to read a row: **Have** is what is on the page now and confirmed. **Need** is what
is missing. **Source** is where the answer comes from — me, the user, Kristina, or a
document. A section with nothing in Need is finished.

---

## The three workstreams

Phase 1 is not one job. It is three that run in parallel, and the slowest is the one
that needs a person to walk around a hangar.

1. **Content** — section by section, below. Mostly resolvable without the client.
2. **Assets** — photographs. Nothing else on this list takes as long, so it starts first.
3. **Plumbing** — the page merges, nav, `verify.py`, the Resend function, the domain
   switch. Needs nobody, can happen any time.

---

## Workstream 2 first: the photo list

This is the long pole and it should be requested before anything else is settled. Every
slot below is a real hole in a Phase 1 page.

| Where it goes | What it needs to be | Priority |
| --- | --- | --- |
| Home — hero-adjacent slot | The hangar, or an aircraft outside it. The one image that says "this is a real place" | **1** |
| Home — second slot | The shop floor mid-work, or a Bell airframe in for service | **2** |
| Services — aircraft section | Optional but strong: a helicopter actually being worked on | 3 |
| Contact — optional | The building from the road, so someone can find it | 4 |

Shooting notes worth passing on: horizontal, highest quality setting, sent as originals
rather than texted (texting shrinks them past use). Real photos only. Check tail numbers
before publishing anyone's aircraft — a tail number identifies its owner.

**If no photos arrive, Phase 1 still launches** — the slots get cut and the pages read
as deliberately text-led rather than unfinished. That is a fallback, not the plan.

---

## Home (`index.html`)

| Section | Have | Need | Source |
| --- | --- | --- | --- |
| Hero — "Keeping Helicopters Flying, Safely and On Schedule" | Eyebrow, headline, and a subhead naming the confirmed airframes | Nothing factual. **Open question of taste:** the headline is competent but generic, and the small-shop angle is the one thing competitors can't copy | Discuss |
| Stat strip | 1979 · 45+ years no maintenance-related accident · Bell CSF · AOG | **Decide 45+ vs 47.** The returned form says "never had a maint. related accident in it's 47 yr. history." 45+ is floored so it never goes stale; 47 is what they said | Decide |
| "Full-Service Helicopter Support" — three blurbs | Maintenance & Repair, Inspections & Safety Checks, Avionics & Systems. All three confirmed, including the engine and avionics exclusions | Nothing | — |
| Quote CTA strip | Copy and phone number | Nothing | — |
| "A Legacy Built on Trust" | Founded 1979 by Robert H. Mitchell; Bell CSF since 1981 | The longer story is a placeholder, **and this section links to History, which isn't live until Phase 2.** Either cut it for Phase 1 or keep two sentences with the link removed | Decide |
| Two photo slots | — | Photos | Kristina |
| "A Bell Customer Service Facility" | What the designation authorizes, held since 1981, audits/training/tooling, cert #XRIR622K | Cut the certificate-ratings placeholder. **Repoint the "Our Bell Authorization" link** — its target page is being folded into About | Me |
| "Supporting Work Alongside NASA" | — | **Delete the whole section.** The page it links to is gone | Me |
| Final CTA | Copy | Nothing | — |

---

## Services (`services.html`) — after the Platforms fold

The biggest change in Phase 1. Platforms content moves in **above** the service cards,
because the models list is how an operator self-qualifies.

| Section | Have | Need | Source |
| --- | --- | --- | --- |
| Hero — "What We Offer" | Fine | Nothing | — |
| **NEW: Aircraft We Work On** *(from Platforms)* | Bell 206 B/L/L-3/L-4 — field maintenance and component overhaul. Bell 407/407GX/407GXi — same. Bell 429 — field maintenance including airframe and engine inspection. MD 500 C/D/E — field maintenance. Plus the exclusions: no engine overhauls in house, avionics through a shop on the field. Plus "not listed? ask anyway" | Four `[model-specific note]` placeholders — tooling held, parts stocked, typical work. **Cut them**, or ask Kristina for one line per airframe. Cutting is fine; the list already answers the question that matters | Decide |
| Services provided | Scheduled Maintenance · Airframe & Engine Repair · Avionics & Systems · Pre-Purchase & Annual Inspections · Bell Warranty Work | **Cut Parts & Fleet Support** (see below). Cut the Bell seal slot — no artwork, and its home moved to About | Me |
| Quote CTA | Copy and phone | The phone-or-form placeholder **resolves itself** once the form works — the answer is both | Me |
| "How Pricing Works" | What to Send Us / What Happens Next / Talk to Us Directly | Check this against what they actually said: quotes need "scope of work to be performed"; quotes come back by "preferred method"; and **no turnaround figure is published**, because "we don't do a lot of quoting" | Me, then review |
| "What Sets South Air Helicopters Apart" | The owner's line | **Thin, and it's the most important section on the page.** Raw material exists: 47 years without a maintenance-related accident, three generations of long-term employees, outlived other Bell facilities in the region, small enough that you talk to the people doing the work, Bell is the forte | Draft together |
| Testimonial slot | — | Cut for Phase 1. They said testimonials "could be acquired if asked" — so it's an ask, not a wait | Kristina, later |
| CTA band | Fine | Nothing | — |

---

## Contact (`contact.html`)

| Section | Have | Need | Source |
| --- | --- | --- | --- |
| Hero | Fine | Nothing | — |
| Airport | Pearland Regional — KLVJ | **Coordinates**, off the FAA airport record. Not a client question | Me |
| Address | 17402 C.R. 127, Pearland, TX 77581 | Nothing | — |
| Phone | 281.648.5187 — confirmed off the business card | Nothing | — |
| Email | General `sahinc@sbcglobal.net`, Mike `mpikesahinc@att.net` | The "these are temporary" note is an **internal comment, not missing content** — the addresses are real and current. Cut the note; swap the addresses when Workspace exists | Me |
| Hours + AOG | 8–5 Mon–Fri, "we will turn out for AOG" | **Give AOG more visual weight** — it's a category expectation and it's currently a sentence at the bottom. Never say 24/7; that question came back blank | Me |
| Send a Message form | Name, email, phone, subject dropdown, message | **Wire to Resend.** Also review the dropdown: "Media / Press Inquiry" is probably dead weight for this business | Me |
| Map embed | Google Maps iframe | Known 5px horizontal overflow at 390px. Pre-existing, worth fixing while we're in here | Me |

---

## Decisions and questions this surfaces

**For the user (no client needed):**
- 45+ years or 47?
- Home hero headline — leave as is, or push it toward the small-shop angle?
- History teaser on the homepage — cut for Phase 1, or keep short and unlinked?
- Per-airframe notes on Services — cut, or ask for them?

**For Kristina (Phase 1 blocking):**
- **Photographs** — the list above. Longest lead time; ask first.
- **Which inbox** should website enquiries go to. *(Fallback exists: `sahinc@sbcglobal.net` is already published on the contact page, so the form can point there on day one and swap later. This does not have to block launch.)*

**For Kristina (cheap, not blocking):**
- Do you sell parts, or hold any ongoing fleet-support contracts? *(Deciding whether "Parts & Fleet Support" was ever a real service — it appears to have been our own starting guess, never confirmed.)*
- Any customer who'd give a short quote about working with you?

**To write, not to ask:**
- The tagline. One shared footer element; one decision covers all five pages. Came back blank and we agreed we'd write options.
- The "What Sets Us Apart" section, from confirmed material.

---

## Plumbing checklist (needs nobody)

- Delete `news.html`, `careers.html`, `nasa-partnership.html`
- Fold `platforms.html` into Services, `bell-service-center.html` into About, then delete both
- Nav and footer down to the live set; `verify.py`'s hard-coded count of 8 changes with it
- `verify.py` — add the `LAUNCHED` list and flip the placeholder rule for pages on it
- `netlify.toml` — 404 the unlaunched pages in production; per-path robots rules
- Netlify Function + Resend, with a visible failure path
- Transfer the site to a company-owned Netlify team **before** the domain switch

**The nav trim and the 404 redirects land together, as one change, on launch day.**
Either alone strips pages out of the preview the client has the link to.
