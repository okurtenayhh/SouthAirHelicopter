# South Air Helicopters — Master Needs List

*Everything the site is waiting on, organized by how it gets collected rather than by which page it lands on.*

**Last updated: 2026-07-30** · Site state: 10 pages, structurally complete, **134 flagged placeholders**, 13 empty photo slots, 0 video assets, contact form submits nowhere.

---

## How to read this

This is a **collection brief**, not a to-do list. Almost nothing here can be answered from the repo — it has to come out of the business. It's split by *activity*, because that's how it actually gets gathered:

| Section | What it is | Who does it |
| --- | --- | --- |
| [1. Video](#1-video) | Hero footage — new capability, nothing exists | Camera at the hangar |
| [2. Photography](#2-photography) | 13 named slots, shot list per slot | Same visit |
| [3. Interviews](#3-interviews) | 5 people, question sets per person | Sit-down or phone |
| [4. Documents](#4-documents-to-physically-collect) | Paper that answers questions faster than talking does | Office visit / email |
| [5. Permissions](#5-permissions-and-clearances) | Bell, NASA, customer aircraft, people in frame | Letters and contracts |
| [6. Text blanks](#6-text-blanks-page-by-page) | Every placeholder, page by page | Mostly Mike + office manager |
| [7. Technical decisions](#7-technical-and-infrastructure-decisions) | Domain, email, form, analytics | The user + client |
| [8. Build work](#8-build-work-that-is-not-blocked-on-anyone) | Not blocked on the client — can move now | Us |
| [9. Invented content](#9-invented-content-that-must-be-confirmed-or-killed) | Things on the live site nobody verified | Confirm or delete |
| [10. Capture day plan](#10-the-capture-day-plan) | One-visit field guide | Whoever goes |
| [11. Launch gate](#11-launch-gate) | What must be true before it goes public | — |

**A questionnaire already exists.** `docs/client-questions.md` (in unmerged PR #4) turns the text placeholders into 50 plain-language questions with a printable `.docx`. This document is broader — it adds video, the shot list, interview structure, documents, technical decisions, and build work, which the questionnaire doesn't cover. **Use the questionnaire as the leave-behind; use this as the plan.** Where they overlap, the questionnaire has the friendlier wording.

### The five answers that unlock the most

| Answer | Unblocks |
| --- | --- |
| Which airframes the shop is rated on, and what work per model | 18 placeholders — `platforms.html` is 100% empty until this lands |
| One day at the hangar with a camera | 11 of 13 photo slots, **all** video, and most of the interview material |
| The founding year | 9 slots across 3 pages, plus every age claim sitewide |
| Bell's CSF seal artwork + written permission | The Bell page's reserved badge slot, plus 4 open wording questions |
| NASA scope in writing (and whether it can be published at all) | The entire NASA page — currently the highest-liability page on the site |

---

## 1. Video

**Status: nothing exists, and the site can't currently play video.** Every hero on the site is a flat color band; the homepage has an inline SVG helicopter illustration where footage would go. Video heroes are a build change plus an asset need — both are listed here.

### 1a. What to film — shot list

Priority order. If only one gets shot, shoot **V1**.

| # | Page | Shot | Notes |
| --- | --- | --- | --- |
| **V1** | Homepage | **Helicopter lifting off / setting down in the field**, camera low and static or slow push | The money shot. Golden hour. Wide enough that the airframe reads at a glance. Dust and rotor wash are good — they signal *real work*, not stock. |
| **V2** | Homepage alt / About | **Hands-on-the-aircraft work** — a mechanic torquing a fitting, opening a cowling, running a borescope, safety-wiring | Tight, shallow depth of field. This is the shot that says "maintenance shop" instead of "charter company." |
| **V3** | Services | **Slow dolly down the shop floor**, aircraft in various states of teardown | Continuous move, no cuts. Reads as capability. |
| **V4** | Bell Service Center | **Wide of the hangar with a helicopter inside, doors open, light spilling in** | ⚠️ Watch for Bell markings on the airframe — see [§5a](#5a-bell). |
| **V5** | Careers | **The team working** — two people on a job, talking, moving | Recruiting footage. Faces matter here; needs the [people release](#5c-people-in-frame). |
| **V6** | History / About | **Exterior of the hangar, sign visible, at dawn or dusk** | Establishing shot. Cheap to get, useful everywhere. |
| **V7** | NASA page | Anything NASA-adjacent | ⚠️ **Do not film without clearance first** — see [§5b](#5b-nasa). Assume this is a no until proven otherwise. |

### 1b. How to shoot it

Practical notes for whoever holds the camera — these are the things that make footage unusable if missed:

- **Shoot horizontal, 4K, 24 or 30fps.** 4K gives room to crop, reframe, and stabilize in post. Vertical footage cannot be salvaged for a desktop hero.
- **Rotor blades and rolling shutter.** Phone and mirrorless CMOS sensors turn spinning rotors into bent, wobbling spaghetti. Two fixes: shoot the rotor **at idle or stopped** where possible, or accept it and frame so the blades are partially out of the shot. A shot ruined this way can't be fixed later.
- **Lock exposure and white balance** before rolling. Auto-exposure hunting mid-shot is the most common reason a clip can't loop.
- **Everything on a tripod or gimbal.** Handheld reads as amateur under a full-screen crop. If neither is available, brace against something and shoot static.
- **Shoot 30+ seconds per setup.** Loops get cut to 8–15 seconds; the extra is what makes a clean loop point possible.
- **Golden hour for anything outdoors** — the hour after sunrise or before sunset. Midday sun on a white hangar is flat and harsh.
- **Get 3× more than the list.** Wide, medium, and tight of every setup. Coverage is free on the day and impossible to get later.
- **Audio doesn't matter** — hero video is muted by browser policy, and the audio track gets stripped anyway.

### 1c. Technical spec for delivered video

What the files need to be once they're edited. This constrains the shoot only lightly, but it's what the site needs:

| Property | Target | Why |
| --- | --- | --- |
| Resolution | 1920×1080 delivered (2560 wide for the homepage) | Heroes go full-bleed; 1280 looks soft on a laptop screen |
| Duration | 8–15 seconds, seamless loop | Long enough not to feel twitchy, short enough to download |
| Format | **H.264 MP4** primary + **WebM/VP9** fallback | MP4 for Safari/iOS, WebM is 30–40% smaller where supported |
| File size | **Under 3 MB**, 5 MB absolute ceiling | This is the hard constraint. A 20 MB hero is a broken site on hangar wifi or a phone. |
| Audio | **Track removed entirely** | Autoplay requires muted; deleting the track saves bytes and avoids an iOS edge case |
| Poster frame | JPEG/WebP still from the video's first frame | Shows during load and *instead of* video for reduced-motion users |
| Overlay | Dark navy scrim, roughly 55–65% opacity | The requested look — and it's what makes white headline text legible over moving footage |

### 1d. Build work the video requires

Not blocked on the client — but it can't be finished without a real file to test against:

- [ ] Video hero component: `<video autoplay muted loop playsinline preload="metadata">` with `<source>` for WebM and MP4, plus a `poster`
- [ ] Dark overlay layer + a text-contrast check against the actual footage (bright sky footage may need a heavier scrim than 55%)
- [ ] `prefers-reduced-motion: reduce` → serve the poster still, no video. **Non-negotiable** — motion sensitivity is a real accessibility requirement, and a full-screen autoplay loop is exactly the trigger
- [ ] Mobile: either serve a cropped vertical-safe frame or fall back to the poster image entirely on narrow screens (saves bandwidth on cellular)
- [ ] Fallback chain: no video file → poster image → current flat color band. The page must never look broken mid-rollout
- [ ] Decide per-page: does every page get a video hero, or only the homepage? *(Recommendation: homepage + Services + Careers get video, the rest get stills. Seven video files is seven chances for a 3 MB download.)*

---

## 2. Photography

**13 empty photo slots.** Eleven of them are one afternoon's work. Here's every single one, mapped to where it renders.

### 2a. The shot list, by slot

| # | File | Line | Slot | What to shoot |
| --- | --- | --- | --- | --- |
| P1 | `index.html` | 139 | Homepage, mid-page | Hangar exterior, team, or an aircraft — the "this is a real place" shot |
| P2 | `index.html` | 147 | Homepage, Bell section | Shop floor, or an airframe in for service. ⚠️ **Photograph only — the Bell seal has its own reserved slot and does not go here** |
| P3 | `about.html` | 54 | About, main | Team or hangar. Wide, sense of scale |
| P4 | `about.html` | 106 | About, team | **Portrait of Mike Pike.** Environmental, not a studio headshot — him in the hangar, arms crossed or working |
| P5 | `about.html` | 111 | About, team slot 2 | Second staff portrait — *or delete the slot if nobody else goes on the site* |
| P6 | `about.html` | 116 | About, team slot 3 | Third staff portrait — same |
| P7 | `bell-service-center.html` | 62 | Bell page | **The repair station certificate on the wall**, or hangar floor. The certificate photo does double duty — see [§4](#4-documents-to-physically-collect) |
| P8 | `careers.html` | 104 | Careers | Shop floor mid-work. Should answer "what would I be walking into?" |
| P9 | `history.html` | 87 | History | **Archive photo** — original hangar, early team, first aircraft. Can't be shot today; has to be found |
| P10 | `nasa-partnership.html` | 62 | NASA page | ⚠️ NASA-related work. **Rights-gated — do not shoot or publish without clearance** |
| P11 | `news.html` | 52 | News card 1 | One image per story — depends on what the stories are |
| P12 | `news.html` | 61 | News card 2 | Same |
| P13 | `news.html` | 70 | News card 3 | Same |

**Also reserved but not a photograph:** `bell-service-center.html:100` holds the Bell-issued CSF seal. It stays empty until Bell sends artwork *and* written permission. Do not fill it with anything else to make the page look finished.

**Not yet built:** `platforms.html` has **zero** image slots, because no aircraft model is named yet. Once models are confirmed, each model card wants a photo of that airframe — **add ~1 photo per model to the shoot list** once the list exists.

### 2b. Extra coverage worth grabbing while there

Not tied to a slot, but these get used:

- The hangar sign / entrance (Open Graph social preview image — currently missing sitewide)
- Detail texture shots: tools, torque wrench, logbooks, parts bins, safety wire — filler for section breaks
- Wide interior with the doors open and light coming in
- Anything hanging on the office walls: certificates, awards, old photos, plaques
- The building from the road, so a customer can recognize it on arrival

### 2c. Photo requirements

- **Horizontal**, minimum 2000px on the long edge, shot at max quality
- **Originals, not texts/WhatsApp exports** — messaging apps recompress to mush. AirDrop, email as "actual size," or a USB stick
- **Alt text for every published photo** — needs writing once photos exist; this is a real accessibility requirement, not a nicety
- **N-numbers**: tail numbers identify the aircraft owner. See [§5d](#5d-customer-aircraft)

---

## 3. Interviews

Five people. The questionnaire covers what to ask; this covers **who** and **how the conversations should be structured**, because several of these answers only come out of talking, not a form.

### 3a. Mike Pike — owner / president · *~90 min, in person, at the hangar*

The highest-value conversation on this list. Bring a recorder.

**Company and story**
- Confirmed founding year (currently "1997 or so" — unprintable)
- Who founded it, why, what the first days looked like
- The longer origin story — specific memories, not a summary. *This is the one thing competitors can't copy*
- 2–3 real milestones with rough dates
- How public should the recent change of ownership be?
- How he got into helicopters personally
- His own bio, in his words

**Capability — the biggest unlock**
- ⚠️ Which airframes is the shop rated on? *Read from the certificate, don't recall from memory*
- ⚠️ What work is authorized per model — inspections, airframe, engine, avionics, component?
- Is the shop Bell-focused, or across manufacturers?
- Confirm the six services on the site are real, and what each actually includes
- Does the shop do charter/flight support at all, or maintenance only? *(The homepage currently claims it)*

**Bell**
- ⚠️ What does the CSF designation actually authorize? Warranty work? What can this shop do that a non-CSF can't?
- Is "Bell **Helicopter** Customer Service Facility" still current wording? *(Bell dropped "Helicopter" in 2018; the business card predates that)*
- How long has the designation been held, and what maintains it — audits, factory training, tooling?
- **Can we see the CSF agreement?** ← the single highest-value document outstanding

**NASA — handle carefully**
- ⚠️ What, specifically and factually, does South Air do for NASA?
- ⚠️ Which center, facility, or program?
- ⚠️ Does the contract limit what can be advertised? **Does it require NASA to review marketing that mentions them?**
- When and how did it start?

**Quoting**
- What does he need from a customer to quote? Make/model, serial, hours, logbook status?
- How does a quote come back — call, email, written scope?
- Typical turnaround *(only publish if he'll stand behind the number)*
- Should quote requests come by phone, form, or both? ← **decides whether the contact form is worth wiring at all**

**The two invented stats**
- Is "100% safety-first culture" something he wants on the site?
- Is "24/7 support" true? *(Someone will call at 2am)*

### 3b. Office manager (the user's mother) · *~30 min, phone is fine*

- Business hours
- Company overview + mission statement paragraph
- Which inbox is the public "general inquiries" one? *(The contact page currently publishes a personal `att.net` address with a name and title, on a public URL)*
- Any current job openings — and if none, confirm we can say so plainly
- Should resumes go to a separate inbox?
- EEO statement — existing wording if there is one
- **The photo archive** — anything historical, and where it lives
- Whether other staff should appear on the site at all *(decides whether About's two empty team slots get filled or deleted)*

### 3c. Lead mechanic / senior A&P · *~30 min, on the shop floor*

Nobody has asked this person anything yet, and they own the two pages that read most hollow right now.

- What does a mechanic actually do here day to day?
- What kind of aircraft and work come through?
- What's the shop like to work in? How many people?
- What would you tell a mechanic considering coming here?
- What's the hardest job you've done here? *(story fuel for History and News)*
- Walk me through a typical job start to finish *(this is how the Services page gets written honestly)*

### 3d. Longest-tenured employee · *~30 min*

- What's changed since you started?
- Stories about the early days, the founder, the first aircraft
- Anything that should be on the History page that nobody thinks to mention

### 3e. A customer · *~15 min, phone*

- One or two sentences on what it's like to work with South Air → fills the testimonial slot on `services.html`
- Ask Mike to nominate someone and make the intro
- ⚠️ **Cannot be a NASA person** — NASA's rules prohibit quotes attributable to their staff

---

## 4. Documents to physically collect

Paper answers faster and more accurately than conversation. A photo of a certificate settles questions that would otherwise take three emails.

| Doc | Why it matters | Priority |
| --- | --- | --- |
| **FAA Repair Station certificate #XRIR622K** — photo of the actual certificate | Answers the ratings and limitations questions *completely*. Also doubles as photo slot P7 | **High** |
| **Bell CSF agreement** | Bell publishes no third-party trademark policy — **this contract is the governing text** for everything on the Bell page | **Highest** |
| **Bell CSF certificate / seal artwork + brand guidelines** | The only legitimate route to a Bell mark on the site. Comes from Mike's Bell account rep, *not* the ethics hotline | **High** |
| **NASA contract publicity clause** | Determines whether the NASA page can exist at all | **High** |
| **Ops specs (OpsSpecs) attached to the repair station certificate** | Where the authorized ratings per airframe are actually listed | High |
| Any other certifications or authorizations | The footer has a certifications slot on all 10 pages, currently empty | Medium |
| EEO statement, if one exists in writing | Use exact existing wording rather than drafting | Medium |
| Old marketing material — brochures, prior website, ads | Free copy, and shows how the business already describes itself | Medium |
| Existing photo archive | May cover the historical slot with no shoot needed | Medium |
| Business insurance certificate | Some competitors list coverage; optional | Low |
| Business card (already have) | Source of the current Bell + certificate claims | ✓ Done |

---

## 5. Permissions and clearances

The part where getting it wrong is expensive rather than just unfinished.

### 5a. Bell

- Bell's logo **cannot** appear without permission. The corporate shield and 2018 wordmark are *not* the same thing as the CSF seal — **only the seal belongs on this site.** The corporate mark says "we are Bell"; the seal says "authorized by Bell."
- Two Bell logo files currently sitting in the user's Downloads are the wrong asset and were deliberately not added. `tools/verify.py` fails the build on any Bell-named image in `images/` — **that guard is intentional, don't disable it to make a page look finished.**
- Copy must never imply Bell endorses South Air. The badge sits *beside* the South Air logo, never merged into it.
- ⚠️ **Open question worth resolving before the shoot:** a photo or video of a Bell airframe in the hangar will naturally show Bell markings on the aircraft itself. That's different from placing Bell's logo as a design element — but it should be confirmed against the CSF agreement rather than assumed. **Ask Bell directly as part of the same email.**

**One email to Mike's Bell account rep covers all of it:** seal artwork + co-branding rules, exact authorized wording for the CSF status, whether models the shop is rated on may be named, whether incidental Bell markings in photography are fine, and whether Bell wants to review the site pre-launch. Draft questions already exist at `docs/trademark-research.md:166-174`.

### 5b. NASA

- **The logo is a settled no.** Insignia, worm, and Seal are protected under 14 CFR 1221. There is no permission path. Stop re-litigating it.
- **Allowed:** a factual, specific description of work performed. NASA's own guidance permits vendors to state that a NASA center is a customer and describe their services factually.
- **Prohibited:** "NASA approved," "official NASA," and — verbatim on NASA's list — **"trusted by."** No trust strip or logo row may ever include NASA.
- **No quotes attributable to NASA staff.** That rules out a testimonial on that page permanently.
- The word **"partnership" implies endorsement** — describe work performed instead. *(The site nav still says "NASA"; the page filename is still `nasa-partnership.html`.)*
- **Any photo containing NASA facilities, hardware, or identifiable NASA personnel needs clearing** — even photos South Air took themselves.
- Full detail in `docs/trademark-research.md`.

### 5c. People in frame

- Anyone recognizable in a published photo or video should know it's going on a public website. A verbal OK noted down is usually enough for a small shop, but ask on the day rather than after.
- Employees who've left, or who don't want to be on the site, should be excluded — check the roster with the office manager before publishing faces.

### 5d. Customer aircraft

- **Tail numbers (N-numbers) publicly identify the aircraft's registered owner.** A customer may not want it known their aircraft was in for maintenance.
- Options, in order of preference: get the customer's OK, frame the shot to exclude the number, or blur it in post.
- Same applies to any visible customer name or operator livery.

### 5e. Everything else

- **No stock footage or stock photos of other people's helicopters.** The whole value of this shoot is that it's the actual shop. Stock reads as stock, and a stock Bell photo would also be a trademark problem.
- **No music** on hero video — it's muted. If a longer non-hero video ever gets made, music needs a license.
- **Google Maps embed** on the contact page is already in place and fine under standard embed terms.

---

## 6. Text blanks, page by page

All 134 flagged placeholders. Marked ⚠️ where a wrong guess causes a real problem, not just a rough page.

### `index.html` — homepage · 14 blanks
- Founding year (hero eyebrow) + the derived "years in operation" stat
- Positioning statement refinement — the one-line pitch
- All three service blurbs
- ⚠️ "100%" safety stat and "24/7" support stat — **both invented** ([§9](#9-invented-content-that-must-be-confirmed-or-killed))
- ⚠️ Bell CSF tile — exact authorized wording pending Bell
- Bell section body copy
- History teaser + NASA teaser copy
- Footer tagline · footer certifications *(these two repeat on all 10 pages — 20 slots from 2 answers)*

### `about.html` · 18 blanks
- Company overview paragraph · mission statement
- All three company values — ⚠️ *the site chose "Safety First / Reliability / Precision," not the client* — plus what each looks like in practice
- Mike Pike's bio
- Two additional team slots: names, roles, bios — **or a decision to delete them**
- 4 photo slots

### `services.html` · 15 blanks
- ⚠️ Confirmation the six-service list is real, not a guess
- What's included in each of the six
- Whether charter/flight support is offered at all
- All three "How Pricing Works" steps: what's needed to quote, who reviews it, how the quote comes back
- ⚠️ Quote turnaround time — *publish only if Mike will be held to it*
- Testimonial

### `bell-service-center.html` · 9 blanks
- ⚠️ Exact current Bell designation wording *(the page says "Bell Helicopter…", the homepage says "Bell…" — **the two pages currently contradict each other**)*
- What the CSF designation authorizes, in plain language
- How long held, what maintains it
- ⚠️ Ratings on certificate #XRIR622K
- Reserved Bell badge slot + 1 photo slot

### `platforms.html` · 18 blanks — **the page is 100% empty**
- ⚠️ 5 aircraft models
- ⚠️ Authorized work per model (5 slots)
- Model-specific notes: tooling held, parts stocked, typical work (5 slots)
- Intro: Bell-focused or multi-manufacturer?
- **Nothing on this page can ship until the ratings list lands.** By design.

### `history.html` · 18 blanks
- ⚠️ Founding year
- Every timeline entry: founding, early growth, expansion, certifications, acquisition — dates *and* descriptions
- The longer founding story
- How public the ownership change should be
- 1 archive photo

### `nasa-partnership.html` · 7 blanks — **highest liability page on the site**
- ⚠️ Which center/facility/program
- ⚠️ What South Air actually does, factually
- ⚠️ When and how it started
- ⚠️ What's publishable under contract
- 1 photo, rights-gated
- Page carries a standing pre-publication warning. **Leave it there until the clearances are in writing.**

### `news.html` · 15 blanks
- 3 headlines, 3 dates, 3 summaries, 3 images
- **Or:** a decision to hold the page until there's real news. *An empty news page is worse than no news page.*

### `careers.html` · 14 blanks
- Whether there are openings at all — **and if not, an explicit "nothing right now"**
- Per role: certificates required, experience, full/part time, shift, Bell experience required or preferred
- Day-to-day description · shop size and culture
- Benefits — *only what actually exists*
- Resume inbox
- ⚠️ EEO statement
- 1 photo
- **Decision:** does Careers ship at launch, or get held back?

### `contact.html` · 6 blanks
- ⚠️ Airport identifier + heliport coordinates — **from the FAA airport record, not a guess.** Both competitors list these at the top
- Business hours
- ⚠️ **The form submits nowhere** — see [§7](#7-technical-and-infrastructure-decisions)
- ⚠️ A personal `att.net` address is published with a name and title on a public URL — decide what should actually be public
- Email placeholders pending domain

---

## 7. Technical and infrastructure decisions

Not client *content*, but the site can't launch without these settled.

### Blocked on a decision

| Item | Question | Blocks |
| --- | --- | --- |
| **Contact form handler** | Which inbox do submissions go to? | ⚠️ **Highest-severity functional bug on the site** — a customer who fills it in today reaches nobody. Netlify Forms makes this a `data-netlify="true"` attribute plus one email address. No backend, no third party |
| **Domain name** | Purchased yet? What is it? | Every email on the site, the OG tags, the sitemap, DNS |
| **Google Workspace email** | Which addresses once the domain exists? | Contact page, footer ×10, careers inbox |
| **Public inbox** | Is `sahinc@sbcglobal.net` the permanent public address? | Footer on all 10 pages |
| **Analytics** | Does the client want traffic data? | If yes: privacy-respecting option (Netlify Analytics / Plausible) over Google Analytics — no cookie banner needed |
| **Google Business Profile** | Does one exist? Claimed? | Local search is how a Pearland-area operator actually finds them. Arguably higher ROI than the whole site |
| **Netlify account ownership** | Who owns it long-term — the user or the client? | Hand-off, billing, DNS control |
| **Who maintains it after launch** | Real question, usually skipped | Whether the build should stay hand-edited HTML or move to a CMS |

### Missing and unasked-for — worth building

Found by audit; nobody has raised these:

- **No Open Graph / Twitter card tags on any page.** Sharing any page in a text message or on Facebook produces a blank grey box. Needs the tags + one 1200×630 social image
- **No `sitemap.xml`**
- **No JSON-LD structured data.** A `LocalBusiness` schema block with address, phone, hours, and geo is exactly what Google uses for a local business panel — high value, low effort, but **needs the hours and coordinates first**
- **No `apple-touch-icon`** — saving to a phone home screen gives a blank icon
- **No 404 page.** Deliberate: `tools/verify.py` requires every `.html` to carry the shared header/footer and 8 nav items. Netlify's default is acceptable
- **Real-device mobile check never done.** Screenshots at 1280px were reviewed two sessions ago and are now stale for `index.html`; 390px was spot-checked only. The live preview URL makes this easy
- **Live preview is stale** — the deploy was blocked by the permission classifier and did not run. The public URL still serves the old homepage **including the unflagged NASA tile.** ⚠️ **Do not send Mike the link until it redeploys**

---

## 8. Build work that is not blocked on anyone

Can move today, no client input required:

- [ ] **Redeploy** — `netlify deploy --prod --dir=.` from the repo root. The stale preview is the thing blocking client hand-off
- [ ] **Merge PR #4** (client questionnaire). Finished work sitting in draft. Expect a rebase conflict — PR #5 rewrote `PROJECT-STATUS.md`
- [ ] **Fix the Bell wording contradiction** at `bell-service-center.html:41` — the two pages disagree today. *(Confirm against Bell's answer rather than guessing which is right)*
- [ ] **Wire the contact form** to Netlify Forms — everything but the destination address can be built now
- [ ] **Build the video hero component** ([§1d](#1d-build-work-the-video-requires)) — buildable against a placeholder file
- [ ] **OG tags, Twitter cards, `sitemap.xml`, apple-touch-icon** across all 10 pages
- [ ] **`LocalBusiness` JSON-LD** scaffold, values filled once hours + coordinates arrive
- [ ] **Draft the Bell email** for Mike to send — this is the unblock for four separate items
- [ ] **Add image slots to `platforms.html`** so it's ready the day the model list lands
- [ ] **Relax `MODEL_RE` in `tools/verify.py`** once models are confirmed — the no-model-names guard is self-imposed and correct *until* the ratings are known
- [ ] **Mobile pass at 390px**, page by page, on a real device against the live URL
- [ ] **View the rewritten homepage in a browser** — it's been verified by script and by reading markup, never by eye

---

## 9. Invented content that must be confirmed or killed

Currently rendering on a public URL, sourced from nobody:

| Claim | Where | Status |
| --- | --- | --- |
| **"100% safety-first culture"** | Homepage stat strip | Design filler. Confirm or delete |
| **"24/7 support availability"** | Homepage stat strip | Design filler. **Someone will call at 2am.** Confirm or delete |
| **"Trusted Since 1997"** | Hero eyebrow, History, ×14 places | Flagged as placeholder sitewide. **No age claim goes back until Mike confirms the year** |
| **Six-service list** | Services + homepage | Generic category guesses, not a confirmed offering |
| **Three company values** | About | The site picked them, not the client |
| **Three news articles** | News | Format demos, not stories |
| **"NASA Partnership" framing** | Page title, filename, nav | ⚠️ "Partnership" is the word that implies endorsement. Homepage tile already fixed *in the repo*; the live site still shows it |
| Personal `att.net` address with name + title | Contact | Real, but published on a public URL. Decide if it should be |

---

## 10. The capture day plan

One visit covers 11 of 13 photos, all the video, and three of the five interviews. Rough shape:

**Before going**
- Confirm with the office manager which staff are OK being photographed
- Ask Mike to have the repair station certificate accessible, and to pull the CSF agreement
- Ask whether a customer aircraft will be in the hangar, and whether its owner is OK being filmed
- Charge everything. Bring more storage than seems necessary

**Golden hour, early** — exterior hangar, sign, establishing shots (V6, P1) · aircraft outside if one is available (V1)

**Mid-morning** — shop floor: the dolly shot (V3), hands-on-work tights (V2), hangar wide (V4) · P2, P7, P8 · the certificate on the wall

**Midday** — **sit down with Mike, recorder running** (~90 min). Take his portrait (P4) in the hangar afterward, while he's still in work mode rather than posed

**Afternoon** — the team working (V5) · staff portraits if anyone else is going on the site (P5, P6) · lead mechanic interview on the shop floor · detail and texture coverage

**Golden hour, late** — second pass at the exterior, better light. If the liftoff shot (V1) hasn't happened yet, this is the window

**Before leaving**
- Photograph the office walls — certificates, awards, old photos
- Ask about the historical photo archive (P9) — it's the one slot a visit can't fill by shooting
- Get the FAA certificate and any paperwork photographed or copied
- Confirm names and titles for everyone photographed

---

## 11. Launch gate

What must be true before the site is public and indexed. Everything else can ship incomplete.

**Hard blockers**
- [ ] Contact form reaches a real inbox *(currently: reaches nobody)*
- [ ] No unverified claims live — "100%", "24/7", and any age claim confirmed or removed
- [ ] NASA page cleared in writing, or removed from nav and unpublished
- [ ] No Bell mark on the site unless Bell supplied the artwork and permission
- [ ] No aircraft model named unless it's on the certificate
- [ ] Founding year confirmed, or every age claim stays out
- [ ] Business hours published
- [ ] Public email is one the client actually wants public
- [ ] Mike has seen and signed off on the logo, the copy, and the whole site
- [ ] `robots.txt` and `X-Robots-Tag: noindex` **removed** — the preview is deliberately blocked from search today
- [ ] `python3 tools/verify.py` green
- [ ] Mobile checked on a real device, page by page

**Should be true**
- [ ] Real photos in every slot, or the slot removed — no empty amber boxes
- [ ] Alt text on every image
- [ ] Careers either has openings or explicitly says it doesn't
- [ ] News has real stories, or the page is held back
- [ ] Domain live with matching email
- [ ] OG tags so shared links don't render as a grey box
- [ ] Google Business Profile claimed

---

## 12. Worth suggesting, nobody asked for

- **Google Business Profile** — for a maintenance shop at a regional airport, this plausibly outperforms the entire website for discovery. Cheap, and independent of everything above
- **A capabilities PDF** — a one-page leave-behind built from the same content. Aviation buyers ask for these, and the content is already being gathered
- **Airport directory listings** — AirNav, and whatever the Pearland Regional operator publishes. Both competitors are there
- **A "Request a Quote" flow that actually asks for what Mike needs** — make/model, serial, hours, logbook status — rather than a generic contact form. Turns the form from a nuisance into a working intake
- **Company name is plural: "South Air Helicopters, Inc."** — confirmed on the business card. The repo name is singular and misleading; ignore it
