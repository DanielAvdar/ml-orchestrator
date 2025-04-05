import dataclasses
from typing import Any, Dict, List, Tuple


@dataclasses.dataclass(unsafe_hash=True)
class EnvironmentParams:
    """
    A dataclass for defining the configuration parameters used to set up the environment
    for pipeline components, including Docker images, package installations, and Kubeflow settings.

    Attributes:
        base_image (str): The base Docker image to use for building and running pipeline components.
        target_image (str): The Docker image to be built as the finalized environment for pipeline execution.
        packages_to_install (List[str]): A list of additional packages to be installed inside the Docker image.
        pip_index_urls (List[str]): A list of custom pip index URLs that can be used to search for Python packages.
        install_kfp_package (bool): Indicates whether the Kubeflow Pipelines (KFP) package should be installed.
        kfp_package_path (str): The path or URL for the Kubeflow Pipelines (KFP) package to be used for installation.
    """

    base_image: str = None
    target_image: str = None
    packages_to_install: List[str] = dataclasses.field(default_factory=lambda: None)
    pip_index_urls: List[str] = dataclasses.field(default_factory=lambda: None)
    install_kfp_package: bool = None
    kfp_package_path: str = None

    @classmethod
    def comp_fields(cls) -> Tuple[dataclasses.Field, ...]:
        """
        Retrieve all the fields defined in the `EnvironmentParams` dataclass.

        Returns:
            Tuple[dataclasses.Field, ...]: A tuple of field definitions.
        """
        return dataclasses.fields(cls)

    def comp_vars(self) -> Dict[dataclasses.Field, Any]:
        """
        Retrieve a mapping of each dataclass field to its corresponding value
        for the current instance.

        Returns:
            Dict[dataclasses.Field, Any]: A dictionary mapping fields to their current values.
        """
        fields = self.comp_fields()
        ins_vars = dict()
        for field in fields:
            ins_vars[field] = getattr(self, field.name)

        return ins_vars
