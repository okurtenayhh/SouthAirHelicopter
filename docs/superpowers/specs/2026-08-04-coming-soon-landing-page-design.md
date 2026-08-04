# Coming-Soon Landing Page — Design

*2026-08-04 · branch `claude/coming-soon-page`*

## Why

South Air Helicopters has bought a domain (registrar: Squarespace, which absorbed
Google Domains in 2023). The full site is built but most of its copy is still flagged
placeholder text and nothing has been approved by the owner, so it cannot go on a
public domain yet.

This page fills the gap: a single page the domain can point at today, carrying real
contact details, while the full site keeps its noindexed preview URL for Mike's review.

It is temporary by design. It is deleted when the real site launches.

## Framing decision

**The page leads with "open for business," not "coming soon."**

South Air is a long-established operating business, not a launch. (No figure is given
here on purpose — the founding year is still unconfirmed and age claims are barred
sitewide until Mike supplies it.) Someone who finds this page may be a customer who
needs a helicopter serviced this week. A
coming-soon teaser implies the *business* is new and buries the phone number under an
announcement nobody arrived for.

So: company identity and contact details are the page. The new-website line is a
footnote at the bottom.

## Content

Every line below is either FAA public record or already treated as confirmed on the
live site. Nothing is invented, so this page carries **no placeholder blocks** — the
first page in the project that legitimately doesn't need them.

| Element | Value | Source |
| --- | --- | --- |
| Mark | rotor icon, `logo-icon-light.svg` | ships on all 10 site pages today |
| Company | South Air Helicopters, Inc. | business card (legal name, plural) |
| Descriptor | Helicopter maintenance, services, and support at Pearland Regional Airport | already unflagged in the site footer |
| Status line | We're open and taking work | framing decision above |
| Phone | 281.648.5187 | **business card, re-confirmed 2026-08-04** |
| Email | sahinc@sbcglobal.net | business card |
| Address | 17402 C.R. 127, Pearland, TX 77581 | business card |
| Certification | FAA Certified Repair Station #XRIR622K | business card; FAA public record |
| Closing | A new website is on the way. | — |

### Deliberately absent

- **Bell Customer Service Facility.** True, and the strongest credential the company
  has, but the business card wording ("Bell **Helicopter** Customer Service Facility")
  is a name Bell retired in 2018. Publishing a guess at the current wording on an
  indexed page means correcting it publicly later. Holding until the Bell rep answers
  — days away, not months. See `docs/trademark-research.md`.
- **Business hours** — not yet supplied by the office manager.
- **Founding year** and any derived age claim — unconfirmed; see the standing
  constraint in `PROJECT-STATUS.md`.
- **Service list** — the site's six services are generic category guesses.
- **Aircraft ratings (206 / 407 / 429)** — reported by the office manager
  2026-08-04, not yet confirmed by the owner against the certificate.

## Visual direction

**Signature: the page is an aircraft data plate.**

Every certified aircraft carries a riveted metal plate stamped with manufacturer,
model, and serial number. It is the most characteristic object in this shop's world,
and South Air has its own version of the serial: **Repair Station #XRIR622K**. Treating
it as a stamped serial is true to what it actually is, not decoration applied to it.

So the identity block — mark, company name, location, certificate number — sits on a
machined gunmetal panel with rivets at its corners. The actions sit below it, off the
plate. The plate is who they are; the buttons are how you reach them.

This is where the "masculine mechanical" feel the user asked for comes from: materials
and typography, not the accent colour. That keeps the accent free to do one job.

### Palette

Confirmed against the company's own shirts on 2026-08-04. The office manager: *"We use
this blue and navy primarily."* Mike, asked whether he preferred navy or something
lighter: *"Navy is fine."*

| Token | Hex | Role |
| --- | --- | --- |
| Navy | `#0b2545` | page ground |
| Navy deep | `#061529` | gradient floor |
| Plate high / low | `#3d4854` / `#2b333d` | the machined panel |
| Edge | `#4a5563` | plate border |
| Steel | `#7d8b99` | rules, rivets, small labels |
| Royal | `#3585cf` | **sampled from the shirt** — links, status |
| White | `#eef2f6` | stamped type |
| Safety orange | `#f26722` | the call button, and nothing else |

The royal was measured across the shirt photograph: hue 211°, saturation 0.73, with
lighting spreading the value from `#1b4784` in shadow to `#55a6e9` on the lit shoulder.

