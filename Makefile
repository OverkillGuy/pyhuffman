
all: install format lint test

install:
	poetry install

test:
	poetry run pytest

format:
	poetry run black src/ tests/

lint: mypy

mypy:
	poetry run mypy src/ tests/
