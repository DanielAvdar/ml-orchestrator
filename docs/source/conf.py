# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
from sybil import Sybil
from sybil.parsers.rest import PythonCodeBlockParser, SkipParser # For .rst files
import pytest

sys.path.insert(0, os.path.abspath("../../"))
# sys.path.insert(0, os.path.abspath("./"))  # in conf.py


project = "ml-orchestrator"
copyright = "2025, DanielAvdar"
author = "DanielAvdar"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",  # Core extension for pulling docstrings
    "sphinx.ext.napoleon",  # Support for Google and NumPy style docstrings
    "sphinx.ext.viewcode",  # Add links to source code
    "sphinx.ext.githubpages",  # If deploying to GitHub Pages
    "sphinx.ext.autodoc",
    'sphinx.ext.doctest',

]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ["_static"]
html_context = {
   # ...
   "default_mode": "dark",
}
# html_theme_options = {
#         "pygments_dark_style ": True
#
# }
pytest_collect_file = Sybil(
    parsers=[
        # This specifically targets .. code-block:: python
        PythonCodeBlockParser(),
        # Allows skipping blocks with .. doctest:: +SKIP or similar markers
        SkipParser(),
    ],
    # Adjust pattern for your docs location and file type
    pattern='docs/**/*.rst', # Example: find all .rst files in docs/ subdir
    # pattern='*.md', # Example for Markdown files
    # exclude='docs/some_file_to_ignore.rst' # Optional exclusion
).pytest()
