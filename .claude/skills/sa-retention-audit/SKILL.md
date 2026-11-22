---
name: sa-retention-audit
description: Use when reviewing South Air Helicopters site pages from a marketing or visitor-retention point of view — "audit the site", "will this lose customers", "does this page convert", "anything that sends people away", before a launch or a client review, or after copy changes to index/about/services/contact.html.
---

# SA Retention Audit

## The one goal

Every visitor is an operator, owner or chief pilot deciding where to send an aircraft.
**The site succeeds when they call 281.648.5187 or send a message. It fails when they
leave.** Audit every line against one question: *does this move them toward the phone,
or give them a reason to go?*

The owner's rule (2026-11-22): **if someone needs help or doesn't see what they need,
they should just call.** So the site never tells a visitor what the shop won't do — it
tells them to call and ask.

## The audit, in order

Read all four launch pages in full (`index.html`, `about.html`, `services.html`,
`contact.html`), including meta tags, panels, cards and the footer. Then work this list.

### 1. Turn-aways — the top priority, always reported first

Anything that could make a visitor decide "they can't help me" without calling.
Search the markup, don't rely on skimming — these hide in panels, `<dl>` lists and
card grids, not just paragraphs:

```
grep -niE "don't|do not|won't|not something|no (fuel|tie|fly)|only|sent out|go out|very few|isn't|aren't|outside|unless|except" *.html
```

Read every hit. Typical turn-aways:
- **Exclusion lists**: "what we don't do", no fueling, no tie-downs, no flying,
  ground runs only, engines sent out, avionics elsewhere.
- **Gatekeeping**: "if it isn't something we do, we'll tell you", "very few fly in and
  out the same day", "we don't do a lot of quoting".
- **Down-ranking a contact route** the page also offers ("a phone call, not a quote form"
  next to a Send a Message button).

Fix shape: **cut it**, or **reframe it as a capability plus "call and ask"**.
"Engines go out" becomes "we handle engine removal, installation and return to
service". Never replace a turn-away with a new capability claim that isn't confirmed
(see the facts rule below).

### 2. Dead ends

- Every page ends with a call action (the `cta-band` with the phone number). A page
  that ends on content is a dead end.
- The phone number is reachable without scrolling on a phone (390px wide).
- Links that lead *off* the site (maps, outside email apps) are fine; links to pages
  that aren't launched are not.

### 3. Friction on the way to the phone

- `tel:` links on every visible number.
- On the form, can a visitor give a call-back number easily, and is the most common
  reason (maintenance/service) easy to pick?
- After-hours wording: a visitor seeing "8 to 5" plus "AOG" should know what to do.
  If the answer isn't confirmed, that is a client question — not copy you write.

### 4. Credibility that keeps them reading

Specific, sourced facts beat adjectives: 1979, Bell CSF since 1981, FAA #XRIR622K,
no maintenance-related accident since 1979. Flag generic lines that any shop could
use ("quality service", "trusted", "full-service", "reach out").

## The facts rule — every fix must obey this

A fix may only use facts that are already confirmed. Confirmed means: on the current
pages, in `PROJECT-STATUS.md`'s "Real" column, or in the client's own answers in
`private/` (read them; **never quote `private/` into anything committed or published
beyond the confirmed fact itself**).

When a fix needs a fact you don't have — response times, same-day turns, after-hours
procedure, model lists, service area, testimonials — **do not write it into
replacement copy**, not even with "[client to confirm]". Put it in the
**Client questions** section of the report as a question.

Locked decisions that fixes must respect (see `PROJECT-STATUS.md` → Decisions Locked):
- **No aircraft model names** anywhere on the site, for now.
- **No exact ages** ("47 years"); floors like "45+" are fine. `tools/verify.py` enforces it.
- **No NASA content.** **Bell:** factual relationship only, no logo or shield, nothing
  implying endorsement.
- **The client's own sentences stay as written.** "Quality and safety is our priority,
  and our history reflects it." is verbatim — do not fix its grammar.
- **No placeholders** on launch pages.

## Report format

Exactly these three sections, in this order:

**Turn-aways** — every one found, each as: `file:line` · quoted text · fix (cut, or exact
replacement built only from confirmed facts).

**Other fixes** — dead ends, friction, credibility; same format, most-impactful first.

**Client questions** — facts the site would benefit from that only the client can
supply, phrased as a question to ask the office manager. No copy here.

## Common mistakes

| Mistake | Instead |
|---|---|
| Skimming paragraphs and missing a navy "What we don't do" panel | Run the grep; read panels, cards and `<dl>`s |
| Writing "Same-day turns available" as a fix | Ask it as a client question |
| Suggesting a Bell model list for clarity | Model names are locked off the site |
| Correcting the client's grammar | Verbatim lines stay |
| Adding new sections or pages | Audit what's there; new content is a client question |
