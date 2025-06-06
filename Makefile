.PHONY: help
.PHONY: default
default: install

install:
	uv sync --all-extras --all-groups --frozen
	uvx pre-commit install

update:
	uv lock
	uvx pre-commit autoupdate
	$(MAKE) install

test: install
	uv run pytest

coverage: install
	uv run pytest --cov=ml_orchestrator --cov-report=xml --junitxml=junit.xml -o junit_family=legacy

cov: install
	uv run pytest --cov=ml_orchestrator --cov-report=term-missing

check: install
	uvx pre-commit run --all-files

mypy: install
	uv run mypy ml_orchestrator --config-file pyproject.toml

doctest: install-docs
	uv run --no-sync sphinx-build -M doctest docs/source docs/build/ -W --keep-going --fresh-env

install-docs:
	uv sync --group docs --frozen --no-group dev

doc:
	uv run --no-sync sphinx-build -M html docs/source docs/build/ -W --keep-going --fresh-env

check-all: check test mypy doc
