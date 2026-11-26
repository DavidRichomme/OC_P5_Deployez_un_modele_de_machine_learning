from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.db import crud
from src.dependencies import get_db, verif_api_key
from src.schemas import PredictionInput, PredictionOut
from src.services.prediction import predire

router = APIRouter(dependencies=[Depends(verif_api_key)])


@router.post("/predict", response_model=PredictionOut)
def predict(entree: PredictionInput, db: Session = Depends(get_db)):
    features = entree.model_dump()
    probabilite, classe_predite = predire(features)
    return crud.log_interaction(db, features, probabilite, classe_predite)


@router.get("/predictions", response_model=list[PredictionOut])
def liste_predictions(limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_prediction_list(db, limit)


@router.get("/predictions/{prediction_id}", response_model=PredictionOut)
def lire_prediction(prediction_id: int, db: Session = Depends(get_db)):
    prediction = crud.get_prediction_by_id(db, prediction_id)
    if prediction is None:
        raise HTTPException(status_code=404, detail="Prédiction introuvable")
    return prediction