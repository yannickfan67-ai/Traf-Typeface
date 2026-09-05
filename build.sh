#!/usr/bin/env bash
set -euo pipefail
rm -rf build
mkdir -p build fonts/ttf
fontmake -u sources/Traf-Regular.ufo -o ttf --output-dir build
cp build/*.ttf fonts/ttf/
