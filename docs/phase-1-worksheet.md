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
| Hero — "Keeping Helicopters Flying, Safely and On Schedule" | Eyebrow and headline. **The subhead currently names the airframes and has to be rewritten** under the no-models decision — it can lead with the Bell CSF and FAA credentials instead | **DECIDED 2026-09-08:** present Mike four options rather than picking one — he has no headline in mind, and choosing shapes the rest of the site's voice. They go on the client question doc. The subhead already carries the airframes, so the headline can carry character. See *Headline options* below | Mike, via Kristina |
| Stat strip | 1979 · Bell CSF · AOG | **DECIDED 2026-09-08:** the safety tile becomes **Zero** / *maintenance-related accidents since 1979*. Putting "Zero" in the number slot is what lands, it never goes stale, and "since 1979" carries the length of the record without a figure to maintain. 47 stays available in body copy | Done |
| "Full-Service Helicopter Support" — three blurbs | Maintenance & Repair, Inspections & Safety Checks, Avionics & Systems. All three confirmed, including the engine and avionics exclusions | **The Maintenance & Repair blurb names the 206 and 407 series** — strip the models under the no-models decision. The rest stands | Me |
| Quote CTA strip | Copy and phone number | Nothing | — |
| "A Legacy Built on Trust" | Founded 1979 by Robert H. Mitchell; Bell CSF since 1981; third generation of long-term employees | **DECIDED 2026-09-08:** keep the section, cut the long-story placeholder, and repoint the dead History link at Services — *"See what we do today →"*. The confirmed history reads as a complete short block on its own; no "check back later" framing, which advertises incompleteness the same way an empty news page does. In Phase 2 the CTA flips to the History page | Me |
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
| **NEW: What We Work On** *(from Platforms)* | The exclusions, which stay: no engine overhauls in house, avionics through a shop on the field. Plus "tell us the airframe and we'll tell you straight" | **DECIDED 2026-09-08: no individual aircraft models on the site, for now.** The per-model cards come out along with their four note placeholders. Someone with a helicopter should call or send the form and talk it through — a model list filters people out, and we cannot verify current ratings without the certificate anyway. `verify.py`'s blanket model-name ban (which still guards the coming-soon page) gets re-applied to the main site, reverting the August allowlist, so the check enforces this rather than relying on memory. **Tradeoff accepted:** search traffic for "Bell 407 maintenance Houston" is lost, and an operator can no longer self-qualify in seconds. A category-level line — Bell Customer Service Facility, other manufacturers too — would recover most of that without naming models, and remains available if we want it | Done |
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
- **Do you sell parts to operators?** *(Stocking or sourcing spares.)*
- **Do you hold any ongoing fleet-support contracts?** *(Tracking component times and planning maintenance across an operator's whole fleet, rather than job by job.)*

  These are two separate services and were bundled into one card, "Parts & Fleet Support" — which appears to have been our own starting guess and was never confirmed. **The card is cut from Phase 1.** If either answer is yes it comes back as its own card with a real description.
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

---

## Headline options for Mike

Ten, spread across distinct **vibes** rather than ten phrasings of one idea. He has no
headline in mind, so the useful ask is not "pick a sentence" — it is **"which of these
sounds like your company?"** He can pick a vibe and we write into it.

None of these name an aircraft model, per the 2026-09-08 decision.

| | Headline | Vibe |
| --- | --- | --- |
| 1 | Helicopter Maintenance at Pearland Regional Since 1979 | **Plain and factual.** Says exactly what it is. Best for search |
| 2 | Forty-Seven Years. Zero Maintenance-Related Accidents. | **The record.** Bold, checkable, nobody else in the region can say it |
| 3 | The Same Shop, the Same Hands, Since 1979 | **Continuity.** The three-generations angle. Warm |
| 4 | Quality and Safety — and a History That Reflects It | **His own words.** Nearly verbatim from his mission statement |
| 5 | Tell Us What It Needs. We'll Tell You Straight. | **Plainspoken.** Sounds like a person, not a company. Direct address |
| 6 | Three Generations of Mechanics, One Hangar | **Craft and pride.** Leads with the people who do the work |
| 7 | The Shop Operators Keep Coming Back To | **Relationship.** Repeat business as the proof |
| 8 | A Bell Customer Service Facility Since 1981 | **Credential-forward.** Institutional, no personality, maximum trust signal |
| 9 | Back in the Air, On Schedule | **Practical / uptime.** Speaks to the thing an operator actually loses — flight hours |
| 10 | We've Been Keeping Helicopters Flying Since 1979 | **Understated.** Quiet confidence, no claim beyond the obvious |

**How to ask:** send all ten and ask which two or three *feel* like South Air, and
which feel wrong. The wrong ones are as useful as the right ones — a clear "not that"
narrows the voice faster than a lukewarm yes.

---

## Voice discovery — how we get Mike's actual voice

The problem: nothing on this site should be written in a voice invented for him, and
so far we have one confirmed sentence of his — the mission statement above. Everything
else came back as short factual answers, because that is what the form asked for.

**Recommendation: this should be a conversation, not another form.** Written
questionnaires have twice come back terse. Twenty minutes on the phone, or an hour at
the hangar, will produce more usable voice than a third document ever will. Record it
or take notes; the exact phrasings are the point.

Questions that work — concrete and story-shaped, never abstract. "What is your mission
statement?" gets nothing. These get paragraphs:

1. When someone at a party asks what you do, what do you say?
2. Why do customers come back? What do they actually tell you?
3. Tell me about a job you were proud of.
4. What do you turn away, and why?
5. What do people misunderstand about helicopter maintenance?
6. What would your longest-serving mechanic say about working here?
7. If a customer went to another shop instead, what would they be giving up?
8. What is the thing you will not compromise on?
9. Is there something you find yourself saying to customers over and over?
10. What would Mitchell or Helton have said about this place?

**What to do with the answers:** pull the phrases he actually used. A real sentence in
his voice beats a polished one in ours, and the tagline, the hero headline and the
"What Sets Us Apart" section can all be built out of his own words rather than
approximations of them.

**On the mission statement:** he did give one — *"Quality and safety is our priority
and our history reflects it."* It is short, it is his, and it is already on the About
page. The job is to confirm it is what he wants published and build around it, not to
invent one.

---

## Customer intake — what a new job actually looks like

Requested 2026-09-08. This is website content and a question set at once: it fills the
existing but thin **"What to Send Us"** and **"What Happens Next"** sections on
Services, and it is the single most useful thing a shop can put on a services page,
because it tells an operator whether calling is going to be easy or painful.

Nobody has been asked any of this. For Kristina:

**Before the job**
1. When someone calls about work, what is the first thing you ask them?
2. What do you need before you can put a quote together — make and model, serial
   number, total time, logbook status, a description of the work?
3. What paperwork should they have ready? Logbooks, airworthiness certificate,
   registration, previous 8130s, anything else?
4. Does it matter whether they are Part 91 or 135, and do you need to know that upfront?

**Getting the aircraft to you**
5. Do they fly it in, truck it in, or do you go out to it? Is that a choice?
6. How much notice do you usually need before you can take something in?
7. Is there anything they should do to the aircraft before it arrives?

**During and after**
8. Once it is here, how does a customer hear about progress — do you call, do they call?
9. What happens if you find something that was not in the original scope?
10. What does a customer get at the end — logbook entries, 8130s, a written scope?
11. How and when does payment work?

**The one that produces the best content**
12. What is the most common thing a customer forgets to bring, or gets wrong?

That last answer, published as a short "here's what to have ready" list, is worth more
to a real operator than any amount of marketing copy.

