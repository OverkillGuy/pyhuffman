# PyHuffman - toy Huffman coding implementation

A simple Python program implementing Huffman coding for learning purposes.
Done as part of the MIT Digital Communications online course ([link](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-02-introduction-to-eecs-ii-digital-communication-systems-fall-2012/)) I read for fun

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

Run the tests via pytest:

	poetry run pytest
	# equivalent to
	make test

Or try to use the implementation as a library (TBD)

	python
	>>> import pyhuffman
	>>> # [TBD steps]

You can run the code formatter via

	make format

and run the python linter `mypy` (checks type):

	make lint

We recommend you run them all in one go as a matter of routine:

	make format lint test
	# conveniently aliased as:
	make
