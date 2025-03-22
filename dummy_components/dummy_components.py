from dataclasses import dataclass, field
from typing import List

from ml_orchestrator import EnvironmentParams
from ml_orchestrator.artifacts import Dataset, Input, Metrics, Model, Output
from ml_orchestrator.meta_comp import MetaComponent


@dataclass
class MetaComponentTest(MetaComponent):
    internal_param: int = field(
        init=False,
    )

    def execute(self) -> None:
        pass


@dataclass
class ComponentTestA(MetaComponentTest):
    param_1: int = 1
    param_2: str = "1"
    artifact: Input[Dataset] = None
    out_artifact: Output[Dataset] = None
    metrics: Output[Metrics] = None


@dataclass
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


@dataclass
class ComponentTestC(ComponentTestB):
    def execute(self) -> int:  # type: ignore
        return 1


@dataclass
class ComponentTestC2(ComponentTestB):
    def execute(self) -> str:  # type: ignore
        return "1"


@dataclass
class ComponentTestC3(ComponentTestB):
    def execute(self) -> bool:  # type: ignore
        return False


@dataclass
class ComponentTestD(ComponentTestB):
    param_list_2: List[int] = field(default_factory=list)
    param_list_3: List[int] = field(default_factory=lambda: [1, 2, 3])

    def execute(self) -> None:
        pass


@dataclass
class ComponentTestD2(ComponentTestB):
    param_dict: dict = field(default_factory=dict)
    param_dict_full: dict = field(default_factory=lambda: {"a": 1, "b": 2})
    param_dict_nan: dict = field(default=None)

    def execute(self) -> None:
        pass
