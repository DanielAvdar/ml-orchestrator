import dataclasses
from typing import Any, Dict, List, Tuple


@dataclasses.dataclass(unsafe_hash=True)
class EnvironmentParams:
    base_image: str = None
    target_image: str = None
    packages_to_install: List[str] = dataclasses.field(default_factory=lambda: None)
    pip_index_urls: List[str] = dataclasses.field(default_factory=lambda: None)
    install_kfp_package: bool = None
    kfp_package_path: str = None

    @classmethod
    def comp_fields(cls) -> Tuple[dataclasses.Field, ...]:
        return dataclasses.fields(cls)

    def comp_vars(self) -> Dict[dataclasses.Field, Any]:
        fields = self.comp_fields()
        ins_vars = dict()
        for field in fields:
            ins_vars[field] = getattr(self, field.name)

        return ins_vars
