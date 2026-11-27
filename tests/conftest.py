import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from fastapi.testclient import TestClient

os.environ.setdefault("API_KEY", "macleapipourtest")
os.environ.setdefault("POSTGRES_USER", "UserPourTest")
os.environ.setdefault("POSTGRES_PASSWORD", "passUserTest")
os.environ.setdefault("POSTGRES_DB", "futurisys_test")
os.environ.setdefault("POSTGRES_HOST", "localhost")
os.environ.setdefault("POSTGRES_PORT", "5433")

from src.dependencies import get_db
from src.main import app
from src.db.database import  Base
import pytest

engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
SessionTest = sessionmaker(bind=engine)

@pytest.fixture
def db_session():
    Base.metadata.create_all(engine)
    session = SessionTest()
    yield session
    session.close()
    Base.metadata.drop_all(engine)


@pytest.fixture
def client(db_session):
    def override():
        yield db_session
    app.dependency_overrides[get_db] = override
    yield TestClient(app)
    app.dependency_overrides.clear()

