# flake8: noqa: F403, F405, B006
from typing import *

from kfp.dsl import *


def component_with_mandatory_param_b(
    param_mandatory_int: int,
    param_mandatory_str: str,
    param_mandatory_list: List[int],
    param_mandatory_list_2: List[int] = [],
    param_dict_full: dict = {"a": 1, "b": 2},
    param_dict_nan: dict = None,
    param_2: str = "1",
):
    from dummy_components.protocol_components import ComponentWithMandatoryParamB

    comp = ComponentWithMandatoryParamB(
        param_mandatory_int=param_mandatory_int,
        param_mandatory_str=param_mandatory_str,
        param_mandatory_list=param_mandatory_list,
        param_mandatory_list_2=param_mandatory_list_2,
        param_dict_full=param_dict_full,
        param_dict_nan=param_dict_nan,
        param_2=param_2,
    )
    comp.execute()
