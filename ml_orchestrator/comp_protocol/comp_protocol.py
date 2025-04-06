from typing import Any, Protocol, Union, runtime_checkable

ComponentOutput = Union[None, str, int, float, bool, list, dict]


@runtime_checkable
class ComponentProtocol(Protocol):
    """
    A protocol defining the structure of a Component object.

    Methods:
        execute() -> ComponentOutput:
            Executes the component and returns the output, which can
            be one of the types defined in `ComponentOutput`.

        __dataclass_fields__() -> Any:
            Provides access to the dataclass fields of the component.
    """

    def execute(self) -> ComponentOutput:
        """
        Executes the component and returns the output.

        Returns:
            ComponentOutput: The result of the component's execution.
        """

    def __dataclass_fields__(self) -> Any:
        """
        Returns the dataclass fields of the component.

        Returns:
            Any: Metadata or structure defining the dataclass fields.
        """
