
all: install format lint docs test

install:
	poetry install

test:
	poetry run pytest

format:
	poetry run black src/ tests/

lint:
	pre-commit run --all --all-files

docs:
	poetry run make -C docs/ html

docs-serve:
	cd docs/build/html && poetry run python -m http.server

docs-clean:
	find docs/build/ -delete



.PHONY: all install test format lint docs docs-serve docs-clean
