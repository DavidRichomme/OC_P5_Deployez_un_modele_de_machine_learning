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