from src.db.models import Prediction, Input


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_predictions_cle_invalide(client):
    response = client.get("/predictions", headers={"X-API-Key": "mauvaise-cle"})
    assert response.status_code == 401


def test_predictions_cle_vide(client):
    response = client.get("/predictions", headers={"X-API-Key": ""})
    assert response.status_code == 401


def test_predictions_sans_cle(client):
    response = client.get("/predictions")
    assert response.status_code == 401


def test_predictions_liste_vide(client, auth_headers):
    response = client.get("/predictions", headers=auth_headers)
    assert response.status_code == 200
    assert response.json() == []


def test_predict_valide(client, auth_headers, payload_valide):
    response = client.post("/predict", json=payload_valide, headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    probabilite = data['probabilite']
    prediction = data['classe_predite']
    assert 0 <= probabilite <= 1
    assert prediction in (0, 1)


def test_predict_hors_bornes(client, auth_headers, payload_valide):
    payload_valide['niveau_education'] = 9
    response = client.post("/predict", json=payload_valide, headers=auth_headers)
    assert response.status_code == 422


def test_predict_champ_inconnu(client, auth_headers, payload_valide):
    payload_valide['permis_de_conduire'] = 0
    response = client.post("/predict", json=payload_valide, headers=auth_headers)
    assert response.status_code == 422

def test_prediction_introuvable(client, auth_headers):
    response = client.get("/predictions/999999", headers=auth_headers)
    assert response.status_code == 404
    assert response.json()["detail"] == "Prédiction introuvable"


def test_prediction_detail(client , auth_headers, payload_valide):
    response_post = client.post("/predict", json=payload_valide, headers=auth_headers)
    assert response_post.status_code == 200
    prediction_id_post = response_post.json()["id"]
    response_get = client.get(f"/predictions/{prediction_id_post}", headers=auth_headers)
    assert response_get.status_code == 200
    assert response_get.json()["probabilite"] == response_post.json()["probabilite"]


def test_predictions_liste_apres_post(client, auth_headers, payload_valide):
    response_post = client.post("/predict", json=payload_valide, headers=auth_headers)
    assert response_post.status_code == 200
    response_get = client.get("/predictions", headers=auth_headers)
    assert response_get.status_code == 200
    assert len(response_get.json()) == 1


def test_predict_enregistre_en_base(client, auth_headers, db_session, payload_valide):
    response_post = client.post("/predict", json=payload_valide, headers=auth_headers)
    assert response_post.status_code == 200
    assert db_session.query(Prediction).count() == 1
    assert db_session.query(Input).count() == 1