# Launch Plan

*Rewritten 2026-09-08, replacing the earlier five-phase version. Locked with the user
in conversation on the same day.*

*`PROJECT-STATUS.md` remains the source of truth for what is real content versus
placeholder. This file is the source of truth for **what the site is, what order it
goes public in, and what has to be true before each step.***

**Nothing in this document has been implemented.** No page has been changed, deleted,
or moved; `tools/verify.py` and `netlify.toml` are untouched. This is the plan only.

---

## The site is five pages

**Home · Services · About · History · Contact**

Four pages were cut. That decision came from the client relationship, not from the
content: this is a small shop, the owner is not going to maintain a website, and a
thin page reads worse than no page. Nothing is lost — it relocates.

| Cut | Where its content goes |
| --- | --- |
| `news.html` | Nothing. Newsworthy items become a homepage section if any ever arrive; an empty news page reads as an abandoned business |
| `platforms.html` | **The top of Services.** The aircraft list is the most commercially useful content on the site, so it moves up in prominence, not down |
| `bell-service-center.html` | **About** — the CSF designation, FAA #XRIR622K, what it authorizes. The Bell warranty work stays as a Services card |
| `careers.html` | A line on Contact, or nothing. The factory-schools benefit is good but does not need a page |
| `nasa-partnership.html` | Deleted. This also removes the hardest unresolved problem on the project |

### Why the aircraft list leads Services

Research across a dozen-plus helicopter MRO sites nationally — Bell CSFs and
others — found one consistent pattern: **every shop leads with which models it is
approved on.** Helicopter Specialties advertises "33+ models"; Rotorcraft Support
publishes an explicit FAA-approved model list; CBH Aviation names "Bell 206B, 206L,
MD500." It is how an operator self-qualifies in about four seconds — *do you touch my
aircraft, yes or no.*

The industry's own stated selection criteria run: certifications, then model-specific
experience, then breadth of capability, then reputation. Company history appears
nowhere on that list — which is the argument for keeping History as its own quiet page
rather than letting the story colonise the front of the site. Nobody picks a shop
because of 1979. But 1979 is why they remember you.

*Caveat on that research: this environment blocks outbound page fetches, so it came
from search results rather than from reading the sites directly. The pattern was
consistent across independent sources; no single detail should be treated as verified.*

### AOG

AOG response is a category expectation — several comparable shops lead with it. South
Air does it. It is currently one line at the bottom of Contact and deserves a visible
callout on Home and Contact both.

**Wording is constrained.** The returned questionnaire gives hours as *"8-5 M-F, will
do AOG"* and left the 24/7 question blank. So: AOG response, yes. Around-the-clock
availability, no — not until someone confirms it.

---

## Two phases

**Phase 1 — Home · Services · Contact, and the domain switch**
The three pages a customer needs: who you are, what you do, how to reach you. This is
what turns southairhelicopters.com from a holding page into a real site.

**Phase 2 — About · History**
The company story. One body of work split across two pages — the founder, the
ownership chain, the people.

That is the whole rollout.

---

## Phase 1

### Before anything goes live

Three things have to be true, in this order.

**1. The site has to be in the company's Netlify account.**

It is currently on the user's personal account, along with the separate coming-soon
site. Netlify supports transferring a project self-serve — *Project configuration →
General → Project information → Transfer project* — provided you have Owner access on
the source and are an Owner or Developer on the destination. If the two teams share
nobody, it needs a support ticket, which is avoidable.

So: the company creates a Netlify team, adds the user to it, and the user transfers the
main site over.

**Do this before the domain switch, not after.** Right now the domain points at the
coming-soon site and the ten-page site is not serving it, so a transfer that goes
sideways is invisible to the public. Netlify's docs do not say whether the
`.netlify.app` subdomain, site ID, and deploy history survive a transfer intact —
doing it pre-launch makes that question harmless. Once the domain is pointed at it,
the same move is a live-site migration.

**2. The contact form has to reach somebody.**

It currently submits nowhere. A customer who fills it in today reaches no one — the
highest-severity item on the site, and it blocks Phase 1 on its own.

**Decided: a Netlify Function calling Resend.** Not Netlify Forms.

Three reasons, in order of weight:

- **Portability.** The function is code in this repo. It moves with the site to
  whatever host, under whoever's account. Netlify Forms ties the client's customer
  inquiries to a Netlify dashboard, and submission history is exactly the kind of
  thing that may not survive a team transfer.
- **Ownership.** With Forms, the client's leads sit in the user's personal Netlify
  account. With Resend, the account can be created under the company's email on day
  one and nothing is retained anywhere.
- **The DNS work is not Resend overhead.** Google Workspace email on this domain is
  already on the list, and it requires replacing the same SPF record. Resend's
  marginal cost is one DKIM record added while already in there.

⚠️ **The DNS trap.** `southairhelicopters.com` carries registrar-default hardening:
`TXT @` = `v=spf1 -all` and `TXT _dmarc` = `p=reject`. In plain terms the domain
currently declares that *no server anywhere may send mail as it*, and that receivers
should reject anything that tries. Resend will appear correctly configured and its
mail will still be rejected until those are replaced with Resend's own SPF include and
DKIM values. *(Read from a note taken during domain signup — confirm in the Squarespace
DNS panel before acting.)*

