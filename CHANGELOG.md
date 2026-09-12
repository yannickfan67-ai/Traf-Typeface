# Changelog

## 2.101 — 2026-09-12
- Reworked capital `I` and lowercase `l` so the two forms remain distinguishable in compact desktop UI text.
- Added a slashed-zero alternate exposed through the OpenType `zero` feature without changing the default `0` form.
- Made production TTF timestamps deterministic so clean rebuilds do not drift from the committed binary.
- Added an explicit binary verification step for `fsType=0`, vendor ID `YTHF`, `gasp`, `prep`, copyright/version metadata, and the `zero` feature.
- Updated CI so normalized UFO source plus the generated TTF are committed back to `main` when needed, and the matching v2.101 release asset is published from the same build.

## 2.100 — 2026-09-05
- Completed GF Latin Core encoded character coverage.
- Added U+25CC DOTTED CIRCLE.
- Added tabular-number alternates and the `tnum` OpenType feature.
- Set Google Fonts-oriented vertical metrics and zero line gaps.
- Added OFL metadata records and source anchor data for mark generation.
- Added GitHub Actions build/QA workflow and repository documentation.

## 2.000 — 2026-09-05
- Expanded Latin coverage and synchronized UFO source with the desktop TTF.
