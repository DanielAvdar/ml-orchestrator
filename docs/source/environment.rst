.. _environment:

Environment Configuration
=========================

The `EnvironmentParams` class lets you manage configurations such as Docker image setups, package installations, and other dependencies for your components.

Class Details
-------------
`EnvironmentParams` provides the following attributes:

- **base_image (str)**: Base Docker image for the runtime environment.
- **target_image (str)**: Final Docker image to build.
- **packages_to_install (List[str])**: Additional Python packages to install.
- **pip_index_urls (List[str])**: Custom Python package sources.
- **install_kfp_package (bool)**: Whether to include the Kubeflow Pipelines SDK.

Example Usage
-------------
Here's an example:

.. code-block:: python

   from ml_orchestrator.env_params import EnvironmentParams

   params = EnvironmentParams(
       base_image="python:3.9",
       packages_to_install=["pandas", "numpy"],
       kfp_package_path="https://github.com/kubeflow"
   )

   print(params.comp_vars())
