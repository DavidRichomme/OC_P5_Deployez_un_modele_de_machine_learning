import joblib
import pandas as pd

from src.config import MODEL_PATH, SEUIL

modele = joblib.load(MODEL_PATH)


def predire(features: dict) -> tuple[float, int]:
    df = pd.DataFrame([features])
    probabilite = float(modele.predict_proba(df)[0, 1])
    classe_predite = 1 if probabilite >= SEUIL else 0
    return probabilite, classe_predite