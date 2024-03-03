import dataclasses


@dataclasses.dataclass
class Artifact:
    name: str | None = None
    uri: str | None = None
    metadata: dict | None = None

    @property
    def path(self) -> str:
        return self.uri
