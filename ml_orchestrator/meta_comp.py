import abc
import dataclasses

from ml_orchestrator.env_params import EnvironmentParams


@dataclasses.dataclass
class _MetaComponent(abc.ABC):
    @abc.abstractmethod
    def execute(
        self,
    ) -> None: ...

    @classmethod
    def kfp_func_name(cls) -> str:
        return cls.__name__.lower()


@dataclasses.dataclass
class MetaComponent(_MetaComponent):
    @property
    def env(self) -> EnvironmentParams:
        return EnvironmentParams()

    @classmethod
    def kfp_func_name(cls) -> str:
        return cls.__name__.lower()


@dataclasses.dataclass
class MetaComponentV2(_MetaComponent):
    @classmethod
    @abc.abstractmethod
    def env(cls) -> EnvironmentParams: ...
