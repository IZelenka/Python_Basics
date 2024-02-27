from sklearn.model_selection import train_test_split
import seaborn as sns
import pandas as pd
from typing import Tuple


def load_titanic(test_size: float = 0.33, random_state: int = 42) -> Tuple[
    pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    data = sns.load_dataset("titanic")
    X = data[["pclass", "sex"]]
    y = data["survived"]

    result = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return result
