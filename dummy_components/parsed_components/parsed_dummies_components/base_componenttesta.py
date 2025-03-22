# flake8: noqa: F403, F405, B006
from typing import *

from kfp.dsl import *


def componenttesta(
    param_1: int = 1,
    param_2: str = "1",
    artifact: Input[Dataset] = None,
    out_artifact: Output[Dataset] = None,
    metrics: Output[Metrics] = None,
):
    from dummy_components.dummy_components_v2 import ComponentTestA

    comp = ComponentTestA(
        param_1=param_1,
        param_2=param_2,
        artifact=artifact,
        out_artifact=out_artifact,
        metrics=metrics,
    )
    comp.execute()
