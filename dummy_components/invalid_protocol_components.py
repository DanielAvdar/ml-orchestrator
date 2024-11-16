from typing import List

from ml_orchestrator import EnvironmentParams
from ml_orchestrator.artifacts import Dataset, Input, Metrics, Model, Output


class MetaComponentTest:
    def execute(self) -> None:
        pass


class ComponentTestA(MetaComponentTest):
    param_1: int = 1
    param_2: str = "1"
    artifact: Input[Dataset] = None
    out_artifact: Output[Dataset] = None
    metrics: Output[Metrics] = None


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
