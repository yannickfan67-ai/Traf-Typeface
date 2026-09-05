#!/usr/bin/env bash
set -euo pipefail
rm -rf build
mkdir -p build fonts/ttf
python tools/fix_ufo.py
fontmake -u sources/Traf-Regular.ufo -o ttf --output-dir build
built="$(find build -maxdepth 1 -type f -name '*.ttf' | head -n1)"
if [[ -z "$built" ]]; then
  echo "fontmake produced no TTF" >&2
  exit 1
fi
cp "$built" fonts/ttf/TrafTypeface-Regular.ttf
python tools/postprocess_font.py fonts/ttf/TrafTypeface-Regular.ttf
cp fonts/ttf/TrafTypeface-Regular.ttf build/TrafTypeface-Regular.ttf
