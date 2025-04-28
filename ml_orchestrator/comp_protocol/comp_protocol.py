"""Module defining protocols and interfaces for ML pipeline components.

This module provides protocol classes that define the expected behavior
of machine learning pipeline components.
"""

from typing import Any, Protocol, Union, runtime_checkable

ComponentOutput = Union[None, str, int, float, bool, list, dict]


@runtime_checkable
class ComponentProtocol(Protocol):
    """A protocol defining the structure of a Component object.

    Methods:
        execute() -> ComponentOutput:
            Execute the component and return the output, which can
            be one of the types defined in `ComponentOutput`.

        __dataclass_fields__() -> Any:
            Provide access to the dataclass fields of the component.

    """

    def execute(self) -> ComponentOutput:
        """Execute the component and return the output.

        Returns:
            ComponentOutput: The result of the component's execution.

        """

    def __dataclass_fields__(self) -> Any:
        """Provide access to the dataclass fields of the component.

        Returns:
            Any: Metadata or structure defining the dataclass fields.

        """
