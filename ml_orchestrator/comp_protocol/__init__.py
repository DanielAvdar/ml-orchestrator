"""Component protocol package for ML pipeline components.

This package defines the protocols and interfaces for ML pipeline components,
as well as parsers for handling these components.
"""

from ml_orchestrator.comp_protocol.comp_protocol import ComponentOutput, ComponentProtocol
from ml_orchestrator.comp_protocol.func_parser import FunctionParser

__all__ = ["ComponentOutput", "ComponentProtocol", "FunctionParser"]
