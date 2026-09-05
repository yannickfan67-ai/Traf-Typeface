# Google Fonts readiness — Traf Typeface 2.100

## Completed in this repository
- Public upstream repository and Google Fonts-style project structure
- Expanded UFO source in `sources/Traf-Regular.ufo`
- One-step `fontmake` build script
- Static TTF output in `fonts/ttf/`
- GF Latin Core encoded coverage in the current binary
- OFL 1.1 license text with final upstream repository URL
- Copyright/license name records in TTF
- Use Typo Metrics enabled; hhea/Typo line gaps set to zero
- Win metrics matched to the current font bounding box
- U+25CC DOTTED CIRCLE with top/bottom mark anchors
- `tnum` tabular figure alternates
- Anchor data in UFO source for automatic mark feature generation by fontmake/ufo2ft
- Removed invalid duplicate numeric glyph names
- Added missing Unicode case-mapping counterparts used by FontBakery
- Build post-processing for installable embedding, `gasp`, and smart-dropout `prep`
- README specimen generated from the built font
- GitHub Actions workflow for build, `fontbakery check-googlefonts`, and gated GitHub Releases
- v2.100 compliance source fixes synchronized into the UFO source

## Remaining human/legal blockers
1. Replace contact placeholders in AUTHORS.txt and CONTRIBUTORS.txt with actual legal credits.
2. Review generated mark positioning and outline quality visually before filing a Google Fonts onboarding issue.

The source fixes are synchronized. The live Build and QA workflow is the authority for the current FontBakery result; a v2.100 GitHub Release is published only after that workflow has no FAIL results.
