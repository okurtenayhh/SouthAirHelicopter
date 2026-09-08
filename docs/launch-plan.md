# Launch Plan

*Drafted 2026-09-08. Supersedes nothing — this is the first written rollout plan.
`PROJECT-STATUS.md` remains the source of truth for what is real content versus
placeholder; this file is the source of truth for **the order things go public in
and what gates each step.***

---

## The shape of it

The site is nine pages once `news.html` is dropped. They do **not** all go live at
once. The domain moves off the coming-soon page in Phase 1 with three pages behind
it, and each later phase adds pages as their content is confirmed.

| Phase | Goes live | Gated on |
| --- | --- | --- |
| **1** | `index.html`, `services.html`, `contact.html` + **the domain** | A working contact route, and a decision on each Phase 1 placeholder |
| **2** | `about.html`, `history.html` | The founding story / milestones sheet; Mike's bio |
| **3** | `bell-service-center.html`, `platforms.html` | Copy of FAA certificate #XRIR622K; Bell's web-format seal artwork |
| **4** | `careers.html` | Whether there are openings; resume inbox; EEO wording |
| **5** | `nasa-partnership.html` | A real answer on whether the NASA work may be published, and in what words |

Phase 5 may never happen, and that is an acceptable outcome. The page exists; it
publishes only if the answer comes back yes.

**Newsworthy items no longer get their own page.** `news.html` is deleted (decided
2026-09-08). If stories ever arrive they become a section on the homepage rather
than a page that looks abandoned when empty.

---

## How a page goes from draft to live

One mechanism, used identically in every phase, so that "launch a page" is a small
and boring action rather than a judgement call each time:

1. **The page is 404'd until its phase.** `netlify.toml` gets an explicit redirect
   to 404 for every not-yet-launched page, exactly the way `docs/` and `tools/` are
   already handled. Launching a page = deleting its redirect block.
2. **The nav and footer only list live pages.** Trimmed in Phase 1 to Home,
   Services, Contact; each phase adds its pages back to the shared header and
   footer across every page. This stays a hand-edit across all files — there is no
   templating layer — so it must be followed by `python tools/verify.py`.
3. **A live page carries zero placeholders.** This inverts the current rule.
   `tools/verify.py` today asserts *at least three* `[PLACEHOLDER]` blocks per page,
   as a guard against invented content reaching a page. That guard is correct for a
   work-in-progress site and exactly wrong for a live one. It becomes two rules
   against an explicit `LAUNCHED` list in `verify.py`:
   - a page on the list: **zero** placeholders, or the check fails;
   - a page not on the list: **three or more**, as today.

   Adding a page to `LAUNCHED` is therefore the single act that both makes it
   public and makes the build refuse to ship it with unfinished copy.
4. **Search indexing follows the same list.** `robots.txt` and the site-wide
   `X-Robots-Tag` in `netlify.toml` currently noindex everything. At Phase 1 they
   become per-path: launched pages indexable, everything else still `noindex`.

The rule this encodes: **a placeholder is never resolved by writing something
plausible.** It is resolved by getting the answer, or by deleting the section it
sits in. Both are fine. Inventing is not.

---

## Phase 0 — before any page goes public

Work that has nothing to do with content and can be done at any time.

- **Wire the contact form to something real.** Highest-severity item on the site: a
  customer who fills it in today reaches nobody. See *Contact form* below — this
  needs a decision before it needs code.
- **Delete `news.html`**, remove it from the nav and footer on all pages, and drop
  the nav-count check in `verify.py` from 8 to whatever the trimmed nav holds.
- **Rework `verify.py`** for the `LAUNCHED` list as described above.
- **Add the 404 redirect blocks** to `netlify.toml` for the six pages not in Phase 1.
- **Take the coordinates off the FAA airport record** for Pearland Regional / KLVJ.
  This is a lookup, not a client question — it does not belong on any ask sheet.
- **Fix the registrar phone number.** The Squarespace account may carry
  `281-684-5187`; the business card reads `281.648.5187`. The site has it right.

---

## Phase 1 — Home, Services, Contact, and the domain

### Content that must be settled first

Sixteen placeholder blocks sit across the three pages. Each one has exactly three
possible resolutions: **fill** (the answer arrives), **cut** (the section is removed
for launch and can return later), or **defer** (the section stays but is rewritten
not to need the missing fact).

**`index.html`**

| Placeholder | Recommended |
| --- | --- |
| Founding story / milestones | **Cut for Phase 1** — it is the History teaser, and History is Phase 2 |
| Photo: hangar, team, or aircraft | **Fill** — needs one usable photo, or cut the slot |
| Photo: shop floor or Bell airframe | **Fill or cut** — same |
| FAA certificate ratings | **Cut from the homepage** — the ratings belong on the Bell page (Phase 3) |
| NASA teaser block | **Cut** — NASA is Phase 5 and unconfirmed for publication |
| Tagline | **Decide** — a tagline can be written; it does not have to be the client's |

**`services.html`**

| Placeholder | Recommended |
| --- | --- |
| Bell CSF seal slot | **Cut for Phase 1** — the seal has its home on the Bell page |
| FAA certificate ratings | **Cut** — same as above |
| "Parts & Fleet Support" card | **Ask** — the one service marked neither way. Keep or remove, one word |
| Quote route: phone, form, or both | **Ask** — but the form decision below may settle it |
| Customer testimonial | **Cut for Phase 1** — returns when a testimonial is obtained |
| Tagline | Same decision as the homepage |

