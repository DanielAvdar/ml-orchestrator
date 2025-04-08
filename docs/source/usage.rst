.. _usage:

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

    # example.py

    from ml_orchestrator import FunctionParser
    from ml_orchestrator.meta_comp import MetaComponent
    from ml_orchestrator.env_params import EnvironmentParams
    from ml_orchestrator.artifacts import Dataset, Input, Output, Model

    from dataclasses import dataclass

    @dataclass
    class MyComponent:
        dataset: Input[Dataset]
        model: Output[Model]
        param_1: str = "default_value"


        def execute(self):
            print("Executing my component!")

    # main.py


    # from example import MyComponent
    comp_list = [
        MyComponent,
    ]
    parser = FunctionParser()
    parser.parse_components_to_file(comp_list, "kfp_functions.py")

will produce a file named kfp_functions.py as follows:

.. code-block:: python

    # flake8: noqa: F403, F405, B006
    from kfp.dsl import *
    from typing import *
    from importlib.metadata import version


    def my_component(
        dataset: Input[Dataset],
        model: Output[Model],
        param_1: str = "default_value",
    ):
        from example import MyComponent

        comp = MyComponent(
            dataset=dataset,
            model=model,
            param_1=param_1,
        )
        comp.execute()


Advanced Example
----------------

.. code-block:: python

    # example.py

    from dataclasses import dataclass

    from ml_orchestrator import FunctionParser
    from ml_orchestrator.artifacts import Dataset, Input, Output, Model


    class DummyModel:
        def save(self, path):
            # Dummy save method
            pass

        @classmethod
        def load(cls, path):
            # Dummy load method
            return cls()

        def train(self, dataset_path, params):
            # Dummy train method
            pass



    @dataclass
    class TrainModel:
        dataset: Input[Dataset]
        model: Output[Model]
        param_1: int
        param_2: float


        def execute(self):
            model = self.init_model()
            params = dict(
                param_1=self.param_1,
                param_2=self.param_2,
            )

            model.train(self.dataset.path, params)
            model.save(self.model.path)

        def init_model(self):
            # Initialize the model here
            return DummyModel()

    @dataclass
    class ReTrainModel(TrainModel):
        trained_model: Input[Model]


        def init_model(self):
            # Initialize the model here
            return DummyModel.load(self.trained_model.path)
    # main.py

    # from example import TrainModel, ReTrainModel
    comp_list = [
        TrainModel,
        ReTrainModel,
    ]
    parser = FunctionParser()
    parser.parse_components_to_file(comp_list, "kfp_functions.py")

will produce a file named kfp_functions.py as follows:

.. code-block:: python

    # flake8: noqa: F403, F405, B006
    from kfp.dsl import *
    from typing import *
    from importlib.metadata import version


    def train_model(
        dataset: Input[Dataset],
        model: Output[Model],
        param_1: int,
        param_2: float,
    ):
        from example import TrainModel

        comp = TrainModel(
            dataset=dataset,
            model=model,
            param_1=param_1,
            param_2=param_2,
        )
        comp.execute()


    def re_train_model(
        dataset: Input[Dataset],
        model: Output[Model],
        param_1: int,
        param_2: float,
        trained_model: Input[Model],
    ):
        from example import ReTrainModel

        comp = ReTrainModel(
            dataset=dataset,
            model=model,
            param_1=param_1,
            param_2=param_2,
            trained_model=trained_model,
        )
        comp.execute()
