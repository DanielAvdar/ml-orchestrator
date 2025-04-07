import abc
import dataclasses

from ml_orchestrator.env_params import EnvironmentParams


@dataclasses.dataclass
class _MetaComponent(abc.ABC):
    @abc.abstractmethod
    def execute(
        self,
    ) -> None: ...

    @classmethod
    def kfp_func_name(cls) -> str:
        return cls.__name__.lower()


@dataclasses.dataclass
class MetaComponent(_MetaComponent):
    """
    Represents a concrete MetaComponent that provides default environment parameters
    and a method for retrieving the component's function name in lowercase format.

    Attributes:
        env (EnvironmentParams): Environment parameters for the component.
    """

    @property
    def env(self) -> EnvironmentParams:
        """
        Returns the environment parameters for this component.

        Returns:
            EnvironmentParams: A default EnvironmentParams instance.
        """
        return EnvironmentParams()

    @classmethod
    def kfp_func_name(cls) -> str:
        """
        Retrieves the name of the Kubeflow Pipeline function for this component.

        Returns:
            str: The lowercase class name of the component.
        """
        return cls.__name__.lower()


@dataclasses.dataclass
class MetaComponentV2(_MetaComponent):
    """
    Represents a more abstract MetaComponent that requires implementing classes
    to define their own environment parameters via a class method.

    Methods:
        env (classmethod): Abstract method to retrieve environment parameters.
    """

    @classmethod
    @abc.abstractmethod
    def env(cls) -> EnvironmentParams:
        """
        Abstract method to retrieve the environment parameters for the component.

        Returns:
            EnvironmentParams: The environment parameters specific to the implementing class.
        """
