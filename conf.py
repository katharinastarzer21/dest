# Configuration file for the Sphinx documentation builder.

import os
import sys
import pathlib


sys.path.insert(0, os.path.abspath("_extensions"))


extensions = [
    "sphinx.ext.githubpages",  # Generiert .nojekyll für GitHub Pages
    "myst_nb",                 # Für Markdown + Jupyter Notebooks (Myst-NB)
    "sphinx_design",           # Für schöne UI-Elemente (Tabs, Buttons, etc.)
]

# Aktiviere diese Erweiterung nur, wenn die Umgebungsvariable GALLERY_BUILD gesetzt ist.
# → Das wird im zentralen Build-Workflow gemacht:
#    GALLERY_BUILD=1 sphinx-build -b html . _temp_gallery
if "GALLERY_BUILD" in os.environ:
    extensions.append("notebook_gallery_generator")


project = 'Jupyter Notebook Gallery'
copyright = '2024, Destination Earth Data Lake'
author = 'Christoph Reimer <christoph.reimer@eodc.eu>'


myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "html_image",
    "dollarmath",
]

# Erlaubte Links und Anker in Überschriften
myst_url_schemes = ["http", "https", "mailto"]
myst_heading_anchors = 3

# Notebooks NICHT ausführen beim Bauen
nb_execution_mode = 'off'

# Quelle: Markdown und Notebooks
source_suffix = {
    ".ipynb": "myst-nb",
    ".md": "markdown",
    ".myst": "myst-nb",
}

# Verzeichnisse für Templates
templates_path = ['_templates']

# Dateien/Ordner, die ignoriert werden
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    '**/.git',
    '.pixi*',
]


html_theme = 'pydata_sphinx_theme'

# Optional: eigene statische Ressourcen (CSS, Bilder)
html_static_path = ['_static']
html_css_files = ['custom.css']

# Logos, Titel, Icons
html_logo = "https://hda.data.destination-earth.eu/ui/images/destination_earth_logo_W.svg"
html_favicon = "https://hda.data.destination-earth.eu/ui/images/favicon.svg"
html_title = "DEDL Notebook Gallery"

# Theme-Optionen
html_theme_options = {
    "logo": {
        "image_light": html_logo,
        "image_dark": html_logo,
        "link": "https://destination-earth.eu/",
        "alt_text": "Destination Earth",
    },
    "navigation_with_keys": True,
    "show_nav_level": 2,
    "navigation_depth": 2,
    "collapse_navigation": False,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/destination-earth",
            "icon": "fa-brands fa-square-github",
            "type": "fontawesome",
        }
    ],
}


master_doc = 'index'
