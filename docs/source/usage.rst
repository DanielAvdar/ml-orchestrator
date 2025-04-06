Usage Guide
===========

This guide will walk you through using the **ml-orchestrator** package in your own projects.

Installation
------------
Install the required dependencies using `Poetry`:

.. code-block:: bash

   pip install ml-orchestrator

ml-orchestrator by itself has no dependencies.

Quick Start
-----------
Here's an example to set up and define a simple pipeline component:

.. code-block:: python

   from ml_orchestrator.meta_comp import MetaComponent
   from ml_orchestrator.env_params import EnvironmentParams

   class MyComponent(MetaComponent):
       @property
       def env(self):
           return EnvironmentParams(
               base_image="python:3.9",
               packages_to_install=["numpy", "pandas"]
           )

       def execute(self):
           print("Executing my component!")
   assert False

Features
--------
- **Define Custom Components**: Build workflows with reusable dataclasses.
- **Environment Management**: Configure Docker images and Python packages effortlessly.
- **Pipeline Serialization**: Generate KFP pipeline strings programmatically.
