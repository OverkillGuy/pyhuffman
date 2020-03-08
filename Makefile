
all: install format lint test

install:
	poetry install

test:
	poetry run pytest

format:
	poetry run black src/ tests/

lint: isort mypy pylint

mypy:
	poetry run mypy src/ tests/

pylint:
	poetry run pylint src/ tests/

isort:
	poetry run isort -rc src/ tests/
