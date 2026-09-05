#!/usr/bin/env python3
"""Post-process fontmake output with Google Fonts-required binary metadata."""
from pathlib import Path
import sys
from fontTools.ttLib import TTFont, newTable
from fontTools.ttLib.tables.ttProgram import Program

REPO = "https://github.com/yannickfan67-ai/Traf-Typeface"
COPYRIGHT = f"Copyright 2026 The Traf Project Authors ({REPO})"
LICENSE = (
    "This Font Software is licensed under the SIL Open Font License, Version 1.1. "
    "This license is available with a FAQ at: https://openfontlicense.org"
)
LICENSE_URL = "https://openfontlicense.org"


def replace_name(font: TTFont, name_id: int, value: str) -> None:
    table = font["name"]
    table.names = [n for n in table.names if n.nameID != name_id]
    table.setName(value, name_id, 3, 1, 0x0409)
    table.setName(value, name_id, 1, 0, 0)


def main(path: str) -> None:
    p = Path(path)
    font = TTFont(p)

    font["OS/2"].fsType = 0
    font["OS/2"].achVendID = "TRAF"
    replace_name(font, 0, COPYRIGHT)
    replace_name(font, 13, LICENSE)
    replace_name(font, 14, LICENSE_URL)

    gasp = newTable("gasp")
    gasp.gaspRange = {65535: 0x000F}
    font["gasp"] = gasp

    prep = newTable("prep")
    program = Program()
    program.fromBytecode(bytes.fromhex("B801FF85B0048D"))
    prep.program = program
    font["prep"] = prep

    font.save(p)
    print(f"Post-processed {p}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: postprocess_font.py path/to/font.ttf")
    main(sys.argv[1])
