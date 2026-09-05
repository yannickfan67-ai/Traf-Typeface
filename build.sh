#!/usr/bin/env bash
set -euo pipefail
rm -rf build
mkdir -p build fonts/ttf
rm -f fonts/ttf/*.ttf
fontmake -u sources/Traf-Regular.ufo -o ttf --output-dir build
built_font="$(find build -maxdepth 1 -type f -name '*.ttf' -print -quit)"
if [[ -z "${built_font}" ]]; then
  echo "fontmake did not produce a TTF" >&2
  exit 1
fi
cp "${built_font}" fonts/ttf/TrafTypeface-Regular.ttf
