# Coming-Soon Landing Page Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship a single self-contained landing page that South Air's new domain can point at, carrying real contact details, while the full site stays on its noindexed preview URL.

**Architecture:** One file — `coming-soon/index.html` — with inline CSS and an inline SVG logo, so it has zero external requests and can be deployed from its own directory as a separate Netlify site. `coming-soon/netlify.toml` beside it carries `noindex` while staged, and is read only when the deploy's working directory is `coming-soon` itself — see Task 2 Step 4. `tools/verify.py` gains a guard block for the new page; the existing root-page checks are untouched because they glob the repo root only.

**Tech Stack:** Hand-written HTML5 + CSS. No framework, no build step, no dependencies. Netlify CLI 26.0.2 for deploys. Python 3.14 for `tools/verify.py`.

Spec: `docs/superpowers/specs/2026-08-04-coming-soon-landing-page-design.md` (`aae76bd`).

## Global Constraints

- **Company name is plural and legal-form exact: `South Air Helicopters, Inc.`** Never the singular. The repo directory name is singular and is a trap.
- **Phone is `281.648.5187`** (tel URI `+12816485187`). Confirmed against a photograph of the owner's business card on 2026-08-04. The string `281.684.5187` and any transposed variant must appear nowhere.
- **Email is `sahinc@sbcglobal.net`.** Do not use `mpikesahinc@att.net` — it is on the card but its public status is unconfirmed.
- **Address is `17402 C.R. 127`, `Pearland, TX 77581`.**
- **Certification text is `FAA Repair Station` as one line, `XRIR622K` as the serial below it** — not concatenated into a single string, and not the word "Certified" (that word is on the Bell line, not this one; Mike's card does not say "Certified" for the FAA line).
- **UPDATED 2026-08-04, after the page was staged and reviewed — do not relitigate this.** The page now carries `Certified Bell Helicopter Customer Service Facility` verbatim, as the only Bell mention on the page (`tools/verify.py` pins the exact string and rejects any other Bell wording). This reverses the original constraint below, which forbade the word "Bell" entirely. **This was the client's explicit choice, made over two raised objections, not an oversight to be "fixed":** the office manager reviewed the staged page and asked for the Bell CSF credential to be added; before shipping it, she and the user were shown that (a) "Helicopter" is a name Bell retired from its brand in 2018, and (b) "Certified" appears nowhere on Mike's business card for this line. Both objections were heard and the client chose this wording anyway. See `PROJECT-STATUS.md` → Decisions Locked for the full record. ~~The word "Bell" must not appear on this page in any form, pending the account rep's confirmation of current authorized wording. Not in copy, not in comments, not in meta tags.~~ (superseded)
- **No aircraft model designation anywhere** — `206`, `407`, `412`, `429`, `505`, `JetRanger`, `LongRanger`, `Huey`, `UH-1`. The office manager reported 206/407/429 on 2026-08-04; that is unconfirmed by the owner.
- **No derived age claim** ("since 1997", "27 years", "nearly three decades") — this half still holds and is guarded by `tools/verify.py`. **The founding-year half no longer applies**: the office manager supplied `Established 1979` (with a caveat, "Or 78, whatever Jeff said") and the user ruled 1979 for this page specifically; it now ships in the `.loc` line. That ruling covers this one page, not the main site's ~14 still-placeholder year references — see `PROJECT-STATUS.md`.
- **No business hours** — not yet supplied.
- **No external requests.** No `<link href="http…">`, no `<script src>`, no `<img src>` to a file. Data URIs are permitted.
- **Palette (revised 2026-08-04 against the company's own shirts):** navy `#0b2545`, navy deep `#061529`, plate `#3d4854`/`#2b333d`, edge `#4a5563`, steel `#7d8b99`, royal `#3585cf`, white `#eef2f6`, safety orange `#f26722`. **Safety orange appears exactly once, on the call button.** The old amber `#f2a71b` is gone — the user rejected it and asked for a masculine, mechanical direction. Do not reintroduce it.
- **The identity block is a riveted data plate.** Mark, company name, location, and certificate number sit on a machined gunmetal panel; the actions sit below it, off the plate. This is where the mechanical feel comes from — materials and typography, not the accent colour.
- **Deploy the second Netlify site with an explicit `--site` flag.** `.netlify/state.json` is gitignored and pins the repo to the existing preview site `b2e4b62c-aa66-40cd-a818-e568464a67e6`. Running `netlify link` or an unqualified `netlify deploy` against the new site would repoint it and break the preview deploy workflow.
- **DNS is out of scope.** This plan ends with a staged, noindexed URL. Pointing the domain is a separate, deliberate decision.

---

### Task 1: Guard the page in `tools/verify.py`, then build it

**Files:**
- Modify: `tools/verify.py` (append a new numbered block after check 8, before the `print()` / exit block at lines 103-107)
- Create: `coming-soon/index.html`
- Create: `coming-soon/netlify.toml`

**Interfaces:**
- Consumes: `ROOT` and `MODEL_RE` and `check()`, already defined at `tools/verify.py:14`, `:23`, `:30`.
- Produces: `coming-soon/index.html` — the deploy artifact Task 2 publishes with `--cwd=coming-soon --dir=.` (not `--dir=coming-soon` run from the repo root — that reads the repo-root `netlify.toml` instead of `coming-soon/netlify.toml` and silently serves the wrong noindex value).

- [ ] **Step 1: Confirm the baseline is green before touching anything**

Run: `python tools/verify.py`
Expected: `all checks passed across 10 pages`

If it is not green, stop and fix that first — do not build on a red baseline.

- [ ] **Step 2: Append the guard block to `tools/verify.py`**

Insert after check 8 (the `.quote-strip` check ending at line 101) and before the blank `print()` at line 103.

Note the explicit `encoding="utf-8"`. The existing checks call bare `.read_text()`, which uses the locale codepage on Windows; the new page contains typographic characters, so it must be read as UTF-8 regardless of what the shell's codepage is.

```python
# 9. The coming-soon landing page. Deployed separately from its own directory,
# so it is deliberately outside PAGES: no shared header, no shared footer, no
# placeholders. It is the one page a member of the public will actually see
# before launch, so what it claims is checked tightly instead of loosely.
CS = ROOT / "coming-soon" / "index.html"
if not CS.exists():
    check("coming-soon page exists", False, "coming-soon/index.html missing")
else:
    cs = CS.read_text(encoding="utf-8")

    external = re.findall(r'<link\s[^>]*href="(?!data:)[^"]+"', cs)
    external += re.findall(r'<script\s[^>]*src=', cs)
    external += re.findall(r'<img\s[^>]*src="(?!data:)[^"]+"', cs)
    check("coming-soon page is self-contained", not external, ", ".join(external))

    check(
        "coming-soon page carries the confirmed phone number",
        "281.648.5187" in cs and "+12816485187" in cs,
    )

    # The digits 648 and 684 were transposed in a screenshot taken during the
    # domain signup. Caught by eye once; not relying on eyes again.
    transposed = [n for n in ("281.684.5187", "281-684-5187", "+12816845187") if n in cs]
    check("no transposed phone number", not transposed, ", ".join(transposed))

    check(
        "coming-soon page names no aircraft model",
        not MODEL_RE.search(cs),
        ", ".join(m.group(0) for m in MODEL_RE.finditer(cs)),
    )

    # Bell status is true but the authorized wording is unconfirmed, and unlike
    # the preview this page is destined to be indexed.
    check("coming-soon page claims no Bell status", "bell" not in cs.lower())

    check("coming-soon page uses the plural legal name", "South Air Helicopters, Inc." in cs)
```

- [ ] **Step 3: Run it and watch it fail for the right reason**

Run: `python tools/verify.py`
Expected: `FAIL  coming-soon page exists  — coming-soon/index.html missing`, followed by `1 FAILED`, exit code 1. The ten root-page checks must all still PASS — if any of them flipped, the block was inserted in the wrong place.

- [ ] **Step 4: Create `coming-soon/netlify.toml`**

```toml
# This file is the ONLY thing controlling indexing for the sah-coming-soon site; going live means removing the [[headers]] block below.
# It is read ONLY when the CLI's working directory is this directory. Deploy with:
#   netlify deploy --prod --cwd=coming-soon --dir=. --site=<sah-coming-soon-site-id>
# `--dir=coming-soon` run from the repo root does NOT set the working directory to
# here, so it reads the repo-root netlify.toml instead of this file and silently
# serves that file's noindex value (or its absence) instead of this one.
#
# No top-level `publish` key here on purpose: Netlify only recognises `publish`
# nested under [build], so a bare `publish = "."` at the top level is silently
# ignored — it looks load-bearing and isn't. The deploy command above always
# passes --dir explicitly anyway, so nothing needs to declare it here. Don't add
# it back thinking its absence is an oversight.

[[headers]]
  for = "/*"
  [headers.values]
    X-Robots-Tag = "noindex, nofollow"
```

`coming-soon/netlify.toml` is the indexing control for this site, and it is only read when the CLI's working directory is `coming-soon` — see Task 2 Step 4 for the exact deploy invocation. An earlier revision of this plan used a `_headers` file instead; that was replaced after confirming by real HTTP response that the repo-root `netlify.toml` silently overrode it (its `[[headers]]` block applies to any `--dir` subdirectory deploy run from the repo root regardless of `_headers`' presence). Do not reintroduce `_headers` — it would be dead code again.

The `[[headers]]` block above is deleted as the go-live step, in a later session — see the comment in the file itself.

- [ ] **Step 5: Create `coming-soon/index.html`**

Write the file below verbatim, with one substitution: between the two `LOGO` comment markers, paste the entire contents of **`images/logo-icon-light.svg`** — the rotor icon alone, 836 bytes, *not* the 7KB stacked lockup. The plate sets the company name in type, so the lockup would repeat it.

On the pasted `<svg>` opening tag: delete `role="img"` and `aria-label="…"`, delete `width="200" height="200"` (the CSS sizes it), and add `class="icon" aria-hidden="true"`. Keep `xmlns` and `viewBox` exactly as they are.

**Then recolour the fills — the shipped icon still carries the old palette and pasting it unchanged would put the rejected amber back on the page:**

| Find | Replace | Why |
| --- | --- | --- |
| `#ffffff` | `#eef2f6` | blades and hub, matched to the page white |
| `#7cc0ec` | `#3585cf` | the one contrasting blade, to the shirt royal |
| `#f2a71b` | `#0b2545` | hub centre. **Not** orange — orange appears once, on the call button. Navy reads as a dark hub bolt, which suits the plate |

Leave the path geometry alone; it is generated output.

**Keep the two comment markers, one above the SVG and one below it**, exactly as written in the template. The owner has given a logo direction and this page is expected to be revisited with a new mark; those markers are what make that a single unambiguous replacement rather than a hunt through 7KB of inlined path data.

The `aria-hidden` matters: the `<h1>` directly below the icon names the company in visible text, so the icon is decorative. Without `aria-hidden` a screen reader announces the company name twice.

**UPDATED 2026-08-04 — this block was rewritten to match the shipped `coming-soon/index.html` after two client-requested changes landed post-review: the Bell CSF credential was added (see Global Constraints above), the false "Open and taking work" status line was removed (the office manager flagged the shop is at capacity) along with its duplicate in the meta description, and `Established 1979` replaced it in the `.loc` line. It also carries the WCAG-AA contrast fixes made in the final review pass — a `--label` token for `.stamp-label`, and raised opacity on `.soon` and `.call-label`. This is no longer a build template; it is a record of what actually shipped.** Two things below are abbreviated for readability, not because they differ from the live file: the favicon `<link>`'s base64 payload (`…`, ~1KB, generated from `images/logo-icon-light.svg`), and the inline SVG between the `<!-- LOGO -->` markers (the same rotor-icon SVG described in the recolour table above, present verbatim in the live file).

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>South Air Helicopters, Inc. — Helicopter Maintenance at Pearland Regional Airport</title>
<meta name="description" content="South Air Helicopters, Inc. is an FAA Repair Station at Pearland Regional Airport in Pearland, Texas. Call 281.648.5187.">
<meta name="theme-color" content="#0b2545">
<link rel="icon" href="data:image/svg+xml;base64,…"> <!-- inlined, generated from images/logo-icon-light.svg; abbreviated here, see note above -->
<style>
  :root {
    --navy:      #0b2545;
    --navy-deep: #061529;
    --plate-hi:  #3d4854;
    --plate-lo:  #2b333d;
    --edge:      #4a5563;
    --steel:     #7d8b99;
    --label:     #9aa7b4; /* lightened steel, used only for small stamp-label text so it clears 4.5:1 against the plate gradient — --steel stays as-is for the rule hairline */
    --royal:     #3585cf;
    --white:     #eef2f6;
    --orange:    #f26722;

    --mono: ui-monospace, "Cascadia Mono", "Segoe UI Mono", Consolas, "SF Mono", Menlo, monospace;
    --sans: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, Helvetica, Arial, sans-serif;
  }

  *, *::before, *::after { box-sizing: border-box; }
  html { -webkit-text-size-adjust: 100%; }

  body {
    margin: 0;
    min-height: 100vh;
    min-height: 100svh;
    display: grid;
    place-items: center;
    padding: 2.5rem 1.25rem;
    background: radial-gradient(115% 75% at 50% 0%, #14345c 0%, var(--navy) 48%, var(--navy-deep) 100%);
    color: var(--white);
    font-family: var(--sans);
    line-height: 1.55;
    text-align: center;
    -webkit-font-smoothing: antialiased;
  }

  .wrap { width: 100%; max-width: 27rem; }

  /* ---------- the data plate ---------- */

  .plate {
    position: relative;
    padding: 1.85rem 1.6rem 1.8rem;
    border-radius: 5px;
    background: linear-gradient(180deg, var(--plate-hi), var(--plate-lo));
    border: 1px solid var(--edge);
    box-shadow:
      inset 0 1px 0 rgba(255, 255, 255, 0.10),
      inset 0 -1px 0 rgba(0, 0, 0, 0.40),
      0 20px 45px rgba(0, 0, 0, 0.45);
  }

  .rivet {
    position: absolute;
    width: 9px; height: 9px;
    border-radius: 50%;
    background: radial-gradient(circle at 33% 30%, #c2ccd6, #6d7986 55%, #454f5a);
    box-shadow: 0 1px 1px rgba(0, 0, 0, 0.55);
  }
  .rivet.tl { top: 9px; left: 9px; }
  .rivet.tr { top: 9px; right: 9px; }
  .rivet.bl { bottom: 9px; left: 9px; }
  .rivet.br { bottom: 9px; right: 9px; }

  .icon { display: block; width: 66px; height: auto; margin: 0 auto 1rem; }

  .name {
    margin: 0;
    font-size: clamp(1.02rem, 4.4vw, 1.22rem);
    font-weight: 700;
    letter-spacing: 0.085em;
    text-transform: uppercase;
    color: var(--white);
  }

  .rule {
    width: 46px; height: 1px;
    margin: 1rem auto;
    border: 0;
    background: var(--steel);
    opacity: 0.55;
  }

  .loc {
    margin: 0;
    font-family: var(--mono);
    font-size: 0.7rem;
    letter-spacing: 0.13em;
    text-transform: uppercase;
    color: rgba(238, 242, 246, 0.62);
  }

  .stamp { margin: 1.5rem 0 0; }
  .stamp-label {
    display: block;
    font-family: var(--mono);
    font-size: 0.61rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--label);
    text-wrap: balance;
  }
  .stamp-label + .stamp-label { margin-top: 0.6rem; }
  .stamp-serial {
    display: block;
    margin-top: 0.4rem;
    font-family: var(--mono);
    font-size: clamp(1.1rem, 5.2vw, 1.3rem);
    font-weight: 700;
    letter-spacing: 0.3em;
    /* matches letter-spacing: cancels the trailing space so the serial
       sits on true optical centre rather than 0.15em left of it */
    padding-left: 0.3em;
    color: var(--white);
  }

  /* ---------- below the plate ---------- */

  .lede {
    margin: 1.9rem 0 0;
    font-size: 0.97rem;
    color: rgba(238, 242, 246, 0.74);
    text-wrap: balance;
  }

  .call {
    display: inline-block;
    margin: 0.9rem 0 0;
    padding: 0.8rem 2.4rem;
    border-radius: 4px;
    background: var(--orange);
    color: #231004;
    text-decoration: none;
    box-shadow: 0 8px 20px rgba(242, 103, 34, 0.16);
    transition: transform 0.15s ease, box-shadow 0.15s ease;
  }
  .call:hover, .call:focus-visible {
    transform: translateY(-2px);
    box-shadow: 0 12px 26px rgba(242, 103, 34, 0.24);
  }
  .call:focus-visible { outline: 3px solid var(--white); outline-offset: 3px; }

  .call-label {
    display: block;
    font-family: var(--mono);
    font-size: 0.62rem; font-weight: 700;
    letter-spacing: 0.2em; text-transform: uppercase;
    opacity: 0.90;
  }
  .call-number {
    display: block;
    margin-top: 0.15rem;
    font-size: clamp(1.42rem, 6vw, 1.62rem);
    font-weight: 700;
    font-variant-numeric: tabular-nums;
  }

  .contact { margin: 1.4rem 0 0; padding: 0; list-style: none; }
  .contact li {
    margin-top: 0.5rem;
    font-family: var(--mono);
    font-size: 0.75rem;
    letter-spacing: 0.045em;
    color: rgba(238, 242, 246, 0.72);
  }
  .contact a {
    color: var(--royal);
    text-decoration-thickness: 1px;
    text-underline-offset: 3px;
  }
  .contact a:hover, .contact a:focus-visible { color: var(--white); }

  .soon {
    margin: 1.9rem 0 0;
    padding-top: 1.3rem;
    border-top: 1px solid rgba(125, 139, 153, 0.22);
    font-family: var(--mono);
    font-size: 0.66rem;
    letter-spacing: 0.13em;
    text-transform: uppercase;
    color: rgba(238, 242, 246, 0.55);
  }

  @media (prefers-reduced-motion: reduce) {
    .call { transition: none; }
    .call:hover, .call:focus-visible { transform: none; }
  }
</style>
</head>
<body>
  <main class="wrap">
    <div class="plate">
      <span class="rivet tl" aria-hidden="true"></span>
      <span class="rivet tr" aria-hidden="true"></span>
      <span class="rivet bl" aria-hidden="true"></span>
      <span class="rivet br" aria-hidden="true"></span>

      <!-- LOGO: inlined from images/logo-icon-light.svg — replace everything
           between this comment and the closing marker to swap the mark -->
      <!-- /LOGO -->

      <h1 class="name">South Air Helicopters, Inc.</h1>
      <hr class="rule">
      <p class="loc">Pearland Regional Airport · Texas<br>Established 1979</p>

      <p class="stamp">
        <span class="stamp-label">Certified Bell Helicopter Customer Service Facility</span>
        <span class="stamp-label">FAA Repair Station</span>
        <span class="stamp-serial">XRIR622K</span>
      </p>
    </div>

    <p class="lede">Helicopter maintenance, services, and support.</p>

    <a class="call" href="tel:+12816485187">
      <span class="call-label">Call us</span>
      <span class="call-number">281.648.5187</span>
    </a>

    <ul class="contact">
      <li><a href="mailto:sahinc@sbcglobal.net">sahinc@sbcglobal.net</a></li>
      <li>17402 C.R. 127 · Pearland, TX 77581</li>
    </ul>

    <p class="soon">A new website is on the way</p>
  </main>
</body>
</html>
```

- [ ] **Step 6: Run verify and confirm it passes**

Run: `python tools/verify.py`
Expected: every check PASS, including the six new `coming-soon` lines, ending `all checks passed across 10 pages`.

If `coming-soon page is self-contained` fails, the logo was linked rather than inlined. If `claims no Bell status` fails, check the meta description and any comment left in the SVG.

- [ ] **Step 7: Commit**

```bash
git add coming-soon/index.html coming-soon/netlify.toml tools/verify.py
git commit -m "Add the coming-soon landing page

One self-contained file with inline CSS and an inline SVG logo, so the
domain can point at it with no external requests and no build step.

Leads with contact details rather than an announcement: South Air is an
operating shop, and someone who lands here may need work done this week.

FAA Repair Station only. Bell CSF is held back until the account rep
confirms current wording, since unlike the preview this page will be
indexed. verify.py grows a guard block for it, including a check for the
648/684 phone transposition caught during the domain signup.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 2: Deploy it to its own Netlify site, staged and noindexed

**Files:** none modified. This task produces a URL.

**Interfaces:**
- Consumes: `coming-soon/` from Task 1.
- Produces: a staged HTTPS URL, recorded in `PROJECT-STATUS.md` by Task 4.

- [ ] **Step 1: Get the account slug without an interactive prompt**

Run: `netlify api listAccountsForUser --data "{}"`

Read the `slug` field of the account that owns the existing preview site. `netlify sites:create` prompts for a team when the slug is omitted, and this shell is non-interactive — an unqualified call will hang until it times out.

- [ ] **Step 2: Create the second site**

Run, substituting the slug from Step 1:

```bash
netlify sites:create --name sah-coming-soon --account-slug <slug>
```

Record the returned `site_id`. If the name is taken, append a short suffix and try again; the name only determines the temporary `*.netlify.app` URL and is replaced by the real domain later.

- [ ] **Step 3: Confirm the existing preview link is intact**

Run: `cat .netlify/state.json`
Expected: still `b2e4b62c-aa66-40cd-a818-e568464a67e6`.

If `sites:create` repointed it, restore that value before going further. The preview deploy workflow for the main site depends on it.

- [ ] **Step 4: Deploy**

Run, substituting the new site ID:

```bash
netlify deploy --prod --cwd=coming-soon --dir=. --site=<new-site-id>
```

`--cwd=coming-soon` is what makes the CLI resolve `netlify.toml` from `coming-soon/` instead of the repo root — Netlify CLI picks up `netlify.toml` from its working directory, not from `--site` or `--dir`, so this flag is the one that actually determines which noindex config gets served. `--dir=.` (relative to that new working directory, i.e. still exactly `coming-soon/`) is what keeps the repo's ten root pages out of this deploy. The explicit `--site` is what keeps the link file pointing at the preview.

**`netlify deploy --prod --dir=coming-soon --site=<new-site-id>` (no `--cwd`) is the wrong shape.** Run from the repo root, it leaves the working directory at the repo root, so the CLI reads the repo-root `netlify.toml` — not `coming-soon/netlify.toml` — and silently serves whatever indexing config the root file happens to declare, which may not be noindex at all once the preview site's own config changes. This is not a hypothetical: an earlier deploy in this project's history did exactly this and served the root file's header without error or warning.

Expected: a `Website URL` in the output. Record it.

- [ ] **Step 5: Verify what actually got served, rather than assuming**

Run in PowerShell, substituting the deployed URL.

Note `curl.exe`, spelled with the extension. Bare `curl` in PowerShell is an alias for `Invoke-WebRequest`, which takes entirely different flags and will fail confusingly. And `NUL`, not `/dev/null` — this is Windows.

```powershell
curl.exe -sS -D - -o NUL https://<url>/
curl.exe -sS https://<url>/ | Select-String -Pattern "281\.648\.5187" -AllMatches
```

Expected: `HTTP/2 200`; an `x-robots-tag` header containing `noindex`; at least one phone-number match.

The header check is the one that matters, and check its exact value, not just its presence. The repo root `netlify.toml` also declares an `X-Robots-Tag` for `/*` — its value is `noindex, nofollow, noarchive, nosnippet` (four tokens), while `coming-soon/netlify.toml`'s value is `noindex, nofollow` (two tokens). If the served header is absent, or reads the four-token root value instead of the two-token `coming-soon/netlify.toml` value, the `--cwd` flag in Step 4 did not take effect and the deploy silently read the repo-root config — stop and resolve that before anyone is given the URL, because the page must not be indexed while staged.

- [ ] **Step 6: Confirm the ten-page preview is untouched**

Run: `curl.exe -sS -o NUL -w "%{http_code}" https://south-air-helicopters.netlify.app/`
Expected: `200`. The full-site preview must be unaffected by any of the above.

---

### Task 3: Look at it in a real browser

No page in this project has ever been opened in a browser — the whole site is verified by script and by reading markup. This is the page a customer will see. The streak ends here.

**Files:** possibly `coming-soon/index.html`, if something is wrong.

- [ ] **Step 1: Load the staged URL at phone width**

Use the Chrome tools: `tabs_context_mcp`, then `tabs_create_mcp` with the staged URL, then `resize_window` to 390×844, then `computer` with `action: "screenshot"`.

- [ ] **Step 2: Check the phone-width render against this list**

- The whole page fits without vertical scrolling, or scrolls only slightly.
- The logo is legible and not clipped — it is a stacked mark with a wordmark, and the wordmark is the part that fails first at small sizes.
- `281.648.5187` is the most prominent element on the screen.
- Nothing overflows horizontally.
- The digits read `648`, not `684`. Read them off the screenshot deliberately.

- [ ] **Step 3: Load at desktop width**

`resize_window` to 1280×800, screenshot again. The card is centred and does not stretch; the gradient reads as intentional rather than as a flat block.

- [ ] **Step 4: Tap-target check**

Run `read_page` and confirm the `tel:` link resolves to `tel:+12816485187`. A wrong `tel:` URI is invisible on a screenshot and dials a stranger.

- [ ] **Step 5: Fix and redeploy if needed**

If anything above fails, edit `coming-soon/index.html`, re-run `python tools/verify.py`, redeploy with the Task 2 Step 4 command (`netlify deploy --prod --cwd=coming-soon --dir=. --site=<site-id>` — not `--dir=coming-soon` from the repo root, which reads the wrong `netlify.toml`), and re-screenshot. Commit any fix separately with a message naming what the screenshot showed.

---

### Task 4: Update the tracker and open the PR

`PROJECT-STATUS.md` is the project's single handoff artifact and this session moved several things it records.

**Files:**
- Modify: `PROJECT-STATUS.md`

- [ ] **Step 1: Record what became real**

In *Waiting On The Client*, and in *Content: Real vs Placeholder* where relevant:

- Phone `281.648.5187` **re-confirmed** against a photo of the business card. Note that a screenshot from the Squarespace domain signup showed `281-684-5187`, and that the registrar account may carry that typo — an action item for the user, not for the site.
- **The domain has been purchased through Squarespace.** Move this out of *Waiting On*. The exact domain string is still outstanding; keep that one line.
- **Bell issued South Air the CSF seal** — it is printed on the owner's business card (red shield, dragonfly device, ringed "Customer Service Facility"). This narrows the ask to the account rep from "may we display a mark" to "please send current artwork". Note that the card reads "Bell **Helicopter** Customer Service Facility", so the seal on it is likely the pre-2018 version and must not be scanned off the card.
- **Aircraft ratings reported as 206 / 407 / 429** by the office manager on 2026-08-04, via text message. File under Mike, still unconfirmed — it has not been checked against the certificate, and `tools/verify.py` still blocks those strings by design.

- [ ] **Step 2: Record the new logo direction**

Under *Decisions Locked*, extend the existing logo entry. The owner has given a direction — a helicopter with "South Air Helicopters" or "South Air" in the mark — which outranks both the current mark and the parked sphere exploration. Record the two objections raised so they are not rediscovered: the supplied reference image is a wall-art product listing and is someone else's copyrighted artwork, and a recognizable Bell airframe inside South Air's own logo asserts affiliation in a way the CSF seal does not. Record the proposed compromise: a stylized helicopter not identifiable as a specific model.

- [ ] **Step 3: Add the landing page to the tracker**

New line in the header block for the staged URL, and a *Content: Real vs Placeholder* row noting this is the one page with no placeholders because every line on it is confirmed.

- [ ] **Step 4: Correct the In Flight branch list**

It currently claims two unmerged branches. There were three — `claude/status-2026-07-30` was pushed with no PR and omitted itself. This branch is built on top of it, so the PR lands both. Rewrite the section to match reality.

- [ ] **Step 5: Refresh the header line**

Update the "last updated" date to 2026-08-04, the branch, and the commit.

- [ ] **Step 6: Commit and push**

```bash
git add PROJECT-STATUS.md
git commit -m "Fold in the office manager's answers and the domain purchase

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
git push -u origin claude/coming-soon-page
```

- [ ] **Step 7: Open the PR**

Title: `Add a coming-soon landing page for the new domain`

The body should state that it also carries last session's tracker commit, list the staged URL, and state explicitly that no DNS change has been made and the page is not public.

---

## Out of scope

- **Pointing the domain.** Deliberately a separate decision, taken after someone has looked at the staged page on a real phone.
- **Removing `noindex`.** Same step as the DNS change.
- **The logo.** Queued as the next task. This page is expected to be revisited once the owner approves a mark.
- **Adding Bell CSF wording or the seal.** Waiting on the account rep.
- **The contact form, `platforms.html`, and every other open item** on the full site. Untouched here.
