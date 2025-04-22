# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

 #---- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import shutil
import sys

sys.path.insert(0, os.path.abspath("_extensions"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Jupyter Notebook Gallery'
copyright = '2024, Destination Earth Data Lake'
author = 'Christoph Reimer <christoph.reimer@eodc.eu>'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.githubpages",
    "myst_nb",
    "sphinx_design",
    "notebook_gallery_generator",
]

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "html_image",
    "dollarmath",
]

nb_execution_mode = 'off'

# Define what extensions will parse which kind of source file
source_suffix = {
    ".ipynb": "myst-nb",
    ".myst": "myst-nb"
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', "**/.git", ".pixi**"]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
#import sphinx_book_theme
#html_theme = 'sphinx_book_theme'
html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']
#html_js_files = ['custom.js']

# DEDL logo
#html_logo = "https://destine-data-lake-docs.data.destination-earth.eu/en/latest/_static/dedl.jpg"
html_logo = "https://hda.data.destination-earth.eu/ui/images/destination_earth_logo_W.svg"
html_favicon = "https://hda.data.destination-earth.eu/ui/images/favicon.svg"

html_title = "DEDL Notebook Gallery"

html_theme_options = {
  "logo": {
      "image_light": html_logo,
      "image_dark": html_logo,
      "link": "https://destination-earth.eu/",
      #"text": "Destination Earth",
      "alt_text": "Destination Earth",
   },
 "navigation_with_keys": True,
 "show_nav_level": 2,          
 "navigation_depth": 2,       
 "collapse_navigation": False, 

  "icon_links": [
        {
            # Label for this link
            "name": "GitHub",
            # URL where the link will redirect
            "url": "https://github.com/destination-earth",  # required
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "fa-brands fa-square-github",
            # The type of image to be used (see below for details)
            "type": "fontawesome",
        }
   ],
}

# MyST config
myst_enable_extensions = ["amsmath", "colon_fence", "deflist", "html_image"]
myst_url_schemes = ["http", "https", "mailto"]
nb_execution_mode = 'off'
myst_heading_anchors = 3