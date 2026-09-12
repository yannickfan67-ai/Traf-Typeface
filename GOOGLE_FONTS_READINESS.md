# Google Fonts readiness — Traf Typeface 2.101

## Completed in this repository
- Public upstream repository and Google Fonts-style project structure
- Expanded UFO source in `sources/Traf-Regular.ufo`
- One-step `fontmake` build script
- Static TTF output in `fonts/ttf/`
- GF Latin Core encoded coverage in the current binary
- OFL 1.1 license text with final upstream repository URL
- Copyright/license name records in TTF
- Official author and contributor contact: Yannick T Harrington-Fan <yannickfan67@gmail.com>
- Use Typo Metrics enabled; hhea/Typo line gaps set to zero
- Win metrics matched to the current font bounding box
- U+25CC DOTTED CIRCLE with top/bottom mark anchors
- `tnum` tabular figure alternates
- Optional slashed-zero alternate through the OpenType `zero` feature
- Anchor data in UFO source for automatic mark feature generation by fontmake/ufo2ft
- Removed invalid duplicate numeric glyph names
- Added missing Unicode case-mapping counterparts used by FontBakery
- Build post-processing for installable embedding, `YTHF`, `gasp`, and smart-dropout `prep`
- Deterministic production timestamps so clean builds remain byte-stable when source is unchanged
- Binary verification in CI for release-critical OS/2/name/table/OpenType-feature metadata
- Automatic synchronization of normalized UFO source and the built TTF in `fonts/ttf/` with the same production build used for release assets
- Original Traf default letterform style preserved; review engineering changes do not redesign core glyphs
- README specimen generated from the built font
- GitHub Actions workflow for build, verification, `fontbakery check-googlefonts`, and gated GitHub Releases

## Remaining review items
- Do a dedicated optical spacing/kerning pass using representative strings such as `HOHO`, `NONO`, `AVATAR`, `WATER`, `minimum`, `runner`, and `Traf Typeface` without changing the established letterform style.
- Audit mark weight/scale consistency across acute, caron, dieresis, double acute, `Ł`, and `Đ` while preserving the existing design language.
- If reviewers request extra UI differentiation, prefer optional stylistic alternates for `I/l/1` rather than changing the default Traf forms.
- Perform Windows/browser rasterization checks at 14–16 px and review punctuation/currency/math symbol weight visually.

The live Build and QA workflow is the authority for the current FontBakery result. v2.101 is the review-fix release line prepared for the next Google Fonts reviewer pass.
