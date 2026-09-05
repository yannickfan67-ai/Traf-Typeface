from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from pathlib import Path

font_path = Path("fonts/ttf/TrafTypeface-Regular.ttf")
out = Path("documentation/traf-specimen.svg")
font = TTFont(font_path)
gs = font.getGlyphSet()
cmap = font.getBestCmap()
hmtx = font["hmtx"].metrics
upm = font["head"].unitsPerEm

def line_paths(text, x, y, size):
    scale = size / upm
    cur = x
    parts = []
    for ch in text:
        if ch == " ":
            cur += size * 0.34
            continue
        name = cmap.get(ord(ch))
        if not name:
            continue
        pen = SVGPathPen(gs)
        gs[name].draw(TransformPen(pen, (scale, 0, 0, -scale, cur, y)))
        d = pen.getCommands()
        if d:
            parts.append(f'<path d="{d}"/>')
        cur += hmtx[name][0] * scale
    return "".join(parts)

svg = [
    '<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="850" viewBox="0 0 1600 850">',
    '<rect width="1600" height="850" fill="#fafafa"/>',
    '<rect x="65" y="60" width="1470" height="730" rx="28" fill="white" stroke="#e2e2e2"/>',
    '<g fill="#111">',
    line_paths("Traf Typeface", 120, 250, 150),
    line_paths("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 125, 420, 47),
    line_paths("abcdefghijklmnopqrstuvwxyz", 125, 505, 47),
    line_paths("0123456789  !?@#$%&*  <= >=  ->", 125, 590, 47),
    line_paths("Clean geometric forms for desktop typography.", 125, 700, 38),
    '</g><rect x="120" y="735" width="240" height="8" fill="#e0b000"/></svg>',
]
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text("".join(svg), encoding="utf-8")
