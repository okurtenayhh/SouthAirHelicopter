# Visual restyle — "2b": Hyundai calm, workshop details

*Approved by the user 2026-11-22.*

## Why

The site read as a generic AI template: system font, blue-to-sky gradient hero,
rounded white cards with soft shadows, line icons. The user wants it to feel
**masculine, grown, reliable**. The reference given was Hyundai, mixed with the
coming-soon page's riveted data-plate look. Of the mockups shown, the user picked **2b**:
the logo's navy leads, gunmetal supports, and orange is used sparingly.

## Approaches considered

1. **Bundle the fonts with the site (chosen).** Self-hosted woff2, SIL OFL. Keeps the
   site's no-external-dependencies rule, sends nothing to Google, and renders the same
   everywhere. Costs about 150 KB.
2. Google Fonts CDN. One line, but it adds a third-party dependency and calls Google on
   every page view.
3. System fonts only. Ruled out: there is no slab serif that's reliable across
   platforms, so the headings would look different on every device.

## Design

- **Color.** Navy `#1e3a5f` (the logo band) for the hero and main color areas; deep
  navy `#14283f` for the nav bar. Gunmetal `#3d4854`→`#2b333d` only for the data plate
  and the closing call band. Safety orange `#f26722` for the header call button and one
  accent rule. No gradients from navy to sky. The accessibility tints already in
  `style.css` stay.
- **Type.** Zilla Slab 500/600 for headings. Inter Tight 300–600 for body text. IBM Plex
  Mono 500 for hard numbers and small labels (XRIR622K, KLVJ, 1979, the phone number).
- **Details.** Square corners; thin rules instead of shadowed cards; more white space;
  the phone number in the header on every page; a riveted data plate (Established 1979
  · Bell CSF 1981 · Repair Station XRIR622K) overlapping the Home hero, replacing the
  stats strip.

## Unchanged / out of scope

All copy, the real logo, page structure, and the coming-soon page. No photos, no new
pages.

## Done means

`tools/verify.py` green (header and footer still byte-identical across pages); text
contrast at least 4.5:1; Home, About, Services and Contact checked at 390px and
1280px with no sideways scroll; review link redeployed.
