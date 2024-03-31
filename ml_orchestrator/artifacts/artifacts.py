from typing import Dict, Optional

from ml_orchestrator.artifacts import Artifact


class Model(Artifact):
    schema_title: str = "system.Model"


class Dataset(Artifact):
    pass


class HTML(Artifact):
    def __init__(self, name: Optional[str] = None, uri: Optional[str] = None, metadata: Optional[Dict] = None) -> None:
        super().__init__(name=name, uri=uri, metadata=metadata)
        self.uri = self.uri + ".html"

    pass


class Markdown(Artifact):
    pass


class Metrics(Artifact):
    def log_metric(self, metric: str, value: float) -> None:
        assert isinstance(value, (int, float, bool, str)), f"Type {type(value)} is not a valid metric value"
        assert isinstance(metric, str), f"Type {type(metric)} is not a valid metric name"
        self.metadata[metric] = value
