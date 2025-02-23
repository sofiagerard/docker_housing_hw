import logging
import os
import argparse
import pandas as pd
import joblib
from src.model_utils import make_predictions  # ⬅️ Cambiar `predict_with_model` por `make_predictions`

# Configuración de logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

def inference(data_path, model_path, output_path):
    """Realiza inferencias utilizando un modelo entrenado y guarda las predicciones."""
    try:
        # Verificar existencia del archivo de datos
        if not os.path.exists(data_path):
            raise FileNotFoundError(f"❌ El archivo de datos {data_path} no existe.")

        # Verificar existencia del modelo entrenado
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"❌ El modelo {model_path} no existe.")

        # Cargar datos
        df = pd.read_csv(data_path)
        logging.info(f"🔍 Columnas en los datos de prueba: {df.columns.tolist()}")

        # Cargar el modelo entrenado
        model = joblib.load(model_path)
        logging.info(f"✅ Modelo cargado exitosamente desde {model_path}")

        # Realizar predicciones
        predictions = make_predictions(model, df)  # ⬅️ Cambiado aquí también

        # Guardar predicciones en archivo CSV
        pd.DataFrame(predictions, columns=["Predictions"]).to_csv(output_path, index=False)
        logging.info(f"✅ Predicciones guardadas en {output_path}")

    except FileNotFoundError as e:
        logging.error(f"❌ Error: {e}")

    except Exception as e:
        logging.exception("❌ Error inesperado durante la inferencia")

    logging.info("🎉 Proceso de inferencia finalizado sin errores.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Realizar inferencias con un modelo entrenado")
    parser.add_argument("--data", type=str, required=True, help="Ruta del archivo de datos de prueba")
    parser.add_argument("--model", type=str, required=True, help="Ruta del modelo entrenado")
    parser.add_argument("--output", type=str, default="predictions.csv", help="Ruta donde se guardarán las predicciones")

    args = parser.parse_args()
    inference(args.data, args.model, args.output)
