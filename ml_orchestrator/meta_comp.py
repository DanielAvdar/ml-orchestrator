import abc
import dataclasses
from typing import Any, Dict, Tuple


@dataclasses.dataclass(unsafe_hash=True)
class MetaComponent(abc.ABC):
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
