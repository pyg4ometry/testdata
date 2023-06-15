# Configuration file for the Sphinx documentation builder.
from __future__ import annotations

import sys
from pathlib import Path

from pkg_resources import get_distribution

sys.path.insert(0, Path(__file__).parents[2].resolve().as_posix())

project = "testdata"
copyright = "Copyright Holder"
version = get_distribution("testdata").version

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "myst_parser",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
master_doc = "index"

# Furo theme
html_theme = "furo"
html_theme_options = {
    "source_repository": "https://github.com/g4edge/testdata",
    "source_branch": "main",
    "source_directory": "docs/source",
}
html_title = f"{project} {version}"

# sphinx-napoleon
# enforce consistent usage of NumPy-style docstrings
napoleon_numpy_docstring = True
napoleon_google_docstring = False
napoleon_use_ivar = True
napoleon_use_rtype = False

# intersphinx
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("http://docs.scipy.org/doc/numpy", None),
    "scipy": ("http://docs.scipy.org/doc/scipy/reference", None),
    "pandas": ("https://pandas.pydata.org/docs", None),
    "matplotlib": ("http://matplotlib.org/stable", None),
}  # add new intersphinx mappings here

# sphinx-autodoc
autodoc_default_options = {"ignore-module-all": True}
# Include __init__() docstring in class docstring
autoclass_content = "both"
autodoc_typehints = "both"
autodoc_typehints_description_target = "documented_params"
autodoc_typehints_format = "short"
