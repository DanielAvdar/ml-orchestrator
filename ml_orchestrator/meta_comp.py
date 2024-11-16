import abc
import dataclasses
from typing import Any, Dict

from ml_orchestrator.env_params import EnvironmentParams


@dataclasses.dataclass
class MetaComponent(abc.ABC):
    @abc.abstractmethod
    def execute(
        self,
    ) -> None: ...

    @classmethod
    def kfp_func_name(cls) -> str:
        return cls.__name__.lower()

    def comp_vars(self) -> Dict[dataclasses.Field, Any]:
        fields = dataclasses.fields(self.__class__)
        ins_vars = dict()
        for field in fields:
            ins_vars[field] = getattr(self, field.name)

        return ins_vars

    @property
    def env(self) -> EnvironmentParams:
        return EnvironmentParams()
