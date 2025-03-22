import dataclasses
from typing import List

from .base_parser import _FunctionParser
from .comp_protocol import ComponentProtocol


@dataclasses.dataclass
class FunctionParser(_FunctionParser):
    def create_kfp_file_str(
        self,
        components: List[ComponentProtocol],
    ) -> str:
        kfp_str = ""
        for component in components:
            kfp_str += self.create_kfp_str(component)

            kfp_str += "\n\n"

        file_content = f"{self.dsl_imports}\n\n\n{kfp_str}"
        return file_content

    def parse_components_to_file(self, components: List[ComponentProtocol], filename: str) -> None:
        kfp_str = self.create_kfp_file_str(components)
        self.write_to_file(filename, kfp_str)

    def create_kfp_str(self, component: ComponentProtocol) -> str:
        function_str = self.create_function(component)
        return function_str

    def write_to_file(self, filename: str, file_content: str) -> None:
        file_content = f"# flake8: noqa: F403, F405, B006\n{file_content}"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(file_content)
