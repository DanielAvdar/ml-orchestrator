import dataclasses
from typing import Dict, List, Set, Type

from ml_orchestrator.env_params import EnvironmentParams
from ml_orchestrator.meta_comp import MetaComponent
from ml_orchestrator.utils.field_utils import (
    get_param_meta_data,
    get_param_meta_data_str,
)

IMPORT_COMPOUND = "from kfp.dsl import *\nfrom typing import *\nimport importlib\n"


@dataclasses.dataclass
class ComponentParser:
    def create_function(self, component: MetaComponent) -> str:
        kfp_func_name = component.kfp_func_name
        component_variables = component.comp_vars()
        comp_class = component.__class__
        func_scope = "(\n\t" + ",\n\t".join(self.get_func_params(component_variables)) + "\n)"
        comp_scope = "(\n\t\t" + ",\n\t\t".join(self.get_comp_params(component_variables)) + "\n\t)"
        func_definition = self._format_function_definition(kfp_func_name, func_scope)
        import_compound = self._format_import_compound(comp_class)
        comp_init = f"comp = {comp_class.__name__}{comp_scope}"
        comp_run = "comp.execute()"
        str_func_body = "\n\t".join([import_compound, comp_init, comp_run])
        str_func = func_definition + "\n\t" + str_func_body
        return str_func

    def _format_function_definition(self, kfp_func_name: str, func_scope: str) -> str:
        return f"def {kfp_func_name}{func_scope}:"

    def _format_import_compound(self, comp_class: Type) -> str:
        return f"from {comp_class.__module__} import {comp_class.__name__}"

    @staticmethod
    def create_decorator(env: EnvironmentParams) -> str:
        dec_vars = env.comp_vars()
        prams = ComponentParser.get_func_params(dec_vars, with_typing=False)
        override_params = ComponentParser._get_decorator_override_params(prams)
        dec_scope = "(\n\t" + ",\n\t".join(override_params) + "\n)"
        dec_scope = dec_scope.replace(", '", ", f'").replace("['", "[f'")
        func_definition = f"@component{dec_scope}"
        return func_definition

    @staticmethod
    def _get_decorator_override_params(prams: List[str]) -> List[str]:
        return [p for p in prams if "None" not in p]

    @staticmethod
    def get_func_params(comp_vars: Dict, with_typing: bool = True) -> List[str]:
        return [
            get_param_meta_data_str(*get_param_meta_data(k, v), with_typing=with_typing) for k, v in comp_vars.items()
        ]

    @staticmethod
    def get_comp_params(comp_vars: Dict) -> List[str]:
        return [f"{k.name}={k.name}" for k, v in comp_vars.items()]

    @staticmethod
    def write_to_file(filename: str, content: str) -> None:
        file_content = f"{IMPORT_COMPOUND}\n\n\n{content}"
        file_content = f"# flake8: noqa: F403, F405\n{file_content}"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(file_content)

    def create_kfp_str(self, component: MetaComponent) -> str:
        decorator_str = self.create_decorator(component.env)
        decorator_str = decorator_str.replace(" = ", "=")
        function_str = self.create_function(component)
        kfp_component_str = f"{decorator_str}\n{function_str}"
        kfp_component_str = kfp_component_str.replace("\t", "    ")
        return kfp_component_str + "\n"

    @staticmethod
    def parse_components_to_file(components: List[MetaComponent], filename: str) -> None:
        kfp_str = ""
        for component in components:
            parser = ComponentParser()
            kfp_str += parser.create_kfp_str(component)
            kfp_str += "\n\n"
        all_unique_params_names: Set[str] = set()
        for component in components:
            all_unique_params_names.update([p.name for p in component.comp_fields()])
        comment_str = "\n# " + "\n# ".join([f"{p}: {p}" for p in all_unique_params_names])
        kfp_str = f"{kfp_str}\n{comment_str}"

        ComponentParser.write_to_file(filename, kfp_str)
