from src.db.database import engine, Base
import src.db.models


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("Tables créées")

