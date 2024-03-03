import dataclasses
from typing import Any, Tuple


def get_param_meta_data(field: dataclasses.Field, value: Any) -> Tuple[str, type, Any]:
    name = field.name
    field_type = field.type
    try:
        field_value = (
            value if value is not None else field.default or field.default_factory()
        )
    except TypeError:
        field_value = None
    return name, field_type, field_value


def get_param_meta_data_str(
    name: str, field_type: type, value: Any, with_typing=True
) -> str:
    if field_type.__name__ == "str":
        value = f'"{value}"'

    if with_typing:
        md_str = f"{name}: {field_type.__name__} = {value}"
    else:
        md_str = f"{name} = {value}"
    # if field_type.__name__ == 'str':

    return md_str
