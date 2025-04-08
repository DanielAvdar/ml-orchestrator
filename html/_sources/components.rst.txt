.. _components:

Components
==========

This section explains the key components provided by **ml-orchestrator** with examples.

MetaComponent and Variants
--------------------------
The `MetaComponent` is a base class designed for implementing custom components for machine learning workflows.

Example:

.. code-block:: python

   from ml_orchestrator.meta_comp import MetaComponent

   class DummyComponent(MetaComponent):
       @property
       def env(self):
           return self.env_params()

       def execute(self):
           print("Hello, World!")

Component Parsers
-----------------
The `ComponentParser` class extends `FunctionParser` to allow generating components as serialized Kubeflow Pipelines (KFP).

Example usage:

.. code-block:: python

   from ml_orchestrator.comp_parser import ComponentParser
   from ml_orchestrator.meta_comp import MetaComponent

   class MyComponent(MetaComponent):
       @property
       def env(self):
           return ...  # Define environment parameters
