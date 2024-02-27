import pickle
from pathlib import Path

import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score


def train(X: pd.DataFrame, y: pd.Series, out_path: str, verbose: int, random_state: int):
    out_path = Path(out_path)
    model = Pipeline(steps=[
        ("preprocess", OneHotEncoder()),
        ("model", LogisticRegression(verbose=verbose, random_state=random_state))
    ])

    model.fit(X, y)

    with open(out_path, "wb") as file:
        pickle.dump(model, file)


def test(model_path: str, X: pd.DataFrame, y: pd.DataFrame, out_path: str):
    out_path = Path(out_path)
    with open(model_path, "rb") as file:
        model = pickle.load(file)

    score = pd.Series(roc_auc_score(y_true=y, y_score=model.predict_proba(X)[:, 1]), name="roc_auc")
    score.to_csv(out_path, index=False)
