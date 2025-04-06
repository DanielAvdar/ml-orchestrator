Introduction
============

The **ml-orchestrator** project is designed to facilitate the management of modular components in Kubeflow Pipelines (KFP),
especially for Machine Learning (ML) workflows.
For installation and getting started, please proceed to :doc:`usage`.

Concepts
--------

The core concept of **ml-orchestrator** is to provide a framework for creating, managing, maintaining kubeflow components.
it allows you to define components logic as dataclasses, which can be easily serialized into KFP strings.
This approach allows for a more structured and maintainable way to define components, making it easier to manage dependencies and configurations.

.. list-table:: Key differences from original KFP components definition
   :header-rows: 1

   * - Aspect
     - Original KFP
     - **ml-orchestrator**
   * - **Component Logic**
     - Logic is defined as part of the function.
     - Logic is defined as part of the dataclass.
   * - **Import & Dependencies**
     - The entire code is inside the function.
     - Assumes that the code will be available from the environment.
   * - **Testability**
     - Hard to test, somtimes requires a full pipeline run.
     - Testable as a regular Python code via `unittest` or `pytest`.
   * - **Comitment to KFP**
     - The code is tightly coupled with KFP.
     - 100% agnostic to KFP.
   * - **Flexibility**
     - functions based logic:
        non-inheritable, duplicate code & parameters.
     - dataclass based logic:
        inheritable, reusable code & parameters.
