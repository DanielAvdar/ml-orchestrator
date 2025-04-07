Contributing to ml-orchestrator
===============================

We welcome contributions to **ml-orchestrator**! Follow the guidelines below to get started.

Setting Up Development Environment
----------------------------------
1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/danielavdar/ml-orchestrator.git

2. Install development dependencies:

   .. code-block:: bash

      poetry install --with docs

Testing and Documentation
-------------------------
- Run tests via **pytest**:

  .. code-block:: bash

     pytest

- Build Sphinx documentation:

  .. code-block:: bash

     sphinx-build docs/source docs/build