**`contact.html`**

| Placeholder | Recommended |
| --- | --- |
| Airport coordinates | **Fill from the FAA record** — Phase 0, not a client question |
| Temporary email addresses | **Ask** — which inbox is public; blocks the footer on every page too |
| Form submits nowhere | **Fix** — see below |
| Tagline | Same decision |

Three of the sixteen are the same tagline placeholder repeated, and five are
recommended cuts that Phases 2–5 bring back. **The genuinely blocking set is small:
the public inbox, "Parts & Fleet Support" yes or no, at least one photo, and a
tagline decision.**

### The contact form

The form is the reason Phase 1 cannot ship on content alone. Two routes:

**Netlify Forms** — a `data-netlify="true"` attribute plus a notification address.
No third-party account, no backend, no DNS work; the notification email arrives
from Netlify's own sending domain. Free tier covers 100 submissions a month, which
is far above what this site will see.

**A Netlify Function calling Resend** — more control over how the email looks, and
it sends *as* the company's own domain. It needs a Resend account, a verified
sending domain, and an API key held as a Netlify environment variable.

⚠️ **If Resend is chosen, the DNS has a trap already waiting.** `southairhelicopters.com`
currently carries hardening records left by the registrar's default setup:
`TXT @` = `v=spf1 -all` and `TXT _dmarc` = `p=reject`. In plain terms, the domain
currently declares that *no server anywhere is authorised to send mail as it*, and
that receivers should reject anything that tries. Resend will appear configured and
its mail will still be rejected until those records are replaced with Resend's own
SPF and DKIM values. Netlify Forms is unaffected, because it never sends as the
domain.

**Recommendation: Netlify Forms for Phase 1.** It removes the blocker today with one
attribute. Resend becomes a Phase 2+ upgrade if branded email is wanted, at which
point the DNS work is a deliberate task rather than a launch-day surprise.

Either way it still needs **one answer: which inbox receives submissions.**

### The domain switch

`southairhelicopters.com` currently points at the `sah-coming-soon` Netlify site
(site id `de01967d-071f-433e-a5af-6e87b7870b22`). The three-page site is a
different Netlify site, currently at `south-air-helicopters.netlify.app`.

Order of operations, and it matters:

1. Deploy the Phase 1 build to the main site and **check it at its `.netlify.app`
   URL first** — every page, on a phone as well as a desktop.
2. Remove `southairhelicopters.com` and `www` from `sah-coming-soon`.
3. Add both to the main site. Netlify reissues the Let's Encrypt certificate; there
   is a window of a few minutes where HTTPS may fail. Do this at a quiet hour.
4. Confirm `www` → apex and `http` → `https` redirects survived the move. They were
   configured on the old site, not inherited.
5. Remove `robots.txt`'s blanket `Disallow: /` and the site-wide `X-Robots-Tag`,
   replacing both with the per-path form.
6. **Keep the coming-soon site deployed** at `sah-coming-soon.netlify.app` rather
   than deleting it. It costs nothing and is the rollback if the new site has a
   problem — the domain can be pointed back in minutes.
7. Load the real domain and confirm the launched pages resolve and the unlaunched
   ones 404.

---

## Phases 2–5

Each follows the same four steps: content confirmed → placeholders resolved → page
added to `LAUNCHED` → nav, footer and `netlify.toml` updated across every file →
`verify.py` → deploy → load the live URL and look at it.

**Phase 2 — About + History.** Both are blocked on the same thing: the founding
story and milestone dates. Three empty timeline slots on History and the origin
story are one document away from done. Also needs Mike's bio, a decision on whether
anyone else appears on the team page, and a one-line description for the third
company value. Launching these two together means one document unblocks a whole
phase.

**Phase 3 — Bell CSF + Platforms.** Blocked on a copy of FAA Repair Station
certificate #XRIR622K (for the ratings, from the document rather than from memory)
and on Bell's web-format seal artwork from the brand portal. The standing trademark
warnings on the Bell page stay until Bell's own written rules are in hand —
`docs/trademark-research.md` settles what is and is not allowed and should be
re-read before this phase, not re-litigated during it.

**Phase 4 — Careers.** Blocked on whether there are current openings, the resume
inbox, and the EEO statement wording. If there are no openings, the page says so
plainly — that is a fine answer and does not block the phase. The factory-schools
benefit is already confirmed and is the strongest thing on the page.

**Phase 5 — NASA.** Blocked on a real answer, not a probably: does the contract
restrict what may be published about the work, does NASA have to review marketing
that mentions them, and is "partnership" an acceptable word. Until then no NASA
detail enters this repo at all. If the answer is no, the page is deleted and the
rollout ends at Phase 4 — which is a complete site.

---

## Open decisions

- **Netlify Forms or Resend** for the contact form. Recommendation above.
- **404 redirects or a `drafts/` folder** for hiding unlaunched pages. The plan
  above uses redirects because it keeps every file at the repo root, so relative
  links and `verify.py` keep working unchanged. A `drafts/` folder is tidier but
  breaks both. Reversible either way.
- **Whether the tagline is written or waited for.** It came back blank, and it is
  the one open item that does not actually need the client.
