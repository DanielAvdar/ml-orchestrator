"""Artifacts package for ML pipeline component inputs and outputs.

This package provides classes and types for representing and managing
different kinds of machine learning artifacts such as models, datasets,
and metrics, with support for JSON serialization.
"""

from typing import Annotated, TypeVar

from ml_orchestrator.artifacts.artifact import Artifact
from ml_orchestrator.artifacts.artifacts import HTML, Dataset, Markdown, Metrics, Model

_T = TypeVar("_T")
Input = Annotated[_T, "input"]
Output = Annotated[_T, "output"]

__all__ = ["Model", "Dataset", "HTML", "Markdown", "Metrics", "Input", "Output", "Artifact"]
