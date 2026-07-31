# Project Status

*Last updated: 2026-07-30 (local, third session) · `main` at `e98e73a` · PRs #1–#3, #5–#8 merged · **PR #4 is open as a draft** — a finished client questionnaire nobody has merged: https://github.com/okurtenayhh/SouthAirHelicopter/pull/4*

*Unmerged branches: `claude/client-content-brief` (this session's brief documents, pushed, no PR) · `claude/sphere-logo` (a logo exploration, local only, parked — see Decisions Locked)*

**Live preview: https://south-air-helicopters.netlify.app** — noindexed, **deployed and current as of 2026-07-30**, verified live. Safe to send to Mike.

> Maintained by the `/sa-wrap-up` skill. If this file and the repo disagree, the repo is right — fix this file.

## Where This Stands

**Ten pages now, structurally complete.** The competitor research at `docs/market-research.md` was worked into the site: three new pages (`bell-service-center.html`, `platforms.html`, `careers.html`), a repeated Request-a-Quote CTA, certifications in the footer sitewide, an airport-identifier slot on Contact, and the placeholder pricing table replaced with a "How Pricing Works" section — MRO shops quote per job rather than publish rates.

So there is now a *place* for everything the category expects. What's in most of those places is still placeholder text, flagged in amber on the page. The gap is content, not structure.

**The site is now deployed** to Netlify at a stable URL that can be refreshed as work
lands. Nothing has been shown to Mike yet, but there is finally a link to show him.

Trademark research for Bell and NASA is written up in `docs/trademark-research.md` —
desk research to compare against what Bell and NASA actually say when asked.

**The homepage now leads with the Bell Customer Service Facility credential rather than
NASA.** That was the user's call, and it resolved the highest-liability item on the site
as a side effect: the unflagged "NASA / Partnership" stat tile is gone. **PR #8 is merged
and the fix is deployed and verified live** — the stale-preview warning that sat here for
two sessions is resolved.

**There is now a complete brief for collecting the missing content**, on the unmerged
branch `claude/client-content-brief`: an internal master list plus two client-facing PDFs
(a 4-page checklist of what to collect, and an 8-page fill-in questionnaire). Everything
in them traces to a real placeholder in the markup. **The two PDFs and the preview link
are what goes to Mike** — that package is now assembled and unblocked.

## Next Up

Things that can move without waiting on anyone:

1. **Send Mike the package — this is now fully unblocked and is the highest-value action.** Three things travel together: the preview link (deployed and current), `docs/client-checklist.pdf`, and `docs/client-questions-form.pdf`. Everything that previously blocked this is resolved. People answer far better against a page they can see, so the preview and the questions go in one message. Nothing else on this list moves the project as much, because almost every remaining item is waiting on answers only he has.
2. **Draft and send the Bell request email.** The user wants a Bell mark on the site and the only legitimate route to one is Bell's own CSF seal artwork. One message to Mike's CSF account rep (not the ethics hotline) covers all four open Bell questions: the seal artwork and co-branding rules, the exact authorized wording for our status, whether we may name the models we're rated on, and whether Bell wants to review the site pre-launch. Questions are already drafted at `docs/trademark-research.md:166-174`. **This is the unblock for four separate items on this page.**
3. **Wire the contact form to a real handler.** Still the highest-severity *functional* item — a customer who fills it in today reaches nobody. Cheap now: the site is on Netlify, so **Netlify Forms** is a `data-netlify="true"` attribute plus a notification address, no third-party service and no backend. Blocked only on knowing which inbox submissions should go to.
4. **Land the two open branches.** `claude/client-content-brief` is pushed with no PR — open one. **PR #4** (the older questionnaire, 50 questions plus a `.docx`) still needs a rebase; `PROJECT-STATUS.md` has been rewritten twice since, so expect a conflict. Its content is already superseded by the new PDFs, so merging it is optional — but decide deliberately rather than leaving it to rot.
5. **Correct the "Bell Helicopter" wording on `bell-service-center.html:41`.** Bell dropped "Helicopter" from the brand in 2018; the page echoes Mike's business card, which predates that. The homepage now says "Bell Customer Service Facility" (current form) while the Bell page says "Bell Helicopter Customer Service Facility" (retired form) — so the two pages currently disagree. Cheap to fix, but confirm against Bell's answer to item 2 rather than guessing.
6. **Decide whether Careers ships.** It's built, but a careers page with no listed openings can read as a dead site. Either get openings (or an explicit "nothing right now") from the office manager, or hold the page back until launch.
7. **Lean into the personal/small-shop angle** in About and the homepage hero — named-owner warmth is the one thing neither Arrow Aviation nor Summit Aviation has. Needs Mike's story, so it's half-blocked, but the *structure* for it is there now.

## Waiting On The Client

**Mike (owner / president)**
- Sign-off on the logo — but **hold this one.** The user approved the current mark, Mike has never seen it, and the user has since reopened the question. Don't put a logo in front of Mike until the user settles which one.
- Exact scope of the NASA relationship, in writing — which center or program, and what South Air actually does for them. Also: **does the contract require NASA to review marketing that mentions them?** (JPL requires it for its vendors; center-specific.) See `docs/trademark-research.md` and the standing warning on `nasa-partnership.html` before writing a word of this.
- **His copy of the Bell Customer Service Facility agreement.** Bell publishes no third-party trademark policy, so the trademark clause in that contract is the actual governing text. This is the single highest-value document still outstanding.
- Confirmed founding year. "1997 or so" is what we have. Every reference to it is now flagged as a placeholder, so this blocks more of the site than it used to — the homepage hero eyebrow, the years stat, and the History page all wait on it.
- **Which airframes the shop is rated on**, and what work is authorized per model. `platforms.html` is entirely empty until this lands, by design.
- What the Bell Customer Service Facility certification actually covers, and what ratings are on Repair Station certificate #XRIR622K.
- The **CSF seal artwork and co-branding guidelines** from his Bell account rep (not the ethics hotline — that's a compliance line, not a brand desk), plus confirmation of the exact current authorized wording. His business card says "Bell **Helicopter** Customer Service Facility"; Bell dropped "Helicopter" from the brand in 2018, so the site may be echoing a retired name.
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
- Photos: hangar, aircraft, team, anything historical. **When these arrive, check each one for NASA facilities, NASA hardware, or identifiable NASA personnel** — those need clearing even though the photos are South Air's own. See `docs/trademark-research.md`.

**Either**
- Domain name once purchased, and the Google Workspace email addresses that follow.
- Any news or stories worth featuring.

## Content: Real vs Placeholder

| Page | Real | Still placeholder |
| --- | --- | --- |
| `index.html` | Logo, nav, footer contact block, quote CTAs, **Bell CSF + FAA Repair Station status** (business-card sourced, now the hero's lead claim) | Hero positioning line, all three service blurbs, the stat strip (**"100%" and "24/7" still invented**; the years figure and the Bell tile's exact wording are flagged), the Bell section body, history and NASA teasers |
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
- **Logo is a two-mark system**, not one logo — a stacked badge for formal use, a three-blade rotor icon for small sizes, both from one shared blade profile. This is what the site ships today and what every page points at.
- **⚠ The logo is no longer settled.** The user reopened it on 2026-07-30 ("we're not set on the logo") and sketched an alternative: the company letters forming a sphere that reads as a bubble-canopy helicopter. That exploration lives on the local branch `claude/sphere-logo` — a spec, a generator, and a full mark family — and was **parked mid-flight at the user's request**. Nothing from it is wired into the site. **Don't restart it unless the user raises it.** If they do, the one thing worth knowing is already written down: `SAH` cannot form a circle, because no letter in it has an arc to donate, and the only letter that does is the `O` in SOUTH.
- **Wordmark carries the legal name** — "SOUTH AIR / HELICOPTERS, INC.", second line letter-spaced flush to the first.
- **Palette: navy `#0b2545`, steel blue `#2f7fb8`, amber `#f2a71b`** — carried from the user's original sketch. Amber appears once, on the hub rivet.
- **Placeholders stay visibly flagged** — dashed amber blocks, not plausible filler. Invented content reaching a real customer is the failure mode worth engineering against.
- **Nav is 8 items; History and Careers are footer-only** — 10 top-level links don't fit, and dropdowns aren't worth the CSS+JS+ARIA cost across 10 hand-copied files. History still has three inbound paths (homepage teaser, About's closing CTA, footer).
- **Nav collapses to the hamburger at 940px, not 860px** — the 8-item nav wraps below ~940px. If nav items are added or renamed, re-check where the wrap actually starts.
- **No published pricing** — quote-only is the category norm; both competitors do it. The old placeholder pricing table is gone, replaced by "How Pricing Works".
- **No aircraft model is named anywhere on the site** — until Mike confirms which airframes the shop is rated on, naming one is a claim a customer could make a maintenance decision on. There's an automated check for this (see below).
- **Structure follows `docs/market-research.md`** — the Bell page, the repeated quote CTA, footer certifications, and the airport identifier slot all exist because the competitor analysis says the category expects them.
- **Hosting is Netlify, not GitHub Pages** — chosen over Pages because it needs no repo-owner action, gives a stable URL, and brings Netlify Forms, which makes the contact form (the top open item) nearly free.
- **The preview deploys to production, not draft URLs** — a stable link Mike can bookmark and refresh beats an unguessable one that changes every deploy. Search engines are blocked instead (`robots.txt` + `X-Robots-Tag`). Note the URL is public to anyone holding it; it is *not* access-controlled. Real restriction needs Netlify's paid password protection.
- **Internal docs are 404'd on the deploy** — `PROJECT-STATUS.md`, `README.md`, `docs/`, and `tools/` are blocked in `netlify.toml`, because the preview URL is a link handed to the client and these are candid working notes.
- **No `404.html` file** — `tools/verify.py` requires every `*.html` to carry the shared header/footer and 8 nav items, so adding one would fail the checks. Netlify's default 404 is fine.
- **The homepage leads with Bell, not NASA** (user's call, 2026-07-30). Bell CSF is a credential South Air holds and can document; the NASA relationship is unconfirmed, and NASA's own guidelines forbid endorsement framing. So the stronger *and* safer claim were the same one. NASA is now a supporting block below the fold, described as work performed rather than a "partnership" — the word "partnership" is what implies endorsement.
- **Bell's *corporate* logo is not the CSF seal, and only the seal goes on this site.** The corporate shield and 2018 wordmark say "we are Bell"; the CSF seal says "authorized by Bell." Summit Aviation, an actual CSF, displays the seal and not the corporate mark. This is why `tools/verify.py` fails the build on any Bell-named image in `images/` — the guard is deliberate, don't disable it to make a page look finished.

## Constraints That Bite

- **Bell trademark.** South Air is an authorized Bell Customer Service Facility, but the Bell logo cannot appear without permission, and the copy must not imply Bell endorses the company. The badge sits *beside* the South Air logo, never merged into it. Researched 2026-07-30: **Bell publishes no third-party trademark policy at all** — the governing terms are in Mike's CSF agreement. The reserved badge slot on `bell-service-center.html` is the right design; Bell issues CSF seal artwork to authorized facilities.
- **NASA: the logo is a settled no.** Not an open question anymore. The Insignia, worm, and Seal are protected under 14 CFR 1221 and NASA states they must not be used as branding on third-party websites. There is no permission path that changes this — stop re-litigating it. What *is* allowed is a **factual, specific** description of the work ("vendors are free to state that JPL is one of their customers, and to describe factually the services and products they provide"). What is prohibited: "NASA approved", "official NASA", and — verbatim on NASA's list — **"trusted by"**. So no trust/logo strip may ever include NASA. Also: no quotes attributable to NASA staff, which rules out a testimonial on that page. Full detail in `docs/trademark-research.md`.
- **The founding year is unconfirmed and was asserted in ~14 places.** All in-page references are now wrapped in `[PLACEHOLDER Year]`, and the year was removed from `<title>`/`<meta>` tags entirely (placeholder styling can't reach those, and they leak into search results and link previews). Derived age claims — "27+ years", "nearly three decades" — went with it. **Don't put any age claim back until Mike confirms the year.**
- **Unverified claims on the homepage.** The stat strip still asserts "100% safety-first culture" and "24/7 support availability." Both were design filler, both are marked for verification, and both should be confirmed or removed before launch. The fourth tile is now "Bell / Customer Service Facility", flagged pending Bell's confirmation of exact wording.
- **Bell logo files are sitting in the user's Downloads and are the wrong asset.** `Bell_Outline_black.png` (corporate shield) and `Bell_logo_2018.svg` (corporate wordmark) were supplied this session; both look like logo-aggregator downloads, neither is Bell-issued, and neither is the CSF seal. They were deliberately **not** added. Bell publishes no third-party trademark policy, so the governing text is the CSF agreement Mike signed — which nobody here has read. If that agreement turns out to grant corporate-mark use, adding it is a five-minute change and the badge slot on `bell-service-center.html` already exists.
- **The repo is public.** Anything committed here is world-readable, including the client's contact details (already public on a business card) and any draft copy. `.recall/` (local session transcripts) and `.netlify/` are gitignored for this reason — **don't commit either.**
- **The no-model-names rule is self-imposed, not a Bell restriction.** Summit Aviation, a Bell CSF, names models freely. Once Mike confirms the shop's ratings, naming models is normal for the category — and `tools/verify.py`'s `MODEL_RE` check will need relaxing at that point. Until then it stays.

## Verification

There's no build step or test suite, so correctness lives in one script. Run it after any change touching the shared header/footer — copy-paste drift across 10 hand-edited files is this architecture's main failure mode.

`python3 tools/verify.py` checks: header and footer byte-identical across all 10 pages, 8 nav items each, every internal link resolves, **no aircraft model names anywhere**, no dead `.pricing-table` CSS, no Bell-branded image assets, every page carries placeholders, and no `.quote-strip` inside a `.section-alt` (where its fill would vanish).

## In Flight

**Two unmerged branches, neither of them urgent.**

- `claude/client-content-brief` — pushed, **no PR opened**. Contains
  `docs/master-needs-list.md` (internal), plus the checklist and questionnaire in
  both `.html` source and `.pdf`. Touches no site file.
- `claude/sphere-logo` — **local only, never pushed, deliberately parked.** A logo
  spec, a generator (`tools/make_sphere_logo.py`), and a full alternative mark
  family. The user stopped this mid-exploration and asked that it not be carried
  forward. It changes no site file and nothing points at it. Leave it alone.

**PR #4 is still an open draft.** Its 50-question questionnaire has been superseded
by `docs/client-questions-form.pdf` on the brief branch, which covers the same ground
in a nicer form. Merging it is now optional; it needs a rebase either way.

**Nothing is uncommitted.** No site page changed this session, so no redeploy was
needed — the deploy that *did* run (2026-07-30) was verified live: all 10 pages
return 200, the homepage no longer contains the unflagged NASA tile, local `main`
and the live homepage match apart from Netlify's pretty-URL rewriting,
`PROJECT-STATUS.md` / `README.md` / `docs/*` / `tools/*` return 404, and both
`X-Robots-Tag: noindex` and `robots.txt Disallow: /` were confirmed by request.

`python tools/verify.py` green across all 10 pages.

**Still never done: a page-by-page look in a real browser.** The site is verified by
script and by reading markup. Screenshots at 1280px are two sessions stale for
`index.html`; mobile at 390px was only ever spot-checked. The live URL makes a
real-device pass easy and it remains the most useful unglamorous task on this list.

Redeploy after any page change with `netlify deploy --prod --dir=.` from the repo root.
