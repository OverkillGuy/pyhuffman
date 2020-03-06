
all: install format lint test

install:
	poetry install

test:
	poetry run pytest

format:
	poetry run black pyhuffman/ tests/

lint:
	poetry run mypy pyhuffman/ tests/
