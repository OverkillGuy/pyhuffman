
install:
	poetry install

test:
	poetry run pytest

format:
	poetry run black pyhuffman/ tests/
