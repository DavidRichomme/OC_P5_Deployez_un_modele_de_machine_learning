from pathlib import Path
import pandas as pd
from sqlalchemy import insert, select, func
from src.db.database import SessionLocal
from src.db.models import Dataset

CSV_PATH = Path("Data/Processed/dataset_join_ready_to_api.csv")   # ⚠️ à vérifier


def main():
    df = pd.read_csv(CSV_PATH)
    records = df.drop(columns=["id"], errors="ignore").to_dict(orient="records")

    with SessionLocal() as session:
        nb = session.scalar(select(func.count()).select_from(Dataset))
        if nb > 0:
            print(f"dataset contient déjà {nb} lignes, rien à faire")
            return
        session.execute(insert(Dataset), records)
        session.commit()
        print(f"{len(records)} lignes insérées")


if __name__ == "__main__":
    main()