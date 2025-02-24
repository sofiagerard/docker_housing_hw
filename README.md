
# **🏠 Predicción de Precios de Casas en CDMX**  
📌 **Autor:** Sofía Gerard  
📌 **Versión:** 0.1  
📌 **Lenguaje:** Python 3.11.2  

## **📌 Objetivo**
Este proyecto tiene como objetivo predecir los precios de casas en la Ciudad de México utilizando un modelo de **regresión lineal** encapsulado en **contenedores Docker**, y documentado con **Sphinx**.  

✅ **¿Qué logramos?**  
- **🔹 Docker:** Convertimos los scripts de **entrenamiento** e **inferencia** en contenedores reutilizables.  
- **🔹 Argparse:** Parametrizamos entradas y salidas de datos, incluyendo el modelo.  
- **🔹 Volúmenes en Docker:** Guardamos datos y modelos en la PC sin perderlos al detener los contenedores.  
- **🔹 Sphinx:** Generamos documentación automática del código con docstrings en formato Google/NumPy.  

---

## **📌 1️⃣ Estructura del Proyecto**
```plaintext
.
├── data                      # 📂 Almacena los datasets de entrenamiento e inferencia
│   ├── inference             # 📂 Datos de prueba para inferencia
│   │   └── test.csv
│   ├── predictions           # 📂 Resultados de predicciones
│   │   └── predictions.csv
│   ├── prep                  # 📂 Datos preprocesados para entrenamiento
│   │   ├── test.csv
│   │   └── train.csv
│   └── raw                   # 📂 Datos en crudo antes del preprocesamiento
│       ├── data_description.txt
│       ├── sample_submission.csv
│       ├── test.csv
│       └── train.csv
├── notebooks                 # 📂 Exploración y análisis de datos
│   ├── eda_model1.ipynb
│   ├── eda_model2_fact.ipynb
│   └── eda_model2.ipynb
├── src                       # 📂 Código fuente modular
│   ├── __init__.py
│   ├── data_utils.py         # 📌 Funciones de carga y limpieza de datos
│   ├── feature_engineering_utils.py  # 📌 Funciones de ingeniería de características
│   └── model_utils.py        # 📌 Funciones de entrenamiento y predicción del modelo
├── tests                     # 📂 Pruebas unitarias
│   └── data_processing.log
├── docs                      # 📂 Documentación con Sphinx
│   ├── conf.py
│   ├── index.rst
│   ├── _build/               # 📂 Documentación generada en HTML
│   ├── Makefile
│   └── source/
├── Dockerfile.train          # 📌 Configuración de Docker para entrenamiento
├── Dockerfile.inference      # 📌 Configuración de Docker para inferencia
├── train.py                  # 📌 Script de entrenamiento del modelo
├── inference.py              # 📌 Script de inferencia
├── requirements.txt          # 📌 Dependencias del proyecto
├── README.md                 # 📌 Documentación del repositorio
└── model.joblib              # 📌 Modelo entrenado
```

---

## **📌 2️⃣ Configuración del Entorno**
Antes de comenzar, asegúrate de tener instalado:
- **Python 3.11+**
- **Docker**
- **Sphinx** para la documentación

📌 **Clona el repositorio y entra al directorio:**
```sh
git clone https://github.com/tu_usuario/docker_housing_hw.git
cd docker_housing_hw
```

📌 **Instala las dependencias usando Conda o pip:**
```sh
conda env create -f environment.yml
conda activate house_prices_env
```
o con pip:
```sh
pip install -r requirements.txt
```

---

## **📌 3️⃣ Uso de Docker para Entrenamiento e Inferencia**
### **🚀 3.1 Construcción del Contenedor de Entrenamiento**
```sh
docker build -t train_model -f Dockerfile.train .
```
📌 **Explicación de `Dockerfile.train`:**
- **Usa `python:3.11.2`** como imagen base.
- **Copia dependencias e instala paquetes** con `pip`.
- **Copia `train.py` y `src/`** dentro del contenedor.
- **Ejecuta `train.py`** al iniciar el contenedor.

### **🏋️ 3.2 Entrenar el Modelo**
```sh
docker run --rm -v $(pwd):/usr/src/app train_model \
  --data data/prep/train.csv \
  --output-model model.joblib
```
📌 **Explicación de los parámetros:**
- `--rm`: Elimina el contenedor al terminar.
- `-v $(pwd):/usr/src/app`: Monta el directorio actual en el contenedor.
- `--data data/prep/train.csv`: Ruta de los datos de entrenamiento.
- `--output-model model.joblib`: Guarda el modelo entrenado.

---

### **🔮 3.3 Construcción del Contenedor de Inferencia**
```sh
docker build -t inference_model -f Dockerfile.inference .
```
📌 **Explicación de `Dockerfile.inference`:**
- Similar al de entrenamiento, pero ejecuta `inference.py`.

### **📈 3.4 Realizar Predicciones**
```sh
docker run --rm -v $(pwd):/usr/src/app inference_model \
  --data data/inference/test.csv \
  --model model.joblib \
  --output predictions.csv
```

---

## **📌 4️⃣ Generar Documentación con Sphinx**
📌 **Inicializa Sphinx dentro del directorio `docs/`:**
```sh
sphinx-quickstart docs
```
📌 **Configura:**
- **Idioma:** Español (`es`)
- **Tema:** `sphinx_rtd_theme`
- **Extensiones:** `autodoc`, `napoleon`, `viewcode`

📌 **Agrega en `docs/conf.py`:**
```python
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
    "sphinx_autodoc_typehints",
]
```

📌 **Genera la documentación:**
```sh
cd docs
sphinx-apidoc -o . ../src
make html
```
📌 **Ver en el navegador:**
```sh
open _build/html/index.html  # Mac
xdg-open _build/html/index.html  # Linux
start _build/html/index.html  # Windows
```

---

## **📌 5️⃣ Conclusión**
✅ **Usamos Docker para encapsular entrenamiento e inferencia.**  
✅ **Creamos un pipeline reproducible sin preocuparse por dependencias.**  
✅ **Generamos documentación automática con Sphinx.**  

