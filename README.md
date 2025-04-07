# define kfp component as dataclasses

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

*   **Dataclass-based Component Definition:** Define your KFP components using Python dataclasses, making component definitions more readable and maintainable.
*   **Automatic Input/Output Handling:**  The package automatically handles the input and output definitions for your components based on the dataclass structure.
*   **Simplified Pipeline Construction:**  Easily integrate your dataclass-defined components into KFP pipelines.

## Installation

```bash
pip install ml-orchestrator
```

If you want to use `ml-orchestrator` with Kubeflow Pipelines, install the `kfp` extra:

```bash
pip install ml-orchestrator[editor]
```

## Usage

### Defining a Component

To define a KFP component, create a Python dataclass and decorate it appropriately (details will be added when the core logic is implemented).

```python
from dataclasses import dataclass
# from ml_orchestrator import component  # Placeholder, replace with the actual import

# @component # Placeholder, replace with the actual decorator
# @dataclass
# class MyComponent:
#     input_data: str
#     output_result: str

#     def execute(self):
#         # Component logic here
#         self.output_result = f"Processed: {self.input_data}"
#         return self.output_result
```

### Creating a Pipeline

(Example of how to create a pipeline using the defined components will be added when the core logic is implemented.)

## Contributing

Contributions are welcome! Please refer to the contributing guidelines for more information.

## License

This project is licensed under the MIT License.
