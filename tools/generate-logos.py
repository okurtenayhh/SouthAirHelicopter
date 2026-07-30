"""Generate the South Air Helicopters logo family as production SVGs.

The committed SVGs in images/ are self-contained — all type is converted to
outlines, so nothing here is needed just to *use* the logos. Keep this script
for when a mark needs regenerating (new colour, new lockup, tweaked geometry).

To run it you need the two source faces as .woff2 in a sibling fonts/ folder:

    fonts/Big_Shoulders_Display_800.woff2   (variable; pinned to wght=800 below)
    fonts/Titillium_Web_700.woff2
    fonts/Titillium_Web_600.woff2

Both are SIL Open Font License faces from Google Fonts. Then:

    pip install fonttools brotli
    python3 tools/generate-logos.py images

Every mark is built from one shared blade profile (see `blade`) so the badge
and the standalone rotor icon stay visibly part of the same family.
"""
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.misc.transform import Transform
from fontTools.varLib import instancer
import os

FONTDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")

# Big Shoulders ships as a variable font whose default instance is Thin (wght=100).
# Pin the axes we actually want before pulling outlines, or the monogram draws hairline.
AXES = {"Big_Shoulders_Display_800.woff2": {"wght": 800}}

_cache = {}


def load(fname):
    if fname not in _cache:
        f = TTFont(os.path.join(FONTDIR, fname))
        if "fvar" in f:
            f = instancer.instantiateVariableFont(f, AXES[fname], updateFontNames=False)
        _cache[fname] = (f, f.getGlyphSet(), f.getBestCmap(), f["head"].unitsPerEm)
    return _cache[fname]


def cap_height(fname, em_size):
    f, _, _, upem = load(fname)
    return f["OS/2"].sCapHeight / upem * em_size


def text_paths(fname, text, em_size, tracking_em=0.0):
    """Return (list_of_path_d, total_advance_width, ymin, ymax) laid out at y=0 baseline."""
    f, gs, cmap, upem = load(fname)
    s = em_size / upem
    tracking = tracking_em * em_size
    x = 0.0
    ds = []
    ymin, ymax = 1e9, -1e9
    for ch in text:
        gname = cmap[ord(ch)]
        pen = SVGPathPen(gs, ntos=lambda v: f"{v:.2f}")
        tpen = TransformPen(pen, Transform(s, 0, 0, -s, x, 0))
        gs[gname].draw(tpen)
        d = pen.getCommands()
        if d.strip():
            ds.append(d)
            bp = BoundsPen(gs)
            gs[gname].draw(bp)
            if bp.bounds:
                ymin = min(ymin, -bp.bounds[3] * s)
                ymax = max(ymax, -bp.bounds[1] * s)
        x += gs[gname].width * s + tracking
    x -= tracking  # no trailing track
    if ymin > 1e8:
        ymin, ymax = 0, 0
    return ds, x, ymin, ymax


def text_group(fname, text, em_size, cx, baseline_y, fill, tracking_em=0.0, anchor="middle"):
    ds, w, _, _ = text_paths(fname, text, em_size, tracking_em)
    if anchor == "middle":
        tx = cx - w / 2
    elif anchor == "start":
        tx = cx
    else:
        tx = cx - w
    inner = "".join(f'<path d="{d}"/>' for d in ds)
    return (
        f'<g transform="translate({tx:.2f},{baseline_y:.2f})" fill="{fill}">{inner}</g>',
        w,
    )


# ---------------------------------------------------------------- geometry
def blade(length, root_hc=6.0, tip_hc=2.2, sweep=-10.0, tip_rise=-4.0):
    """Canonical tapered rotor blade pointing +x from hub at origin.

    Leading edge bows via `sweep`; the tip sits at `tip_rise` (negative = up).
    Every mark in the family reuses this one profile.
    """
    L = length
    return (
        f"M 0 {-root_hc*0.55:.2f} "
        f"Q {L*0.39:.2f} {sweep:.2f} {L:.2f} {tip_rise:.2f} "
        f"Q {L:.2f} {tip_rise+tip_hc*0.55:.2f} {L:.2f} {tip_rise+tip_hc:.2f} "
        f"Q {L*0.58:.2f} {tip_hc+2.0:.2f} 0 {root_hc:.2f} Z"
    )


