from pathlib import Path

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler


DATA_PATH = Path("Data/Processed/dataset_join_ready_to_ml.csv")
MODEL_PATH = Path("Models/model_reg_log.joblib")
TARGET = "a_quitte_l_entreprise"
PASSTHROUGH = ["FE1_tranche_salariale", "FE3_tranche_age"]
SEUIL = 0.3
BEST_PARAMS = {'C': 0.1, 'class_weight': 'balanced'}


def main():
    df = pd.read_csv(DATA_PATH, index_col=0)
    X = df.drop(columns=TARGET)
    y = df[TARGET]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    cols_to_scale = [c for c in X.columns if c not in PASSTHROUGH]
    preprocessor = ColumnTransformer(
        [("scale", MinMaxScaler(), cols_to_scale)],
        remainder="passthrough",
    )

    model = Pipeline([
        ("prep", preprocessor),
        ("model", LogisticRegression(max_iter=1000, random_state=42, **BEST_PARAMS)),
    ])

    model.fit(X_train, y_train)

    y_pred = (model.predict_proba(X_test)[:, 1] >= SEUIL).astype(int)
    print("precision", precision_score(y_test, y_pred))
    print("recall", recall_score(y_test, y_pred))
    print("f1", f1_score(y_test, y_pred))

    MODEL_PATH.parent.mkdir(exist_ok=True)
    joblib.dump(model, MODEL_PATH)


if __name__ == "__main__":
    main()