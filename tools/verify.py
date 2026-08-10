#!/usr/bin/env python3
"""Verification checks for the South Air Helicopters site.

Everything here is read-only. Run after any change that touches the shared
header/footer, since copy-paste drift across 10 hand-edited files is this
architecture's main failure mode.
"""

import hashlib
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES = sorted(p.name for p in ROOT.glob("*.html"))

HEADER_RE = re.compile(r'<header class="site-header">.*?</header>', re.DOTALL)
FOOTER_RE = re.compile(r'<footer class="site-footer">.*?</footer>', re.DOTALL)
NAV_LI_RE = re.compile(r'<ul class="nav-links">(.*?)</ul>', re.DOTALL)
HREF_RE = re.compile(r'href="([^"#?:]+\.html)"')
# Bell model designations and common nicknames. Must never appear until
# ownership confirms which airframes the shop is actually rated on.
MODEL_RE = re.compile(
    r"\b(206|407|412|429|505|jetranger|longranger|huey|uh-1)\b", re.IGNORECASE
)
# A founding year is permanent; an age derived from it rots every January.
# State 1979, never "46 years" or "nearly five decades".
AGE_CLAIM_RE = re.compile(
    r"\b\d{1,3}\+?[\s-]?(?:years?|yrs?)\b"
    r"|\b(?:(?:almost|nearly|over|more than|well over|about|roughly)\s+)?"
    r"(?:one|two|three|four|five|six|seven|eight|nine|ten)\s+decades?\b",
    re.IGNORECASE,
)
# 1997 is a transposition of the real founding year that sat in the
# placeholders for several sessions. Pin it so it cannot come back.
FOUNDED = "1979"
WRONG_FOUNDED_RE = re.compile(r"\b(?:1997|1978|1980)\b")

failures = []


def check(label, ok, detail=""):
    print(f"{'PASS' if ok else 'FAIL'}  {label}{'  — ' + detail if detail else ''}")
    if not ok:
        failures.append(label)


# 1. Shared blocks must be byte-identical across every page.
for label, pattern in (("header", HEADER_RE), ("footer", FOOTER_RE)):
    digests = {}
    for name in PAGES:
        found = pattern.findall((ROOT / name).read_text())
        if len(found) != 1:
            failures.append(f"{name}: {len(found)} {label} blocks")
            continue
        digests.setdefault(hashlib.sha256(found[0].encode()).hexdigest(), []).append(name)
    check(
        f"{label} byte-identical across {len(PAGES)} pages",
        len(digests) == 1,
        f"{len(digests)} distinct versions: "
        + "; ".join(f"{d[:7]}={v}" for d, v in digests.items())
        if len(digests) != 1
        else "",
    )

# 2. Nav item count.
for name in PAGES:
    body = NAV_LI_RE.search((ROOT / name).read_text())
    count = body.group(1).count("<li>") if body else -1
    if count != 8:
        failures.append(f"{name}: {count} nav items")
check("every page has 8 nav items", not any("nav items" in f for f in failures))

# 3. Every internal .html link resolves to a real file.
existing = set(PAGES)
broken = set()
for name in PAGES:
    for href in HREF_RE.findall((ROOT / name).read_text()):
        if href not in existing:
            broken.add(f"{name} -> {href}")
check("all internal .html links resolve", not broken, ", ".join(sorted(broken)))

# 4. No aircraft model names anywhere.
hits = []
for name in PAGES:
    for match in MODEL_RE.finditer((ROOT / name).read_text()):
        hits.append(f"{name}:{match.group(0)}")
check("no invented aircraft model names", not hits, ", ".join(hits))

# 5. Dead CSS gone.
css = (ROOT / "css" / "style.css").read_text()
html_all = "".join((ROOT / n).read_text() for n in PAGES)
check("no .pricing-table references", "pricing-table" not in css + html_all)

# 5b. The founding year is confirmed, so guard it on the main site too:
#     no derived age claim, and no near-miss year.
age_hits, year_hits = [], []
for name in PAGES:
    text = (ROOT / name).read_text()
    age_hits += [f"{name}:{m}" for m in AGE_CLAIM_RE.findall(text)]
    year_hits += [f"{name}:{m.group(0)}" for m in WRONG_FOUNDED_RE.finditer(text)]
check("no age claim that will go stale", not age_hits, ", ".join(age_hits))
check("no near-miss founding year", not year_hits, ", ".join(year_hits))

# 6. No Bell logo asset snuck in.
imgs = sorted(p.name for p in (ROOT / "images").glob("*"))
unexpected = [i for i in imgs if "bell" in i.lower()]
check("no Bell-branded image assets", not unexpected, ", ".join(unexpected))

