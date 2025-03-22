import json
from typing import Any, Dict, Mapping, Optional


class JSONSerializableDict(dict):
    def __setitem__(self, key: Any, value: Any) -> None:
        try:
            json.dumps(value)
            return super().__setitem__(key, value)

        except (TypeError, OverflowError, ValueError):
            pass
        raise ValueError(f"Value for key '{key}' is not JSON serializable: {value}")

    def update(self, m: Mapping = None, **kwargs: Any) -> None:  # type: ignore[override]
        try:
            json.dumps(m)
            return super().update(m, **kwargs)

        except TypeError:
            pass
        raise ValueError(f"Aritfact metadata must be JSON serializable, got: {m}")

    def __or__(self, other: Mapping) -> "JSONSerializableDict":
        new_dict = JSONSerializableDict(self)
        new_dict.update(other)
        return new_dict


class Artifact:
    schema_title = "system.Artifact"
    schema_version = "0.0.1"

    def __init__(self, name: Optional[str] = None, uri: Optional[str] = None, metadata: Optional[Dict] = None) -> None:
        self.uri = uri or "./"
        self.name = name or "artifact"
        self._metadata = JSONSerializableDict(metadata or dict())

    @property
    def path(self) -> str:
        return self.uri

    @property
    def metadata(self) -> "JSONSerializableDict":
        return self._metadata

    @metadata.setter
    def metadata(self, new_data: Mapping) -> None:
        try:
            json.dumps(new_data)
            self._metadata = JSONSerializableDict(new_data)
            return

        except TypeError:
            pass
        raise ValueError(f"Aritfact metadata is not JSON serializable: {new_data}")
