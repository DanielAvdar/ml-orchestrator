from dataclasses import dataclass, field
from typing import List

from ml_orchestrator import EnvironmentParams
from ml_orchestrator.artifacts import Dataset, Input, Metrics, Model, Output


@dataclass(unsafe_hash=True)
class MetaComponentTest:
    internal_param: int = field(
        init=False,
    )

    def execute(self) -> None:
        pass


@dataclass(unsafe_hash=True)
class ComponentTestA(MetaComponentTest):
    param_1: int = 1
    param_2: str = "1"
    artifact: Input[Dataset] = None
    out_artifact: Output[Dataset] = None
    metrics: Output[Metrics] = None


@dataclass(unsafe_hash=True)
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
            packages_to_install=["ml-orchestrator=={version('ml-orchestrator')}"],
            pip_index_urls=["pip_index_urls"],
            install_kfp_package=True,
            kfp_package_path="kfp_package_path",
        )


@dataclass(unsafe_hash=True)
class ComponentTestC(ComponentTestB):
    def execute(self) -> int:  # type: ignore
        return 1


@dataclass(unsafe_hash=True)
class ComponentTestC2(ComponentTestB):
    def execute(self) -> str:  # type: ignore
        return "1"


@dataclass(unsafe_hash=True)
class ComponentTestC3(ComponentTestB):
    def execute(self) -> bool:  # type: ignore
        return False


@dataclass(unsafe_hash=True)
class ComponentWithMandatoryParam:
    param_mandatory_int: int

    def execute(self) -> None:
        pass


@dataclass(unsafe_hash=True)
class ComponentWithMandatoryParamB(ComponentWithMandatoryParam):
    param_mandatory_str: str
    param_mandatory_list: List[int]
    param_mandatory_list_2: List[int] = field(default_factory=list)
    param_dict_full: dict = field(default_factory=lambda: {"a": 1, "b": 2})
    param_dict_nan: dict = field(default=None)
    param_2: str = "1"
