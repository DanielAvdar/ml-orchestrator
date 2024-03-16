import abc
import dataclasses
from typing import Any, Dict, Tuple

from ml_orchestrator.env_params import EnvironmentParams


@dataclasses.dataclass
class MetaComponent(abc.ABC):
    @property
    def kfp_func_name(self) -> str:
        return self.__class__.__name__.lower()

    @abc.abstractmethod
    def execute(
        self,
    ) -> None:
        pass

    @classmethod
    def comp_fields(cls) -> Tuple[dataclasses.Field, ...]:
        return dataclasses.fields(cls)

    def comp_vars(self) -> Dict[dataclasses.Field, Any]:
        fields = self.comp_fields()
        ins_vars = dict()
        for field in fields:
            ins_vars[field] = getattr(self, field.name)

        return ins_vars

    @property
    def env(self) -> EnvironmentParams:
        # ml_orchestrator_ver = importlib.metadata.version("ml-orchestrator")
        return EnvironmentParams()
