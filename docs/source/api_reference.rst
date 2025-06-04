.. _api_reference:


API Reference
=============

This section provides an auto-generated summary of the main public APIs.

Top-Level Exports
-------------------
The following components and functions are available directly from the ``ml_orchestrator`` package:

.. automodule:: ml_orchestrator
   :members:
   :undoc-members:
   :show-inheritance:

Core Modules
------------

.. automodule:: ml_orchestrator.meta_comp
   :members:
   :undoc-members:
   :show-inheritance:
   :synopsis: Base classes for creating custom components.

.. automodule:: ml_orchestrator.env_params
   :members:
   :undoc-members:
   :show-inheritance:
   :synopsis: Defines component runtime environments.

.. automodule:: ml_orchestrator.artifacts
   :members:
   :undoc-members:
   :show-inheritance:
   :synopsis: Defines standard and custom artifact types.

Component Parsers
-----------------

.. automodule:: ml_orchestrator.comp_parser
   :members:
   :undoc-members:
   :show-inheritance:
   :synopsis: Parses components into KFP YAML specifications.

.. automodule:: ml_orchestrator.comp_protocol.func_parser
   :members: FunctionParser, KFP_FUNC_HEADER
   :undoc-members:
   :show-inheritance:
   :synopsis: Parses components into Python functions for KFP.

.. automodule:: ml_orchestrator.comp_protocol.comp_protocol
   :members:
   :undoc-members:
   :show-inheritance:
   :synopsis: Defines the core protocol (interface) for ml-orchestrator components.