# 7. Every page carries placeholders (a page with none means invented content).
thin = [
    n for n in PAGES if (ROOT / n).read_text().count("PLACEHOLDER") < 3
]
check("every page has >=3 placeholders", not thin, ", ".join(thin))

# 8. quote-strip must never sit inside a .section-alt (its fill would vanish).
misplaced = []
for name in PAGES:
    text = (ROOT / name).read_text()
    for match in re.finditer(r'<section class="section section-alt">(.*?)</section>', text, re.DOTALL):
        if "quote-strip" in match.group(1):
            misplaced.append(name)
check("no .quote-strip inside .section-alt", not misplaced, ", ".join(misplaced))

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
    external += re.findall(r'<iframe\s[^>]*src="(?!data:)[^"]+"', cs, re.IGNORECASE)
    # SVG <image href="…"> / xlink:href="…" — a second way to pull in a raster asset.
    external += re.findall(r'<image\s[^>]*(?:xlink:href|href)="(?!data:)[^"]+"', cs, re.IGNORECASE)
    external += re.findall(r'@import\s+[^;]+;', cs, re.IGNORECASE)
    # Any CSS url(...) that isn't a data: URI — covers background:, @font-face src:,
    # list-style-image, cursor, etc. in one net rather than one property at a time.
    external += re.findall(r'url\(\s*(?!["\']?data:)[^)]+\)', cs, re.IGNORECASE)
    check("coming-soon page is self-contained", not external, ", ".join(external))

    check(
        "coming-soon page carries the confirmed phone number",
        "281.648.5187" in cs and "+12816485187" in cs,
    )

    # The digits 648 and 684 were transposed in a screenshot taken during the
    # domain signup. Caught by eye once; not relying on eyes again. Matched on
    # the bare digit sequence with any (or no) separator between groups, so
    # "(281) 684-5187", "281 684 5187", and "2816845187" are all caught too —
    # not just the two literal forms seen so far.
    transposed = re.findall(r"281\D{0,3}684\D{0,3}5187", cs)
    check("no transposed phone number", not transposed, ", ".join(transposed))

    check(
        "coming-soon page names no aircraft model",
        not MODEL_RE.search(cs),
        ", ".join(m.group(0) for m in MODEL_RE.finditer(cs)),
    )

    # The Bell wording is the office manager's explicit choice (2026-08-04),
    # kept verbatim over the objection that "Bell Helicopter" is a name Bell
    # retired in 2018. Pin the exact approved string: any other Bell phrasing
    # on this page is unapproved use of someone else's trademark.
    APPROVED_BELL = "Certified Bell Helicopter Customer Service Facility"
    check(
        "coming-soon page uses only the approved Bell wording",
        cs.count(APPROVED_BELL) == 1 and cs.lower().count("bell") == 1,
    )

    # Presence of the plural alone isn't enough — the repo directory is named
    # "SouthAirHelicopter" (singular), which invites exactly that typo creeping
    # into the markup while the plural still appears elsewhere (e.g. <title>).
    # Assert the singular form is absent too, matched as a whole word so it
    # doesn't fire on the substring inside "Helicopters".
    singular_hit = re.search(r"South Air Helicopter(?!s)\b", cs)
    check(
        "coming-soon page uses the plural legal name",
        "South Air Helicopters, Inc." in cs and not singular_hit,
        singular_hit.group(0) if singular_hit else "",
    )

    check("coming-soon page states the confirmed founding year", "Established 1979" in cs)

    # "46 years", "27+ yrs", "46-year history", "over four decades" — anything
    # derived from the founding year goes stale silently. Catches numeric forms
    # (with or without a hyphen to the following word) and spelled-out decade
    # claims, optionally qualified ("nearly", "over", "more than", ...).
    AGE_CLAIM_RE = re.compile(
        r"\b\d{1,3}\+?[\s-]?(?:years?|yrs?)\b"
        r"|\b(?:(?:almost|nearly|over|more than|well over|about|roughly)\s+)?"
        r"(?:one|two|three|four|five|six|seven|eight|nine|ten)\s+decades?\b",
        re.IGNORECASE,
    )
    age_claims = AGE_CLAIM_RE.findall(cs)
    check("coming-soon page makes no age claim that will go stale", not age_claims, ", ".join(age_claims))

print()
if failures:
    print(f"{len(failures)} FAILED")
    sys.exit(1)
print(f"all checks passed across {len(PAGES)} pages")
