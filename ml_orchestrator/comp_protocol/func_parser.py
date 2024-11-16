import dataclasses
from typing import Any, Dict, List, Tuple, Type, Union

from ml_orchestrator.utils.field_utils import get_param_meta_data, get_param_meta_data_str

from .comp_protocol import ComponentProtocol

IMPORT_COMPOUND = "from kfp.dsl import *\nfrom typing import *\nfrom importlib.metadata import version\n"


@dataclasses.dataclass
class FunctionParser:
    @classmethod
    def get_class_def(cls, component: Union[type, ComponentProtocol]) -> type:
        is_class_def = isinstance(component, type)
        com_class = component if is_class_def else component.__class__
        return com_class  # type: ignore

    def create_function(self, component: ComponentProtocol) -> str:
        comp_class = self.get_class_def(component)
        comp_init, func_definition = self.get_function_parts(comp_class)
        import_compound = f"from {comp_class.__module__} import {comp_class.__name__}"
        comp_run = self.comp_execute(comp_class)
        str_func_body = "\n\t".join([import_compound, comp_init, comp_run])
        str_func = func_definition + "\n\t" + str_func_body
        return str_func

    def get_function_parts(self, comp_class: Type[ComponentProtocol]) -> Tuple[str, str]:
        component_variables = self.comp_vars(comp_class)
        kfp_func_name = comp_class.__name__.lower()
        func_scope = "(\n\t" + ",\n\t".join(self.get_func_params(component_variables)) + "\n)"
        comp_scope = "(\n\t\t" + ",\n\t\t".join(self.get_comp_params(component_variables)) + "\n\t)"
        func_definition = f"def {kfp_func_name}{func_scope}:"
        comp_init = f"comp = {comp_class.__name__}{comp_scope}"
        return comp_init, func_definition

    @classmethod
    def comp_execute(cls, comp: Type[ComponentProtocol]) -> str:
        execute_return_type = comp.execute.__annotations__.get("return")
        comp_run = "comp.execute()"
        if execute_return_type is not None:
            comp_run = "return comp.execute()"
        return comp_run

    @staticmethod
    def get_func_params(comp_vars: Dict[dataclasses.Field, Any], with_typing: bool = True) -> List[str]:
        return [
            get_param_meta_data_str(*get_param_meta_data(k, v), with_typing=with_typing) for k, v in comp_vars.items()
        ]

    @classmethod
    def comp_vars(cls, component: Type[ComponentProtocol]) -> Dict[dataclasses.Field, Any]:
        fields = dataclasses.fields(component)  # type: ignore
        ins_vars = dict()
        for field in fields:
            ins_vars[field] = getattr(component, field.name)

        return ins_vars

    @staticmethod
    def get_comp_params(comp_vars: Dict[dataclasses.Field, Any]) -> List[str]:
        return [f"{k.name}={k.name}" for k, v in comp_vars.items()]

    def create_kfp_str(self, component: ComponentProtocol) -> str:
        function_str = self.create_function(component)
        return function_str

    def create_kfp_file_str(
        self,
        components: List[ComponentProtocol],
    ) -> str:
        kfp_str = ""
        for component in components:
            kfp_str += self.create_kfp_str(component)

            kfp_str += "\n\n"

        file_content = f"{IMPORT_COMPOUND}\n\n\n{kfp_str}"
        return file_content

    def write_to_file(self, filename: str, file_content: str) -> None:
        file_content = f"# flake8: noqa: F403, F405, B006\n{file_content}"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(file_content)
