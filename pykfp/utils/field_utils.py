import dataclasses
from typing import Any, Tuple


def get_artifact_type_string(field_type: type):
    artifact_type = field_type.__args__[0].__name__
    side = "Input" if "input" in field_type.__metadata__[0] else "Output"

    return f"{side}[{artifact_type}]"


def get_param_meta_data(field: dataclasses.Field, value: Any) -> Tuple[str, str, Any]:
    name = field.name
    field_type = field.type.__name__
    try:
        field_value = value if value is not None else field.default_factory()()
    except TypeError:
        field_value = None
    if field_type == "Annotated":
        field_type = get_artifact_type_string(field.type)
    return name, field_type, field_value


def get_param_meta_data_str(
    name: str, field_type: str, value: Any, with_typing=True
) -> str:
    if field_type == "str":
        value = f'"{value}"'

    if with_typing:
        md_str = f"{name}: {field_type} = {value}"
    else:
        md_str = f"{name} = {value}"
    # if field_type.__name__ == 'str':

    return md_str
