# Project Status

*Last updated: 2026-08-06 (local, sixth session) · `main` at `e98e73a` · working branch `claude/coming-soon-page` at `7df5cdf` · PRs #1–#3, #5–#8 merged · **PR #4 is open as a draft** — a finished client questionnaire nobody has merged: https://github.com/okurtenayhh/SouthAirHelicopter/pull/4*

*Unmerged branches: `claude/coming-soon-page` (current — carries the built coming-soon landing page, now staged and live, plus last session's tracker commit) · `claude/client-content-brief` (brief documents, pushed, no PR) · `claude/sphere-logo` (a logo exploration, local only, parked — see Decisions Locked)*

**Live preview (ten-page work-in-progress site): https://south-air-helicopters.netlify.app** — noindexed, deployed and current as of 2026-07-30, verified live. Safe to send to Mike.

**Coming-soon landing page (one page, built for the real domain): https://sah-coming-soon.netlify.app** — noindexed, staged, **not attached to the client's domain — no DNS change has been made, and the page is not public and not indexed.** Its own Netlify site, separate from the preview above (which is untouched): site id `de01967d-071f-433e-a5af-6e87b7870b22`, site name `sah-coming-soon`.

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

## Next Up

Things that can move without waiting on anyone:

1. **Point the domain at the coming-soon page.** The page is finished, staged, and approved; the domain is bought and pointing nowhere. Two steps, in this order: remove the `[[headers]]` block from `coming-soon/netlify.toml`, redeploy with `netlify deploy --prod --cwd=coming-soon --dir=. --site=de01967d-071f-433e-a5af-6e87b7870b22`, then **confirm by real HTTP request that no `X-Robots-Tag` comes back at all** — if you see the four-token `noindex, nofollow, noarchive, nosnippet`, the wrong config was read and the page will never be indexed. Then the DNS records in Squarespace. **The exact domain string is still not written down anywhere** — get it first.
2. **Send Mike the package — this is now fully unblocked and is a very high-value action.** Three things travel together: the preview link (deployed and current), `docs/client-checklist.pdf`, and `docs/client-questions-form.pdf`. Everything that previously blocked this is resolved. People answer far better against a page they can see, so the preview and the questions go in one message. Nothing else on this list moves the project as much, because almost every remaining item is waiting on answers only he has.
3. **Reply to Zachariah Langley at Bell, and request brand-portal access.** Bell opened the door on 2026-08-06 and explicitly invited questions, so this is now a reply rather than a cold ask — the hard part is done. Seven things are still outstanding and one message covers them all: the **Bell Seal Guidelines** document (referenced twice in the deck, not attached — it's where web rules live), **web-format artwork** (RGB vector or transparent PNG; Summit Aviation serves exactly such a file, so it exists), the exact authorized body-copy wording, whether we may name the 206/407/429, whether a footer attribution line is required, whether Bell wants to review the site pre-launch, and whether a stylized helicopter may appear in South Air's *own* logo (Mike asked for a 429 — the do-not list forbids shield lockups but is silent on aircraft, so this needs asking, not inferring). The live list is at `docs/trademark-research.md` under "What Bell still hasn't answered." **Separately, request access at <https://brand.bellflight.com/> — but from a South Air address, not the user's.** Bell is vetting its own vendor network; a request from the facility they already emailed moves faster than one from a stranger.
4. **Propagate the founding year through the main site — now unblocked.** **1979 is confirmed** (user, 2026-08-04, restated after the office manager's original *"1979. Or 78, whatever Jeff said"*). Unwrap `[PLACEHOLDER Year]` in roughly fourteen places across the ten-page site. **Do not bring back derived age claims** ("46 years") when this lands — a year is permanent, a computed age rots annually. `tools/verify.py` already guards the coming-soon page against exactly that pattern; extend the same guard to the main site once the year lands there too.
5. **Wire the contact form to a real handler.** Still the highest-severity *functional* item — a customer who fills it in today reaches nobody. Cheap now: the site is on Netlify, so **Netlify Forms** is a `data-netlify="true"` attribute plus a notification address, no third-party service and no backend. Blocked only on knowing which inbox submissions should go to.
6. **Land the open branches.** `claude/coming-soon-page` has a PR open now, carrying the built coming-soon landing page and last session's tracker commit. `claude/client-content-brief` is pushed with no PR — open one. **PR #4** (the older questionnaire, 50 questions plus a `.docx`) still needs a rebase; `PROJECT-STATUS.md` has now been rewritten several times since, so expect a conflict. Its content is superseded by the new PDFs, so merging it is optional — but decide deliberately rather than leaving it to rot.
7. **Correct the "Bell Helicopter" wording on `bell-service-center.html:41`.** Bell dropped "Helicopter" from the brand in 2018; the page echoes Mike's business card, which predates that. The homepage says "Bell Customer Service Facility" (current form) while the Bell page says "Bell Helicopter Customer Service Facility" (retired form) — so the two pages disagree. Note the coming-soon page now deliberately uses the retired form too, but that was the client's explicit, overruled-objection choice for that one page (see Decisions Locked) — it doesn't settle what the main site should say. Confirm against Bell's answer to item 2 rather than guessing either way.
8. **Decide whether Careers ships.** It's built, but a careers page with no listed openings can read as a dead site. Either get openings (or an explicit "nothing right now") from the office manager, or hold the page back until launch.
9. **Lean into the personal/small-shop angle** in About and the homepage hero — named-owner warmth is the one thing neither Arrow Aviation nor Summit Aviation has. Needs Mike's story, so it's half-blocked, but the *structure* for it is there now.

## Waiting On The Client

**Mike (owner / president)**
- Sign-off on the logo — but **hold this one.** The user approved the current mark, Mike has never seen it, and the user has since reopened the question. Don't put a logo in front of Mike until the user settles which one.
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
| `coming-soon/index.html` (staged, separate site — not part of the 10-page site above) | **Everything. The only page in the project with no placeholders** — legal name, address, confirmed phone number, FAA Repair Station #XRIR622K, the client-approved Bell CSF wording, founding year 1979 | None |

## Decisions Locked

- **Static HTML/CSS/JS, no framework** — a marketing site with no backend; keeps hosting free and hand-editing possible later.
- **Company name is plural: "South Air Helicopters, Inc."** — confirmed on Mike's business card. The repo name `SouthAirHelicopter` is singular and misleading; ignore it.
- **Logo is a two-mark system**, not one logo — a stacked badge for formal use, a three-blade rotor icon for small sizes, both from one shared blade profile. This is what the site ships today and what every page points at.
- **⚠ The logo is no longer settled, and the owner has now given a direction.** The user reopened it on 2026-07-30 ("we're not set on the logo") and sketched an alternative: the company letters forming a sphere that reads as a bubble-canopy helicopter. That exploration lives on the local branch `claude/sphere-logo` — a spec, a generator, and a full mark family — and was **parked mid-flight at the user's request**. If it is ever revived, the one thing worth knowing is already written down: `SAH` cannot form a circle, because no letter in it has an arc to donate, and the only letter that does is the `O` in SOUTH.
- **Mike's logo direction, relayed 2026-08-04: a helicopter, with "South Air Helicopters" or "South Air" in the mark.** This is the owner's own stated preference, so it outranks both the shipping mark and the sphere exploration. **This is the next task after the landing page.** Two objections were raised and should not need rediscovering. *(a)* The reference image supplied with it is a wall-art product listing — someone else's copyrighted line drawing — usable as a style reference, never as a source. *(b)* Mike asked specifically for a **429**, and a recognizable Bell airframe inside South Air's *own* logo asserts affiliation in a way the CSF seal does not: the seal says "authorized by Bell", a Bell aircraft in your mark says "we are Bell". The proposed compromise is a stylized helicopter that reads as a helicopter without being identifiable as a specific model — Mike keeps the aircraft and the name, the affiliation problem disappears. If he wants the 429 specifically, that is a question for the same account rep who is sending the seal.
- **The office manager is the approval channel, and her sign-off is the real one** (established 2026-08-04). She sees Mike in person and asks him directly, which no amount of emailing achieves. So "approved by the office manager" is not a lesser form of "approved by the owner" — it is how owner approval actually arrives on this project. **Stop holding work back waiting for Mike to review something himself.** Send it to her. Earlier sessions treated these as two separate gates and that was wrong; the practical effect was work sitting unapproved for weeks. The one thing still worth stating plainly when handing her something is what is unconfirmed in it, so she knows what to ask him.
- **The coming-soon landing page leads with contact information, not a "coming soon" teaser** (user's call, 2026-08-04). South Air is an operating shop, and someone who finds the page may need work done that week. A teaser implies the *business* is new and buries the phone number under an announcement nobody arrived for. Contact details are the page; the new-website line is a footnote. **Corrected the same day:** the page originally also stated it was "open and taking work." The office manager reviewed the staged page and flagged that the shop is at capacity ("we're full at the moment") — that status line was factually wrong, not a style choice, and was removed (including a second copy that had leaked into the meta description). It was replaced with `Established 1979`. The page makes no claim about current availability; it states who South Air is and how to reach them.
- **The landing page carries the Bell CSF status, verbatim as "Certified Bell Helicopter Customer Service Facility"** (reversed same day, 2026-08-04, at the user's explicit direction, after the office manager reviewed the staged page and asked for it). This reverses the same-day call, recorded earlier in this file, to hold Bell back and carry only the FAA Repair Station number until the account rep confirmed current wording. Two objections were raised before the reversal and should not need re-raising: "Helicopter" is a name Bell retired in 2018, and "Certified" appears nowhere on Mike's business card. The user was shown both and chose this wording anyway. **Not to be relitigated next session.** `tools/verify.py` now pins this exact string as the only permitted Bell mention on the page, so the wording cannot drift. The Repair Station number stays on the page too, alongside it, unchanged.
- **The landing page deploys as its own Netlify site, not as a route on the existing one.** A host-scoped rewrite in `netlify.toml` would have been one site and one deploy, but if that rule ever failed open the public domain would serve the unfinished, placeholder-riddled site. Two sites makes the worst case "the landing page is briefly wrong" instead. It also means `tools/verify.py` needs no weakening, since it globs the repo root only.
- **Wordmark carries the legal name** — "SOUTH AIR / HELICOPTERS, INC.", second line letter-spaced flush to the first.
- **Palette, confirmed against the company's own shirts 2026-08-04.** Navy `#0b2545`, royal blue `#3585cf`, white `#eef2f6`, with gunmetal `#3d4854`/steel `#7d8b99` as structural neutrals and safety orange `#f26722` as the single accent. The office manager: *"we use this blue and navy primarily"*; Mike, asked navy or lighter: *"navy is fine."* The royal was measured off a photo of a company shirt — hue 211°, saturation 0.73. **The old sketch palette was nearly right already**: its steel blue `#2f7fb8` is hue 205°, within six degrees of the real garment, so this is a nudge not a rewrite. **The amber `#f2a71b` is dropped** — it was the only invented colour in the project and the user rejected it, asking instead for complementary colours with a masculine, mechanical feel. Safety orange is hue 22° against the blue's 211°, so a true complement, and reads as equipment rather than gold. **Ask the office manager for the shirt's brand and colour name off the tag** — a garment spec beats sampling a photo taken under office lighting.
- **Sitewide roll-out of the new palette rides with the logo task, not before it.** `css/style.css` and nine logo SVGs all carry the old values; recolouring them twice is wasted work when the logo is about to be redrawn anyway. The landing page uses the new palette from the start because it has not been built yet.
- **The landing page's identity block is an aircraft data plate** (2026-08-04). Every certified aircraft carries a riveted plate stamped with its serial; South Air's Repair Station number **is** that kind of number, so stamping it on a machined panel is true to the content rather than decoration applied to it. This is where the "masculine mechanical" feel comes from — materials and typography — which keeps the accent colour doing exactly one job.
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
- **The logo has to embroider.** The company bought a Brother embroidery machine and intends to make its own shirts once a mark is settled (2026-08-04) — so the mark is not a screen-only artefact. Embroidery cannot render gradients or hairlines, every colour is a thread change, and text below roughly 5mm cap height collapses into mush. This rules out fine detail in the mark, and it is **the most persuasive argument against Mike's detailed line-art helicopter**: at chest-pocket size it will not stitch legibly. That lands with a shop owner in a way a trademark argument does not, and it points at the same simpler mark. Note the shirts' current serif wordmark is *not* settled identity — it predates any of this and will be replaced.
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

`python tools/verify.py` is now **17 checks** (up from 9 — the header/footer loop emits
two checks, one per shared block, not one). Nine cover the 10-page site:
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

**Session of 2026-08-06 was short and entirely documentary.** The user handed over the
Bell material from the office manager and asked to save. **No site file changed, no page
was touched, nothing was deployed** — both Netlify sites are exactly as the 2026-08-04
session left them, and neither needs a redeploy. The work was reading Bell's material and
writing it into `docs/trademark-research.md` and this file.

The user said "first" when handing the Bell folder over, implying more client material was
coming, then stopped. **So assume there is more that hasn't been seen yet** — ask before
concluding the Bell story is fully told.

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
- `claude/sphere-logo` — **local only, never pushed, deliberately parked.** A logo
  spec, a generator (`tools/make_sphere_logo.py`), and a full alternative mark
  family. Superseded as a direction by Mike's own brief — see Decisions Locked.

**PR #4 is still an open draft.** Its 50-question questionnaire has been superseded
by `docs/client-questions-form.pdf` on the brief branch, which covers the same ground
in a nicer form. Merging it is now optional; it needs a rebase either way.

**Nothing is uncommitted.** No markup changed on 2026-08-06 — only `docs/trademark-research.md`
and this file. The ten-page preview is still the 2026-07-30 deploy and the coming-soon page
still the 2026-08-04 deploy; neither was invalidated by anything since. `python tools/verify.py`
re-run 2026-08-06: all 17 checks green.

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
