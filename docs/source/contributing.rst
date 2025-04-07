Contributing to ml-orchestrator
===============================

We welcome contributions to **ml-orchestrator**! Follow the guidelines below to get started.

Setting Up Development Environment
----------------------------------
1. Clone the repository:

.. code-block:: bash

    git clone https://github.com/danielavdar/ml-orchestrator.git

2. Install with dev and docs dependencies:

.. code-block:: bash

    make

Testing and Documentation
-------------------------
- Run tests via **pytest**:

.. code-block:: bash

    make test

- Run code style checks and formatting/ ruining pre-commit hooks:

.. code-block:: bash

     make check

- Run type checks via **mypy**:

.. code-block:: bash

     make mypy

- Build Sphinx documentation:

.. code-block:: bash

    make doc
