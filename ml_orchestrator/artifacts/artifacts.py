from ml_orchestrator.artifacts import Artifact


class Model(Artifact):
    schema_title: str = "system.Model"


class Dataset(Artifact):
    pass


class HTML(Artifact):
    pass


class Markdown(Artifact):
    pass


class Metric(Artifact):
    def log_metric(self, metric: str, value: float) -> None:
        self.metadata[metric] = value
