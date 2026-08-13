# Project Status

*Last updated: 2026-08-13 (local, eighth session — **the questionnaire came back from Mike**) · `main` at `e98e73a` · working branch `claude/coming-soon-page` · PRs #1–#3, #5–#8 merged · **PR #9 is open and carries the live landing page** — https://github.com/okurtenayhh/SouthAirHelicopter/pull/9 · **PR #4 is open as a draft** — a finished client questionnaire nobody has merged: https://github.com/okurtenayhh/SouthAirHelicopter/pull/4*

*Unmerged branches: `claude/coming-soon-page` (current — carries the landing page that is now **live on the client's domain**, the logo, the palette, and several sessions of tracker updates. **This branch is the live site; land it.**) · `claude/client-content-brief` (brief documents, pushed, no PR) · `claude/sphere-logo` (a logo exploration, local only, **now dead** — the logo is settled, see Decisions Locked)*

**Live preview (ten-page work-in-progress site): https://south-air-helicopters.netlify.app** — noindexed, **redeployed 2026-08-10 with the new logo**, verified live. Safe to send to Mike.

**🚀 LIVE: https://southairhelicopters.com** — the coming-soon landing page, on the real domain over HTTPS, as of **2026-08-10**. `www` redirects to the apex, `http` redirects to `https`, the Let's Encrypt certificate is issued, and the page is indexable (no `X-Robots-Tag`). Also still reachable at its Netlify subdomain, https://sah-coming-soon.netlify.app. **This is the first thing the public can find. Treat changes to it accordingly** — the deploy command and its trap are under Constraints That Bite. It is its own Netlify site, separate from the ten-page preview above: site id `de01967d-071f-433e-a5af-6e87b7870b22`, site name `sah-coming-soon`.

> Maintained by the `/sa-wrap-up` skill. If this file and the repo disagree, the repo is right — fix this file.

## Where This Stands

**🔑 The questionnaire came back on 2026-08-13, filled in by hand — and it is Mike
answering, not the office manager relaying him.** This is the largest single delivery of
real content the project has had, and it changes what is buildable more than anything
since the logo. Full verbatim transcription at **`private/client-answers-2026-08-13.md`**,
with the scan beside it. **`private/` is gitignored and must stay that way** — the repo is
public and his NASA answers are not publishable yet (see below).

What it unblocks, in rough order of value: **the aircraft ratings**, which have kept
`platforms.html` deliberately empty since it was built; **the founder's name and year**
(Robert H. Mitchell, 1979); **business hours** (8–5 M–F, with AOG callout); **the airport
identifier** (KLVJ); a **mission statement** and a **one-line description of the company**
in his own words; the **services list** corrected by his own hand; and replacements for
both unverified homepage claims. It also **closes the "Bell Helicopter" wording question**
that has sat on this list for four sessions.

**Two things in it need going back to him, and one of them is a stop sign.** The
**attached sheet** carrying the founding story and the history milestones is referenced
three times and **is not in the scan** — seven pages came through and all seven are the
questionnaire. And on NASA, asked whether NASA needs to review anything mentioning them,
he wrote **"PROBABLY"**; asked whether "partnership" is accurate, he wrote **"?"**. That
is the owner himself saying he doesn't know if this is publishable. `nasa-partnership.html`
is now blocked on a specific answerable question rather than on vague unease — which is
progress, but it is a harder block than before, not a softer one.

**Ten pages now, structurally complete.** The competitor research at `docs/market-research.md` was worked into the site: three new pages (`bell-service-center.html`, `platforms.html`, `careers.html`), a repeated Request-a-Quote CTA, certifications in the footer sitewide, an airport-identifier slot on Contact, and the placeholder pricing table replaced with a "How Pricing Works" section — MRO shops quote per job rather than publish rates.

So there is now a *place* for everything the category expects. What's in most of those places is still placeholder text, flagged in amber on the page. The gap is content, not structure.

**The site is deployed** to Netlify at a stable URL that can be refreshed as work lands.

Trademark research for Bell and NASA is written up in `docs/trademark-research.md` —
desk research to compare against what Bell and NASA actually say when asked.

**The homepage now leads with the Bell Customer Service Facility credential rather than
NASA.** That was the user's call, and it resolved the highest-liability item on the site
as a side effect: the unflagged "NASA / Partnership" stat tile is gone. **PR #8 is merged
and the fix is deployed and verified live** — the stale-preview warning that sat here for
two sessions is resolved.

**The content brief worked, and this is the evidence.** `claude/client-content-brief`
carries an internal master list plus two client-facing PDFs — a checklist of what to
collect and a fill-in questionnaire, every question traceable to a real placeholder in the
markup. It went out on 2026-08-04, produced a partial reply that month, and on 2026-08-13
came back filled in by the owner himself. **The approach is validated: ask in writing,
question by question, against a page they can see.** Reuse it for the follow-ups rather
than inventing a new format.

**The domain is `southairhelicopters.com`, bought through Squarespace and now pointed at
the landing page** (2026-08-10). The ten-page site stays on its noindexed preview URL until
the placeholder copy is replaced — it cannot go on a public, indexed domain as it stands.

**Bell answered — with the seal artwork and written co-branding rules (2026-08-06).**
Mike's CSF account rep, **Zachariah Langley**, emailed South Air unprompted with the CSF
seal, Bell's *Seal Signage Program* deck, and a link to Bell's brand portal. This was
an open ask on this list at the time, and it resolved itself. Authorization was never in question and now the
*rules* aren't either: the seal must be smaller than the company logo, never connected to
it, never redrawn, recoloured, rotated, or shadowed, and **the bare Bell shield may not
appear at all.** Full detail in `docs/trademark-research.md`, which is now primary source
material rather than desk research. Two consequences: the reserved badge slot on
`bell-service-center.html` is confirmed as the correct design, and the artwork we were
sent is print-only CMYK — **the proper web artwork still has to come from the brand portal,
and redrawing it ourselves is explicitly forbidden.** *(Since 2026-08-10 the seal is
published on the live landing page, converted CMYK→RGB for display; see Constraints That
Bite. The portal file replaces it when access lands.)*

**The landing page is live on the client's domain** — https://southairhelicopters.com, as
of 2026-08-10. **The office manager reviewed and approved the design** ("Looks good,
kiddo") — the project's first client sign-off, and a binding one: see Decisions Locked on
who actually approves things. She asked for two content changes, both made: the Bell CSF
credential verbatim, and `Established 1979` replacing a status line that turned out to be
factually wrong. **Since then it has also gained the new logo, the confirmed palette,
copy-to-clipboard email, a proper link-preview card, and a prominent Bell CSF block
carrying the seal Bell issued.** It is the only page in the project with no placeholders,
and now the only one the public can find.

**The logo is chosen and approved (2026-08-10).** The user handed over a five-variant set at
`C:\Users\kourt\Desktop\SAH LOGO\` and named **`south-air-5a.jpg` as the official mark** —
stacked, on a near-white ground: heavy slab-serif `SOUTH AIR`, a detailed grayscale
helicopter illustration, a navy band reading `HELICOPTERS`, and a rule-flanked
`PEARLAND, TX`. This closes the logo question that has been open since 2026-07-30 and
supersedes both the shipping two-mark system and the parked sphere exploration.

**The mark is now live on both sites** (2026-08-10). The user supplied the aircraft art
isolated on white, which made real assets possible, and the user's instruction was to
proceed with this logo. So the full set was rebuilt and deployed: header lockups, stacked
primary, icon, and favicon, in light and dark. **The ten pages needed no markup change** —
they already point at `images/logo-horizontal-light.svg`, so replacing the file in place
updated every page and left the shared header byte-identical. Regenerate any time with
`python tools/build_logo.py`.

**Two things about the artwork are worth being honest about.** The assets are **PNG
embedded in an SVG wrapper**, because both sources are raster — there is still no vector,
which matters for print, signage and embroidery but not for the web. And the **favicon
reads as a helicopter at 32px and as a vague shape below that**, which is the detail level
the source art allows.

**Nothing about the logo is blocked.** Both the office manager and Mike approved the mark,
and **Mike was told how it was made and okayed that too** — it is a Canva AI sketch of a
photograph the user was given. That closed the provenance question; don't reopen it. What
is left is ordinary production work: a **vector** for print and signage and a **stitchable**
version for the embroidery machine (Next Up item 4), plus Bell's answer on whether an
identifiable **429** may sit in South Air's own mark (item 3). Both under Constraints That
Bite, including why one regeneration from the existing text prompt would produce the
stitchable version and leave the approved wordmark and layout untouched.

## Next Up

Things that can move without waiting on anyone:

1. ~~**Build the answers into the site.**~~ **Done 2026-08-13, deployed and verified live.** Everything the questionnaire settled is on the page: `platforms.html` built from the confirmed ratings, both homepage stat claims corrected, `services.html` rebuilt to his markup, hours and KLVJ on Contact, the founder and the 1981 Bell designation on the timeline, what the CSF authorizes on the Bell page, and the factory-schools benefit on Careers. **What is left on each page is in the table below**, and almost all of it traces to the attached sheet, the certificate copy, or the NASA question. **The next build-only job is small**: unwrap the remaining `[PLACEHOLDER Year]` spans (item 5) and decide the tagline.
2. **Go back to him for the attached sheet, and settle NASA.** One short message, two asks. The **attached sheet** with the founding story and the history milestones was referenced three times and never arrived — it is the whole company-story section and the one thing competitors cannot copy. And **NASA needs a real answer**, because "PROBABLY" is not one: does the contract require NASA to review marketing that mentions them, and is "partnership" his word or ours? Send this *after* the pages above are built, so it goes with something to look at. Worth folding in the smaller gaps too — a copy of certificate #XRIR622K, which inbox is public, phone-or-form for quotes, and whether "Parts & Fleet Support" stays.
3. **Reply to Zachariah Langley at Bell, and request brand-portal access.** Bell opened the door on 2026-08-06 and explicitly invited questions, so this is now a reply rather than a cold ask — the hard part is done. Seven things are still outstanding and one message covers them all: the **Bell Seal Guidelines** document (referenced twice in the deck, not attached — it's where web rules live), **web-format artwork** (RGB vector or transparent PNG; Summit Aviation serves exactly such a file, so it exists), the exact authorized body-copy wording, whether we may name the 206/407/429, whether a footer attribution line is required, whether Bell wants to review the site pre-launch, and whether a recognizable Bell airframe may appear in South Air's *own* logo (the do-not list forbids shield lockups but is silent on aircraft, so this needs asking, not inferring). **That last question got sharper on 2026-08-10 and should lead:** the chosen mark does not contain a generic stylized helicopter, it contains a detailed rendering that reads as a specific Bell airframe — so this is no longer hypothetical, it is a question about the logo the company has actually adopted. The live list is at `docs/trademark-research.md` under "What Bell still hasn't answered." **Separately, request access at <https://brand.bellflight.com/> — but from a South Air address, not the user's.** Bell is vetting its own vendor network; a request from the facility they already emailed moves faster than one from a stranger.
4. **Get vector and stitchable versions of the logo.** The web assets are done and deployed; what is missing is a **vector** for print and signage, and a **reduced high-contrast version that can be stitched** — the current art is grayscale shading with hairline blades, which no needle will render. Regenerating the aircraft from the text prompt in `.recall/history.md` produces the stitchable version. **Not urgent, and not blocking anything.** ~~Identify the source image~~ — **closed 2026-08-10: Mike was told how the mark was made and okayed it.** See Constraints That Bite. **The web assets themselves are done and deployed** (`tools/build_logo.py` regenerates them); what is still missing is a **vector** for print, signage and embroidery, and a **reduced high-contrast version that can be stitched** — the current art is grayscale shading and hairline blades, which no needle will render. **Regenerating the aircraft to the 2026-08-06 prompt in `.recall/history.md` remains the move that pays off either way** — it produces the stitchable version *and* is the escape route if the licence answer is bad, since replacing the aircraft leaves the approved wordmark, band and layout untouched.
5. ~~**Finish propagating the founding year.**~~ **Done 2026-08-13.** 1979 now reads as real content on the homepage eyebrow, stats tile, history teaser and Bell section, on the About page, and as the first history timeline entry. **Three `[PLACEHOLDER Year]` spans remain and all three are in `history.html`** — they are *milestone* dates, not the founding year, and they are on the missing attached sheet, so they belong to item 2 rather than here. `tools/verify.py` guards the year sitewide: no derived age claim, no near-miss year. **Do not reintroduce an age claim** — a year is permanent, a computed age rots annually.
6. **Wire the contact form to a real handler.** Still the highest-severity *functional* item — a customer who fills it in today reaches nobody. Cheap now: the site is on Netlify, so **Netlify Forms** is a `data-netlify="true"` attribute plus a notification address, no third-party service and no backend. Blocked only on knowing which inbox submissions should go to. **Note this was asked twice on the questionnaire and left blank both times** — "should quote requests come in by phone, through a form, or both?" and "which email address should be the public one?". Neither is an oversight worth guessing past: pointing the form at the wrong inbox is worse than the form not existing, because it fails silently. Ask once more, plainly, and it is a ten-minute job.
7. **Land the open branches.** `claude/coming-soon-page` has **PR #9** open, carrying the built coming-soon landing page and last session's tracker commit. **This branch is what is actually serving the live domain** — `main` does not contain the landing page, so leaving it unmerged means the deployed site and `main` disagree. `claude/client-content-brief` is pushed with no PR — open one. **PR #4** (the older questionnaire, 50 questions plus a `.docx`) still needs a rebase; `PROJECT-STATUS.md` has now been rewritten several times since, so expect a conflict. Its content is superseded by the new PDFs, so merging it is optional — but decide deliberately rather than leaving it to rot.
8. ~~**Make the "Bell Helicopter" wording consistent.**~~ **Done 2026-08-13.** Mike settled it — *"It changed in 2018 but 60-70 ys of being Bell Helicopter, either is accepted"* — and the main site now uses Bell's current form throughout: the string "Bell Helicopter" appears nowhere in the ten pages, including the shared footer, which previously carried the retired form on every page. **The coming-soon page deliberately still uses the retired form** and is pinned to it by `verify.py`; that is a separate, twice-affirmed client decision. Don't re-raise the 2018 rebrand with him — he addressed it.
9. **Decide whether Careers ships.** It's built, but a careers page with no listed openings can read as a dead site. Every hiring question on the questionnaire came back blank except two, and both are usable: *"a great place to work"*, and — the genuinely good one — **the shop pays to send mechanics to factory schools after a year on staff**. That is a concrete benefit a competitor page doesn't have. Still not enough on its own; it needs an explicit "nothing right now" or a list, plus EEO wording and a resume inbox. Hold the page back until then.
10. **Lean into the personal/small-shop angle** in About and the homepage hero — named-owner warmth is the one thing neither Arrow Aviation nor Summit Aviation has. **The raw material for this is precisely what is on the missing attached sheet** (item 2), so it is blocked on one piece of paper rather than on a conversation. The *structure* is there and waiting.

## Waiting On The Client

*Substantially rewritten 2026-08-13 after the returned questionnaire. Everything it
answered has been deleted from this list rather than struck through — the answers live in
`private/client-answers-2026-08-13.md` and in the Real column below. What is left is only
what is genuinely still open.*

**Mike (owner / president)** — *he has now answered once, in writing, which is the
precedent worth using. He responds well to a specific written question next to a page he
can look at.*

- **The attached sheet.** Referenced three times on the returned form — the founding story, the milestones, and how public the ownership change should be — and not in the scan. **This is the single most valuable thing still outstanding**, because it is the only item on this whole list that a competitor could not also write.
- **NASA, and this one blocks a page.** He answered *what* the work is, *which* field, and *when* it started. He did **not** answer whether it can be published: asked if NASA needs to review anything mentioning them he wrote **"PROBABLY"**, and asked if "partnership" is the right word he wrote **"?"**. Needed before a word of `nasa-partnership.html` goes public: does the contract restrict what may be advertised, does NASA review it, and what does he want it called. See `docs/trademark-research.md` and the standing warning on the page.
- **A copy of FAA Repair Station certificate #XRIR622K.** He wrote **"MAKE COPY"**, so he intends to send one. It settles the ratings and any limitations from the source document rather than from memory.
- **His copy of the Bell Customer Service Facility agreement.** Bell publishes no third-party trademark policy, so the trademark clause in that contract is the actual governing text. Still the highest-value *document* outstanding, and unaffected by the seal arriving — the signage deck is not the licence.
- **Does "Parts & Fleet Support" stay?** The one service on the list he marked neither way, while marking every other one clearly.
- **A short bio, and whether anyone else goes on the team page.** Two slots sit open.
- **Phone, form, or both for quote requests** — see Next Up item 6; left blank.

**Office manager (the user's mother)**

*Her own sections are still the gap. The 2026-08-13 return answered Mike's questions, and
two of hers by side effect — hours, and the mission statement.*

- **Which inbox is the public "general inquiries" one.** Asked on the form, left blank. Blocks the contact form.
- Whether there are any current job openings — and if not, that's fine, `careers.html` should just say so. Plus the resume inbox and the EEO statement wording.
- Photos: hangar, aircraft, team, anything historical — or an afternoon at the hangar with a phone camera, which the form offered and which came back blank. **When these arrive, check each one for NASA facilities, NASA hardware, or identifiable NASA personnel** — those need clearing even though the photos are South Air's own. See `docs/trademark-research.md`.

**Either**
- Any news or stories worth featuring. Asked, blank. An empty news page is worse than no news page, so `news.html` waits.
- A tagline, if one exists. Asked, blank — and a perfectly fine answer, since we can write options.
- The Google Workspace email addresses that follow from the domain. Until they exist, the sbcglobal address stands. **⚠ When that happens, the DNS has a trap waiting.** `southairhelicopters.com` currently carries Squarespace's default email-hardening records: `TXT @` = `v=spf1 -all` (meaning *no server on earth is authorised to send mail as this domain*) and `TXT _dmarc` = `v=DMARC1; p=reject; sp=reject`, which tells receivers to reject anything that fails. That is correct for a domain that sends no mail, and it must be **updated before or as Workspace is set up** — otherwise every message sent from a `@southairhelicopters.com` address gets rejected, and it will look like Workspace is broken rather than DNS. Google publishes the SPF value to use; DKIM comes from the Workspace admin console.

**Action on the user, not the client**
- **The Squarespace account may carry a typo'd phone number.** A screenshot taken during the domain signup shows `281-684-5187`; the business card reads `281.648.5187`. The site has always had it right. Fix it at the registrar.
- ~~**Ask what "I'm working on getting the logo for you" means.**~~ **Answered 2026-08-06 — it meant the Bell account rep, which was exactly the right move.** She got Bell to send the seal directly. Worth telling her so; this was the single biggest unblock on the project and she did it without being asked.
- **Tell the office manager not to collect Bell media kit photos.** She offered; a media kit licenses press use, not a vendor's own commercial marketing site. Worth saying before she spends time on it.

## Content: Real vs Placeholder

> **Rebuilt 2026-08-13 after the answers were built in.** Everything the returned
> questionnaire settled is now on the page, deployed and checked over HTTP — so the left
> column is real again and the ✅ answered-but-not-built markers are gone, having lasted
> exactly one session, which is how long they should last. **What is in the right column
> now is genuinely still waiting on somebody**, and most of it traces to one of three
> things: the missing attached sheet, the promised certificate copy, or the unanswered
> NASA question.

| Page | Real | Still placeholder |
| --- | --- | --- |
| `index.html` | Nav, footer, quote CTAs, logo, **the whole stat strip** (1979 · Zero maintenance-related accidents since 1979 · Bell CSF · AOG response — no flags left in it), **the hero positioning line naming the confirmed airframes**, **all three service blurbs**, **the Bell section body** (warranty work, held since 1981, audits/training/tooling), **the history teaser** (founded 1979 by Robert H. Mitchell) | The certificate *ratings* (copy promised); the longer founding story (missing attached sheet); the NASA teaser, which is hard-blocked. Two photo slots |
| `about.html` | Mike Pike as President; Bell CSF + #XRIR622K; Pearland Regional Airport; **company overview**, **mission statement verbatim**, **the three values confirmed**, and Safety First / Precision described from his own answers | Reliability's description (he left it blank — worth one question, not invention); Mike's bio; two other team slots; every photo |
| `services.html` | **The corrected service list** — four confirmed plus a Bell Warranty Work card; Ground Support removed; charter gone (ground runs only); no fuel, no tie-downs. **All three quoting cards**, with no turnaround figure published. The owner's line in the callout | **Parts & Fleet Support** — the one service he marked neither way, still flagged. The certificate ratings. A customer testimonial (he says one could be got by asking) |
| `bell-service-center.html` | #XRIR622K; **what the CSF designation authorizes** (warranty work on new Bell aircraft and parts); **held since 1981**, kept by audits, factory training and tooling. **Now uses Bell's current name**, matching the homepage | The certificate ratings. The reserved badge slot, waiting on Bell's web artwork. The standing trademark warning stays |
| `platforms.html` | **Built.** 206 B/L/L-3/L-4 and 407/407GX/407GXi (field maintenance + component overhaul), 429 (field maintenance, inspection, airframe and engine), MD 500 C/D/E. An Engines & Avionics card carries the two exclusions: no engine overhauls in house, avionics through a shop on the field | Per-model notes (tooling, parts stocked). **The page still carries one flag: the list has not been checked against certificate #XRIR622K itself.** Verify before launch |
| `history.html` | **Two real timeline entries** — 1979, founded by Robert H. Mitchell; 1981, becomes a Bell CSF. **The NASA entry has been removed**, since it asserted a "partnership" he could not confirm | Three empty timeline slots and the origin story, all blocked on the missing attached sheet. How public the ownership change should be — same sheet |
| `nasa-partnership.html` | — | Everything, and **the block got harder on 2026-08-13**. The page now carries a do-not-publish warning quoting his own "PROBABLY" and "?". **The word "partnership" is stripped from the page, from the footer link on all 10 pages, and from the History CTA** — it is the exact framing he could not confirm. No NASA facts are in this repo |
| `news.html` | — | All three article cards are format demos, not stories |
| `careers.html` | Phone and general email as the apply-to contact; **factory schools after a year on staff** | Openings (incl. whether there are any), the resume inbox, the EEO statement, the day-to-day role, and a specific answer on shop size. **Still should not ship** |
| `contact.html` | Address, phone, both emails, map embed, **business hours (8–5 Mon–Fri) and the AOG line**, **airport identifier KLVJ** | The coordinates — take them off the FAA record, not from him. **The form still submits nowhere**, and both questions that would fix it came back blank. Note a pre-existing 5px horizontal overflow at 390px from the map iframe: measured before and after, not introduced by the content work |
| `coming-soon/index.html` — **LIVE at southairhelicopters.com**, separate site, not part of the 10-page site above | **Everything. The only page in the project with no placeholders** — legal name, address, confirmed phone number, FAA Repair Station #XRIR622K, the client-approved Bell CSF wording and Bell's own CSF seal, founding year 1979, the approved logo | None |

## Decisions Locked

- **Static HTML/CSS/JS, no framework** — a marketing site with no backend; keeps hosting free and hand-editing possible later.
- **Company name is plural: "South Air Helicopters, Inc."** — confirmed on Mike's business card. The repo name `SouthAirHelicopter` is singular and misleading; ignore it.
- **The logo is `south-air-5a.jpg` — chosen by the user on 2026-08-10 and approved the same day by both the office manager and Mike.** Built by the user: **helicopter art in Canva, composition in Claude Design** (see the licence caveat under Constraints That Bite before treating the aircraft as final). A stacked mark on a near-white ground: heavy slab-serif `SOUTH AIR`, a detailed grayscale helicopter illustration, a navy band reading `HELICOPTERS` in letter-spaced white, and a rule-flanked `PEARLAND, TX`. It delivers Mike's own brief — a helicopter, with the name in the mark — so it outranks everything below it. **The design is not to be reopened.** Source set of five variants: `C:\Users\kourt\Desktop\SAH LOGO\` (`5a`–`5e`); the other four share the same aircraft art on different grounds and layouts. **Deliberately not committed** — it is a flat JPEG that no page can use, and the aircraft's provenance is unconfirmed (see Constraints That Bite). **This is currently the only copy; move the folder somewhere durable before the Desktop gets tidied.**
- ~~**Logo is a two-mark system**~~ — **gone as of 2026-08-10.** The stacked badge and three-blade rotor icon have been replaced everywhere by the approved mark: all 7 `images/logo-*.svg`, `images/favicon.svg`, the mark **inlined** at `coming-soon/index.html:208`, and the **base64 favicon** at `coming-soon/index.html:9`. That list is the full set of places a logo change has to touch — keep it, since there is no templating layer.
- **The logo assets are PNG embedded in an SVG wrapper, deliberately** (2026-08-10). Both sources are raster, so there is no vector being thrown away; the wrapper exists so every existing `.svg` reference and file extension keeps working, which is why swapping the logo needed **zero markup change** across the ten pages and kept the shared header byte-identical for `verify.py`. It also satisfies the coming-soon page's self-contained guard, which already permits `data:` URIs on `<image>`. **When real vector artwork arrives, replace the file contents and the same trick still holds.** Regenerate with `python tools/build_logo.py`; it reads the two approved sources off the Desktop and writes all seven files.
- ~~The sphere exploration~~ — **dead, 2026-08-10.** Superseded by 5a. `claude/sphere-logo` is local-only and never pushed; delete it or leave it, but do not revive it. The one durable lesson, so nobody re-derives it: `SAH` cannot form a circle, because no letter in it has an arc to donate, and the only letter that does is the `O` in SOUTH.
- **Mike asked specifically for a 429, and the chosen mark's aircraft is one** — built to the 429's actual published dimensions, not a generic helicopter that happens to resemble one (see Constraints That Bite for how it was made). Recording this because it is the live risk in an otherwise settled decision, not to reopen the design. A Bell aircraft inside South Air's *own* logo asserts affiliation in a way the CSF seal does not: the seal says "authorized by Bell", a Bell aircraft in your mark says "we are Bell". Bell's do-not list forbids shield lockups and is silent on aircraft, so this is a question to ask, not a rule to infer — it is on the list for Zachariah at Next Up item 3. **If Bell objects, the fix is redrawing the aircraft to be generic, not abandoning the mark**; the wordmark, band and layout are unaffected either way.
- **The office manager is the approval channel, and her sign-off is the real one** (established 2026-08-04). She sees Mike in person and asks him directly, which no amount of emailing achieves. So "approved by the office manager" is not a lesser form of "approved by the owner" — it is how owner approval actually arrives on this project. **Stop holding work back waiting for Mike to review something himself.** Send it to her. Earlier sessions treated these as two separate gates and that was wrong; the practical effect was work sitting unapproved for weeks. The one thing still worth stating plainly when handing her something is what is unconfirmed in it, so she knows what to ask him.
- **The coming-soon landing page leads with contact information, not a "coming soon" teaser** (user's call, 2026-08-04). South Air is an operating shop, and someone who finds the page may need work done that week. A teaser implies the *business* is new and buries the phone number under an announcement nobody arrived for. Contact details are the page; the new-website line is a footnote. **Corrected the same day:** the page originally also stated it was "open and taking work." The office manager reviewed the staged page and flagged that the shop is at capacity ("we're full at the moment") — that status line was factually wrong, not a style choice, and was removed (including a second copy that had leaked into the meta description). It was replaced with `Established 1979`. The page makes no claim about current availability; it states who South Air is and how to reach them.
- **The landing page carries the Bell CSF status, verbatim as "Certified Bell Helicopter Customer Service Facility"** (reversed same day, 2026-08-04, at the user's explicit direction, after the office manager reviewed the staged page and asked for it). This reverses the same-day call, recorded earlier in this file, to hold Bell back and carry only the FAA Repair Station number until the account rep confirmed current wording. Two objections were raised before the reversal and should not need re-raising: "Helicopter" is a name Bell retired in 2018, and "Certified" appears nowhere on Mike's business card. The user was shown both and chose this wording anyway. **Not to be relitigated next session.** `tools/verify.py` now pins this exact string as the only permitted Bell mention on the page, so the wording cannot drift. The Repair Station number stays on the page too, alongside it, unchanged.
- **The landing page deploys as its own Netlify site, not as a route on the existing one.** A host-scoped rewrite in `netlify.toml` would have been one site and one deploy, but if that rule ever failed open the public domain would serve the unfinished, placeholder-riddled site. Two sites makes the worst case "the landing page is briefly wrong" instead. It also means `tools/verify.py` needs no weakening, since it globs the repo root only.
- **Wordmark carries the legal name** — "SOUTH AIR / HELICOPTERS, INC.", second line letter-spaced flush to the first.
- **Palette, confirmed against the company's own shirts 2026-08-04.** Navy `#0b2545`, royal blue `#3585cf`, white `#eef2f6`, with gunmetal `#3d4854`/steel `#7d8b99` as structural neutrals and safety orange `#f26722` as the single accent. The office manager: *"we use this blue and navy primarily"*; Mike, asked navy or lighter: *"navy is fine."* The royal was measured off a photo of a company shirt — hue 211°, saturation 0.73. **The old sketch palette was nearly right already**: its steel blue `#2f7fb8` is hue 205°, within six degrees of the real garment, so this is a nudge not a rewrite. **The amber `#f2a71b` is dropped** — it was the only invented colour in the project and the user rejected it, asking instead for complementary colours with a masculine, mechanical feel. Safety orange is hue 22° against the blue's 211°, so a true complement, and reads as equipment rather than gold. **Ask the office manager for the shirt's brand and colour name off the tag** — a garment spec beats sampling a photo taken under office lighting.
- **The chosen logo does not use the locked palette, and the logo wins on the mark itself** (measured off `south-air-5a.jpg`, 2026-08-10). Its actual colours are navy **`#1e3a5f`** (the `HELICOPTERS` band), a near-black **`#14171c`** (the wordmark), and an off-white ground **`#f2f2f0`**. Three divergences, all real: that navy is materially lighter and softer than the locked `#0b2545`; the wordmark black is a new value that is in no palette; and **the royal blue `#3585cf` and safety orange `#f26722` appear nowhere in the mark.** Do not silently recolour the logo to match the site — a logo is a fixed asset and the site is the flexible one. **Reconcile in this direction: take `#1e3a5f` as the true brand navy** (it is the one the client actually approved and the one that will be stitched), keep royal and orange as *site* accents that the mark simply does not use, and treat `#0b2545` as retired. This is a real edit to `css/style.css` and rides with the logo task, not before it.
- ~~Sitewide palette roll-out rides with the logo task~~ — **done 2026-08-10, both sites.** It was parked so the recolour happened once rather than twice, and the logo landing released it. **Navy is now `#1e3a5f`, the mark's own band colour**, not the older `#0b2545` — where the shirt reading and the logo disagreed the logo won, because a logo is a fixed asset and the site is the flexible one. The coming-soon page's `--navy` and `theme-color` moved with it, since a page background in a different navy from the logo sitting on it was the real inconsistency. **Amber `#f2a71b` is gone as brand**; safety orange `#f26722` is the single accent.
- **The palette needed three extra tints for contrast, and they are not decoration** (2026-08-10). Neither brand colour clears 4.5:1 for small text — orange on navy is 3.8:1, orange on white 3.1:1, royal on white 3.8:1. So fills and large type use the brand values, and `--color-accent-on-dark` (5.1:1), `--color-accent-on-light` (5.3:1) and `--color-sky-on-light` (6.8:1) carry links, eyebrows and captions. **Don't collapse them back into the brand values to "simplify" the palette** — that silently fails accessibility on every link and eyebrow. Button and nav-pill text also moved from navy to the logo's black `--color-ink`, taking those from 3.8:1 to 5.9:1.
- **Placeholder flags stay amber, under their own `--color-flag` names** (2026-08-10). They are a build-time warning, not brand. Now that the accent is orange they no longer read as a design choice, which is exactly what the flagging discipline wants — before this, amber placeholders sat in an amber-accented site and blended in.
- **The landing page's identity block is an aircraft data plate** (2026-08-04). Every certified aircraft carries a riveted plate stamped with its serial; South Air's Repair Station number **is** that kind of number, so stamping it on a machined panel is true to the content rather than decoration applied to it. This is where the "masculine mechanical" feel comes from — materials and typography — which keeps the accent colour doing exactly one job.
- **Email addresses copy to the clipboard rather than opening a mail client** (user's call, 2026-08-10). All 14 addresses — the shared footer on 10 pages, the two on `contact.html`, and the coming-soon page — carry a copy icon and flash a "Copied" chip. **The phone deliberately stays a real `tel:` link**, because tapping to dial is the most useful thing on the site for someone who needs work done that week. Built as progressive enhancement: they are still real `mailto:` links that JS upgrades, so they work with JS off, and a failed clipboard write falls back to opening the mail client rather than doing nothing. **The coming-soon page carries its own inline copy of the CSS and JS** — it has to stay self-contained, so that duplication is deliberate; change both if you change either.
- **Placeholders stay visibly flagged** — dashed amber blocks, not plausible filler. Invented content reaching a real customer is the failure mode worth engineering against.
- **Nav is 8 items; History and Careers are footer-only** — 10 top-level links don't fit, and dropdowns aren't worth the CSS+JS+ARIA cost across 10 hand-copied files. History still has three inbound paths (homepage teaser, About's closing CTA, footer).
- **Nav collapses to the hamburger at 940px, not 860px** — the 8-item nav wraps below ~940px. If nav items are added or renamed, re-check where the wrap actually starts.
- **No published pricing** — quote-only is the category norm; both competitors do it. The old placeholder pricing table is gone, replaced by "How Pricing Works".
- ~~**No aircraft model is named anywhere on the site**~~ — **the condition on this has been met (2026-08-13).** The rule was always explicitly conditional: no model names *until Mike confirms which airframes the shop is rated on*, because naming one is a claim a customer could make a maintenance decision on. **He has now confirmed, in his own handwriting, on the question that was marked IMPORTANT for exactly this reason.** So the models may be named, and `tools/verify.py`'s `MODEL_RE` guard comes off **as part of building `platforms.html`, not before** — dropping the guard while the page is still empty removes the protection and gains nothing. **Two things survive the change:** publish the *pairing* of model to authorized work rather than a bare model list, since "we're rated on the 429" and "we do field maintenance on the 429" are different claims and only the second is what he said; and **get the certificate copy anyway** (he wrote "MAKE COPY"), because a handwritten answer is a confirmation and a certificate is a source. Note his list is **wider than the office manager's** 2026-08-04 relay — it adds the 206 sub-variants, the 407 GX/GXi, component overhaul, and the MD 500 series, which is not a Bell airframe at all.
- **Returned client paperwork lives in `private/`, which is gitignored** (2026-08-13). Scans, transcriptions, anything in the client's own hand. **The reason is specific, not general caution:** the repo is public, and his NASA answers describe work he himself thinks NASA probably has to review before it is published. Committing them would publish them ahead of that review — precisely what the NASA discipline on this project exists to prevent. The rest of his answers are destined for a public website anyway, but they travel in the same document, so the whole document stays out. **Don't "tidy" this into `docs/`.**
- **His safety claim is published as a *floored* age, and the age rule was refined to allow it** (user's call, 2026-08-13). He wrote *"SAH has never had a maint. related accident in it's 47 yr. history"* — a real, specific claim, and far better than the invented "100% safety-first culture" it replaced. It is live as **"45+ · Years without a maintenance-related accident"**. **The reasoning is worth keeping, because it corrects a rule this project had slightly wrong:** what goes stale is an *exact* age — "47 years" is wrong next January. A *floor* does not. "45+" is true today and still true in ten years; it can only become understated, never incorrect. So `tools/verify.py` now blocks exact ages and permits explicitly floored ones (`45+ years`, `over 45 years`, `over four decades`), and **"almost"/"nearly"/"roughly" remain blocked** because they approximate an exact age rather than flooring it. **The cost is real but small:** a floor drifts from flattering to modest, so bump it every few years — that is a copy decision, not a correctness bug. **The coming-soon page deliberately keeps the original blanket rule**, floors included: it is the one page the public can reach and its whole job is "Established 1979", so the looser rule would buy nothing there and cost the guarantee.

- **"Bell Helicopter" and "Bell" are both acceptable, per the client** (2026-08-13). Asked directly, Mike wrote *"It changed in 2018 but 60-70 ys of being Bell Helicopter, either is accepted."* **This closes a question that has been reopened in four separate sessions.** The objection that Bell's own signage deck is actively retiring the old name is real and is recorded under Constraints That Bite — but it has now been put to the client, twice, and answered. **Stop raising it.** What remains is internal consistency only, at Next Up item 8.
- **Structure follows `docs/market-research.md`** — the Bell page, the repeated quote CTA, footer certifications, and the airport identifier slot all exist because the competitor analysis says the category expects them.
- **Hosting is Netlify, not GitHub Pages** — chosen over Pages because it needs no repo-owner action, gives a stable URL, and brings Netlify Forms, which makes the contact form (the top open item) nearly free.
- **The preview deploys to production, not draft URLs** — a stable link Mike can bookmark and refresh beats an unguessable one that changes every deploy. Search engines are blocked instead (`robots.txt` + `X-Robots-Tag`). Note the URL is public to anyone holding it; it is *not* access-controlled. Real restriction needs Netlify's paid password protection.
- **Internal docs are 404'd on the deploy** — `PROJECT-STATUS.md`, `README.md`, `docs/`, and `tools/` are blocked in `netlify.toml`, because the preview URL is a link handed to the client and these are candid working notes.
- **No `404.html` file** — `tools/verify.py` requires every `*.html` to carry the shared header/footer and 8 nav items, so adding one would fail the checks. Netlify's default 404 is fine.
- **The homepage leads with Bell, not NASA** (user's call, 2026-07-30). Bell CSF is a credential South Air holds and can document; the NASA relationship is unconfirmed, and NASA's own guidelines forbid endorsement framing. So the stronger *and* safer claim were the same one. NASA is now a supporting block below the fold, described as work performed rather than a "partnership" — the word "partnership" is what implies endorsement.
- **Bell's *corporate* logo is not the CSF seal, and only the seal goes on this site.** The corporate shield and 2018 wordmark say "we are Bell"; the CSF seal says "authorized by Bell." Summit Aviation, an actual CSF, displays the seal and not the corporate mark. **Bell confirmed this in writing on 2026-08-06** — the shield may not be used standalone or in a lockup, in Bell's own words. This is why `tools/verify.py` fails the build on any Bell-named image in `images/` — the guard is deliberate, don't disable it to make a page look finished.
- **The Bell badge, when it finally lands, is laid out to Bell's spec, not ours** (2026-08-06). Seal smaller than the South Air logo, ample clear space, physically unconnected, no rotation, no recolour, no drop shadow, Bell's own vector file. This is not a design preference to be traded off against page composition — it's the condition of using the mark at all. It also happens to match the reserved slot already built on `bell-service-center.html`.

## Constraints That Bite

- **The coming-soon site's deploy command is `netlify deploy --prod --cwd=coming-soon --dir=. --site=de01967d-071f-433e-a5af-6e87b7870b22`. This is the single most important operational fact from this session — get it wrong at go-live and the page stays unindexed while everyone believes it was published.** `--dir=coming-soon` run from the repo root does **not** change the CLI's working directory: the CLI stays rooted at the repo, so it reads the repo-root `netlify.toml` instead of `coming-soon/netlify.toml` and silently serves the wrong indexing header (or none). netlify-cli 26.0.2 has no `--config` flag to point at an alternate config file; `--cwd` is an undocumented global flag, found only by reading the CLI's source. `coming-soon/netlify.toml` carries this same warning in its own header comment — read it before running the command by hand. **Go-live means deleting the `[[headers]]` block in `coming-soon/netlify.toml` and redeploying with that same command — and it is not done until you verify it with a real HTTP request, not just a clean CLI exit.** Run `curl.exe -sS -D - -o NUL https://<url>/` against the live domain afterward and confirm **no `X-Robots-Tag` header comes back at all.** If the response instead carries the four-token value `noindex, nofollow, noarchive, nosnippet`, that is the *repo-root* `netlify.toml` answering — the deploy used the wrong command shape (missing `--cwd=coming-soon`, or `--dir=coming-soon` run from the repo root) and the domain is still noindexed even though the deploy reported success.
- **Bell trademark.** South Air is an authorized Bell Customer Service Facility, but the Bell logo cannot appear without permission, and the copy must not imply Bell endorses the company. The badge sits *beside* the South Air logo, never merged into it. Researched 2026-07-30: **Bell publishes no third-party trademark policy at all** — the governing terms are in Mike's CSF agreement. The reserved badge slot on `bell-service-center.html` is the right design; Bell issues CSF seal artwork to authorized facilities.
- **Bell's own rules are now in hand, and they are specific.** Superseding the business-card inference of 2026-08-04: Bell sent the seal and its *Seal Signage Program* deck on 2026-08-06. Binding constraints, verbatim from Bell — the company logo must be **the most prominent visual brand**; the seal must be **smaller than the company logo** with **ample clear space**; **never physically connect** your logo to the seal; and do not rotate, redraw, substitute fonts in, recolour, or add effects (drop shadows) to it. **The bare Bell shield may never be used as a standalone element or in a lockup** — that closes the Downloads-files question permanently. Two operational consequences: **the seal cannot be hand-built as an SVG** (redrawing is explicitly forbidden, so the badge slot waits on Bell's own vector file from the brand portal), and **the artwork we have is CMYK print JPEG on white** — unusable on the web as-is. Full text in `docs/trademark-research.md`.
- **The CSF seal is now published on the live landing page** (2026-08-10, at the user's direction). Inlined as a base64 PNG in `coming-soon/index.html`, converted from Bell's print CMYK to RGB for display — a medium conversion, not a recolour, which is what Bell's rule targets. Laid out to Bell's spec: smaller than the South Air mark, own white ground, ample clear space, physically separate, unaltered. **Replace it with the RGB/vector file when brand-portal access lands** (Next Up item 3) — better fidelity, and it removes the CMYK caveat entirely. The `images/` guard still blocks Bell-named files there, and the corporate shield remains forbidden outright.
- **The domain's DNS shape, recorded 2026-08-10 at go-live.** `southairhelicopters.com` is registered at **Squarespace** (active to 2029-07-31), and Squarespace is DNS host as well as registrar. Going live meant **deleting the "Squarespace Defaults" preset whole** — it carried four apex `A` records pointing at Squarespace's own IPs, a `www` CNAME to `ext-sq.squarespace.com`, and an `HTTPS` record whose `ipv4hint` named those same IPs. **All three had to go together**; leaving the `HTTPS` record alone is the easy mistake, since deleting the A records looks sufficient. Replaced with two custom records at 30-minute TTL: `A` `@` → **`75.2.60.5`** (Netlify's apex load balancer, resolvable from `apex-loadbalancer.netlify.com`) and `CNAME` `www` → `sah-coming-soon.netlify.app`. On the Netlify side the domain is the site's `custom_domain` with `www.southairhelicopters.com` as an alias. **The `_domainconnect` CNAME and the Email Security TXT records were left alone** — not website routing.
- **The Bell source folder is still not in the repo.** `C:\Users\kourt\Desktop\fwbellcsfbrandingmaterial (1)` — the two seal JPEGs and the *Seal Signage Program* deck. **Move it somewhere durable before the Desktop gets tidied**; it is currently the only copy, and Bell's brand portal is the only other source.
- **Bell is actively retiring the name "Bell Helicopter" from its network.** The issued seal reads "Customer Service Facility" / "CSF" — no "Helicopter", no "Certified". The deck instructs facilities to **remove existing Bell Helicopter signs at their own cost** and replace them. This does not change the coming-soon page's wording, which is a twice-affirmed client decision (see Decisions Locked) — but it upgrades the objection from an inference about Bell's 2018 rebrand to Bell's own current document. **Put it to the office manager once, factually, then drop it either way.**
- **The logo has to embroider.** The company bought a Brother embroidery machine and intends to make its own shirts once a mark is settled (2026-08-04) — so the mark is not a screen-only artefact. Embroidery cannot render gradients or hairlines, every colour is a thread change, and text below roughly 5mm cap height collapses into mush. This rules out fine detail in the mark. **The chosen logo has exactly this problem and it is now a production constraint rather than a design argument** (2026-08-10): the helicopter is rendered in continuous grayscale shading with hairline rotor blades, and neither survives a needle — at chest-pocket size it will stitch as a grey smudge with the blades dropped entirely. The mark does not need to change, but **a separate reduced stitch version has to exist**: solid fills only, no shading, thickened blades, a minimum stroke weight, and few enough colours to be practical thread changes. Treat the full-detail mark as print/screen-only. This lands with a shop owner in a way a trademark argument does not. Note the shirts' current serif wordmark is *not* settled identity — it predates any of this and will be replaced.
- **The delivered logo is a flat JPEG and nothing on the site can consume it** (2026-08-10). `south-air-5a.jpg` is 1160×822 RGB with an **opaque `#f2f2f0` ground baked in** — no transparency and no vector. Every logo slot on the site is light-on-navy, so dropping this in would put a pale grey rectangle in the header of all ten pages; and the favicon has to read at 32px, where a photorealistic helicopter is mud. **There is no way to ship the mark without going back to whatever produced it and getting the vector.** Do not work around this by tracing or upscaling the JPEG: an auto-trace of grayscale shading produces hundreds of junk paths, and hand-redrawing the aircraft is precisely the provenance question below.
- **The aircraft's provenance is settled as far as this project is concerned, and Mike has accepted it.** **How it was made (user, 2026-08-10):** started from **a photograph somebody took**, whose file the user was given; ran it through **Canva's AI to convert it to a sketch**; cleaned it up; composed the mark in Claude Design. **The user explained it to Mike and Mike okayed it.** That is the owner accepting a documented risk on his own business, which is his call and not the user's to relitigate. **Do not reopen this.** *(This file guessed the provenance twice before getting it straight — first as the project's own 2026-08-06 text prompt, then as a Canva stock element. Both retracted. The lesson worth keeping: record what the user says, not what the workflow looks like from outside.)*
  - **The one thing left unwritten is who took the photograph.** Recorded because it is the kind of thing that is easy to establish now and impossible in two years, not because anything is blocked on it. If it turns out to be a South Air photo, this is completely clean and the note can be deleted.
  - **If it ever needs redoing, the fix is cheap and already specified:** regenerate the aircraft from the **text** prompt in `.recall/history.md`, which inherits from no source image and also fixes the embroidery and favicon problems. **The approved wordmark, band and layout are untouched either way.**
- **The aircraft is an identifiable Bell 429**, which is the exact model `tools/verify.py:23` blocks from the markup. The guard is textual so an image slips past it, but the site would then *depict* a rating the shop has not confirmed and Bell has not been asked about. Unchanged by the provenance correction above, and still on the list for Zachariah at Next Up item 3.
- **The delivered aircraft does not meet the rendering constraints a good logo needs, and that is why it will not embroider** (2026-08-10). It is continuous grayscale shading with hairline blades, sitting skids-down. **There is already a written spec for the version that would work**, in `.recall/history.md` from 2026-08-06: *flat plain single-color background*, *two or three flat tones maximum*, *solid fills and clean edges, not photographic gradients*, and **"must read as one clean silhouette — recognizable if filled solid black"** — plus a full dimensioned feature list for the 429. **Lift that prompt rather than rewriting it**, and fix the one uncertainty it flags (it asserts a port-side tail rotor as an unverified inference — any clear photo of a 429 tail settles it). **This matters twice over now.** It is the cheap fix for the embroidery and favicon problems; and if the Canva licence question above lands badly, **a fresh generation is also the escape route** — it replaces the aircraft without touching the wordmark, band or layout, so the approved design survives intact.
- **Bell media kit photos are not usable on this site.** Offered by the office manager 2026-08-04. A media kit licenses press use — journalists writing about Bell. A Bell service vendor putting Bell's photography on its own commercial marketing site is a different use and is not covered by it. Same line as everything else here: the seal says "authorized by Bell", Bell's own photography says "we are Bell".
- **NASA: the logo is a settled no.** Not an open question anymore. The Insignia, worm, and Seal are protected under 14 CFR 1221 and NASA states they must not be used as branding on third-party websites. There is no permission path that changes this — stop re-litigating it. What *is* allowed is a **factual, specific** description of the work ("vendors are free to state that JPL is one of their customers, and to describe factually the services and products they provide"). What is prohibited: "NASA approved", "official NASA", and — verbatim on NASA's list — **"trusted by"**. So no trust/logo strip may ever include NASA. Also: no quotes attributable to NASA staff, which rules out a testimonial on that page. Full detail in `docs/trademark-research.md`.
- **The founding year is 1979** (confirmed by the user 2026-08-04; originally from the office manager, who offered "1979. Or 78, whatever Jeff said"). It is live on the coming-soon page. The main site still has it wrapped in `[PLACEHOLDER Year]` in ~14 places, and it was stripped from `<title>`/`<meta>` tags entirely — those need unwrapping, and the meta tags need it written back by hand, since placeholder styling never reached them. **Don't put any age claim back anywhere** — `tools/verify.py` already guards the coming-soon page against exactly that ("46 years" etc.), and the same guard should extend to the main site once the year lands there too.
- **The two unverified homepage claims are now adjudicated, and one of them was false** (2026-08-13). Both were design filler carried since the first build. **"24/7 support availability" is not true** — the shop is 8–5 Monday–Friday and will turn out for AOG, which is a real and better claim but is not the same claim. It has to come off; it is exactly the kind of thing someone calls at 2am expecting. **"100% safety-first culture" is replaced by something stronger and factual** — no maintenance-related accident since 1979, in his words. **Until the homepage is edited, the live-adjacent preview still carries a claim the owner has effectively contradicted**, so this is now a correction rather than a to-do. The fourth tile is "Bell / Customer Service Facility" and its wording is settled — see Decisions Locked.
- **NASA is now a harder block than it was, and the block is specific.** The 2026-08-13 return finally described the work: South Air assisted NASA's initial introduction to helicopters and its first flight, after completing the necessary inspections and repairs; it began in 2025 with the receipt of Bell TH-57s; the location is given as Ellington Field, with his own question mark. **But asked whether NASA needs to review anything mentioning them he wrote "PROBABLY", and asked whether "partnership" is accurate he wrote "?".** Treat that as a stop, not a shrug: the owner does not know whether this is publishable, so nobody else does either. **Nothing from that section goes on the site, or into the public repo, until he answers properly** — the detail is held in `private/` for that reason. This sits on top of the existing NASA rules, which are unchanged and are not the issue here: the logo is a permanent no, "trusted by" is prohibited outright, and only factual description of services is permitted. The new risk is different — it is *contractual*, about what he is allowed to advertise, and it is the one question `docs/trademark-research.md` flagged as center-specific and unanswerable from the outside.
- **Bell logo files are sitting in the user's Downloads and are the wrong asset — now settled, not merely suspected.** `Bell_Outline_black.png` (corporate shield) and `Bell_logo_2018.svg` (corporate wordmark) were logo-aggregator downloads, neither Bell-issued nor the CSF seal, and were deliberately not added. **Bell's own do-not list now forbids the bare shield outright** ("Do not create company logo or text lockups with the Bell shield or use it as a standalone element"), so this is no longer contingent on reading the CSF agreement. Delete them; there is no version of this project where they get used.
- **The repo is public.** Anything committed here is world-readable, including the client's contact details (already public on a business card) and any draft copy. `.recall/` (local session transcripts) and `.netlify/` are gitignored for this reason — **don't commit either.**
- **The no-model-names rule is self-imposed, not a Bell restriction.** Summit Aviation, a Bell CSF, names models freely. Once Mike confirms the shop's ratings, naming models is normal for the category — and `tools/verify.py`'s `MODEL_RE` check will need relaxing at that point. Until then it stays.

## Verification

**Three known gaps in these guards, deliberately left** (adjudicated 2026-08-04 after the
final review; recorded so nobody rediscovers them as new): the transposed-phone check
misses HTML-entity separators (`281&nbsp;684&nbsp;5187`), the age-claim check misses
numeric-decade and century phrasings (`over 4 decades`, `a quarter century`), and the
self-contained check misses single-quoted attributes (`<img src='...'>`). All three are
fail-open — a bad string could pass — but each needs an authoring style the page doesn't
use, and the page is one screen that gets read on every change. Close them if the copy
ever grows; don't treat them as regressions.

There's no build step or test suite, so correctness lives in one script. Run it after any change touching the shared header/footer — copy-paste drift across 10 hand-edited files is this architecture's main failure mode.

**The model-name guard changed shape on 2026-08-13 rather than being deleted** — see
Decisions Locked. `MODEL_RE` still blocks every model on the coming-soon page;
`UNCONFIRMED_MODEL_RE` guards the ten-page site and blocks only what ownership has *not*
confirmed — the 412, the 505, JetRanger, LongRanger, Huey, UH-1, and the TH-57, which is
in there because it is NASA material rather than because of any rating question. **Proven
both ways before committing**: the confirmed models pass, and injecting a 412 and a TH-57
into `platforms.html` failed the check.

`python tools/verify.py` is now **19 checks** (the header/footer loop emits two checks, one
per shared block, not one). **Two were added 2026-08-10 when the founding year landed:** no
age claim anywhere on the ten pages (previously coming-soon only) and no near-miss founding
year, which pins `1997`/`1978`/`1980` out of the markup after `1997` — a transposition of
the real year — sat in the placeholders for several sessions. The age guard caught its own
documentation on the first run, because the placeholder note spelled out the bad examples
literally; that is the check working, not a false positive. Eleven cover the 10-page site:
header and footer byte-identical across all 10 pages, 8 nav items each, every internal
link resolves, **no aircraft model names anywhere**, no dead `.pricing-table` CSS, no
Bell-branded image assets, every page carries placeholders, and no `.quote-strip` inside
a `.section-alt` (where its fill would vanish). Eight more guard the coming-soon landing
page specifically — it's outside the 10-page glob, so these are separate and tighter,
since it's the one page a member of the public will actually see before launch: the page
is self-contained (no external assets), the confirmed phone number is present and the
transposed screenshot variant (`281-684-5187`) is absent, no aircraft model name, the
client-approved wording `Certified Bell Helicopter Customer Service Facility` as the
*only* Bell mention on the page, the plural legal name, the founding year present, and
no derived age claim that would go stale.

## In Flight

**2026-08-13 — the questionnaire came back from Mike, and it is built.** One session, two
halves: receive and record, then build. The transcription is at
`private/client-answers-2026-08-13.md`, gitignored on purpose; every page it unblocked is
now written, committed and deployed.

**Shipped this session:** `platforms.html` rebuilt from the confirmed ratings (empty → the
best-sourced page on the site); both invented homepage stat claims replaced with true ones;
`services.html` corrected to his own markup, including removing charter entirely;
hours and KLVJ on Contact; founder and the 1981 Bell designation on the timeline; what the
CSF authorizes on the Bell page and the homepage; the factory-schools benefit on Careers;
the "additional certifications" placeholder removed from the shared footer on all ten pages
because he answered no; and the word **"partnership" stripped sitewide**.

**Verified, not assumed.** `verify.py` green at 19 before each commit. The retargeted model
guard was proven in both directions — confirmed models pass, an injected 412 and TH-57 fail.
Pages loaded in a real browser at 1280px and 390px, console clean. **The 5px horizontal
overflow on `contact.html` at 390px was measured against the pre-change file and is
pre-existing** — the map iframe, not the content work; recorded rather than quietly fixed
or quietly ignored. The preview was redeployed with the pinned site id and then checked
over real HTTP: the four confirmed airframes serving, no `24/7` or `100%` anywhere, no
"additional certifications" or "NASA Partnership" string, hours and KLVJ live, and the
preview still returning its four-token `noindex`.

**The safety claim was flagged for review and the user resolved it, improving the rule in
the process.** It is live as **"45+ · Years without a maintenance-related accident"**. The
first attempt rendered it as a year ("since 1979") to dodge the age-claim guard; the user
pointed out a floored age reads better and can simply be bumped every few years. That is
right, and sharper than the rule it replaced: a floor cannot go false, only understated.
`verify.py` now encodes that distinction — exact ages blocked, explicit floors allowed,
approximations still blocked — and was tested against 8 stale forms and 11 durable ones
before committing. **Full reasoning in Decisions Locked; the claim itself is unchanged and
is his.**

**The NASA page moved backwards on purpose.** It now carries a do-not-publish block quoting
his own "PROBABLY" and "?", and the timeline entry that asserted a partnership has been
deleted. No NASA fact from the questionnaire is anywhere in this repo.

**Next session.** **Item 2 is now the whole game**: one message asking for the attached
sheet and a real answer on NASA, plus the certificate copy, which inbox is public,
phone-or-form for quotes, and whether Parts & Fleet Support stays. Send it with the preview
link — he has just demonstrated he answers well against something he can look at. After
that, **PR #9** is still open and `main` still does not contain the live landing page.

**The landing page is live and public** at https://southairhelicopters.com, on its own
Netlify site (id `de01967d-071f-433e-a5af-6e87b7870b22`, name `sah-coming-soon`). Built
behind the `verify.py` guard described above and checked in a real browser at 390px, 760px
and 1280px, console clean.

Along the way, the plan's own architecture turned out to be wrong: the plan called for a
`coming-soon/_headers` file to set the noindex header, but the served header actually came
from the *repo-root* `netlify.toml` — `_headers` was a no-op. Left alone, the documented
go-live step ("delete `_headers`") would have done nothing, and the page would have stayed
unindexed while everyone believed it was published. Fixed by giving the subdirectory its
own `coming-soon/netlify.toml`, deployed with the `--cwd` flag documented under
Constraints That Bite. The spec's architecture diagram, which still named `_headers`, has
been corrected to match reality.

**Three unmerged branches.**

- `claude/coming-soon-page` — current, pushed, PR opens with this commit. Carries the
  built coming-soon landing page, the spec and plan, this tracker update, and **last
  session's tracker commit `6bb69ac`**, which was pushed on `claude/status-2026-07-30`
  with no PR and which an earlier version of this file failed to list. One PR lands
  all of it.
- `claude/client-content-brief` — pushed, **no PR opened**. Contains
  `docs/master-needs-list.md` (internal), plus the checklist and questionnaire in
  both `.html` source and `.pdf`. Touches no site file.
- `claude/sphere-logo` — **local only, never pushed, and now dead rather than parked**
  (2026-08-10). A logo spec, a generator (`tools/make_sphere_logo.py`), and a full
  alternative mark family, all superseded by the chosen `south-air-5a`. Safe to delete;
  the only thing worth keeping from it is the one-line lesson in Decisions Locked.

**PR #4 is still an open draft.** Its 50-question questionnaire has been superseded
by `docs/client-questions-form.pdf` on the brief branch, which covers the same ground
in a nicer form. Merging it is now optional; it needs a rebase either way.

**Nothing is uncommitted.** 2026-08-10 was a long build session: the 6 logo assets, all 10
pages, the coming-soon page, `css/style.css`, `js/main.js`, `tools/build_logo.py`,
`tools/verify.py`, `.gitignore` and this file. **Both sites were redeployed three times and
verified live each time.** `python tools/verify.py`: all 19 checks green.

**Live-verified after the final deploy**, by real HTTP request rather than a clean CLI
exit: navy `#1e3a5f` and accent `#f26722` serving in `css/style.css` with no `--color-amber`
left; the coming-soon page on the same navy in both its variable and its `theme-color`;
`Trusted Since 1979` present and no `1997` anywhere; the copy handler present in both
`js/main.js` and the coming-soon inline script; the deleted `logo-badge.svg` returning 404;
and the coming-soon page still returning the two-token `noindex, nofollow`.

**The homepage hero is now single-column** (2026-08-10, user's call). The flat cartoon
helicopter read as a different company from the detailed mark in the header, so it and the
`.hero-art` rules are gone. `.hero-copy` is capped at 760px rather than left to run the
full container width, so it reads as composed rather than as a two-column layout missing
its second column. **The hero is a natural home for a real photo or the video loop the
brief asks for** — that slot is now empty by choice, not by oversight.

**The palette is rolled out** — see Decisions Locked. Both sites are on navy `#1e3a5f` and
safety orange `#f26722`; the amber survives only as the placeholder flag colour.
`images/logo-badge.svg` was deleted as part of it: the old two-mark badge, orphaned when
the new logo landed and still carrying the retired navy.

**One trap worth knowing, because it cost time twice this session and looked like broken
code both times:** a browser holding a cached `css/style.css` or `js/main.js` shows the new
markup with the old rules. It presented first as a dead copy button and then as a copy icon
rendering at 300×150. Both were caching, not bugs — local and live both measured correct.
**Measure the computed style before believing a rendering bug**, and hard-refresh. The icons
now carry explicit `width="14" height="14"` so that particular failure can't recur.

**Still never done: a page-by-page look at the ten-page site in a real browser.** The
coming-soon page got exactly that treatment this session — the first page in the project
to. The ten-page site is still verified only by script and by reading markup; screenshots
at 1280px are several sessions stale for `index.html`, and mobile at 390px was only ever
spot-checked.

Redeploy the ten-page preview after any page change with
`netlify deploy --prod --dir=. --site=b2e4b62c-aa66-40cd-a818-e568464a67e6` from the repo
root. **The `--site` flag is not optional now that a second Netlify site exists.**
`.netlify/` is gitignored, so on a fresh clone there is no linked site to fall back on —
an unqualified `netlify deploy` prompts interactively for one, and answering
`sah-coming-soon` would push the unfinished ten-page site onto the URL the client's domain
will eventually point at. Pin the preview site id explicitly, the same way the coming-soon
command is pinned to its own site id. Redeploy the coming-soon page with the `--cwd`
command under Constraints That Bite — the two sites use different deploy commands and
mixing them up serves the wrong content or the wrong indexing header.
