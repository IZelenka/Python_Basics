from typing import List
import pandas as pd
import pandas.api as pd_api


def is_categorical(vals: pd.Series, threshold: float) -> bool:
    """
    Checks, whether given column is categorical. The categorical column is a column
    that returns true on pandas api `is_categorical_dtype` or `is_bool_dtype`
    or can be inferred using the threshold.
    The threshold specifies the maximum ratio of unique values to all values
    for which we consider the input series to be categorical.

    Args:
        vals (pd.Series): Input column.
        threshold: If ratio of unique values to all values is lower than this, then the series is considered a categorical.

    Returns:
        True, if the series is categorical.
    """
    assert 0 <= threshold <= 1
    # categorical or boolean dtype is automatically considered to be categorical
    if pd_api.types.is_categorical_dtype(vals) or pd_api.types.is_bool_dtype(vals):
        return True

    # float => cannot be categorical
    if pd_api.types.is_float_dtype(vals):
        return False

    if threshold is None:
        raise ValueError("In this invocation 'threshold' is required.")

    vals = vals.dropna()
    unique_count = len(vals.unique())
    total_count = len(vals)

    # if there is very small ratio of unique values compared to all => treat as a categorical
    ratio = unique_count / total_count
    if ratio <= threshold:
        return True

    # otherwise don't treat as a categorical
    return False


def get_categorical_cols(data: pd.DataFrame, threshold: float) -> List[str]:
    """
    Obtains all categorical columns.

    Args:
        data (pd.DataFrame): Input data.
        threshold (float): Threshold value.
    """
    cols = []
    for col in data.columns:
        if is_categorical(data[col], threshold):
            cols.append(col)
    return cols

