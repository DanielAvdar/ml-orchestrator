.PHONY: help
.PHONY: default
default: install

install:
	poetry install
	poetry run pre-commit autoupdate
	poetry run pre-commit install

test:
	poetry run pytest

check:
	poetry run pre-commit run --all-files
