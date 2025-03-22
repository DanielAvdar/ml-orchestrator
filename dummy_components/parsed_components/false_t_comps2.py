# flake8: noqa: F403, F405, B006
from typing import *

from kfp.dsl import *


@component(
    base_image="base_image",
    target_image="target_image",
    packages_to_install=["packages_to_install", "", f"sd''{d}"],
    pip_index_urls=["pip_index_urls"],
    install_kfp_package=True,
    kfp_package_path="kfp_package_path",
)
def componenttestb(
    param_1: int = 1,
    param_2: str = "1",
    artifact: Input[Dataset] = None,
    out_artifact: Output[Dataset] = None,
    metrics: Output[Metrics] = None,
    param_3: int = 2,
    param_4: str = "2",
    param_list: List[int] = None,
    model: Output[Model] = None,
):
    from dummy_components.dummy_components import ComponentTestB

    comp = ComponentTestB(
        param_1=param_1,
        param_2=param_2,
        artifact=artifact,
        out_artifact=out_artifact,
        metrics=metrics,
        param_3=param_3,
        param_4=param_4,
        param_list=param_list,
        model=model,
    )
    comp.execute()


@component()
def componenttesta(
    param_1: int = 1,
    param_2: str = "1",
    artifact: Input[Dataset] = None,
    out_artifact: Output[Dataset] = None,
    metrics: Output[Metrics] = None,
):
    from dummy_components.dummy_components import ComponentTestA

    comp = ComponentTestA(
        param_1=param_1,
        param_2=param_2,
        artifact=artifact,
        out_artifact=out_artifact,
        metrics=metrics,
    )
    comp.execute()
