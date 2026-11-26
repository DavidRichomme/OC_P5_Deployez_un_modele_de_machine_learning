import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ["API_KEY"]              # secret, jamais dans le code
SEUIL = 0.3                                  # seuil de décision du modèle
MODEL_PATH = Path("Models/model_reg_log.joblib")