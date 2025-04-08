# Defining Kubeflow Pipeline (KFP) Components with Python Dataclasses

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ml-orchestrator)](https://pypi.org/project/ml-orchestrator/)
[![version](https://img.shields.io/pypi/v/ml-orchestrator)](https://img.shields.io/pypi/v/ml-orchestrator)
[![License](https://img.shields.io/:license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
![OS](https://img.shields.io/badge/ubuntu-blue?logo=ubuntu)
![OS](https://img.shields.io/badge/win-blue?logo=windows)
![OS](https://img.shields.io/badge/mac-blue?logo=apple)
[![Tests](https://github.com/DanielAvdar/ml-orchestrator/actions/workflows/ci.yml/badge.svg)](https://github.com/DanielAvdar/ml-orchestrator/actions/workflows/ci.yml)
[![Code Checks](https://github.com/DanielAvdar/ml-orchestrator/actions/workflows/code-checks.yml/badge.svg)](https://github.com/DanielAvdar/ml-orchestrator/actions/workflows/code-checks.yml)
[![codecov](https://codecov.io/gh/DanielAvdar/ml-orchestrator/graph/badge.svg?token=N0V9KANTG2)](https://codecov.io/gh/DanielAvdar/ml-orchestrator)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## Features

* **Dataclass-Driven Component Definition:** Define component logic using Python dataclasses, seamlessly translating
  them into Kubeflow Pipelines (KFP) compatible functions and components.
* **KFP Agnostic:** Empower developers to design and implement component logic as standard Python code, independent of
  the KFP framework.

## Installation

```bash
pip install ml-orchestrator
```

Note: `ml-orchestrator` is designed to be lightweight and free of external dependencies, ensuring efficient runtime
performance without additional overhead.

Note: `ml-orchestrator` does not require the `kfp` package to parse or create Kubeflow components.

Note: To construct `kfp` pipelines and utilize the components, the `kfp` package is required.

## Usage

please read the ![documentation](https://danielavdar.github.io/ml-orchestrator/)
