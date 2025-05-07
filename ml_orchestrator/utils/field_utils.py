"""Utility functions for working with dataclass fields.

This module provides utility functions for extracting type information and
formatting parameter metadata from dataclass fields, particularly for
generating function signatures.
"""

import dataclasses
from typing import Any, Tuple


def get_artifact_type_string(field_type: Any) -> str:
    """Extract a string representation of a field type.

    Handles annotated types, regular types, and typing types to generate
    a clean string representation suitable for use in generated code.

    Args:
        field_type: The type annotation to convert to a string

    Returns:
        A string representation of the type that can be used in code generation

    """
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
    """Extract the name, type, and value from a dataclass field.

    Args:
        field: The dataclass field to extract metadata from
        value: The current value of the field

    Returns:
        A tuple containing the field name, type string, and value

    """
    name = field.name
    field_value = value
    if callable(field.default_factory) and field_value is None:
        field_value = field.default_factory()
    field_type = get_artifact_type_string(field.type)
    return name, field_type, field_value


def get_param_meta_data_str(name: str, field_type: str, value: Any, with_typing: bool = True) -> str:
    """Generate a string representation of a parameter for function signatures.

    Args:
        name: The parameter name
        field_type: The string representation of the parameter type
        value: The default value of the parameter, if any
        with_typing: Whether to include type annotations in the output

    Returns:
        A formatted string representation of the parameter, suitable for use in
        a function signature

    """
    md_str = f"{name}"
    if with_typing:
        md_str = f"{md_str}: {field_type}"
    if value is not dataclasses.MISSING:
        if field_type == "str":
            value = f'"{value}"'
        md_str += f" = {value}"

    return md_str
