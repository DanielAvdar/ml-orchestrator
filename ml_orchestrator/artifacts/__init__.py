from typing import Annotated, TypeVar

from ml_orchestrator.artifacts.artifact import Artifact
from ml_orchestrator.artifacts.artifacts import HTML, Dataset, Markdown, Metric, Model

_T = TypeVar("_T")
Input = Annotated[_T, "input"]
Output = Annotated[_T, "output"]

__all__ = ["Model", "Dataset", "HTML", "Markdown", "Metric", "Input", "Output", "Artifact"]
