# Refactored code
import dataclasses
from typing import List

from ml_orchestrator.compute_params import ComputeResources
from ml_orchestrator.env_params import EnvironmentParams
from ml_orchestrator.meta_comp import MetaComponent
from ml_orchestrator.utils.field_utils import (
    get_param_meta_data,
    get_param_meta_data_str,
)

IMPORT_COMPOUND = "from kfp.dsl import *\nfrom typing import *"


@dataclasses.dataclass
class ComponentParser:
    kfp_func_name: str
    component: MetaComponent
    environment_params: EnvironmentParams
    compute_resources: ComputeResources

    def create_function(self) -> str:
        component_variables = self.component.comp_vars()
        comp_class = self.component.__class__
        func_scope = "(\n\t" + ",\n\t".join(self.get_func_params(component_variables)) + "\n)"
        comp_scope = "(\n\t\t" + ",\n\t\t".join(self.get_comp_params(component_variables)) + "\n\t)"
        func_definition = self._format_function_definition(func_scope)
        import_compound = self._format_import_compound(comp_class)
        comp_init = f"comp = {comp_class.__name__}{comp_scope}"
        comp_run = "comp.execute()"
        str_func_body = "\n\t".join([import_compound, comp_init, comp_run])
        str_func = func_definition + "\n\t" + str_func_body
        return str_func

    def _format_function_definition(self, func_scope: str) -> str:
        return f"def {self.kfp_func_name}{func_scope}:"

    def _format_import_compound(self, comp_class: type) -> str:
        return f"from {comp_class.__module__} import {comp_class.__name__}"

    @staticmethod
    def create_decorator(environment_params: EnvironmentParams) -> str:
        dec_vars = environment_params.comp_vars()
        prams = ComponentParser.get_func_params(dec_vars, with_typing=False)
        override_params = ComponentParser._get_decorator_override_params(prams)
        dec_scope = "(\n\t" + ",\n\t".join(override_params) + "\n)"
        func_definition = f"@component{dec_scope}"
        return func_definition

    @staticmethod
    def _get_decorator_override_params(prams: List[str]) -> List[str]:
        return [p for p in prams if "None" not in p]

    @staticmethod
    def get_func_params(comp_vars: dict, with_typing: bool = True) -> List[str]:
        return [
            get_param_meta_data_str(*get_param_meta_data(k, v), with_typing=with_typing) for k, v in comp_vars.items()
        ]

    @staticmethod
    def get_comp_params(comp_vars: dict) -> List[str]:
        return [f"{k.name}={k.name}" for k, v in comp_vars.items()]

    @staticmethod
    def write_to_file(filename: str, content: str) -> None:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)

    def create_kfp_str(self) -> str:
        environment_params = self.environment_params or self.component.env
        decorator_str = self.create_decorator(environment_params)
        decorator_str = decorator_str.replace(" = ", "=")
        function_str = self.create_function()
        kfp_component_str = f"{decorator_str}\n{function_str}"
        kfp_component_str = f"{IMPORT_COMPOUND}\n\n\n{kfp_component_str}"
        kfp_component_str = kfp_component_str.replace("\t", "    ")
        return kfp_component_str + "\n"
