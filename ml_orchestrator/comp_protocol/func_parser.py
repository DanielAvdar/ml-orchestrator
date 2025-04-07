import dataclasses
from typing import List

from .base_parser import _FunctionParser
from .comp_protocol import ComponentProtocol


@dataclasses.dataclass
class FunctionParser(_FunctionParser):
    """
    Handles the parsing and generation of components into KFP (Kubeflow Pipelines) DSL files.

    This class is responsible for orchestrating the process of generating string representations
    of components compatible with KFP DSL, and writing them to files for usage in Kubeflow Pipelines.

    """

    def create_kfp_file_str(
        self,
        components: List[ComponentProtocol],
    ) -> str:
        kfp_str = ""
        for component in components:
            kfp_str += self._create_kfp_str(component)

            kfp_str += "\n\n"

        file_content = f"{self.dsl_imports}\n\n\n{kfp_str}"
        return file_content

    def parse_components_to_file(self, components: List[ComponentProtocol], filename: str) -> None:
        """
        Parses a list of components adhering to the ComponentProtocol into a py file
        and writes the result to the specified file. This process involves generating a
        KFP string functions representation of the components and saving it to the target file.

        :param components: List of components conforming to the ComponentProtocol
                           protocol, which defines the structure and behavior required
                           for each component to be processed by this method.

        :param filename: Name of the file where the generated KFP representation of
                         components will be saved.

        :return: This method does not return anything as its purpose is to perform file
                 writing as a side effect.
        """
        kfp_str = self.create_kfp_file_str(components)
        self._write_to_file(filename, kfp_str)

    def _create_kfp_str(self, component: ComponentProtocol) -> str:
        function_str = self.create_function(component)
        return function_str

    def _write_to_file(self, filename: str, file_content: str) -> None:
        file_content = f"# flake8: noqa: F403, F405, B006\n{file_content}"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(file_content)
