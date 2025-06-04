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
   from ml_orchestrator.env_params import EnvironmentParams
   from dataclasses import dataclass

   @dataclass
   class MyCustomComponent(MetaComponent):
       # You can define input/output artifacts or parameters here if needed
       # For example:
       # message: str = "Default message"

       @property
       def env(self):
           # Define the component's runtime environment
           return EnvironmentParams(base_image="python:3.9")

       def execute(self):
           print("Executing my custom component!")
           # Example logic:
           # print(f"Received message: {self.message}")
           print(f"Component environment base image: {self.env.base_image}")

   # To run this example (locally, not in KFP):
   if __name__ == "__main__":
       comp = MyCustomComponent()
       comp.execute()

Component Parsers
-----------------
The `ComponentParser` class extends `FunctionParser` to allow generating components as serialized Kubeflow Pipelines (KFP) component specification files (typically YAML).
These YAML files can then be used to load components into your KFP pipelines.

Example usage:

.. code-block:: python

   from ml_orchestrator.comp_parser import ComponentParser
   from ml_orchestrator.meta_comp import MetaComponent
   # Assume MyCustomComponent is defined as above, or define a similar one here
   # For brevity, we'll use the MyCustomComponent from the example above.
   # Ensure EnvironmentParams is imported if you define a new component here.
   from ml_orchestrator.env_params import EnvironmentParams
   from dataclasses import dataclass
   from pathlib import Path

   @dataclass
   class SimpleComponent(MetaComponent):
       name: str = "World"

       @property
       def env(self):
           return EnvironmentParams(base_image="python:3.9-slim")

       def execute(self):
           print(f"Hello, {self.name}!")
           print(f"Running with image: {self.env.base_image}")

   # Example of using ComponentParser
   if __name__ == "__main__":
       # Create a list of components to parse
       components_to_parse = [MyCustomComponent, SimpleComponent]

       # Instantiate the parser
       parser = ComponentParser()

       # Define the output directory path for KFP component YAMLs
       output_dir = Path("kfp_components")
       output_dir.mkdir(exist_ok=True) # Ensure the directory exists

       # Parse components to KFP component YAML files (one per component)
       # For example, this will create `kfp_components/mycustomcomponent.yaml` and `kfp_components/simplecomponent.yaml`
       parser.parse_components_to_file(components_to_parse, output_dir)

       print(f"Components parsed to YAML files in {output_dir}")

       # Note: ComponentParser generates individual YAML files for each component in the specified output directory.
       # For generating Python function-based components (which are then typically compiled by KFP SDK),
       # you would typically use FunctionParser.

       # Example for generating Python functions (using FunctionParser)
       # This is often a separate step or a different parser (like FunctionParser from usage.rst)
       from ml_orchestrator import FunctionParser

       output_py_file = Path("parsed_pipeline_functions.py")
       py_parser = FunctionParser()
       py_parser.parse_components_to_file(components_to_parse, output_py_file)
       print(f"Components parsed to Python functions in {output_py_file}")


EnvironmentParams
-----------------

The `EnvironmentParams` dataclass is used to define the runtime environment for your components when they are executed in a Kubeflow Pipelines environment.
It allows you to specify details such as the base Docker image, necessary Python packages, and image pull policies.

Key Attributes:
~~~~~~~~~~~~~~~

- ``base_image`` (str): The Docker image to be used as the foundation for the component's execution environment. This should be an image that has Python and other necessary system-level dependencies.
- ``packages_to_install`` (Optional[List[str]]): A list of Python packages to be installed via pip before the component code runs. For example, ``["pandas==2.0.0", "scikit-learn>=1.0"]``.
- ``image_pull_policy`` (Optional[str]): The Kubernetes image pull policy, such as ``"Always"``, ``"IfNotPresent"``, or ``"Never"``. This dictates if and when KFP attempts to pull the specified ``base_image``.
- ``setup_commands`` (Optional[List[str]]): A list of shell commands to be executed in the container before ``packages_to_install`` are installed and the component logic runs. Useful for system-level setup.

Example of Defining EnvironmentParams:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from ml_orchestrator.env_params import EnvironmentParams
   from ml_orchestrator.meta_comp import MetaComponent # For context
   from dataclasses import dataclass

   # Example of defining a custom environment
   custom_env = EnvironmentParams(
       base_image="tensorflow/tensorflow:latest-gpu",
       packages_to_install=["pandas==2.0.0", "scikit-learn"],
       image_pull_policy="Always",
       setup_commands=["apt-get update && apt-get install -y my-custom-package"]
   )

   # This custom_env can then be used in a MetaComponent's env property
   @dataclass
   class MyComponentWithCustomEnv(MetaComponent):
       @property
       def env(self):
           return custom_env

       def execute(self):
           print(f"Running with image: {self.env.base_image}")
           if self.env.packages_to_install:
               print(f"Packages to install: {', '.join(self.env.packages_to_install)}")
           print(f"Image pull policy: {self.env.image_pull_policy}")
           # In a real scenario, these parameters would configure the KFP component definition

   if __name__ == "__main__":
       comp_instance = MyComponentWithCustomEnv()
       comp_instance.execute()
       # To see the KFP YAML structure, you would parse this component:
       # from ml_orchestrator.comp_parser import ComponentParser
       # from pathlib import Path
       # output_yaml_dir = Path("env_example_components")
       # output_yaml_dir.mkdir(exist_ok=True)
       # parser = ComponentParser()
       # parser.parse_components_to_file([MyComponentWithCustomEnv], output_yaml_dir)
       # print(f"Parsed MyComponentWithCustomEnv to {output_yaml_dir}/mycomponentwithcustomenv.yaml")
