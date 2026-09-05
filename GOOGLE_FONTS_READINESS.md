# Google Fonts readiness — Traf Typeface 2.100

## Completed in this repository
- Public-repo-compatible upstream folder structure
- UFO source and one-step `fontmake` build script
- Static TTF output
- GF Latin Core encoded coverage in the current binary
- OFL 1.1 license text with final upstream repository URL
- Copyright/license name records in TTF
- Use Typo Metrics enabled; hhea/Typo line gaps set to zero
- Win metrics matched to the current font bounding box
- U+25CC DOTTED CIRCLE
- `tnum` tabular figure alternates
- Anchor data added to UFO source for automatic mark feature generation by fontmake/ufo2ft
- GitHub Actions workflow for build and `fontbakery check-googlefonts`

## Remaining human/legal blockers
1. Public upstream repository: `https://github.com/yannickfan67-ai/Traf-Typeface` (set in OFL.txt).
2. Replace contact placeholders in AUTHORS.txt and CONTRIBUTORS.txt with actual legal credits.
3. Run the GitHub Actions / FontBakery workflow and resolve any failures it reports.
4. Review generated mark positioning and outline quality visually before filing a Google Fonts onboarding issue.

This file intentionally does not claim FontBakery PASS until CI has actually run.
