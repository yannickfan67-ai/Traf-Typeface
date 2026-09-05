# Traf Typeface

![Traf Typeface specimen](documentation/traf-specimen.svg)

Traf Typeface is a geometric Latin typeface developed from the `Traf` lettering used in the Unknown / Traf visual identity. It is intended for desktop UI, branding, headings, compact documentation, and other interface-oriented typography while remaining readable in ordinary English text.

## Current scope

- Regular static TrueType font
- UFO source in `sources/Traf-Regular.ufo`
- GF Latin Core encoded character coverage
- Extended Latin, punctuation, fractions, math, arrows, and currency symbols
- Proportional default figures plus `tnum` tabular alternates
- SIL Open Font License 1.1

## Building

```bash
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
make build
```

The output is copied to `fonts/ttf/`.

## QA

```bash
make test
```

The GitHub Actions workflow builds the font from the editable UFO source and runs the Google Fonts FontBakery profile on pushes and pull requests. The current v2.100 production build has 0 ERROR, 0 FATAL, and 0 FAIL in that profile; remaining findings are WARN-level review items.

## Google Fonts status

The repository is structured for Google Fonts upstream development: editable source files are in `sources/`, the build is one-step and open-source, the font targets GF Latin Core, and the project is licensed under OFL 1.1. The official copyright author and maintainer is Yannick T Harrington-Fan <yannickfan67@gmail.com>; see `AUTHORS.txt` and `CONTRIBUTORS.txt`.

## AI-assisted development disclosure

AI tools were used during development for exploratory visual references, technical assistance, QA guidance, repository/build automation, and assistance with generating or refining some glyph geometry. The released font is distributed as editable UFO source together with reproducible open-source build scripts so that the complete source and production process can be reviewed.

## Design notes

The core style uses rounded geometric construction, restrained stroke contrast, and unusual `m`, `w`, `n`, `u`, and `r` forms inherited from the original Traf lettering. The font is designed primarily for PC/desktop use; web use is possible but is not the design's primary constraint.

## License

Traf Typeface is licensed under the SIL Open Font License, Version 1.1. See `OFL.txt`.

## Upstream

https://github.com/yannickfan67-ai/Traf-Typeface
