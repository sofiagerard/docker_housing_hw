
import os
import sys

# 📌 Asegurar que Sphinx pueda encontrar los módulos en `src/`
sys.path.insert(0, os.path.abspath('../'))  # Sube un nivel para encontrar `src/`

# -- Información del Proyecto -------------------------------------------------
project = 'docker_housing_hw'
copyright = '2025, Sofia Gerard'
author = 'Sofia Gerard'
release = '0.1'

# -- Configuración General ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",        # 📌 Extrae documentación de docstrings automáticamente
    "sphinx.ext.napoleon",       # 📌 Soporte para docstrings Google y NumPy
    "sphinx.ext.viewcode",       # 📌 Agrega enlaces al código fuente
    "sphinx.ext.autosummary",    # 📌 Genera resúmenes automáticos
    "sphinx_autodoc_typehints",  # 📌 Muestra anotaciones de tipo en la documentación
]


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'es'

# -- Opciones de Salida en HTML -----------------------------------------------
html_theme = "sphinx_rtd_theme"  # Usar ReadTheDocs como tema
html_static_path = ['_static']

# -- Configuración de Napoleon ------------------------------------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False  # Excluye docstrings de __init__
napoleon_use_param = True
napoleon_use_rtype = False
