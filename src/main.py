from fastapi import FastAPI
from src.routers.predictions import router as predictions_router

app = FastAPI(
    title="API de prédiction des démissions",
    description=(
        "Prédit la probabilité qu'un salarié démissionne (régression logistique, seuil de décision 0.3). "
        "Toutes les routes de prédiction demandent l'en-tête X-API-Key. "
        "Les valeurs d'entrée doivent être déjà transformées (log1p, poste encodé en décimal) : "
        "voir l'exemple prérempli de POST /predict et le README."
    ),
)

@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(predictions_router)