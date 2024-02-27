import pytest
import pandas as pd
from unittest.mock import patch

from demo_package.utils import get_categorical_cols, is_categorical

@pytest.mark.parametrize(["input_vals", "threshold", "expected"], [
    (
        pd.Series([1, 2, 3]),
        1,
        True
    ),
    (
        pd.Series([1, 1, 1]),
        0.5,
        True
    ),
    (
        pd.Series([1, 1, 2]),
        0.5,
        False
    )
])

def test_is_categorical(input_vals: pd.Series, threshold: float, expected: bool):
    assert is_categorical(input_vals, threshold) == expected

@patch("demo_package.utils.is_categorical")
def test_get_categorical_cols(is_categorical):
    is_categorical.side_effect = [True, False]
    data = pd.DataFrame({
        "cat": [1, 1, 1],
        "not_cat": [1, 2, 3]
    })
    threshold = 0.5

    actual_cols = get_categorical_cols(data, threshold)
    assert actual_cols == ["cat"]


def test_get_categorical_cols():
    pass
