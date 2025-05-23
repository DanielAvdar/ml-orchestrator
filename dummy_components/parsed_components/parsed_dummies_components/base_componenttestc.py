# flake8: noqa: F403, F405, B006
from typing import *

from kfp.dsl import *


def componenttestc(
    param_1: int = 1,
    param_2: str = "1",
    artifact: Input[Dataset] = None,
    out_artifact: Output[Dataset] = None,
    metrics: Output[Metrics] = None,
    param_3: int = 2,
    param_4: str = "2",
    param_list: List[int] = None,
    model: Output[Model] = None,
) -> int:
    from dummy_components.dummy_components_v2 import ComponentTestC

    comp = ComponentTestC(
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
    return comp.execute()
