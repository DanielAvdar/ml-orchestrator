from typing import Any, Protocol, Union, runtime_checkable

ComponentOutput = Union[None, str, int, float, bool, list, dict]


@runtime_checkable
class ComponentProtocol(Protocol):
    def execute(self) -> ComponentOutput: ...

    def __dataclass_fields__(self) -> Any: ...
