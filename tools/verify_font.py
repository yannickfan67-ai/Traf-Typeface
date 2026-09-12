#!/usr/bin/env python3
"""Fail CI if the committed/produced TTF misses release-critical metadata."""
from pathlib import Path
import sys
from fontTools.ttLib import TTFont

EXPECTED_PREP = bytes.fromhex("B801FF85B0048D")
EXPECTED_VENDOR = "YTHF"
EXPECTED_VERSION = "Version 2.101"


def name_values(font: TTFont, name_id: int) -> set[str]:
    values: set[str] = set()
    for record in font["name"].names:
        if record.nameID == name_id:
            try:
                values.add(record.toUnicode())
            except UnicodeDecodeError:
                pass
    return values


def main(path: str) -> None:
    p = Path(path)
    font = TTFont(p)
    errors: list[str] = []

    if font["OS/2"].fsType != 0:
        errors.append(f"OS/2.fsType={font['OS/2'].fsType}, expected 0")
    if font["OS/2"].achVendID != EXPECTED_VENDOR:
        errors.append(f"OS/2.achVendID={font['OS/2'].achVendID!r}, expected {EXPECTED_VENDOR!r}")
    if "gasp" not in font:
        errors.append("missing gasp table")
    elif font["gasp"].gaspRange.get(65535) != 0x000F:
        errors.append(f"unexpected gasp range: {font['gasp'].gaspRange!r}")
    if "prep" not in font:
        errors.append("missing prep table")
    else:
        prep = bytes(font["prep"].program.getBytecode())
        if prep != EXPECTED_PREP:
            errors.append(f"unexpected prep bytecode: {prep.hex().upper()}")

    versions = name_values(font, 5)
    if EXPECTED_VERSION not in versions:
        errors.append(f"nameID 5 does not contain {EXPECTED_VERSION!r}: {sorted(versions)!r}")

    copyrights = name_values(font, 0)
    if not any("Traf Typeface Project Authors" in value for value in copyrights):
        errors.append("nameID 0 is missing the project copyright string")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1)

    print(
        f"Verified {p}: fsType=0 vendor={EXPECTED_VENDOR} "
        "gasp=present prep=present version=2.101"
    )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: verify_font.py path/to/font.ttf")
    main(sys.argv[1])
