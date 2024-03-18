import dataclasses
from typing import List

from ml_orchestrator import EnvironmentParams
from ml_orchestrator.artifacts import Dataset, Input, Metrics, Model, Output
from ml_orchestrator.meta_comp import MetaComponent


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
            output_component_file="output_component_file",
            install_kfp_package=True,
            kfp_package_path="kfp_package_path",
        )
