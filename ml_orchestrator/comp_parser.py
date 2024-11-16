import dataclasses
from typing import List

from ml_orchestrator.comp_protocol.comp_protocol import ComponentProtocol
from ml_orchestrator.comp_protocol.func_parser import FunctionParser
from ml_orchestrator.env_params import EnvironmentParams
from ml_orchestrator.meta_comp import MetaComponent


@dataclasses.dataclass
class ComponentParser(FunctionParser):
    add_imports: List[str] = dataclasses.field(default_factory=lambda: [])
    only_function: bool = False

    @staticmethod
    def create_decorator(env: EnvironmentParams) -> str:
        dec_vars = env.comp_vars()
        prams = ComponentParser.get_func_params(dec_vars, with_typing=False)
        override_params = ComponentParser._get_decorator_override_params(prams)
        dec_scope = "(\n\t" + ",\n\t".join(override_params) + "\n)"
        dec_scope = ComponentParser.convert_to_format_str(dec_scope)
        func_definition = f"@component{dec_scope}"
        return func_definition

    @staticmethod
    def convert_to_format_str(text: str) -> str:
        new_text = text.replace(", '", ", f'").replace("['", "[f'")
        new_text = new_text.replace(', "', ', f"').replace('["', '[f"')
        return new_text

    @staticmethod
    def _get_decorator_override_params(prams: List[str]) -> List[str]:
        return [p for p in prams if "None" not in p]

    def create_kfp_str(self, component: MetaComponent) -> str:  # type: ignore
        function_str = super().create_kfp_str(component)  # type: ignore
        if self.only_function:
            return function_str
        decorator_str = self.create_decorator(component.env)
        decorator_str = decorator_str.replace(" = ", "=")
        kfp_component_str = f"{decorator_str}\n{function_str}"
        kfp_component_str = kfp_component_str.replace("\t", "    ")
        return kfp_component_str + "\n"

    def parse_components_to_file(self, components: List[ComponentProtocol], filename: str) -> None:
        kfp_str = self.create_kfp_file_str(components)
        self.write_to_file(filename, kfp_str)

    def write_to_file(self, filename: str, file_content: str) -> None:
        for imp in self.add_imports:
            file_content = f"{imp}\n{file_content}"
        return super().write_to_file(filename, file_content)
