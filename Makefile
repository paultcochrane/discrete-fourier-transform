.PHONY: clean

default:
	latexmk

clean:
	latexmk -c
