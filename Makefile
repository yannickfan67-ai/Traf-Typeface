PYTHON ?= python3

build:
	./build.sh

test:
	fontbakery check-googlefonts --full-lists --succinct fonts/ttf/*.ttf

proof:
	@echo "Install gftools or use the GitHub Actions artifact for proofing."

clean:
	rm -rf build
