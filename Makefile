.PHONY: help
.PHONY: default
default: install

install:
	poetry install --all-extras --all-groups
#	poetry run pre-commit autoupdate
	poetry run pre-commit install

test:
	poetry run pytest

check:
	poetry run pre-commit run --all-files
mypy:
	poetry run mypy ml_orchestrator --config-file pyproject.toml

doc:
	poetry run sphinx-build -M html docs/source docs/build/
