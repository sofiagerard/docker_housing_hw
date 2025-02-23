# Proyecto: Predicción de Precios de Casas en CDMX
## 📌 Creación de Contenedores para Entrenamiento e Inferencia en Docker 🐳📂
## ✅ Objetivo:

- Convertir tu script de entrenamiento (train.py) en un contenedor Docker.
- Convertir tu script de inferencia (inference.py) en otro contenedor Docker.
- Usar argparse para parametrizar entradas y salidas de datos (incluyendo el modelo).
  
## Estructura del Repositorio

```plaintext
.
├── data
│   ├── inference
│   │   └── test.csv
│   ├── predictions
│   │   └── predictions.csv
│   ├── prep
│   │   ├── test.csv
│   │   └── train.csv
│   └── raw
│       ├── data_description.txt
│       ├── sample_submission.csv
│       ├── test.csv
│       └── train.csv
├── notebooks
│   ├── eda_model1.ipynb
│   ├── eda_model2_fact.ipynb
│   └── eda_model2.ipynb
├── src
│   ├── __init__.py
│   ├── data_utils.py
│   ├── feature_engineering_utils.py
│   └── model_utils.py
├── tests
│   └── data_processing.log
├── .gitignore
├── environment.yml
├── inference.py
├── main_program.py
├── model.joblib
├── prep.py
├── README.md
├── sandbox.ipynb
└── train.py
```

## Descripción del Proyecto
Este proyecto tiene como objetivo predecir los precios de casas en la Ciudad de México utilizando un modelo de regresión lineal implementado en Python. Se utilizan datos públicos y técnicas de ingeniería de características, limpieza de datos y modelado.

## Archivos Principales

- **prep.py**: Preprocesa los datos, aplica ingeniería de características y guarda una copia para inferencia.
- **train.py**: Entrena un modelo de regresión lineal utilizando los datos preprocesados.
- **inference.py**: Utiliza el modelo entrenado para hacer predicciones sobre nuevos datos.
- **main_program.py**: Ejecuta el flujo completo del proyecto (preprocesamiento, entrenamiento e inferencia).

## Estructura de Código

- **src/data_utils.py**: Funciones para cargar y limpiar datos.
- **src/feature_engineering_utils.py**: Funciones para crear nuevas características.
- **src/model_utils.py**: Funciones para entrenar, cargar y predecir con el modelo.

## Requerimientos

Para instalar las dependencias necesarias, usa:
```bash
conda env create -f environment.yml
conda activate house_prices_env
```

## Uso

1. Preprocesar los datos:
```bash
python prep.py
```

2. Entrenar el modelo:
```bash
python train.py
```

3. Generar predicciones:
```bash
python inference.py
```

4. Ejecutar todo el flujo de trabajo:
```bash
python main_program.py
```

## Mejores Prácticas

- Se usaron `pylint` y `black` para garantizar un código limpio y estandarizado:
"Your code has been rated at 7.21/10 (previous run: 7.01/10, +0.20)"

- Se emplearon `Docstrings` en todas las funciones para facilitar la comprensión.
- Se utilizó una estructura modular en la carpeta `src` para promover la reutilización de código.
- Se debe correr el siguiente comando al final para verificar el estilo y calidad en todos los archivos `.py`:

```bash
black src/*.py *.py --check > black_report.txt && \
pylint src/*.py *.py > pylint_report.txt && \
flake8 src/*.py *.py > flake8_report.txt
```

Esto generará tres reportes que se pueden revisar para garantizar un código consistente y libre de errores.


## Autoría
**Sofía Gerard**