def hub(cx, cy, r_ring, ink, rivet, ring_op=0.55):
    return (
        f'<circle cx="{cx}" cy="{cy}" r="{r_ring:.2f}" fill="none" stroke="{ink}" '
        f'stroke-width="{r_ring*0.12:.2f}" opacity="{ring_op}"/>'
        f'<circle cx="{cx}" cy="{cy}" r="{r_ring*0.65:.2f}" fill="{ink}"/>'
        f'<circle cx="{cx}" cy="{cy}" r="{r_ring*0.23:.2f}" fill="{rivet}"/>'
    )


def rotor_topdown(cx, cy, length, ink, accent, rivet, disc=None):
    """Three-blade rotor seen from above — the icon mark."""
    b = blade(
        length,
        root_hc=length * 0.095,
        tip_hc=length * 0.035,
        sweep=-length * 0.149,
        tip_rise=-length * 0.054,
    )
    parts = []
    if disc:
        parts.append(
            f'<circle cx="{cx}" cy="{cy}" r="{length*1.3:.2f}" fill="none" stroke="{disc}" '
            f'stroke-width="1" stroke-dasharray="3 5" opacity="0.5"/>'
        )
    fills = [ink, accent, ink]
    for i, fill in enumerate(fills):
        parts.append(
            f'<g transform="translate({cx},{cy}) rotate({i*120})">'
            f'<path d="{b}" fill="{fill}"/></g>'
        )
    parts.append(hub(cx, cy, length * 0.20, ink, rivet))
    return "".join(parts)


def rotor_side(cx, cy, reach, ink, rivet, accent=None):
    """Two-blade rotor seen edge-on, blades coning down at rest — tops the badge.

    Proportions track `reach` so the badge and the icon share one blade family.
    """
    b = blade(
        reach,
        root_hc=reach * 0.088,
        tip_hc=reach * 0.033,
        sweep=-reach * 0.038,
        tip_rise=reach * 0.060,
    )
    parts = [
        f'<g transform="translate({cx},{cy})"><path d="{b}" fill="{ink}"/></g>',
        f'<g transform="translate({cx},{cy}) scale(-1,1)"><path d="{b}" fill="{ink}"/></g>',
    ]
    if accent:
        t = reach * 0.86
        parts.append(
            f'<path d="M {cx-t:.2f} {cy+7.0:.2f} Q {cx-t*0.55:.2f} {cy+1.5:.2f} {cx-t*0.30:.2f} {cy+0.4:.2f}" '
            f'stroke="{accent}" stroke-width="1.5" fill="none" opacity="0.45" stroke-linecap="round"/>'
        )
        parts.append(
            f'<path d="M {cx+t:.2f} {cy+7.0:.2f} Q {cx+t*0.55:.2f} {cy+1.5:.2f} {cx+t*0.30:.2f} {cy+0.4:.2f}" '
            f'stroke="{accent}" stroke-width="1.5" fill="none" opacity="0.45" stroke-linecap="round"/>'
        )
    parts.append(hub(cx, cy, reach * 0.145, ink, rivet))
    return "".join(parts)


BSD = "Big_Shoulders_Display_800.woff2"
TW7 = "Titillium_Web_700.woff2"
TW6 = "Titillium_Web_600.woff2"


# ---------------------------------------------------------------- marks
def mark_icon(ink, accent, rivet, disc=None, size=200):
    """B — three-blade rotor, standalone."""
    body = rotor_topdown(100, 100, 74, ink, accent, rivet, disc)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="{size}" height="{size}" '
        f'role="img" aria-label="South Air Helicopters rotor mark">{body}</svg>'
    )


