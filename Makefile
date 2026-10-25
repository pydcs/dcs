.PHONY: build upload clean

build:
	uv build

upload:
	uvx twine upload dist/*

clean:
	rm -Rf dist/
