.. _introduction:

Introduction
============

The **ml-orchestrator** project is designed to streamline the management of modular components in Kubeflow Pipelines (KFP),
with a primary focus on Machine Learning (ML) workflows.

Concepts
--------

The core concept of **ml-orchestrator** is to provide a framework designed for creating, managing, and maintaining components for Kubeflow Pipelines (KFP).
It enables you to define component logic using Python dataclasses. This logic can then be easily serialized into KFP-compatible Python functions or KFP component YAML specifications.
This structured approach simplifies component management, enhances maintainability, and facilitates dependency and configuration handling.

.. list-table:: Key differences from the original KFP components definition
   :header-rows: 1

   * - Aspect
     - Original KFP
     - **ml-orchestrator**
   * - **Component Logic**
     - Defined as part of
       the function.
     - Defined within a
       Python dataclass using **ml-orchestrator**.
   * - **Import & Dependencies**
     - All Python code for
       the component logic
       is embedded directly.
     - Component logic imports
       dependencies as standard
       Python code. The runtime
       environment (e.g., Docker
       image) must provide these.
   * - **Testability**
     - Difficult to test;

       often requires a
       full pipeline run.
     - Easy to test;

       testable with `unittest`
       or `pytest`.
   * - **Commitment to KFP**
     - Code is tightly
       coupled with KFP.
     - Completely agnostic
       to KFP.
   * - **Flexibility**
     - Function-based logic:

       non-inheritable,

       repetitive code and
       parameters.
     - Dataclass-based logic:

       inheritable,

       reusable code and parameters.

KFP Agnostic Design
-------------------

**ml-orchestrator** is designed to be KFP agnostic, offering several benefits:

- **Independent Development:** Develop component logic as standard Python code, without direct dependencies on KFP. This means you can build and iterate on your components' core functionality in any Python environment.
- **Testability:** Since the component logic is decoupled from KFP, it's significantly easier to write and run unit tests using standard Python testing frameworks like `unittest` or `pytest`. This leads to more robust and reliable components.
- **Flexibility & Reusability:** The use of dataclasses for defining component logic promotes an object-oriented approach. This makes components inheritable and highly reusable across different ML workflows and pipelines.
- **Reduced Coupling:** Your codebase is not tightly coupled with KFP-specific structures or libraries. This makes it more adaptable to changes in KFP or even migration to other orchestration systems in the future.
