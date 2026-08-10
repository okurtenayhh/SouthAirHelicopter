# Project Status

*Last updated: 2026-08-10 (local, seventh session) · `main` at `e98e73a` · working branch `claude/coming-soon-page` · PRs #1–#3, #5–#8 merged · **PR #4 is open as a draft** — a finished client questionnaire nobody has merged: https://github.com/okurtenayhh/SouthAirHelicopter/pull/4*

*Unmerged branches: `claude/coming-soon-page` (current — carries the built coming-soon landing page, now staged and live, plus last session's tracker commit) · `claude/client-content-brief` (brief documents, pushed, no PR) · `claude/sphere-logo` (a logo exploration, local only, **now dead** — the logo is settled, see Decisions Locked)*

**Live preview (ten-page work-in-progress site): https://south-air-helicopters.netlify.app** — noindexed, **redeployed 2026-08-10 with the new logo**, verified live. Safe to send to Mike.

**Coming-soon landing page (one page, built for the real domain): https://sah-coming-soon.netlify.app** — noindexed, staged, **redeployed 2026-08-10 with the new logo** (indexing header re-verified after the deploy: two-token `noindex, nofollow`, which is its own config answering, not the repo root's), **not attached to the client's domain — no DNS change has been made, and the page is not public and not indexed.** Its own Netlify site, separate from the preview above (which is untouched): site id `de01967d-071f-433e-a5af-6e87b7870b22`, site name `sah-coming-soon`.

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

**The questionnaire went to the office manager on 2026-08-04 and the first answers came
back.** None of them were from her own section — the site is still waiting on hours, the
company overview, the general-inquiries inbox, job openings, and photos. What did come
back was an aircraft-ratings answer belonging to Mike's section, a logo direction from
Mike, and the discovery that **the Bell CSF seal is printed on Mike's business card**.

**The domain has been purchased, through Squarespace.** That unblocked a real launch path
and created a near-term need: something for it to point at, since the full site is still
mostly flagged placeholder text and cannot go on a public, indexed domain.

**Bell answered — with the seal artwork and written co-branding rules (2026-08-06).**
Mike's CSF account rep, **Zachariah Langley**, emailed South Air unprompted with the CSF
seal, Bell's *Seal Signage Program* deck, and a link to Bell's brand portal. This was
Next Up item 3 and it resolved itself. Authorization was never in question and now the
*rules* aren't either: the seal must be smaller than the company logo, never connected to
it, never redrawn, recoloured, rotated, or shadowed, and **the bare Bell shield may not
appear at all.** Full detail in `docs/trademark-research.md`, which is now primary source
material rather than desk research. Two consequences: the reserved badge slot on
`bell-service-center.html` is confirmed as the correct design, and the artwork we were
sent is print-only CMYK — **web-format artwork still has to come from the brand portal,
and redrawing it ourselves is explicitly forbidden.**

**The coming-soon landing page is now built, deployed, and staged** at
https://sah-coming-soon.netlify.app — see the link above. **The office manager reviewed
it and approved the design** ("Looks good, kiddo") — the project's first client sign-off,
and a binding one: see Decisions Locked on who actually approves things. She also asked for two
content changes, both made: the page now carries the Bell CSF credential verbatim, and
the founding year `Established 1979` replaced a status line that turned out to be
factually wrong. Both are explained under Decisions Locked. No DNS points at the page yet.

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

**What remains is not an approval.** Both the office manager and Mike approved the mark.
Outstanding: the **Canva licence question** (Canva forbids stock content in a logo, so it
matters whether the aircraft is a stock element or Canva AI — Next Up item 4), Bell's
answer on whether an identifiable **429** may sit in South Air's own mark (item 3), and a
vector/embroidery version. All three are under Constraints That Bite, including why one
regeneration would fix the artwork *and* serve as the escape route if the licence answer
goes badly, leaving the approved wordmark and layout untouched.

## Next Up

Things that can move without waiting on anyone:

1. **Point the domain at the coming-soon page.** The page is finished, staged, and approved; the domain is bought and pointing nowhere. Two steps, in this order: remove the `[[headers]]` block from `coming-soon/netlify.toml`, redeploy with `netlify deploy --prod --cwd=coming-soon --dir=. --site=de01967d-071f-433e-a5af-6e87b7870b22`, then **confirm by real HTTP request that no `X-Robots-Tag` comes back at all** — if you see the four-token `noindex, nofollow, noarchive, nosnippet`, the wrong config was read and the page will never be indexed. Then the DNS records in Squarespace. **The exact domain string is still not written down anywhere** — get it first.
2. **Send Mike the package — this is now fully unblocked and is a very high-value action.** Three things travel together: the preview link (deployed and current), `docs/client-checklist.pdf`, and `docs/client-questions-form.pdf`. Everything that previously blocked this is resolved. People answer far better against a page they can see, so the preview and the questions go in one message. Nothing else on this list moves the project as much, because almost every remaining item is waiting on answers only he has.
3. **Reply to Zachariah Langley at Bell, and request brand-portal access.** Bell opened the door on 2026-08-06 and explicitly invited questions, so this is now a reply rather than a cold ask — the hard part is done. Seven things are still outstanding and one message covers them all: the **Bell Seal Guidelines** document (referenced twice in the deck, not attached — it's where web rules live), **web-format artwork** (RGB vector or transparent PNG; Summit Aviation serves exactly such a file, so it exists), the exact authorized body-copy wording, whether we may name the 206/407/429, whether a footer attribution line is required, whether Bell wants to review the site pre-launch, and whether a recognizable Bell airframe may appear in South Air's *own* logo (the do-not list forbids shield lockups but is silent on aircraft, so this needs asking, not inferring). **That last question got sharper on 2026-08-10 and should lead:** the chosen mark does not contain a generic stylized helicopter, it contains a detailed rendering that reads as a specific Bell airframe — so this is no longer hypothetical, it is a question about the logo the company has actually adopted. The live list is at `docs/trademark-research.md` under "What Bell still hasn't answered." **Separately, request access at <https://brand.bellflight.com/> — but from a South Air address, not the user's.** Bell is vetting its own vendor network; a request from the facility they already emailed moves faster than one from a stranger.
4. **Identify the source image behind the aircraft. This is the highest-priority item on the list.** The helicopter is a Canva AI **sketch of an existing image**, and image-to-image AI produces a derivative work — the sketch carries whatever rights the input carried. **Nobody has recorded what the input was**, and the mark is now live on both sites and headed for merchandise. Ask the user first; if they can't place it, a reverse image search on the source will. Full detail and the range of answers under Constraints That Bite. **If the answer is anything other than "a photo South Air owns," regenerate the aircraft from the text prompt in `.recall/history.md`** — text-to-image from measured dimensions inherits from nothing, and it fixes the embroidery and favicon problems at the same time. The approved wordmark, band and layout are untouched either way. **The web assets themselves are done and deployed** (`tools/build_logo.py` regenerates them); what is still missing is a **vector** for print, signage and embroidery, and a **reduced high-contrast version that can be stitched** — the current art is grayscale shading and hairline blades, which no needle will render. **Regenerating the aircraft to the 2026-08-06 prompt in `.recall/history.md` remains the move that pays off either way** — it produces the stitchable version *and* is the escape route if the licence answer is bad, since replacing the aircraft leaves the approved wordmark, band and layout untouched.
5. **Finish propagating the founding year — mostly done 2026-08-10.** **1979 is confirmed** (user, 2026-08-04). The wrong `1997` is gone everywhere and the year now reads as real content on the homepage eyebrow, the homepage stats tile (`1979 / Established`, replacing a "Years in Operation" tile that was a derived age claim) and the first history timeline entry. **`tools/verify.py` now guards this sitewide** — no age claim, no near-miss year. **Six `[PLACEHOLDER Year]` spans remain**, in `about.html`, `history.html` and `index.html`; they are mostly *other* dates (timeline milestones, "Since —" on the homepage's history teaser) rather than the founding year, **so check each one before unwrapping — not all of them are 1979.** The `<title>`/`<meta>` tags also never carried the year, since placeholder styling never reached them; write it in by hand if it belongs there. **Do not bring back derived age claims** ("46 years") when this lands — a year is permanent, a computed age rots annually. `tools/verify.py` already guards the coming-soon page against exactly that pattern; extend the same guard to the main site once the year lands there too.
6. **Wire the contact form to a real handler.** Still the highest-severity *functional* item — a customer who fills it in today reaches nobody. Cheap now: the site is on Netlify, so **Netlify Forms** is a `data-netlify="true"` attribute plus a notification address, no third-party service and no backend. Blocked only on knowing which inbox submissions should go to.
7. **Land the open branches.** `claude/coming-soon-page` has a PR open now, carrying the built coming-soon landing page and last session's tracker commit. `claude/client-content-brief` is pushed with no PR — open one. **PR #4** (the older questionnaire, 50 questions plus a `.docx`) still needs a rebase; `PROJECT-STATUS.md` has now been rewritten several times since, so expect a conflict. Its content is superseded by the new PDFs, so merging it is optional — but decide deliberately rather than leaving it to rot.
8. **Correct the "Bell Helicopter" wording on `bell-service-center.html:41`.** Bell dropped "Helicopter" from the brand in 2018; the page echoes Mike's business card, which predates that. The homepage says "Bell Customer Service Facility" (current form) while the Bell page says "Bell Helicopter Customer Service Facility" (retired form) — so the two pages disagree. Note the coming-soon page now deliberately uses the retired form too, but that was the client's explicit, overruled-objection choice for that one page (see Decisions Locked) — it doesn't settle what the main site should say. Confirm against Bell's answer to item 2 rather than guessing either way.
9. **Decide whether Careers ships.** It's built, but a careers page with no listed openings can read as a dead site. Either get openings (or an explicit "nothing right now") from the office manager, or hold the page back until launch.
10. **Lean into the personal/small-shop angle** in About and the homepage hero — named-owner warmth is the one thing neither Arrow Aviation nor Summit Aviation has. Needs Mike's story, so it's half-blocked, but the *structure* for it is there now.

## Waiting On The Client

**Mike (owner / president)**
- ~~Sign-off on the logo.~~ **Closed 2026-08-10 — approved by the office manager *and* by Mike.** `south-air-5a.jpg`, confirmed by the user. **Both named approvers, which is a first on this project** — every prior sign-off came through the office manager relaying Mike. Don't read it as a change in how approvals work (see Decisions Locked: her sign-off remains the working channel), but the logo specifically has the owner's direct approval and does not need re-confirming. It is also the mark he briefed, so this is him approving his own request.
- Exact scope of the NASA relationship, in writing — which center or program, and what South Air actually does for them. Also: **does the contract require NASA to review marketing that mentions them?** (JPL requires it for its vendors; center-specific.) See `docs/trademark-research.md` and the standing warning on `nasa-partnership.html` before writing a word of this.
- **His copy of the Bell Customer Service Facility agreement.** Bell publishes no third-party trademark policy, so the trademark clause in that contract is the actual governing text. This is the single highest-value document still outstanding.
- **Which airframes the shop is rated on**, and what work is authorized per model. `platforms.html` is entirely empty until this lands, by design. **Partially answered 2026-08-04** — the office manager reported by text that the shop is certified on the **206 series, 407 series, and 429**. Treat as unconfirmed: it came from the wrong person for this question, it has not been checked against the certificate, and it says nothing about *what work* is authorized per model. `tools/verify.py:23` still blocks those three strings from the markup and that guard stays until Mike confirms.
- What the Bell Customer Service Facility certification actually covers, and what ratings are on Repair Station certificate #XRIR622K.
- ~~The **CSF seal artwork and co-branding guidelines** from his Bell account rep.~~ **Delivered 2026-08-06 — this item is closed.** Zachariah Langley (CSF Network Manager, Americas) sent the seal and the signage rules directly. What replaces it is narrower and is now Next Up item 3: the Bell Seal Guidelines document, web-format artwork, and five factual answers. **His copy of the CSF agreement is still wanted** — see the item above — because the signage deck is not the licence.
- Confirmed service list. The current six services are generic helicopter-shop categories, not a confirmed offering.
- How quoting actually works — what he needs from a customer to quote, how the quote comes back, and typical turnaround. Fills the three cards on `services.html`.
- The airport identifier and heliport coordinates for Pearland Regional Airport.
- How public the recent change of ownership should be.

**Office manager (the user's mother)**

*She has the questionnaire as of 2026-08-04 and has started replying. Nothing below has
been answered yet — her replies so far were about Mike's items, not her own. Everything
in this list is still open.*

- Business hours.
- Company overview and mission statement for the About page.
- Which inbox is the public "general inquiries" one, and whether other staff should appear on the team page.
- Whether there are any current job openings — and if not, that's fine, `careers.html` should just say so.
- Whether resumes should go to a separate inbox rather than the general one, plus the EEO statement wording.
- Photos: hangar, aircraft, team, anything historical. **When these arrive, check each one for NASA facilities, NASA hardware, or identifiable NASA personnel** — those need clearing even though the photos are South Air's own. See `docs/trademark-research.md`.

**Either**
- **The exact domain string as registered.** The domain *was* purchased on or before 2026-08-04, through **Squarespace** (which absorbed Google Domains in 2023), but nobody has written down which name was bought. Needed before DNS can be pointed at anything.
- The Google Workspace email addresses that follow from the domain. Until they exist, the sbcglobal address stands.
- Any news or stories worth featuring.

**Action on the user, not the client**
- **The Squarespace account may carry a typo'd phone number.** A screenshot taken during the domain signup shows `281-684-5187`; the business card reads `281.648.5187`. The site has always had it right. Fix it at the registrar.
- ~~**Ask what "I'm working on getting the logo for you" means.**~~ **Answered 2026-08-06 — it meant the Bell account rep, which was exactly the right move.** She got Bell to send the seal directly. Worth telling her so; this was the single biggest unblock on the project and she did it without being asked.
- **Tell the office manager not to collect Bell media kit photos.** She offered; a media kit licenses press use, not a vendor's own commercial marketing site. Worth saying before she spends time on it.

## Content: Real vs Placeholder

| Page | Real | Still placeholder |
| --- | --- | --- |
| `index.html` | Nav, footer contact block, quote CTAs, **logo, founding year 1979 (eyebrow + stats tile)**, **Bell CSF + FAA Repair Station status** (business-card sourced, now the hero's lead claim) | Hero positioning line, all three service blurbs, the stat strip (**"100%" and "24/7" still invented**; the years figure and the Bell tile's exact wording are flagged), the Bell section body, history and NASA teasers. **The hero is now single-column** — the cartoon helicopter that sat beside it was removed 2026-08-10 |
| `about.html` | Mike Pike as President; Bell Customer Service Facility + Repair Station #XRIR622K; Pearland Regional Airport | Company overview, mission, all three values, Mike's bio, two other team slots, every photo |
| `services.html` | Bell certification line; quote-only framing | The entire six-service list, all three "How Pricing Works" steps, the testimonial |
| `bell-service-center.html` | Repair Station #XRIR622K; Bell CSF status (business-card wording) | What the certification covers, how long it's been held, the ratings on the certificate. Page carries a standing trademark warning and an empty reserved badge slot |
| `platforms.html` | — | **Everything.** No aircraft model is named anywhere. Page carries a standing warning that the model list is unconfirmed |
| `history.html` | **Founding year 1979** (first timeline entry) | Every other timeline entry, and what actually happened in 1979; the longer origin story |
| `nasa-partnership.html` | — | Everything. Page carries a standing pre-publication warning |
| `news.html` | — | All three article cards are format demos, not stories |
| `careers.html` | Phone and general email as the apply-to contact | Why-work-here cards, all openings (incl. whether there are any), resume inbox, EEO statement |
| `contact.html` | Address, phone, both emails, Google map embed | Airport identifier/coordinates; business hours; **the form doesn't submit anywhere** |
| `coming-soon/index.html` (staged, separate site — not part of the 10-page site above) | **Everything. The only page in the project with no placeholders** — legal name, address, confirmed phone number, FAA Repair Station #XRIR622K, the client-approved Bell CSF wording, founding year 1979 | None |

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
- **No aircraft model is named anywhere on the site** — until Mike confirms which airframes the shop is rated on, naming one is a claim a customer could make a maintenance decision on. There's an automated check for this (see below).
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
- **The Bell artwork is deliberately NOT in this repo.** The source folder is `C:\Users\kourt\Desktop\fwbellcsfbrandingmaterial (1)`. The repo is public, this is Bell's trademark artwork, and `tools/verify.py` fails the build on any Bell-named image in `images/` — that guard stays. **Move the folder somewhere durable before the Desktop gets tidied**; it is currently the only copy, and Bell's brand portal is the only other source.
- **Bell is actively retiring the name "Bell Helicopter" from its network.** The issued seal reads "Customer Service Facility" / "CSF" — no "Helicopter", no "Certified". The deck instructs facilities to **remove existing Bell Helicopter signs at their own cost** and replace them. This does not change the coming-soon page's wording, which is a twice-affirmed client decision (see Decisions Locked) — but it upgrades the objection from an inference about Bell's 2018 rebrand to Bell's own current document. **Put it to the office manager once, factually, then drop it either way.**
- **The logo has to embroider.** The company bought a Brother embroidery machine and intends to make its own shirts once a mark is settled (2026-08-04) — so the mark is not a screen-only artefact. Embroidery cannot render gradients or hairlines, every colour is a thread change, and text below roughly 5mm cap height collapses into mush. This rules out fine detail in the mark. **The chosen logo has exactly this problem and it is now a production constraint rather than a design argument** (2026-08-10): the helicopter is rendered in continuous grayscale shading with hairline rotor blades, and neither survives a needle — at chest-pocket size it will stitch as a grey smudge with the blades dropped entirely. The mark does not need to change, but **a separate reduced stitch version has to exist**: solid fills only, no shading, thickened blades, a minimum stroke weight, and few enough colours to be practical thread changes. Treat the full-detail mark as print/screen-only. This lands with a shop owner in a way a trademark argument does not. Note the shirts' current serif wordmark is *not* settled identity — it predates any of this and will be replaced.
- **The delivered logo is a flat JPEG and nothing on the site can consume it** (2026-08-10). `south-air-5a.jpg` is 1160×822 RGB with an **opaque `#f2f2f0` ground baked in** — no transparency and no vector. Every logo slot on the site is light-on-navy, so dropping this in would put a pale grey rectangle in the header of all ten pages; and the favicon has to read at 32px, where a photorealistic helicopter is mud. **There is no way to ship the mark without going back to whatever produced it and getting the vector.** Do not work around this by tracing or upscaling the JPEG: an auto-trace of grayscale shading produces hundreds of junk paths, and hand-redrawing the aircraft is precisely the provenance question below.
- **⚠ The aircraft is an AI sketch *of another image*, and the source image is unidentified. This is the most serious open item on the project.** **Provenance, as the user finally described it (2026-08-10):** they started from **an existing image**, used **Canva's AI to convert it to a sketch**, cleaned it up, and composed the logo in Claude Design. *(This file guessed twice before landing on that — first that the aircraft came from this project's own 2026-08-06 text prompt, then that it was a Canva stock element or a Canva text-to-image generation. Both are retracted. Record what the user says, not what the workflow looks like.)*
  - **Why it matters: image-to-image AI produces a derivative work.** Running a picture through a style filter does not reset its copyright, and neither does hand-cleanup afterwards. Whatever rights the input carried, the sketch inherits. Canva's own terms disclaim any guarantee that output is cleared and put responsibility on the user for what the image depicts.
  - **So the only question that matters now is what the input was**, and nobody has written it down. The plausible sources, worst to best: **the wall-art product listing** supplied with Mike's brief (someone's copyrighted line drawing — the 2026-08-06 session flagged it as style reference only, never a source); **a Bell marketing or press photo** (Bell's photography, and the media-kit constraint below already rules that out); **a licensed stock photo** (most stock licences separately prohibit trademark and logo use); or **a photograph South Air owns** — the only clean answer, and the one that ends this entirely.
  - **This is going on a public commercial site and onto merchandise the company intends to make.** That is the use least likely to be covered by any licence attached to the first three.
  - **The fix, if the answer is bad, is already specified and cheap.** Regenerate the aircraft from the **text** prompt in `.recall/history.md` — text-to-image from measured dimensions has no source image to inherit from, which is exactly why it is clean. It also fixes the embroidery and favicon problems. **The approved wordmark, band and layout are untouched either way**, so the mark survives; only the aircraft changes.
- **The aircraft is an identifiable Bell 429**, which is the exact model `tools/verify.py:23` blocks from the markup. The guard is textual so an image slips past it, but the site would then *depict* a rating the shop has not confirmed and Bell has not been asked about. Unchanged by the provenance correction above, and still on the list for Zachariah at Next Up item 3.
- **The delivered aircraft does not meet the rendering constraints a good logo needs, and that is why it will not embroider** (2026-08-10). It is continuous grayscale shading with hairline blades, sitting skids-down. **There is already a written spec for the version that would work**, in `.recall/history.md` from 2026-08-06: *flat plain single-color background*, *two or three flat tones maximum*, *solid fills and clean edges, not photographic gradients*, and **"must read as one clean silhouette — recognizable if filled solid black"** — plus a full dimensioned feature list for the 429. **Lift that prompt rather than rewriting it**, and fix the one uncertainty it flags (it asserts a port-side tail rotor as an unverified inference — any clear photo of a 429 tail settles it). **This matters twice over now.** It is the cheap fix for the embroidery and favicon problems; and if the Canva licence question above lands badly, **a fresh generation is also the escape route** — it replaces the aircraft without touching the wordmark, band or layout, so the approved design survives intact.
- **Bell media kit photos are not usable on this site.** Offered by the office manager 2026-08-04. A media kit licenses press use — journalists writing about Bell. A Bell service vendor putting Bell's photography on its own commercial marketing site is a different use and is not covered by it. Same line as everything else here: the seal says "authorized by Bell", Bell's own photography says "we are Bell".
- **NASA: the logo is a settled no.** Not an open question anymore. The Insignia, worm, and Seal are protected under 14 CFR 1221 and NASA states they must not be used as branding on third-party websites. There is no permission path that changes this — stop re-litigating it. What *is* allowed is a **factual, specific** description of the work ("vendors are free to state that JPL is one of their customers, and to describe factually the services and products they provide"). What is prohibited: "NASA approved", "official NASA", and — verbatim on NASA's list — **"trusted by"**. So no trust/logo strip may ever include NASA. Also: no quotes attributable to NASA staff, which rules out a testimonial on that page. Full detail in `docs/trademark-research.md`.
- **The founding year is 1979** (confirmed by the user 2026-08-04; originally from the office manager, who offered "1979. Or 78, whatever Jeff said"). It is live on the coming-soon page. The main site still has it wrapped in `[PLACEHOLDER Year]` in ~14 places, and it was stripped from `<title>`/`<meta>` tags entirely — those need unwrapping, and the meta tags need it written back by hand, since placeholder styling never reached them. **Don't put any age claim back anywhere** — `tools/verify.py` already guards the coming-soon page against exactly that ("46 years" etc.), and the same guard should extend to the main site once the year lands there too.
- **Unverified claims on the homepage.** The stat strip still asserts "100% safety-first culture" and "24/7 support availability." Both were design filler, both are marked for verification, and both should be confirmed or removed before launch. The fourth tile is now "Bell / Customer Service Facility", flagged pending Bell's confirmation of exact wording.
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

**Session of 2026-08-10 started documentary and ended as the biggest build session yet.**
The user handed over the logo set, named 5a as official, confirmed both approvals, supplied
the aircraft art isolated on white, and said to proceed. **Five things shipped, all live on
both sites:** the logo asset set, the confirmed founding year, copy-to-clipboard emails, the
hero cartoon's removal, and the palette roll-out. The source JPEGs are still **deliberately
not committed** — see Decisions Locked — but `tools/build_logo.py` is, so the assets are
reproducible.

**Verified, not assumed:** `verify.py` green at 19 checks; index, about, contact and
coming-soon loaded in a real browser at 1280px, 760px and 390px with a clean console; the
clipboard read back after a click to confirm it genuinely held the address; computed styles
measured rather than eyeballed; and every deploy re-checked over HTTP.

**The one thing that is entirely unresolved is the Canva licence question** — Next Up item
4. It is the only open item that could invalidate work already deployed, because the
aircraft is live on both sites now. Everything else on the list is ordinary work.

Last session's guess that more client material was coming was right — this was it.

**Approval is fully settled: the office manager and Mike both approved 5a.** No approval
gate remains anywhere on the logo.

**Provenance went wrong once mid-session and the correction matters.** An earlier commit
inferred from `.recall/history.md` that the aircraft came from this project's own 2026-08-06
prompt, built off Bell's spec PDF and a watermarked the-blueprints.com drawing. **The user
then stated it plainly: helicopter art made in Canva, composition in Claude Design.** The
inference is retracted in the file. **Chasing it did produce the session's most valuable
finding, though** — Canva's Content License Agreement forbids using Free or Pro stock
content in a logo, which means **one unanswered question can invalidate the approved
aircraft**: stock element, or Canva AI? That is Next Up item 4 and is written up under
Constraints That Bite.

**Four things were asked of the user and are unanswered as of this writing:** stock-vs-AI,
which Canva plan, the editable Canva and Claude Design source files, and — unrelated but
still blocking Next Up item 1 — the exact domain string.

**Next session, per the user (2026-08-04):** point the domain (Next Up item 1), and fold in
an update on the questionnaire. Get the exact domain string first — it is still written down
nowhere. **Added 2026-08-06:** replying to Bell (Next Up item 3) is now a fast, high-value
job — the rep is warm and invited questions.


**The landing page is built, deployed, and staged — not merely planned.** Live at
https://sah-coming-soon.netlify.app on its own Netlify site (id
`de01967d-071f-433e-a5af-6e87b7870b22`, name `sah-coming-soon`). Built behind the
`verify.py` guard described above, checked in a real browser at 390px and 1280px against
the live URL (console clean, zero errors, zero warnings), and approved by the office
manager. No DNS points at it; it is not indexed and not public.

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
