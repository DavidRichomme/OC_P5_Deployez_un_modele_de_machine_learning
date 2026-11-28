from src.services.prediction import predire
from src.schemas import EXEMPLE

def test_predire_exemple():
    probabilite, classe_predite = predire(EXEMPLE)
    assert 0 <= probabilite <= 1
    assert classe_predite in (0, 1)