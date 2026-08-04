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
| Logo | current mark, `logo-primary-light.svg` | ships on all 10 site pages today |
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

Mike has given a logo direction (a helicopter, with "South Air Helicopters" or "South
Air" in the mark). That work is queued next, and this page is expected to be updated
with the approved logo before the domain is pointed at it. The inline SVG is wrapped
in a clearly delimited comment block so the swap is a single edit.

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