Two notes on how this palette was arrived at, so it is not re-litigated. The project's
previous steel blue `#2f7fb8` was carried from the user's original sketch and turned out
to be hue 205° — within six degrees of the real garment, so this is a nudge rather than
a replacement. And the previous amber `#f2a71b` was the only genuinely invented colour
in the project; the user rejected it and asked for a masculine, mechanical direction.
Safety orange `#f26722` replaces it: hue 22° against the blue's 211°, so a true
complement, and it is the language of hi-vis equipment rather than of gold.

### Type

No web fonts — the page must make no external requests, and base64-embedding a face is
not worth the weight for one temporary page. The pairing is therefore built from system
stacks, which suits the brief rather than merely conceding to it:

- **Monospace** (`ui-monospace, "Cascadia Mono", "Segoe UI Mono", Consolas, "SF Mono", Menlo`) for the serial, the labels, the address, and the footer. Monospace is the native typography of part numbers, torque tables, and placards.
- **System sans** for the company name, the one-line description, and the phone number. The name is uppercased in CSS with wide tracking so it reads stamped; the source text keeps its correct mixed case.

The phone number stays in the sans rather than the mono. The button is already the only
hot element on the page; making it the odd typeface as well is one accessory too many.

## Architecture

A **single self-contained file** at `coming-soon/index.html`: inline CSS, inline SVG
logo, no external requests. One file is the whole deliverable.

```
coming-soon/
  index.html     the page — inline everything
  _headers       X-Robots-Tag: noindex while staged
```

### Why a subdirectory and a second Netlify site

The alternative considered was a host-scoped rewrite in `netlify.toml` — Netlify
supports domain-qualified `from` URLs, so one site could serve the landing page on the
real domain and the full site on the `netlify.app` URL. Rejected: if that rule ever
fails open, the public domain serves the unfinished, placeholder-riddled site. Two
separate sites make the worst case "the landing page is briefly wrong" instead of
"the unfinished site is public."

Convenient consequence: `tools/verify.py:15` globs `ROOT.glob("*.html")` — repo root
only — so a page in a subdirectory is invisible to the existing checks. None of them
have to be weakened to accommodate a page that legitimately has no shared nav, no
shared footer, and no placeholders.

### Logo swap

The page uses `logo-icon-light.svg` — the rotor icon alone, not the full stacked
lockup — because the plate already sets the company name in type and the lockup would
repeat it. The icon is also 836 bytes against the lockup's 7KB, which keeps the inlined
file readable.

Mike has given a logo direction (a helicopter, with "South Air Helicopters" or "South
Air" in the mark). That work is queued next, and this page is expected to be updated
with the approved mark before the domain is pointed at it. The inline SVG is wrapped in
a clearly delimited comment block so the swap is a single edit.

**A constraint discovered 2026-08-04 that belongs to the logo task, recorded here so it
is not lost:** the company has bought a Brother embroidery machine and intends to make
its own shirts once a mark is settled. Embroidery cannot render gradients or hairlines,
every colour is a thread change, and text below roughly 5mm cap height collapses. This
is also the most persuasive available argument against the detailed line-art helicopter
Mike asked for — at chest-pocket size it will not stitch legibly, which is a point a
shop owner will find more compelling than a trademark argument.

## Verification

`tools/verify.py` gains one small check for this page — it is otherwise unverified,
which is worse than the guard being trivial:

- the file exists and is self-contained (no `<link>`, `<script src>`, or `<img src>`)
- the confirmed phone number `281.648.5187` appears, and the transposed `281.684.5187`
  appears nowhere
- no aircraft model name (reuses the existing `MODEL_RE`)
- no Bell-branded wording pending the rep's answer

Root-page checks are untouched.

Beyond the script: the staged URL gets loaded in a real browser and screenshotted at
390px and 1280px before anyone calls it done. No page in this project has ever had a
real-browser pass; this one is small enough that there's no excuse.

## Deployment

Staged first, pointed second — deliberately two steps.

1. **This session.** Deploy to a separate Netlify site at a temporary URL, `noindex`
   on. User and office manager review it on a real phone.
2. **Later, as its own decision.** Remove the `noindex` header, point the Squarespace
   DNS at Netlify. Public and indexable from that moment.

The gap between them exists because this page becomes the first thing Google knows
about the company. A wrong digit or a typo'd company name is cheap to fix before that
and awkward after.

The existing preview at `south-air-helicopters.netlify.app` is untouched throughout.

## Open items

- **Exact domain as registered** — still needed. Required for step 2 only; does not
  block the build.
- **The Squarespace account may carry a typo'd phone number.** A screenshot taken
  during signup shows `281-684-5187`; the business card reads `281.648.5187`. Worth
  correcting at the registrar.
- **`mpikesahinc@att.net`** appears on the business card and nowhere on the site.
  Unclear whether it is public-facing. Not used here.
