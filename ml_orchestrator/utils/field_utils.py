import dataclasses
from typing import Any, Tuple


def get_artifact_type_string(field_type: Any) -> str:
    if "Annotated" in str(field_type):
        artifact_type = repr(field_type.__args__[0]).split("'")[-2].split(".")[-1]

        side = "Input" if "input" in field_type.__metadata__[0] else "Output"
        return f"{side}[{artifact_type}]"
    if not isinstance(field_type, type):
        field_type_name = repr(field_type)
        return field_type_name.replace("typing.", "")

    field_type_name = field_type.__qualname__
    return field_type_name


def get_param_meta_data(field: dataclasses.Field, value: Any) -> Tuple[str, str, Any]:
    name = field.name
    try:
        field_value = value
    except TypeError:
        field_value = None
    if callable(field.default_factory) and field_value is None:
        field_value = field.default_factory()
    field_type = get_artifact_type_string(field.type)
    return name, field_type, field_value


def get_param_meta_data_str(name: str, field_type: str, value: Any, with_typing: bool = True) -> str:
    md_str = f"{name}"
    if with_typing:
        md_str = f"{md_str}: {field_type}"
    if value is not dataclasses.MISSING:
        if field_type == "str":
            value = f'"{value}"'
        md_str += f" = {value}"

    return md_str
