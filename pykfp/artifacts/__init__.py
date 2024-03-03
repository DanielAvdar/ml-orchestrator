import dataclasses
from typing import Annotated, TypeVar

from pykfp.artifacts.artifact import Artifact

_T = TypeVar("_T")
Input = Annotated[_T, "input"]
Output = Annotated[_T, "output"]


@dataclasses.dataclass
class Model(Artifact):
    pass


@dataclasses.dataclass
class Dataset(Artifact):
    pass


@dataclasses.dataclass
class HTML(Artifact):
    pass


@dataclasses.dataclass
class Markdown(Artifact):
    pass


__all__ = [
    "Model",
    "Dataset",
    "HTML",
    "Markdown",
    "Input",
    "Output",
]
