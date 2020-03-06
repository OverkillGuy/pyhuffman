# PyHuffman - Toy implementation of Huffman coding 

A Python program implementing Huffman coding for learning purposes using Python best-practices.

Done after reading Chapter 1 of the [MIT Digital Communications online course](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-02-introduction-to-eecs-ii-digital-communication-systems-fall-2012/)), which made me want to build Huffman coding for real.

## Dependencies
- Python 3
- [Poetry](https://python-poetry.org/) for package management
- [Pytest](https://pytest.org/) for testing
- [black](https://black.readthedocs.io/en/stable/) python formatter

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

Or try to use the implementation as a library. See the `tests/` folder
for usage examples.

The code formatter can be run via

	make format

and the python linter `mypy` (checks type errors):

	make lint

We recommend you run them all in one go as a matter of routine:

	make format lint test
	# conveniently aliased as:
	make

## License

GPL v3 (or later) license is used. See `LICENCE.txt` for details.
