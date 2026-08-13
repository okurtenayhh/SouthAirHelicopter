# Bell & NASA Trademark Research

*Compiled 2026-07-30 from public sources. This is desk research to compare against
what Bell and NASA actually tell you — not legal advice, and not a substitute for
the written permission both pages already wait on.*

Confidence is marked per finding: **[Authoritative]** = quoted from the regulator or
owner. **[Observed]** = what a comparable company actually does. **[Inferred]** = my
reading, verify it.

---

## NASA — the rules are public, specific, and strict

### The logo: no

**[Authoritative]** The NASA Insignia ("meatball"), Logotype ("worm"), and Seal are
**not in the public domain** and are protected by law under [14 CFR Part 1221](https://www.ecfr.gov/current/title-14/chapter-V/part-1221).
NASA's Brand Center states they "should not be used as branding devices... on
third-party websites or communications material" and may not be "used in or for
advertising, trade dress, promotions, or similar marketing purposes."

14 CFR 1221.110 enumerates who may use the Insignia — NASA letterhead, NASA vehicles,
NASA buildings, employee credentials, and contractor uniforms *only* for public
affairs, guard, or fire protection duties performed inside NASA installations. A
contractor's own commercial website is not on the list.

**Conclusion: the NASA logo cannot go on this site.** There is no permission process
that would plausibly change that — the merchandise approval path exists for
NASA-themed consumer products, not for vendor marketing.

### The endorsement rule: the one that actually bites

**[Authoritative]** "As a U.S. government agency, NASA will not promote, sponsor,
co-create, or endorse — or appear to promote, sponsor, co-create, or endorse — a
commercial product, service, or activity."

And from 1221.110: "No approval for use of the NASA Insignia will be authorized when
its use can be construed as an endorsement by NASA of a product or service."

Explicitly prohibited wording includes **"NASA approved," "official NASA," "genuine
NASA," "authentic NASA," "trusted by,"** or similar.

Note the phrase *appear to*. The test is not whether South Air intends to imply
endorsement — it's whether a reader could construe it. Design choices carry this too:
a NASA reference sitting in a "trusted by" strip alongside customer logos implies
endorsement even if every word is factually true.

### What South Air *can* say

**[Authoritative]** This is the useful part, and it's more permissive than people
assume. JPL's supplier guidance states plainly:

> "Vendors are free to state that JPL is one of their customers, and to describe
> factually the services and products they provide."

So a **factual, specific, unadorned** statement of the relationship is allowed. What
makes it safe is specificity — "we perform [specific work] on [specific aircraft] for
[specific center/program]" is a fact. "Trusted by NASA" is an endorsement claim.

**[Authoritative]** Two catches worth knowing before Mike writes anything:

1. **Prior review may be mandatory.** JPL requires that "vendor news releases and
   other promotional materials (blogs, videos, commercials etc.) must be reviewed and
   approved by JPL." If South Air's work runs through a center with the same rule,
   this page needs sign-off before it goes live — not just Mike's blessing.
2. **No attributed quotes.** Vendors "may not attribute any statements or opinions to
   NASA without explicit permission," and NASA employees may not provide quotes for
   vendor materials. Rules out the testimonial pattern on this page.

**[Inferred]** JPL is a specific center and South Air's work may be with another. The
principles are NASA-wide, but the review requirement is center-specific — that's a
question for whoever administers the contract.

### Photographs — affects the photo request already out to the office manager

**[Authoritative]** Two rules that constrain which photos can be used, worth knowing
*before* the office manager digs through the archive:

- **No identifiable NASA personnel.** Advertising may not use the likenesses, names, or
  personality traits of NASA astronauts or current employees. (Former employees can
  grant permission themselves.)
- **Images must comply with NASA's Media Usage Guidelines.** Many publicly released
  NASA images are usable, but a photo taken *at* a NASA facility is a different matter
  — JPL's parallel rule bars vendor materials from including "images taken on Lab."

**[Inferred]** So if any historical photo shows a NASA facility, NASA hardware, or
identifiable NASA staff, it needs clearing before it goes on the site — even though it
belongs to South Air and shows South Air's own work. Flag this when the photos arrive
rather than after they're laid into a page.

### Contact for NASA brand questions

**[Authoritative]** Requests go in writing to **nasa-merchandise-&-brand-team@mail.nasa.gov**,
and should include a description of the intended use plus layouts where possible.

**[Inferred]** This is the brand team, so it's the right address for "may we word it
this way" — but the contract/center public affairs officer is the better first stop for
questions about the relationship itself. Use both: PAO for what the work *is*, brand
team for how it may be *described*.

### Questions to put to NASA (via Mike's contract contact)

- Which center/program, and is there a public affairs officer who reviews vendor material?
- Does our contract require prior review of marketing that references NASA?
- Can you confirm in writing the exact sentence we may use to describe the work?
- Is there anything about the relationship that is not public / not releasable?

---

## Bell — Bell has now answered, and sent rules in writing

> **Updated 2026-08-06.** Everything in this section down to "What Bell still hasn't
> answered" is now **primary source material from Bell**, not desk research. The desk
> research that follows it is kept because it was largely right and explains *why* the
> questions were asked — but where the two disagree, Bell's own document wins.

### Bell made contact, unprompted, with the seal artwork

**[Authoritative — from Bell]** On 2026-08-06, **Zachariah Langley, CSF Network Manager,
Americas** (zlangley@bellflight.com, 817-280-8123) emailed South Air's sbcglobal address
with the CSF seal artwork attached and a link to Bell's brand portal. This is the
account-rep route the research below predicted, and it worked — **authorization is not in
question and never was.** They closed by inviting further questions, which is the opening
for everything under "What Bell still hasn't answered."

Three things arrived. The source folder is `C:\Users\kourt\Desktop\fwbellcsfbrandingmaterial (1)`
— **not in this repo, deliberately.** The repo is public and this is Bell's trademark
artwork; `tools/verify.py` also fails the build on any Bell-named image in `images/`, and
that guard stays.

1. **The CSF seal, two versions** — full colour and all-black. 750×750px, **CMYK JPEG on a
   white background.** These are print assets for signage. They are *not* usable on the
   website as-is: no transparency, wrong colour space, raster only.
2. **`CSF AMC facility signs_2025.pptx`** — Bell's *Seal Signage Program* deck, revised
   October 2025, covering CSFs, AMCs, Authorized Delivery Centers, Authorized Resellers,
   Customer Training Facilities, and Independent Representatives.
3. **A link to Bell's media hangar, <https://brand.bellflight.com/>** — external vendors
   click "Request access" at the bottom of the login screen. Bell employees use SSO.

### The seal itself does not say "Helicopter"

**[Authoritative — from Bell]** The issued seal reads **"CUSTOMER SERVICE FACILITY"**
around the ring and **"CSF"** on the lower banner, around the red Bell shield with the
dragonfly device. The word "Helicopter" appears nowhere on it. Neither does "Certified."

More pointedly, **the entire deck is about retiring that name.** Slide 2: "CSFs/AMCs
should remove all existing Bell Helicopter signs and install new Bell seal signs," at the
facility's own cost. Slides 4 and 5 are procedures for replacing legacy *Bell Helicopter*
sign panels. So "Bell Helicopter Customer Service Facility" is not merely a dated form —
it is a name Bell is actively paying its network to take down.

This bears directly on the coming-soon page, which carries "Certified Bell Helicopter
Customer Service Facility" as an explicit, twice-affirmed client decision. **That decision
stands until the client changes it** — see Decisions Locked in `PROJECT-STATUS.md`. What's
new is that the objection is no longer an inference from Bell's 2018 rebrand; it is Bell's
own current document. Worth putting to the office manager once, factually, and then
dropping either way.

### The co-branding rules, in Bell's words

**[Authoritative — from Bell]** Slide 3, on size and placement. Written for signage, but
it is Bell's statement of how the seal relates to a facility's own brand, and the
principles carry to a website:

- **"Please make sure that your company signage is the most prominent visual brand."**
- **The seal must be "surrounded by ample clear space and smaller in size than your
  company logo."**
- **"You should never physically connect your company logo or any others directly to the
  Bell seal logo."**
- Where other OEM logos appear, the Bell seal should be **"as equal in size as possible"**
  to them, with **"balanced and equal clear space between them."**

The slide's own mockup shows the pattern plainly: the facility's wordmark large at the
left of the sign, the Bell seal small at the right, an equal-sized slot beside it for
another OEM, generous space around everything.

**This is exactly the reserved badge slot already built on `bell-service-center.html`.**
That design was right before we had the rules; it now has a citation.

### The do-not list

**[Authoritative — from Bell]** Slide 6, "What To Avoid." Six illustrated prohibitions:

| Rule | What it means here |
| --- | --- |
| **Do not rotate the seal.** | No jaunty angles, no CSS transforms. |
| **Do not create company logo or text lockups with seals.** | The seal never becomes part of a South Air composite mark. |
| **Do not create lockups with the Bell shield or use it as a standalone element.** | **Settles the corporate-shield question permanently.** The bare red shield may not appear at all. |
| **Do not substitute the font type or redraw the seals.** | **We cannot hand-build the seal as an SVG.** Bell's own vector file is the only legitimate source — which is what the brand portal is for. |
| **Do not alter the colors** in the shield or any element of the seal. | No recolouring to the site palette, no monochrome variant we invent ourselves. Bell supplies an all-black version; use theirs. |
| **Do not add effects — such as drop shadows — to the seal.** | No CSS shadow, glow, or border treatment on the badge. |

Slide 6 also points to a separate **"Bell Seal Guidelines" document** for the full rules.
**That document was not attached** and is presumably in the brand portal. It is where any
*digital/web-specific* rules would live — the deck we have is signage-only.

### What Bell still hasn't answered

The signage deck answers artwork, placement, and prohibitions. It does not answer:

- **The Bell Seal Guidelines document itself** — the full rules, including web use.
- **Web-format artwork** — RGB, vector or transparent PNG. Summit Aviation serves exactly
  such a file (see below), so it exists.
- **The exact authorized wording** for describing our status in body copy.
- **Whether we may name the models we're rated on** (206 series, 407 series, 429), and how
  those designations should be written.
- **Whether any trademark attribution line is required** in the footer.
- **Whether Bell wants to review the site before launch.**
- **Whether a stylized helicopter may appear in South Air's own logo** — Mike asked for a
  429 specifically. Note slide 6 forbids lockups with the *shield*; it says nothing about
  aircraft, so this genuinely needs asking rather than inferring.

Zachariah invited questions. One reply covers all seven.

**One practical note:** the brand-portal access request should come from a **South Air
address** — Bell is vetting its own vendor network, and a request from an unfamiliar
personal address is a slower path than one from the facility Bell already emailed.

---

### Desk research (2026-07-30) — superseded above, kept for context

### There is no published third-party trademark policy

**[Authoritative]** [Bell's legal page](https://www.bellflight.com/legal) lists Terms
of Use, privacy policies, a copyright notice, and patents — **no trademark or brand
usage policy**. The only contact offered is the Bell Ethics and Compliance Department
(1-800-892-9871, ethics@bellflight.com), which is a compliance hotline, not a brand desk.

The Textron Aviation brand guidelines that turn up in search results
([txtav.com/en/brand](https://txtav.com/en/brand)) are a **different Textron business
unit** — Cessna and Beechcraft. They do not govern Bell marks. Don't cite them at Bell.

**[Inferred]** This means the governing document is almost certainly the **Customer
Service Facility agreement Mike signed with Bell.** Authorized-dealer trademark rights
are conventionally granted as a limited licence inside that agreement, with the brand
rules attached or incorporated by reference. **Ask Mike for his copy of the CSF
agreement and read the trademark clause** — that is the actual answer, and it's sitting
in a filing cabinet rather than on the internet.

### What Bell CSFs actually do in practice

**[Observed]** [Summit Aviation](https://summit-aviation.com/services/maintenance/bell/)
— a Bell Authorized CSF, and one of the two competitors in `market-research.md` —
displays a **Bell-issued CSF seal**: a circular emblem served as `bell_seal_csf_rgb_web2.png`.

That filename matters. It's a Bell-produced RGB web asset, which means **Bell issues
badge artwork to its authorized facilities**. This is a program seal, not the Bell
corporate logo.

Summit also uses the tagline "Your Bell Is Our Business," names specific models, and
carries **no visible trademark attribution or disclaimer**.

**[Inferred]** So the right question for Bell is not *"may we use your logo?"* — which
invites a no. It is:

> "We're an authorized Customer Service Facility. Please send us the current CSF seal
> artwork and any co-branding guidelines that apply, so we use it correctly on our new
> website."

That's a request for something Bell already produces and hands out, and it routes to
someone whose job is to say yes.

### Flag: the wording on the business card may be out of date

> **Confirmed 2026-08-06.** This was inferred; Bell's own signage deck now says it
> outright. See "The seal itself does not say 'Helicopter'" above.

**[Inferred — worth checking]** Mike's card says "**Bell Helicopter** Customer Service
Facility." Bell dropped "Helicopter" from its brand in 2018, becoming simply **Bell**
(legal entity Bell Textron Inc.). Current Bell and CSF materials say "**Bell**
Authorized Customer Service Facility."

The site currently uses the business-card wording. If the card predates the rebrand,
the site is repeating a retired brand name — a small thing that reads as dated to
anyone in the industry, and the kind of detail a Bell rep will notice immediately.
**Confirm the exact current authorized wording when you ask for the artwork.**

### Questions to put to Bell (via Mike's CSF account rep, not the ethics line)

> **Partly answered 2026-08-06** by Zachariah Langley's email — see the top of this
> section. The rep is identified, reachable, and has invited follow-up. The live version
> of this list is now **"What Bell still hasn't answered"** above; the original list is
> kept here to show what was asked and what came back.

- ~~Please send the current CSF seal artwork and any co-branding guidelines.~~
  **Answered** — print artwork received, plus the signage deck's placement and do-not
  rules. Still outstanding: web-format artwork and the full Bell Seal Guidelines document.
- What is the exact authorized wording for our status — "Bell Authorized Customer
  Service Facility"? Does it still include "Helicopter"? **Partly answered** — the seal
  says "Customer Service Facility" with no "Helicopter," and Bell is retiring that name
  from signage. The exact *body-copy* wording is still unconfirmed.
- May we state which Bell models we're authorized to work on, and how should those
  model designations be written? **Unanswered.**
- Is any trademark attribution line required in our footer? **Unanswered.**
- Does Bell need to review the site before launch? **Unanswered.**

---

## What this changes on the site

Nothing yet — no page should change until Bell and NASA answer in writing. But the
research narrows what we're waiting for:

| Page | Current state | What the research says |
| --- | --- | --- |
| `nasa-partnership.html` | Empty, standing pre-publication warning | Warning stays. The **logo is a settled no** — stop treating that as an open question. A factual description is achievable; get the sentence approved, and check whether prior review is contractual |
| `bell-service-center.html` | Empty reserved badge slot, standing warning | The badge slot is **confirmed correct** by Bell's own placement rules (2026-08-06): seal smaller than the company logo, ample clear space, never physically connected. It stays empty until **web-format artwork** arrives from the brand portal — the print JPEGs can't be used, and redrawing the seal is explicitly forbidden |
| `index.html` | No Bell/NASA marks | Keep it that way. **"Trusted by" is verbatim on NASA's prohibited-wording list** — so a trust/logo strip is not merely risky framing, it's the exact phrase NASA names. Don't build one that includes NASA |

Also worth noting: **Summit names Bell models on their site.** South Air's
no-model-names rule is a *self-imposed* accuracy guard pending Mike's confirmation, not
a Bell restriction. Once Mike confirms the ratings, naming models is normal for the
category — and `tools/verify.py` will need its `MODEL_RE` check relaxed at that point.

---

## Sources

- [14 CFR Part 1221 — The NASA Seal and Other Devices](https://www.ecfr.gov/current/title-14/chapter-V/part-1221)
- [14 CFR 1221.110 — Use of the NASA Insignia](https://www.law.cornell.edu/cfr/text/14/1221.110)
- [NASA Brand Center](https://www.nasa.gov/nasa-brand-center/)
- [NASA Advertising Guidelines](https://www.nasa.gov/nasa-brand-center/advertising-guidelines/)
- [NASA STI disclaimers](https://sti.nasa.gov/disclaimers/)
- [JPL Acquisition & Supplier Resources](https://acquisition.jpl.nasa.gov/)
- [Bell legal information](https://www.bellflight.com/legal)
- [Bell brand portal / media hangar](https://brand.bellflight.com/) — external vendors
  request access from the login screen
- **Bell, *Seal Signage Program*, revised October 2025** (`CSF AMC facility signs_2025.pptx`)
  — supplied direct by Bell 2026-08-06. Not in this repo; see the Bell section above for
  where the source folder sits and why it's kept out
- **Bell CSF seal artwork**, colour and all-black, CMYK print JPEGs — supplied with the
  same email
- [Summit Aviation — Bell maintenance](https://summit-aviation.com/services/maintenance/bell/)
