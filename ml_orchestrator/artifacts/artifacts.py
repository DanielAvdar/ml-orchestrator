from typing import Dict, Optional, Union

from ml_orchestrator.artifacts import Artifact

MetricTypes = Union[int, float, bool, str]


class Model(Artifact):
    schema_title: str = "system.Model"


class Dataset(Artifact):
    schema_title = "system.Dataset"

    pass


class HTML(Artifact):
    schema_title = "system.HTML"

    def __init__(self, name: Optional[str] = None, uri: Optional[str] = None, metadata: Optional[Dict] = None) -> None:
        super().__init__(name=name, uri=uri, metadata=metadata)
        self.uri = self.uri + ".html"


class Markdown(Artifact):
    schema_title = "system.Markdown"


class Metrics(Artifact):
    schema_title = "system.Metrics"

    def log_metric(self, metric: str, value: MetricTypes) -> None:
        assert isinstance(value, (int, float, bool, str)), f"Type {type(value)} is not a valid metric value"
        assert isinstance(metric, str), f"Type {type(metric)} is not a valid metric name"
        self.metadata[metric] = value
