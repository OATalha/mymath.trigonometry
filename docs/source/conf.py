# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

sys.path.insert(0, os.path.abspath('./_ext'))

project = 'mymath.trigonometry'
copyright = '2022, Talha Ahmed'
author = 'Talha Ahmed'
release = version = '0.0.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'autoapi.extension',
    'sphinx_affiliates',
    'sphinx.ext.autodoc.typehints',
    'sphinx.ext.coverage',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.duration',
    'sphinx.ext.githubpages',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.todo',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]

autoapi_dirs = ['../../python']
autoapi_keep_files = False
autoapi_add_toctree_entry = True
autoapi_python_class_content = 'both'
autoapi_python_use_implicit_namespaces = False
autoapi_template_dir = '_templates/autoapi'

affiliate_options = {
    'canonical_url': 'https://oatalha.github.io/mymath.trigonometry/'
}

templates_path = ['_templates']
exclude_patterns = ['autoapi/templates', 'api']

rst_prolog = '''
 .. |logo| image:: http://oatalha.github.io/_static/One-Animation-Logo-Small.png
             :alt: One Animation Logo
             :target: https://oatalha.github.io/

.. |repos| replace:: :doc:`REPOS<maindocs:repos>`
.. |apidocs| replace:: :doc:`APIDOCS<maindocs:apidocs>`

=========================== ============================ ================================
|logo|                      .. centered :: |repos|       .. centered :: |apidocs|
=========================== ============================ ================================
'''

autodoc_typehints = 'description'
# autodoc_default_options = {'members': True, 'undoc-members': True}
# autodoc_mock_imports = []
#
# autosummary_generate = True
# autosummary_generate_overwrite = True
# autosummary_imported_members = True
# autosummary_ignore_module_all = True

autosectionlabel_prefix_document = True

todo_include_todos = True

intersphinx_mapping = {'maindocs': ('https://oatalha.github.io', None)}
extlinks = {'maindocs': ('https://oatalha.github.io/%s', '%s')}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = 'https://oatalha.github.io/_static/One-Animation-Logo-Small.png'
html_favicon = 'https://oatalha.github.io/_static/favicon.ico'
