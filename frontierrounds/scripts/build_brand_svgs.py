#!/usr/bin/env python3
"""Build Frontier Rounds brand SVGs.

Two assets:
1) icon (from v3 inverse concept, made strictly two-tone black/white):
   - a black rounded-square tile with a white open ring (gap upper-right),
     3 inner nodes joined by short arcs (neural chain), one node escaping
     the gap (frontier).
2) wordmark: "Frontier Rounds" typeset in Instrument Serif Regular,
   converted to SVG <path> outlines (so it renders identically everywhere).

Outputs to ../branding/ : fr-icon.svg, fr-wordmark.svg
"""
from __future__ import annotations

import math
import re
from pathlib import Path

from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen

OUT = Path(__file__).resolve().parent.parent / "branding"
FONT_SRC = Path(
    r"e:\clients\frontierrounds\branding\InstrumentSerif-Latin.woff2"
)

# ----------------------------------------------------------------------------
# 1. Icon — geometry tuned from the v3 render
# ----------------------------------------------------------------------------
S = 512  # viewBox size
C = S / 2
BG = "#000000"          # tile
FG = "#FFFFFF"          # mark

# open ring: drawn as a stroked circle arc; gap spans these angles
# (SVG y-down: 0deg = +x (3 o'clock), +90 = +y (6 o'clock); ring opens ~2 o'clock)
GAP_START = 303.0       # where visible ring starts (going CCW the long way)
GAP_END = 342.0         # where visible ring ends
RING_R = 168.0          # ring centreline radius
RING_W = 54.0           # ring stroke width
NODE_R = 26.0           # inner node radius
ARC_W = 22.0            # connector arc width
# inner nodes (centres) — placed around the lower-left arc, clear of the gap
NODES = [150.0, 200.0, 250.0]           # angles in degrees (SVG coords)
NODE_ARC_R = 108.0                      # radius of inner node circle / arcs
# escaping node: sits in the gap, centre on gap bisector at larger radius
ESC_R = 150.0 + RING_W + 8.0            # radius (centre) of escaping node
ESC_ANG = (GAP_START + GAP_END) / 2.0   # gap bisector


def pt(radius: float, ang_deg: float) -> tuple[float, float]:
    a = math.radians(ang_deg)
    return (C + radius * math.cos(a), C + radius * math.sin(a))


def arc_path(r: float, a0: float, a1: float, large=0, sweep=1) -> str:
    x0, y0 = pt(r, a0)
    x1, y1 = pt(r, a1)
    return (
        f"M {x0:.2f} {y0:.2f} "
        f"A {r:.2f} {r:.2f} 0 {large} {sweep} {x1:.2f} {y1:.2f}"
    )


def build_icon(tile: bool = True) -> str:
    # visible ring runs from GAP_END back to GAP_START the long way
    ring = arc_path(RING_R, GAP_END, GAP_START + 360.0 if GAP_START < GAP_END else GAP_START,
                    large=1, sweep=1)

    # connector arcs between successive inner nodes (subtend < 180)
    connectors = []
    for a0, a1 in zip(NODES, NODES[1:]):
        connectors.append(arc_path(NODE_ARC_R, a0, a1))

    nodes = [f'<circle cx="{pt(NODE_ARC_R, a)[0]:.2f}" cy="{pt(NODE_ARC_R, a)[1]:.2f}" r="{NODE_R}"/>'
             for a in NODES]

    ex, ey = pt(ESC_R, ESC_ANG)
    esc = f'<circle cx="{ex:.2f}" cy="{ey:.2f}" r="{NODE_R + 6}"/>'

    if tile:
        # v3 inverse style: black tile + white mark
        bg = f'<rect x="6" y="6" width="{S - 12}" height="{S - 12}" rx="{S * 0.17}" fill="{BG}"/>'
        fg = FG
    else:
        # transparent + monochrome black mark
        bg = ""
        fg = "#000000"

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {S} {S}" role="img" aria-label="Frontier Rounds">
  {bg}
  <path d="{ring}" fill="none" stroke="{fg}" stroke-width="{RING_W}" stroke-linecap="round"/>
  {''.join(f'<path d="{c}" fill="none" stroke="{fg}" stroke-width="{ARC_W}" stroke-linecap="round"/>' for c in connectors)}
  {''.join(nodes)}
  {esc}
</svg>
"""
    return svg


# ----------------------------------------------------------------------------
# 2. Wordmark — "Frontier Rounds" in Instrument Serif Regular → paths
# ----------------------------------------------------------------------------
WORD = "Frontier Rounds"
FONT_SIZE = 100.0
LETTER_SPACING = 2.0  # px @100px cap height scale (approx)


def build_wordmark() -> str:
    font = TTFont(str(FONT_SRC))
    upm = font["head"].unitsPerEm
    scale = FONT_SIZE / upm
    cmap = font.getBestCmap()
    gs = font.getGlyphSet()
    hmtx = font["hmtx"]

    # vertical metrics in RAW font units
    hhea = font["hhea"]
    ascender_u = hhea.ascent
    descender_u = hhea.descent  # negative typically
    spacing_u = LETTER_SPACING / scale  # letter spacing in raw units

    # collect per-glyph raw path + raw advance
    pen_paths: list[tuple[str, float]] = []
    cx_units = 0.0
    for ch in WORD:
        gname = cmap.get(ord(ch))
        if gname is None:
            raise SystemExit(f"No glyph for {ch!r} in Instrument Serif subset")
        spen = SVGPathPen(gs)
        gs[gname].draw(spen)
        pen_paths.append((spen.getCommands(), cx_units))
        cx_units += hmtx[gname][0] + spacing_u

    total_w_units = cx_units
    pad_u = 40.0
    # translate to (pad, baseline) then flip y (font y-up -> svg y-down) + scale
    # baseline offset in units measured from font origin; descender may be negative
    # put baseline at y = (ascender_u + pad_u) in svg px after flip
    vb_w = (total_w_units + pad_u * 2) * scale
    vb_h = (ascender_u - descender_u + pad_u * 2) * scale

    inner = "".join(
        f'<path transform="translate({txu:.2f} 0)" d="{d}"/>' for d, txu in pen_paths
    )

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vb_w:.2f} {vb_h:.2f}" role="img" aria-label="Frontier Rounds">
  <g transform="translate({pad_u * scale:.2f} {(ascender_u + pad_u) * scale:.2f}) scale({scale:.6f} {-scale:.6f})">
  {inner}
  </g>
</svg>
"""
    return svg


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "fr-icon.svg").write_text(build_icon(tile=True), encoding="utf-8")
    (OUT / "fr-icon-mono.svg").write_text(build_icon(tile=False), encoding="utf-8")
    (OUT / "fr-wordmark.svg").write_text(build_wordmark(), encoding="utf-8")
    print("wrote:", OUT / "fr-icon.svg")
    print("wrote:", OUT / "fr-icon-mono.svg")
    print("wrote:", OUT / "fr-wordmark.svg")


if __name__ == "__main__":
    main()