**Build in a visible failure path.** Resend stores nothing. If the API call fails the
inquiry is gone and nobody knows. The function must return an error the visitor
actually sees — "something went wrong, please call us" — rather than a false success.

Still needed from the client: **which inbox receives submissions.**

**3. The Phase 1 placeholders have to be resolved.**

Sixteen blocks across the three pages. Each resolves one of three ways: **fill** (the
answer arrives), **cut** (the section comes out and returns in a later phase), or
**defer** (rewrite the section so it no longer needs the missing fact). Filling one in
with something plausible is not on the list.

Most resolve to cuts now that the site is five pages — the certificate ratings, the
Bell seal slot and the NASA teaser belong to pages that no longer exist. Three are the
same tagline placeholder repeated, and a tagline can be written; it does not have to
come from the client.

**What genuinely blocks Phase 1 is four items:**

1. Which inbox receives contact-form submissions
2. Whether "Parts & Fleet Support" stays as a service — the one item never marked
   either way on the returned form
3. At least one usable photograph
4. Whether quote requests should come by phone, by form, or both

The airport coordinates are also outstanding, but those come off the FAA record for
Pearland Regional. That is a lookup, not a client question.

### The domain switch

Order matters.

1. Deploy the Phase 1 build and **check it at the `.netlify.app` URL first** — every
   page, on a phone as well as a desktop.
2. Remove `southairhelicopters.com` and `www` from the coming-soon site.
3. Add both to the main site. Netlify reissues the Let's Encrypt certificate; there is
   a window of a few minutes where HTTPS may fail. Do it at a quiet hour.
4. Confirm `www` → apex and `http` → `https` survived. They were configured on the old
   site, not inherited.
5. Replace `robots.txt`'s blanket `Disallow: /` and the site-wide `X-Robots-Tag` with
   per-path versions — launched pages indexable, About and History still noindex.
6. **Keep the coming-soon site deployed.** It costs nothing and it is the rollback: the
   domain can be pointed back in minutes.
7. Load the real domain. Confirm the three pages resolve and the unlaunched two 404.

---

## Phase 2 — About and History

Both are largely written and both now have real material.

**History** has eight datable events from the company-history note the client sent:
founded October 1979 by Robert H. Mitchell; Jeffrey P. Helton joins May 1980; Bell CSF
network 1981; MD 500 added through the 1980s; Helton buys the company February 2001 and
Mitchell retires after 22 years; 407 / 407GX / GXi in the early 2000s; Bell 429 in 2011;
Mike Pike becomes president around 2025.

Two cautions carried forward, both about accuracy rather than about the client:

- **The dates want one confirmation pass** before they are published. They were typed
  up quickly in answer to a question, not taken from a record, and a wrong date on a
  live timeline is the kind of thing a long-serving employee notices immediately.
- **Bell 47 and 222 appear in that note** as certifications gained in 1981. They are
  not on the site and they are not on any record we hold. They may belong on the
  timeline as history; they must not appear anywhere as current capability. The FAA
  certificate settles current ratings, and nothing settles historical ones.

**About** needs Mike's bio, a decision on the other two team slots, and descriptions
for the three company values — all three came back blank on the questionnaire, not
just one.

Still outstanding for both: how openly the ownership change should be described. That
question is not answered by the fact that a staff member described it in a note to us.

---

## The launch gate

One mechanism, so that launching a page stays a small boring action.

- **A `LAUNCHED` list in `tools/verify.py`.** A page on the list must carry **zero**
  placeholders or the check fails. A page not on the list still needs three or more,
  as today. Adding a page to that list is the single act that both makes it public and
  makes the build refuse to ship it with unfinished copy.
- **`netlify.toml` 404s the unlaunched pages** in production, matching the existing
  `docs/` and `tools/` pattern. Launching a page means deleting its redirect block.
- **Nav and footer list only live pages** — Home, Services, Contact at Phase 1, all
  five at Phase 2. There is no templating layer, so this is a hand-edit across every
  file, and `python tools/verify.py` runs after each one.
- Dropping `news.html` takes the nav from eight items to seven before that trim, and
  `verify.py`'s hard-coded count of 8 changes with it.

**Sequencing note.** The nav trim and the 404 redirects must land together, as one
change, on launch day. Doing either early strips pages out of the preview site the
client has the link to.

---

## Accounts and ownership

Things that should end up in the company's name, in order of how much it would hurt to
lose them:

1. **The domain.** This is the actual asset. Currently Squarespace, under the user's
   personal account. Worth sorting sooner than the rest, or at minimum getting in
   writing — moving a live domain is more stressful than moving a staging one.
2. **Netlify.** Per Phase 1 above, transferred before the domain switch.
3. **Resend.** Created under the company's email from the start, so it never needs
   moving.
4. **Google Workspace.** Theirs by definition, once it exists.

None of this blocks Phase 1 except the Netlify transfer, which is deliberately
sequenced into it.

---

## Still open

- **Which inbox** receives contact-form submissions — blocks the form.
- **"Parts & Fleet Support"** — stays or comes off.
- **At least one photograph.**
- **Phone, form, or both** for quote requests.
- **The tagline** — can be written rather than waited for.
- Client questions now route through **Kristina, the office manager**, who asks Mike
  and others as needed. The question document is drafted but not revised or sent.
