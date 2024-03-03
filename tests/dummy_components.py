import dataclasses
from typing import List

from pykfp.artifacts import Dataset, Input, Output
from pykfp.meta_comp import MetaComponent


@dataclasses.dataclass(unsafe_hash=True)
class MetaComponentTest(MetaComponent):
    def execute(self) -> None:
        pass


@dataclasses.dataclass(unsafe_hash=True)
class ComponentTestA(MetaComponentTest):
    param_1: int = 1
    param_2: str = "1"
    artifact: Input[Dataset] = None
    out_artifact: Output[Dataset] = None


@dataclasses.dataclass(unsafe_hash=True)
class ComponentTestB(ComponentTestA):
    param_3: int = 2
    param_4: str = "2"
    param_list: List[int] = None

