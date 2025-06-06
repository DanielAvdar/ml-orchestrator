# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
from importlib.metadata import version

sys.path.insert(0, os.path.abspath("../../"))
# sys.path.insert(0, os.path.abspath("./"))  # in conf.py

project = "ml-orchestrator"
version = version(project)
release = version
copyright = "2025, DanielAvdar"  # noqa
author = "DanielAvdar"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",  # Core extension for pulling docstrings
    "sphinx.ext.napoleon",  # Support for Google and NumPy style docstrings
    "sphinx.ext.viewcode",  # Add links to source code
    "sphinx.ext.githubpages",  # If deploying to GitHub Pages
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "github_url": "https://github.com/DanielAvdar/ml-orchestrator",
    "use_edit_page_button": True,
    "show_toc_level": 2,
    "navbar_align": "left",
}

html_context = {
    "github_user": "DanielAvdar",
    "github_repo": "ml-orchestrator",
    "github_version": "main",
    "doc_path": "docs/source",
}
master_doc = "index"
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = []
