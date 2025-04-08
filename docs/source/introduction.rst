.. _introduction:

Introduction
============

The **ml-orchestrator** project is designed to streamline the management of modular components in Kubeflow Pipelines (KFP),
with a primary focus on Machine Learning (ML) workflows. For installation instructions and getting started, please refer to :doc:`usage`.

Concepts
--------

The core concept of **ml-orchestrator** is to provide a framework designed for creating, managing, and maintaining Kubeflow components.
It enables you to define component logic using dataclasses, which can easily be serialized into KFP strings.
This structured approach simplifies component management, enhances maintainability, and facilitates dependency and configuration handling.

.. list-table:: Key differences from the original KFP components definition
   :header-rows: 1

   * - Aspect
     - Original KFP
     - **ml-orchestrator**
   * - **Component Logic**
     - Defined as part of the function.
     - Defined within a dataclass.
   * - **Import & Dependencies**
     - Entire code resides inside the function.
     - Assumes code is available from the environment.
   * - **Testability**
     - Difficult to test; often requires a full pipeline run.
     - Testable using standard Python tools like `unittest` or `pytest`.
   * - **Commitment to KFP**
     - Code is tightly coupled with KFP.
     - Completely agnostic to KFP.
   * - **Flexibility**
     - Function-based logic: non-inheritable, repetitive code and parameters.
     - Dataclass-based logic: inheritable, reusable code and parameters.
