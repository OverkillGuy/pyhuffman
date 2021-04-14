
all: install format lint test

install:
	poetry install

test:
	poetry run pytest

format:
	poetry run black src/ tests/


lint: isort mypy flake8

mypy:
	poetry run mypy src/ tests/

flake8:
	poetry run flake8 src/

isort:
	poetry run isort -rc src/ tests/
