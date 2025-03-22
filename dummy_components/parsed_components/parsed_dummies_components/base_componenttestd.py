# flake8: noqa: F403, F405, B006
from typing import *

from kfp.dsl import *


def componenttestd(
    param_1: int = 1,
    param_2: str = "1",
    artifact: Input[Dataset] = None,
    out_artifact: Output[Dataset] = None,
    metrics: Output[Metrics] = None,
    param_3: int = 2,
    param_4: str = "2",
    param_list: List[int] = None,
    model: Output[Model] = None,
    param_list_2: List[int] = [],
    param_list_3: List[int] = [1, 2, 3],
):
    from dummy_components.dummy_components_v2 import ComponentTestD

    comp = ComponentTestD(
        param_1=param_1,
        param_2=param_2,
        artifact=artifact,
        out_artifact=out_artifact,
        metrics=metrics,
        param_3=param_3,
        param_4=param_4,
        param_list=param_list,
        model=model,
        param_list_2=param_list_2,
        param_list_3=param_list_3,
    )
    comp.execute()
