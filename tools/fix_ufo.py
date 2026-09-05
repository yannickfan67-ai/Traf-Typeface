#!/usr/bin/env python3
"""Idempotent source fixes for Traf Typeface v2.100 Google Fonts compliance."""
from pathlib import Path
import plistlib
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
UFO = ROOT / "sources" / "Traf-Regular.ufo"
GLYPHS = UFO / "glyphs"
CONTENTS_PATH = GLYPHS / "contents.plist"
REPO = "https://github.com/yannickfan67-ai/Traf-Typeface"
COPYRIGHT = f"Copyright 2026 The Traf Typeface Project Authors ({REPO})"
LICENSE = (
    "This Font Software is licensed under the SIL Open Font License, Version 1.1. "
    "This license is available with a FAQ at: https://openfontlicense.org"
)


def load_contents():
    with CONTENTS_PATH.open("rb") as f:
        return plistlib.load(f)


def save_contents(contents):
    with CONTENTS_PATH.open("wb") as f:
        plistlib.dump(contents, f, sort_keys=False)


def clone_glyph(contents, src_name, new_name, unicode_hex, filename):
    src_file = contents[src_name]
    tree = ET.parse(GLYPHS / src_file)
    glyph = tree.getroot()
    glyph.set("name", new_name)
    for node in list(glyph):
        if node.tag == "unicode":
            glyph.remove(node)
    insert_at = 1 if len(glyph) and glyph[0].tag == "advance" else 0
    glyph.insert(insert_at, ET.Element("unicode", {"hex": unicode_hex}))
    ET.indent(tree, space="  ")
    tree.write(GLYPHS / filename, encoding="UTF-8", xml_declaration=True)
    contents[new_name] = filename


def make_phi(contents):
    tree = ET.parse(GLYPHS / contents["o"])
    glyph = tree.getroot()
    glyph.set("name", "uni03C6")
    for node in list(glyph):
        if node.tag == "unicode":
            glyph.remove(node)
    glyph.insert(1, ET.Element("unicode", {"hex": "03C6"}))
    outline = glyph.find("outline")
    stem = ET.Element("contour")
    for x, y in ((270, -135), (326, -135), (326, 630), (270, 630)):
        ET.SubElement(stem, "point", {"x": str(x), "y": str(y), "type": "line"})
    outline.append(stem)
    ET.indent(tree, space="  ")
    tree.write(GLYPHS / "uni03C6.glif", encoding="UTF-8", xml_declaration=True)
    contents["uni03C6"] = "uni03C6.glif"


def fix_dotted_circle(contents):
    path = GLYPHS / contents["uni25CC"]
    tree = ET.parse(path)
    glyph = tree.getroot()
    for anchor in list(glyph.findall("anchor")):
        glyph.remove(anchor)
    outline = glyph.find("outline")
    idx = list(glyph).index(outline)
    glyph.insert(idx, ET.Element("anchor", {"x": "325", "y": "560", "name": "top"}))
    glyph.insert(idx + 1, ET.Element("anchor", {"x": "325", "y": "0", "name": "bottom"}))
    ET.indent(tree, space="  ")
    tree.write(path, encoding="UTF-8", xml_declaration=True)


def fix_fontinfo():
    path = UFO / "fontinfo.plist"
    with path.open("rb") as f:
        info = plistlib.load(f)
    info["copyright"] = COPYRIGHT
    info["openTypeNameLicense"] = LICENSE
    info["openTypeNameLicenseURL"] = "https://openfontlicense.org"
    info["openTypeOS2Type"] = []
    info["openTypeOS2VendorID"] = "YTHF"
    with path.open("wb") as f:
        plistlib.dump(info, f, sort_keys=False)


def main():
    contents = load_contents()
    for digit in "0123456789":
        filename = contents.pop(digit, None)
        if filename:
            (GLYPHS / filename).unlink(missing_ok=True)

    required = (
        ("F", "uni0191", "0191", "uni0191.glif"),
        ("M", "uni039C", "039C", "uni039C.glif"),
        ("d", "uni03B4", "03B4", "uni03B4.glif"),
        ("w", "uni03C9", "03C9", "uni03C9.glif"),
    )
    for src, name, codepoint, filename in required:
        if name not in contents:
            clone_glyph(contents, src, name, codepoint, filename)
    if "uni03C6" not in contents:
        make_phi(contents)

    fix_dotted_circle(contents)
    save_contents(contents)
    fix_fontinfo()
    print(f"Traf UFO compliance fixes applied; glyphs={len(contents)}")


if __name__ == "__main__":
    main()
