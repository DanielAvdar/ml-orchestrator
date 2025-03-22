# flake8: noqa: F403, F405, B006
from typing import *

from kfp.dsl import *


def component_with_mandatory_param(
    param_mandatory_int: int,
):
    from dummy_components.protocol_components import ComponentWithMandatoryParam

    comp = ComponentWithMandatoryParam(
        param_mandatory_int=param_mandatory_int,
    )
    comp.execute()
