# PyHuffman - Toy implementation of Huffman coding

A Python program implementing Huffman coding for learning purposes using Python best-practices.

Done after reading Chapter 1 of the [MIT Digital Communications online course](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-02-introduction-to-eecs-ii-digital-communication-systems-fall-2012/)), which made me want to build a Huffman coding program for myself.

## Dependencies
- Python 3.7: Use of typing features
- [poetry](https://python-poetry.org/), to manage packages (creating my own package and listing dependencies)

To see dependencies in more detail, in particular the packages used for development (testing, linting etc) have a look in the `pyproject.toml` file.

## Installation

Use poetry directly

	poetry install

alternatively, use the provided Makefile to simplify common commands (or just to learn them):

	make install

## Usage


	make

Just run `make`! It's that easy.

You can run the tests via pytest:

	poetry run pytest
	# equivalent to
	make test

Or use the implementation as a library. See the `tests/` folder
for examples using the library. See the documentation by running

	make docs docs-serve
and following the provided link

The code formatter can be run via

	make format

and the python linters are all available via:

	make lint

We recommend you run all these commands together as a matter of routine:

	make install format lint docs test
	# conveniently aliased as:
	make

This project uses [pre-commit](https://pre-commit.com) to run lint checks.

## License

GPL v3 (or later) license is used. See `LICENCE.txt` for details.
