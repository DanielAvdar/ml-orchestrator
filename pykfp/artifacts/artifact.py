import dataclasses


@dataclasses.dataclass
class Artifact:
    name: str = None
    uri: str = None
    metadata: dict = None

    @property
    def path(self) -> str:
        return self.uri
