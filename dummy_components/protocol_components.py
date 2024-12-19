import dataclasses
from typing import List

from ml_orchestrator import EnvironmentParams
from ml_orchestrator.artifacts import Dataset, Input, Metrics, Model, Output


@dataclasses.dataclass(unsafe_hash=True)
class MetaComponentTest:
    def execute(self) -> None:
        pass


@dataclasses.dataclass(unsafe_hash=True)
class ComponentTestA(MetaComponentTest):
    param_1: int = 1
    param_2: str = "1"
    artifact: Input[Dataset] = None
    out_artifact: Output[Dataset] = None
    metrics: Output[Metrics] = None


@dataclasses.dataclass(unsafe_hash=True)
class ComponentTestB(ComponentTestA):
    param_3: int = 2
    param_4: str = "2"
    param_list: List[int] = None
    model: Output[Model] = None

    @property
    def env(self) -> EnvironmentParams:
        return EnvironmentParams(
            base_image="base_image",
            target_image="target_image",
            packages_to_install=["packages_to_install", "", "sd''{d}"],
            pip_index_urls=["pip_index_urls"],
            install_kfp_package=True,
            kfp_package_path="kfp_package_path",
        )


@dataclasses.dataclass(unsafe_hash=True)
class ComponentTestC(ComponentTestB):
    def execute(self) -> int:  # type: ignore
        return 1


@dataclasses.dataclass(unsafe_hash=True)
class ComponentTestC2(ComponentTestB):
    def execute(self) -> str:  # type: ignore
        return "1"


@dataclasses.dataclass(unsafe_hash=True)
class ComponentTestC3(ComponentTestB):
    def execute(self) -> bool:  # type: ignore
        return False


@dataclasses.dataclass(unsafe_hash=True)
class ComponentWithMandatoryParam:
    param_mandatory_int: int

    def execute(self) -> None:
        pass


@dataclasses.dataclass(unsafe_hash=True)
class ComponentWithMandatoryParamB(ComponentWithMandatoryParam):
    param_mandatory_str: str
    param_mandatory_list: List[int]
    param_mandatory_list_2: List[int] = dataclasses.field(default_factory=list)

    param_2: str = "1"
