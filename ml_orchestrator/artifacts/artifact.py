from typing import Dict, Optional


class Artifact:
    schema_title = "system.Artifact"
    schema_version = "0.0.1"

    def __init__(self, name: Optional[str] = None, uri: Optional[str] = None, metadata: Optional[Dict] = None) -> None:
        self.uri = uri or "./"
        self.name = name or "artifact"
        self.metadata = metadata or {}

    @property
    def path(self) -> str:
        return self.uri
