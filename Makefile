PYTHON ?= python3

build:
	./build.sh

verify:
	$(PYTHON) tools/verify_font.py fonts/ttf/TrafTypeface-Regular.ttf

test: verify
	fontbakery check-googlefonts --full-lists --succinct fonts/ttf/*.ttf

proof:
	@echo "Install gftools or use the GitHub Actions artifact for proofing."

clean:
	rm -rf build
