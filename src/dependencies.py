import secrets
from fastapi import Header, HTTPException, APIRouter, Depends
from src.config import API_KEY
from src.db.database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def verif_api_key(x_api_key: str = Header(default=None, alias="X-API-Key")):
    if x_api_key is None or not secrets.compare_digest(
        x_api_key.encode(), API_KEY.encode()
    ):
        raise HTTPException(status_code=401, detail="Clé API invalide")