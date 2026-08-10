"""Rebuild the South Air logo assets from the two approved source files.

Sources (neither is in the repo):
  C:/Users/kourt/Desktop/SAH LOGO/south-air-5a.jpg  - the approved composition
  C:/Users/kourt/Downloads/Untitled design (1).jpg  - the aircraft art, isolated on white

The aircraft is taken from the isolated file rather than cropped out of 5a: it is
810x316 there against 274x116 in the composition, so roughly 3x the linear detail.

Everything is composited as RGBA at 3x and emitted as a PNG embedded in an SVG
wrapper, so the pages keep referencing .svg and no markup changes.
"""
import base64, io
import numpy as np
from PIL import Image

SRC_LOGO = "C:/Users/kourt/Desktop/SAH LOGO/south-air-5a.jpg"
SRC_HELI = "C:/Users/kourt/Downloads/Untitled design (1).jpg"
OUT = "C:/Users/kourt/Desktop/SouthAirHelicopter/images/"
PREV = "C:/Users/kourt/AppData/Local/Temp/claude/C--Users-kourt-Desktop-SouthAirHelicopter/455d2030-55bf-4f69-8bff-0bfde67e16dd/scratchpad/logo/"

NAVY = (30, 58, 95)      # #1e3a5f - measured off the approved band
INK = (20, 23, 28)       # #14171c - measured off the approved wordmark
WHITE = (255, 255, 255)

S = 3  # supersample factor


def ink_layer(img_rgb, colour, ground=242, ink=20):
    """Turn artwork into a coloured layer, keying `ground` out to full transparency.

    Naive alpha = 255 - luminance leaves the source's own background as a faint
    rectangle, because these crops sit on #f2f2f0 (or navy), not on pure white.
    Mapping [ground..ink] onto [0..255] instead makes the ground genuinely empty.
    Pass ground > ink for dark-on-light art, ground < ink for light-on-dark.
    """
    lum = np.array(img_rgb.convert("L")).astype(np.float32)
    alpha = (lum - ground) / float(ink - ground)
    rgba = np.zeros(lum.shape + (4,), dtype=np.uint8)
    rgba[..., 0], rgba[..., 1], rgba[..., 2] = colour
    rgba[..., 3] = np.clip(alpha * 255.0, 0, 255).astype(np.uint8)
    return Image.fromarray(rgba, "RGBA")


# Ground/ink pairs measured off each source rather than assumed.
HELI_KEY = dict(ground=252, ink=40)    # aircraft art sits on pure #ffffff
WORD_KEY = dict(ground=236, ink=24)    # wordmark + rules sit on #f2f2f0
BAND_KEY = dict(ground=66, ink=225)    # white text on the #1e3a5f band


def fit(layer, w=None, h=None):
    ow, oh = layer.size
    if w is None:
        w = round(ow * h / oh)
    if h is None:
        h = round(oh * w / ow)
    return layer.resize((max(1, w), max(1, h)), Image.LANCZOS)


logo = Image.open(SRC_LOGO).convert("RGB")
heli_full = Image.open(SRC_HELI).convert("RGB")

# Measured bounding boxes (see session notes)
heli_src = heli_full.crop((549, 384, 1359, 700))          # 810 x 316
word_src = logo.crop((205, 128, 953, 236))                # SOUTH AIR
band_txt = logo.crop((354, 545, 807, 585))                # HELICOPTERS, white on navy
pearl_src = logo.crop((225, 660, 935, 700))               # rules + PEARLAND, TX


