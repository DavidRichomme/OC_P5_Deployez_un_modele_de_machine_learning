from src.db.models import Input, Prediction




def log_interaction(session, features: dict, probabilite: float, classe_predite: int):
    input_row = Input(**features)
    prediction = Prediction(
        input=input_row,
        probabilite=probabilite,
        classe_predite=classe_predite,
    )
    session.add(prediction)    # ajoute aussi l'input, relié par la relationship
    session.commit()
    session.refresh(prediction)
    return prediction


def get_prediction_list(session, limit: int = 100):
    return session.query(Prediction).order_by(Prediction.id).limit(limit).all()


def get_prediction_by_id(session, prediction_id: int):
    return session.get(Prediction, prediction_id)