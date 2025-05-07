"""Module for parsing component functions into Kubeflow Pipeline DSL.

This module provides a parser that converts components adhering to the
ComponentProtocol into Kubeflow Pipeline DSL code.
"""

import dataclasses
from typing import List

from .base_parser import _FunctionParser
from .comp_protocol import ComponentProtocol


@dataclasses.dataclass
class FunctionParser(_FunctionParser):
    """Handle the parsing and generation of components into KFP (Kubeflow Pipelines) DSL files.

    This class is responsible for orchestrating the process of generating string representations
    of components compatible with KFP DSL, and writing them to files for usage in Kubeflow Pipelines.

    """

    def create_kfp_file_str(
        self,
        components: List[ComponentProtocol],
    ) -> str:
        """Create a KFP DSL string from a list of components.

        Args:
            components: List of components conforming to the ComponentProtocol

        Returns:
            str: The generated KFP DSL string for all components

        """
        kfp_str = ""
        for component in components:
            kfp_str += self._create_kfp_str(component)

            kfp_str += "\n\n"

        file_content = f"{self.dsl_imports}\n\n\n{kfp_str}"
        return file_content

    def parse_components_to_file(self, components: List[ComponentProtocol], filename: str) -> None:
        """Parse components into a Python file for use with Kubeflow Pipelines.

        Generate a KFP string functions representation of the components and save it to
        the target file.

        Args:
            components: List of components conforming to the ComponentProtocol
                       protocol, which defines the structure and behavior required
                       for each component to be processed by this method.
            filename: Name of the file where the generated KFP representation of
                     components will be saved.

        """
        kfp_str = self.create_kfp_file_str(components)
        self._write_to_file(filename, kfp_str)

    def _create_kfp_str(self, component: ComponentProtocol) -> str:
        """Create a KFP DSL string for a single component.

        Args:
            component: A component that adheres to the ComponentProtocol

        Returns:
            str: The generated KFP DSL string for the component

        """
        function_str = self.create_function(component)
        return function_str

    def _write_to_file(self, filename: str, file_content: str) -> None:
        """Write the generated KFP DSL code to a file.

        Args:
            filename: The name of the file to write to
            file_content: The KFP DSL code to write to the file

        """
        file_content = f"# flake8: noqa: F403, F405, B006\n{file_content}"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(file_content)
