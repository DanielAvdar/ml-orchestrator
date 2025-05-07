"""ML Orchestrator package for machine learning pipeline components management.

This package provides tools for creating, parsing, and managing machine learning
pipeline components with a focus on Kubeflow Pipelines integration.
"""

from importlib.metadata import version

from .comp_parser import ComponentParser
from .comp_protocol.func_parser import FunctionParser
from .env_params import EnvironmentParams
from .meta_comp import MetaComponent

__version__ = version("ml-orchestrator")
__all__ = ["ComponentParser", "FunctionParser", "MetaComponent", "EnvironmentParams"]