def build_horizontal(light):
    """240 x 74 header lockup: aircraft left, wordmark over HELICOPTERS right."""
    W, H = 240 * S, 74 * S
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    fg = WHITE if light else INK
    sub = WHITE if light else NAVY

    heli = fit(ink_layer(heli_src, fg, **HELI_KEY), h=30 * S)
    canvas.alpha_composite(heli, (0, (H - heli.size[1]) // 2))

    x = heli.size[0] + 8 * S
    tw = W - x - 3 * S          # keep the wordmark off the right edge
    word = fit(ink_layer(word_src, fg, **WORD_KEY), w=tw)
    heli_txt = fit(ink_layer(band_txt, sub, **BAND_KEY), w=tw)

    block = word.size[1] + 4 * S + heli_txt.size[1]
    y = (H - block) // 2
    canvas.alpha_composite(word, (x, y))
    canvas.alpha_composite(heli_txt, (x, y + word.size[1] + 4 * S))
    return canvas


def build_primary(light):
    """The approved stacked composition, rebuilt with the high-res aircraft."""
    W, H = 420 * S, 300 * S
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    fg = WHITE if light else INK

    word = fit(ink_layer(word_src, fg, **WORD_KEY), w=300 * S)
    canvas.alpha_composite(word, ((W - word.size[0]) // 2, 18 * S))

    heli = fit(ink_layer(heli_src, fg, **HELI_KEY), w=240 * S)
    canvas.alpha_composite(heli, ((W - heli.size[0]) // 2, 68 * S))

    # navy band with white HELICOPTERS
    bw, bh = 380 * S, 42 * S
    band = Image.new("RGBA", (bw, bh), NAVY + (255,))
    txt = fit(ink_layer(band_txt, WHITE, **BAND_KEY), w=int(bw * 0.45))
    band.alpha_composite(txt, ((bw - txt.size[0]) // 2, (bh - txt.size[1]) // 2))
    canvas.alpha_composite(band, ((W - bw) // 2, 196 * S))

    pearl = fit(ink_layer(pearl_src, fg, **WORD_KEY), w=270 * S)
    canvas.alpha_composite(pearl, ((W - pearl.size[0]) // 2, 254 * S))
    return canvas


def build_icon(light):
    fg = WHITE if light else INK
    heli = fit(ink_layer(heli_src, fg, **HELI_KEY), w=200 * S)
    canvas = Image.new("RGBA", (200 * S, 200 * S), (0, 0, 0, 0))
    canvas.alpha_composite(heli, (0, (200 * S - heli.size[1]) // 2))
    return canvas


def build_favicon():
    """Navy tile, white aircraft. At 32px this reads as a helicopter shape, not detail."""
    N = 64 * S
    tile = Image.new("RGBA", (N, N), NAVY + (255,))
    heli = fit(ink_layer(heli_src, WHITE, **HELI_KEY), w=int(N * 0.84))
    tile.alpha_composite(heli, ((N - heli.size[0]) // 2, (N - heli.size[1]) // 2))
    # rounded corners
    from PIL import ImageDraw
    m = Image.new("L", (N, N), 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, N - 1, N - 1], radius=int(N * 0.18), fill=255)
    tile.putalpha(Image.composite(tile.getchannel("A"), Image.new("L", (N, N), 0), m))
    return tile


def as_svg(img, vb_w, vb_h, label):
    buf = io.BytesIO()
    img.save(buf, "PNG", optimize=True)
    b64 = base64.b64encode(buf.getvalue()).decode()
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vb_w} {vb_h}" '
        f'role="img" aria-label="{label}">'
        f'<image href="data:image/png;base64,{b64}" x="0" y="0" '
        f'width="{vb_w}" height="{vb_h}"/></svg>\n'
    )


LABEL = "South Air Helicopters, Inc."
jobs = [
    ("logo-horizontal-light.svg", build_horizontal(True), 240, 74, LABEL),
    ("logo-horizontal.svg", build_horizontal(False), 240, 74, LABEL),
    ("logo-primary-light.svg", build_primary(True), 420, 300, LABEL),
    ("logo-primary.svg", build_primary(False), 420, 300, LABEL),
    ("logo-icon-light.svg", build_icon(True), 200, 200, "South Air Helicopters mark"),
    ("logo-icon.svg", build_icon(False), 200, 200, "South Air Helicopters mark"),
    ("favicon.svg", build_favicon(), 64, 64, LABEL),
]

for name, img, w, h, label in jobs:
    svg = as_svg(img, w, h, label)
    open(OUT + name, "w", encoding="utf-8").write(svg)
    # preview on a representative ground
    ground = NAVY if "light" in name or name == "favicon.svg" else (242, 242, 240)
    p = Image.new("RGB", img.size, ground)
    p.paste(img, (0, 0), img)
    p.save(PREV + "preview-" + name.replace(".svg", ".png"))
    print("%-28s %5d bytes  %sx%s" % (name, len(svg), img.size[0], img.size[1]))
