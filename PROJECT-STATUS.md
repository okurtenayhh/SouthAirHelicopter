# Project Status

*Last updated: 2026-11-22 (twelfth session, user's PC) · working branch `claude/phase-1-ready`, **PR #21 open** (carries this tracker and absorbs PR #20) · `main` still at `fe4c534` · review link redeployed and checked live 2026-11-22.*

> Maintained by the `/sa-wrap-up` skill. If this file and the repo disagree, the repo is right — fix this file. **Rewritten short on 2026-11-22**; the long history it used to carry is in git (`git log -p PROJECT-STATUS.md`).

**Three URLs, three different things:**

| URL | What it is | State |
| --- | --- | --- |
| https://phase-1-ready--south-air-helicopters.netlify.app | **The finished Phase 1 site, for client review** (branch deploy alias) | Redeployed 2026-11-22 from `claude/phase-1-ready`; all 4 pages 200, `private/` 404. Noindexed |
| https://south-air-helicopters.netlify.app | The older preview Mike has bookmarked | Still `main` at `fe4c534` — **deliberately not redeployed**; see In Flight |
| https://southairhelicopters.com | **Live, public**: the coming-soon landing page | Unchanged since 2026-08-10. Separate Netlify site `sah-coming-soon` |

## Where This Stands

**The Phase 1 site is finished and waiting on the office manager's sign-off.** Four pages (Home, About, Services, Contact), **zero placeholders** (`verify.py` now enforces it), every sentence traceable to a confirmed source. On 2026-11-22 it got a copy pass, a retention pass (nothing that turns a visitor away), and a full visual restyle ("2b": navy-led, riveted gunmetal plates, self-hosted slab/sans/mono fonts, square corners). The user is showing it to the office manager now.

**Launch is three steps away:** her sign-off → a realistic form test with the office watching the inbox → merge PR #21 and switch the domain.

## Next Up

1. **Office manager reviews the review link.** Ask her specifically about the three items under Waiting On The Client.
2. **Realistic form test** with the office watching `sahinc@sbcglobal.net` (inbox *and* spam). Netlify alerts are set; the first test (2026-10-21) was spam-filtered because it said "test".
3. **Merge PR #21** (user's job — the auto-mode guard blocks Claude from merging). It also closes #20, which it absorbed.
4. **Launch switch** (Claude, ~15 min, after 1–3): serve the four pages on `southairhelicopters.com`, delete `robots.txt` and the `X-Robots-Tag` block, verify with `curl -D -` that no `X-Robots-Tag` comes back. **Mechanic not yet decided** — see In Flight.
5. **After launch:** move the Netlify sites to an account the business owns; glance at Netlify's form spam list now and then (spam-flagged messages send no email).
6. *Small, any time:* Home shows 1979 / 1981 / XRIR622K twice (data plate + lower fact panel) — trim if wanted. Fix the registrar phone typo at Squarespace (`281-684-5187` → `281.648.5187`).

## Waiting On The Client

**Office manager** (her sign-off is how Mike's approval arrives — don't wait for Mike directly)
- **Approve the words written for Mike:** the Reliability and Precision value descriptions (About), and the founding paragraph on Home — including the history sheet's "Bell service facilities have come and gone across the region… South Air is still here".
- **Has the shop always been on this field?** The site only says where it is today, so nothing is wrong either way.
- **History-sheet facts, for when History returns:** two name spellings and the year Mike took over — the questions are at the bottom of `private/client-history-sheet-2026-08-26.md`. Not needed for Phase 1.
- Photos (hangar, shop floor, team, Mike, the certificate on the wall). Each riveted fact panel can be swapped for a photo with no other change. **Screen arrivals for customer tail numbers and NASA hardware/facilities/people.**

**Mike**
- A copy of FAA certificate **#XRIR622K** (he wrote "MAKE COPY") — the ratings, then aircraft models can come back.
- **NASA:** may it be published at all, does NASA review it, is "partnership" his word? ("PROBABLY" / "?"). Nothing NASA goes on the site until answered.
- His copy of the Bell CSF agreement (the governing trademark text).

**Either**
- Testimonials — none for now (user, 2026-11-22). Mike said they "could be acquired if asked".
- Google Workspace email on the domain. ⚠ **DNS trap:** the domain carries `v=spf1 -all` and `_dmarc p=reject`; update SPF/DKIM/DMARC *before or with* Workspace or every outgoing message is rejected.

## Content: Real vs Placeholder

**The four launch pages have no placeholders.** Everything on them is confirmed; the sources are the 2026-08-13 questionnaire and the 2026-08-26 history sheet (both in `private/`), plus the user's own answers on 2026-11-22.

| Page | What's on it | Cut for launch (comes back when the input arrives) |
| --- | --- | --- |
| `index.html` | Hero with the company name; riveted data plate (1979 · Bell CSF 1981 · #XRIR622K · zero maintenance-related accidents since 1979); three services; founding paragraph (Mitchell, Oct 1979, Bell 1981, north side of the field, formerly Clover Field); Bell section | Photos; certificate ratings |
| `about.html` | Who we are (Mike Pike, President); facts plate; three values each backed by a confirmed fact | Team section (bios); photos; Bell seal |
| `services.html` | Five confirmed services; Bell section; Certifications; **"Getting Your Aircraft In"** (call during hours to schedule); What Sets Us Apart | Parts & Fleet Support (never confirmed); "What We Don't Do"; pricing/quotes; testimonial; Bell badge; ratings |
| `contact.html` | KLVJ + coordinates, address, phone, both emails, hours, map, **working form** (reply time 1–3 business days, default topic "Maintenance / Service") | — |
| `drafts/` (History, Platforms, News, Careers) | Held back, 404'd on deploy | Their headers lack the new call link — add it when one is promoted |
| `coming-soon/index.html` (live) | Everything real; no placeholders | — |

## Decisions Locked

*Newest first. The reason is what stops a decision being reopened.*

- **Nothing on the site sends a visitor away** (user, 2026-11-22): no "what we don't do" lists, no named exclusions, no gatekeeping. Unsure visitors are told to call. *Reverses* the older `sa-prose` advice (unmerged `claude/rollout-plan` branch) that named limits were the voice's best feature. Audited by the `sa-retention-audit` skill.
- **No quote requests and no testimonials for now** (user, 2026-11-22). The shop schedules work during business hours "like an auto shop"; it doesn't own the strip. Pricing section became "Getting Your Aircraft In"; the form's "Request a Quote" option became "Scheduling".
- **Form replies: "usually within one to three business days"** (user's estimate, 2026-11-22).
- **No AOG wording anywhere on the site** (user, 2026-11-22): "We will turn out for AOG" came off the call band on every page and off Contact. Don't bring it back in that form; if AOG returns, the user words it.
- **Visual style is "2b"** (user, 2026-11-22, after mockups): Hyundai calm + workshop details, *"more blue… make it feel grown."* Navy `#1e3a5f` leads, deep navy `#14283f` header/footer, gunmetal only for riveted plates and the call band, orange only on the header call link and the call band's top rule. Zilla Slab headings, Inter Tight body, IBM Plex Mono for numbers. Square corners, rules not shadowed cards. Spec: `docs/superpowers/specs/2026-11-22-visual-restyle-design.md`.
- **Fonts are self-hosted** in `fonts/` (SIL OFL, `fonts/OFL.txt`) — no font CDN; `verify.py` fails on any external font or stylesheet.
- **Primary buttons are navy (white on dark grounds), not orange** — Claude's call from 2b, unchallenged so far; one CSS block to revert if the user wants louder call buttons.
- **Launch pages carry zero placeholders**; unconfirmed content waits in `drafts/` or as a client question, never behind an amber box on a root page (`verify.py` check 7b).
- **Tagline "Bell is our forte."** (2026-10-21) — the client's own phrase.
- **No aircraft model names anywhere** until the list is checked against certificate #XRIR622K (2026-10-21). `verify.py` `MODEL_RE`.
- **Four-page first launch** (2026-10-21): Bell Service Center folded into Services; NASA page deleted; History/News/Careers/Platforms in `drafts/`.
- **Stays on the user's personal Netlify until launch, then moves to a business-owned account** (2026-10-21). Form alerts go only to the client's address.
- **The office manager is the approval channel** (2026-08-04) — her sign-off *is* Mike's, delivered in person.
- **Company name is plural: "South Air Helicopters, Inc."** — business card, confirmed again 2026-08-26 over the history sheet's singular. The repo name is a trap.
- **Logo is `south-air-5a`** (2026-08-10), approved by both; provenance explained to and accepted by Mike. Don't reopen. Vector and stitchable versions still to make (not blocking).
- **Palette navy is the logo's `#1e3a5f`**; the `--color-*-on-*` tints exist for 4.5:1 contrast — don't collapse them.
- **"Bell" and "Bell Helicopter" are both acceptable** (Mike, 2026-08-13). Main site uses "Bell"; the coming-soon page keeps its client-approved "Certified Bell Helicopter Customer Service Facility", pinned by `verify.py`.
- **Exact ages are banned, floors allowed** ("45+", "since 1979") — exact ages go stale. `verify.py` enforces it.
- **Anything about the client, the relationship, or our uncertainty goes in `private/`** (gitignored). The repo is public.
- **Static HTML/CSS/JS, no build; hosting on Netlify; email addresses copy to the clipboard, the phone stays a real `tel:` link.**

## Constraints That Bite

- **Deploy only from a clean checkout, never the desktop folder** — it holds the gitignored `private/`, and `netlify.toml` doesn't 404 `/private/*`. Procedure: `git worktree add --detach <tmp> <branch>`; `python tools/verify.py` there; **from inside `<tmp>`** `netlify deploy --no-build --dir=. --site=b2e4b62c-aa66-40cd-a818-e568464a67e6 < /dev/null` (add `--prod` for the main preview, or `--alias=phase-1-ready` for the review link); `git worktree remove <tmp>`; `curl` every page plus `/private/client-answers-2026-08-13.md` (must 404). `--no-build`, running from inside the folder, and the closed stdin all matter — without them the CLI hangs.
- **Coming-soon deploys:** `netlify deploy --prod --cwd=coming-soon --dir=. --site=de01967d-071f-433e-a5af-6e87b7870b22`. `--dir=coming-soon` alone reads the wrong `netlify.toml`. Verify any indexing change with a real `curl -D -`.
- **Bell trademark:** factual relationship only, no endorsement wording, **no Bell shield or corporate logo ever**; the CSF seal only as Bell-issued artwork, smaller than and separate from the South Air logo, never redrawn. The seal file we have is print CMYK. Full rules: `docs/trademark-research.md`. Bell media-kit photos are not usable.
- **NASA:** logo is a permanent no; "trusted by" and endorsement framing are prohibited; and Mike hasn't said the work is publishable at all. Nothing NASA on the site.
- **The logo's aircraft is an identifiable Bell 429** — a question for Bell if it ever matters; the fix would be regenerating the aircraft, not the mark.
- **DNS:** Squarespace is registrar and DNS host. Apex `A` → `75.2.60.5`, `www` CNAME → `sah-coming-soon.netlify.app`. The email-hardening records (SPF `-all`, DMARC reject) are the Workspace trap above.
- **Desktop-only copies:** the logo source set `C:\Users\kourt\Desktop\South Air Helicopter\SAH LOGO\` and the Bell branding folder beside it. Move somewhere durable.
- **The repo is public.** Don't commit `.recall/`, `.netlify/`, `.superpowers/` or `private/`.

## In Flight

- **PR #21 is open** with everything from 2026-11-22 (copy, retention pass, restyle, the new skill, this tracker) and the merged #20. Merging is the user's job.
- **The main preview (`south-air-helicopters.netlify.app`) was deliberately not redeployed** — the new site lives on the review alias until PR #21 merges. After merging, redeploy from `main` with `--prod` so the bookmarked preview matches.
- **Launch mechanic is undecided.** Either (a) move the domain from `sah-coming-soon` to the main site, or (b) deploy the four pages to `sah-coming-soon` (which already holds the domain and its certificate). (b) avoids a domain move and certificate reissue, but that site's directory is `coming-soon/`, so it needs a clean build folder of only the public files. Decide at launch time; either way, remove `robots.txt` and the `X-Robots-Tag` header and verify with `curl`.
- **New project skill `sa-retention-audit`** (`.claude/skills/`). Tested against a no-skill baseline: the baseline missed the "What we don't do" panel and invented facts; with the skill, it caught every turn-away and invented nothing.
- **`sa-wrap-up` is partly stale** — it still describes 10 pages, 8 nav items, and a form that "submits nowhere". The tracker is right; update the skill text when convenient.
- **Local-only branch `claude/rollout-plan`** still holds the `sa-prose` skill and two planning docs. Unpushed (public-repo concern). `sa-prose`'s "name the limits" advice is now overridden — see Decisions Locked.
