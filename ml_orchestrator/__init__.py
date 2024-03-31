from importlib.metadata import version

from .comp_parser import ComponentParser
from .env_params import EnvironmentParams
from .meta_comp import MetaComponent

__version__ = version("ml-orchestrator")
__all__ = [
    "ComponentParser",
    "MetaComponent",
    "EnvironmentParams",
]
