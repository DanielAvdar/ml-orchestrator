"""Module for defining meta-components for ML pipelines.

This module provides abstract and concrete base classes for ML pipeline
components, defining the interface and basic functionality that all
components must implement.
"""

import abc
import dataclasses

from ml_orchestrator.env_params import EnvironmentParams


@dataclasses.dataclass
class _MetaComponent(abc.ABC):
    """Abstract base class for all meta-components.

    Defines the core interface that all components must implement, including
    an execute method and a method to get the function name for Kubeflow Pipelines.
    """

    @abc.abstractmethod
    def execute(
        self,
    ) -> None:
        """Execute the component's main functionality.

        Returns:
            None

        """
        ...

    @classmethod
    def kfp_func_name(cls) -> str:
        """Get the function name for this component in Kubeflow Pipelines.

        Returns:
            str: The lowercase class name of the component

        """
        return cls.__name__.lower()


@dataclasses.dataclass
class MetaComponent(_MetaComponent):
    """Concrete MetaComponent with default environment parameters.

    This class provides default environment parameters and a method for
    retrieving the component's function name in lowercase format.

    Attributes:
        env (EnvironmentParams): Environment parameters for the component.

    """

    @property
    def env(self) -> EnvironmentParams:
        """Get the environment parameters for this component.

        Returns:
            EnvironmentParams: A default EnvironmentParams instance.

        """
        return EnvironmentParams()

    @classmethod
    def kfp_func_name(cls) -> str:
        """Get the name of the Kubeflow Pipeline function for this component.

        Returns:
            str: The lowercase class name of the component.

        """
        return cls.__name__.lower()


@dataclasses.dataclass
class MetaComponentV2(_MetaComponent):
    """Abstract MetaComponent requiring custom environment parameters.

    This class requires implementing classes to define their own environment
    parameters via a class method.

    Methods:
        env (classmethod): Abstract method to retrieve environment parameters.

    """

    @classmethod
    @abc.abstractmethod
    def env(cls) -> EnvironmentParams:
        """Get the environment parameters for the component.

        Returns:
            EnvironmentParams: The environment parameters specific to the implementing class.

        """
