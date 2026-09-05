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
- U+25CC DOTTED CIRCLE
- `tnum` tabular figure alternates
- Anchor data in UFO source for automatic mark feature generation by fontmake/ufo2ft
- README specimen generated from the built font
- GitHub Actions workflow for build and `fontbakery check-googlefonts`

## Remaining human/legal blockers
1. Replace contact placeholders in AUTHORS.txt and CONTRIBUTORS.txt with actual legal credits.
2. Resolve any failures or actionable warnings reported by the live FontBakery CI run.
3. Review generated mark positioning and outline quality visually before filing a Google Fonts onboarding issue.

The UFO bootstrap workflow completed successfully. This file intentionally does not claim FontBakery PASS until the dedicated Build and QA workflow has actually completed.
