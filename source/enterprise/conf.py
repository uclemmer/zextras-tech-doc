# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
# sys.path.insert(0, os.path.abspath('.'))
import sphinx_rtd_theme
import time
current_year = time.strftime('%Y')

# -- Project information -----------------------------------------------------

project = 'Zextras Carbonio Enterprise'
copyright = '2021, The Zextras Team'
author = 'The Zextras Team'

# The full version, including alpha/beta/rc tags
release = '0.1-alpha'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [ 'sphinx_design', 'sphinx.ext.extlinks' ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

rst_prolog = """

.. note:: All content is provisional and is meant **only** to showcase
   the feature of the new framework.

""" + open("replace.txt").read()

extlinks = {
    'carbonio': ('http://192.168.157.66/carbonio/html/%s.', None ),
    'enterprise': ('http://192.168.157.66/enterprise/html/%s', None ),
    'community': ('https://community.zextras.com/', None)
}


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_show_sourcelink = False
html_favicon = 'img/favicon.png'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = [ 'css/enterprise.css' ]
html_logo = 'img/zextras_white.svg'


# html_theme_options = {
#     'sticky_navigation': True,
#     'logo_only': True
# }
