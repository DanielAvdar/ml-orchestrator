import dataclasses
from typing import List

from ml_orchestrator.comp_protocol.func_parser import FunctionParser
from ml_orchestrator.env_params import EnvironmentParams
from ml_orchestrator.meta_comp import MetaComponent, _MetaComponent


@dataclasses.dataclass
class ComponentParser(FunctionParser):
    add_imports: List[str] = dataclasses.field(default_factory=lambda: [])
    only_function: bool = False

    @classmethod
    def _create_decorator(cls, env: EnvironmentParams) -> str:
        dec_vars = env.comp_vars()
        prams = ComponentParser.get_func_params(dec_vars, with_typing=False)
        override_params = ComponentParser._get_decorator_override_params(prams)
        dec_scope = "(\n\t" + ",\n\t".join(override_params) + "\n)"
        dec_scope = ComponentParser.convert_to_format_str(dec_scope)
        func_definition = f"@component{dec_scope}"
        return func_definition

    @classmethod
    def create_decorator(cls, component: MetaComponent) -> str:
        if isinstance(component, MetaComponent):
            return cls._create_decorator(component.env)
        return cls._create_decorator(component.env())

    @staticmethod
    def convert_to_format_str(text: str) -> str:
        new_text = text.replace(", '", ", f'").replace("['", "[f'")
        new_text = new_text.replace(', "', ', f"').replace('["', '[f"')
        return new_text

    @staticmethod
    def _get_decorator_override_params(prams: List[str]) -> List[str]:
        return [p for p in prams if "None" not in p]

    def create_kfp_str(self, component: _MetaComponent) -> str:  # type: ignore
        function_str = super().create_kfp_str(component)  # type: ignore
        if self.only_function:
            return function_str

        decorator_str = self.create_decorator(component)  # type: ignore
        decorator_str = decorator_str.replace(" = ", "=")
        kfp_component_str = f"{decorator_str}\n{function_str}"
        kfp_component_str = kfp_component_str.replace("\t", "    ")
        return kfp_component_str + "\n"

    def write_to_file(self, filename: str, file_content: str) -> None:
        for imp in self.add_imports:
            file_content = f"{imp}\n{file_content}"
        return super().write_to_file(filename, file_content)
