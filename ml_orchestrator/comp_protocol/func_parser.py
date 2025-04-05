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
            kfp_str += self.create_kfp_str(component)

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
        self.write_to_file(filename, kfp_str)

    def create_kfp_str(self, component: ComponentProtocol) -> str:
        """
        Generates a string representation of a Kubeflow Pipelines (KFP) function from
        the provided component object. The resulting string represents the translation
        of the component into a format understandable by KFP.

        :param component: The component object that implements the ComponentProtocol
                          interface, serving as the input to generate the KFP function
                          string.
        :type component: ComponentProtocol
        :return: A string representation of the KFP function derived from the provided
                 component.
        :rtype: str
        """
        function_str = self.create_function(component)
        return function_str

    def write_to_file(self, filename: str, file_content: str) -> None:
        """
        Writes content to a specified file with additional preamble for flake8 exclusions.

        This method appends a preamble string, which disables specific linter rules
        for flake8, to the given file content and writes the resulting string to the
        file specified by the filename. The file will be saved with UTF-8 encoding.

        :param filename: Name of the file to which the content will be written.
        :param file_content: Content to be written to the file before appending
            the preamble for flake8 exclusions.
        :return: None
        """
        file_content = f"# flake8: noqa: F403, F405, B006\n{file_content}"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(file_content)
