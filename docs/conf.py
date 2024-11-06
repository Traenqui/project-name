"""Sphinx configuration."""

project = "Project Name"
author = "Jonas Gerber"
copyright = "2024, Jonas Gerber"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
