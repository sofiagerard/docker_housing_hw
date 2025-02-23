import logging
import os
import argparse
import pandas as pd
from src.model_utils import train_and_save_model

# Configuración de logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Columnas esperadas por el modelo
EXPECTED_FEATURES = [
    "OverallQual",
    "GrLivArea",
    "TotalBsmtSF",
    "GarageCars",
    "GarageArea",
    "1stFlrSF",
    "FullBath",
    "TotRmsAbvGrd",
    "YearBuilt",
    "YearRemodAdd",
    "HouseAge",
    "TotalSF",
    "TotalBath",
]

def train(data_path, model_path):
    """Entrena el modelo utilizando los datos preprocesados y lo guarda en el disco."""
    try:
        # Verificar existencia del archivo de datos
        if not os.path.exists(data_path):
            raise FileNotFoundError(f"❌ El archivo {data_path} no existe.")

        # Cargar datos y verificar columnas
        df = pd.read_csv(data_path)
        logging.info(f"🔍 Columnas en el dataset: {df.columns.tolist()}")

        missing_columns = [col for col in EXPECTED_FEATURES if col not in df.columns]
        if missing_columns:
            raise ValueError(f"❌ Faltan las siguientes columnas: {missing_columns}")

        # Crear la carpeta donde se guardará el modelo si no existe
        os.makedirs(os.path.dirname(model_path), exist_ok=True)

        # Entrenar y guardar el modelo
        train_and_save_model(data_path, model_path)
        logging.info(f"✅ Entrenamiento completado exitosamente. Modelo guardado en {model_path}")

    except FileNotFoundError as e:
        logging.error(f"❌ Error: {e}")

    except ValueError as e:
        logging.error(f"❌ Error de validación: {e}")

    except Exception as e:
        logging.exception("❌ Error inesperado durante el entrenamiento")

    logging.info("🎉 Proceso finalizado sin errores. Modelo listo para usar.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Entrenar un modelo de Machine Learning")
    parser.add_argument("--data", type=str, required=True, help="Ruta del archivo de datos de entrenamiento")
    parser.add_argument("--output-model", type=str, default="/usr/src/app/model.joblib", help="Ruta donde se guardará el modelo entrenado")

    args = parser.parse_args()
    train(args.data, args.output_model)