def mark_badge(ink, accent, rivet, with_wordmark=True):
    """A+B — circle badge, SA monogram, side rotor. The primary signature."""
    CY, R, MONO = 104, 68, 92
    p = []
    p.append(rotor_side(100, CY - R + 12, 92, ink, rivet, accent))
    p.append(f'<circle cx="100" cy="{CY}" r="{R}" fill="none" stroke="{ink}" stroke-width="5"/>')
    # optically centre the monogram on the circle using real cap height
    mono, _ = text_group(BSD, "SA", MONO, 100, CY + cap_height(BSD, MONO) / 2, ink, tracking_em=0.04)
    p.append(mono)
    top, height = 30, 148
    if with_wordmark:
        w1, _ = text_group(TW7, "SOUTH AIR", 27, 100, 212, ink, tracking_em=0.20)
        w2, _ = text_group(TW6, "HELICOPTERS", 14, 100, 233, accent, tracking_em=0.34)
        p.extend([w1, w2])
        height = 209
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 {top} 200 {height}" '
        f'role="img" aria-label="South Air Helicopters">{"".join(p)}</svg>'
    )


def mark_horizontal(ink, accent, rivet):
    """C — one-baseline lockup for headers, letterhead, email signatures."""
    CX, CY, R, MONO = 44, 50, 29, 38
    p = []
    p.append(rotor_side(CX, CY - R + 1, 42, ink, rivet))
    p.append(f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="none" stroke="{ink}" stroke-width="3.4"/>')
    mono, _ = text_group(BSD, "SA", MONO, CX, CY + cap_height(BSD, MONO) / 2, ink, tracking_em=0.04)
    p.append(mono)
    w1, w1w = text_group(TW7, "SOUTH AIR", 25, 88, 48, ink, tracking_em=0.13, anchor="start")
    w2, w2w = text_group(TW6, "HELICOPTERS", 12.4, 88, 67, accent, tracking_em=0.235, anchor="start")
    p.extend([w1, w2])
    total = 88 + max(w1w, w2w) + 6
    # crop to the artwork so a CSS height maps to real visual size, not padding
    top, height = 11, 74
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 {top} {total:.0f} {height}" '
        f'role="img" aria-label="South Air Helicopters">{"".join(p)}</svg>'
    )


def mark_favicon(bg, ink, accent, rivet):
    """Icon mark on its own ground — a bare rotor vanishes on both light and dark tabs."""
    body = rotor_topdown(50, 50, 33, ink, accent, rivet)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" '
        f'role="img" aria-label="South Air Helicopters">'
        f'<rect width="100" height="100" rx="18" fill="{bg}"/>{body}</svg>'
    )


NAVY, SKY, AMBER = "#0b2545", "#2f7fb8", "#f2a71b"
PAPER, SKY_L, AMBER_L = "#ffffff", "#7cc0ec", "#f2a71b"

if __name__ == "__main__":
    import sys

    outdir = sys.argv[1]
    os.makedirs(outdir, exist_ok=True)

    files = {
        "logo-icon.svg": mark_icon(NAVY, SKY, AMBER),
        "logo-icon-light.svg": mark_icon(PAPER, SKY_L, AMBER_L),
        "logo-primary.svg": mark_badge(NAVY, SKY, AMBER),
        "logo-primary-light.svg": mark_badge(PAPER, SKY_L, AMBER_L),
        "logo-badge.svg": mark_badge(NAVY, SKY, AMBER, with_wordmark=False),
        "logo-horizontal.svg": mark_horizontal(NAVY, SKY, AMBER),
        "logo-horizontal-light.svg": mark_horizontal(PAPER, SKY_L, AMBER_L),
        "favicon.svg": mark_favicon(NAVY, PAPER, SKY_L, AMBER_L),
    }
    for name, svg in files.items():
        with open(os.path.join(outdir, name), "w") as fh:
            fh.write(svg + "\n")
        print(f"wrote {name} ({len(svg)} bytes)")
