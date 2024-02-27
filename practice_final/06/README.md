# Testing in Python

## Installation

```shell
python -m venv "venv"
source venv/bin/activate 
python -m pip install -r "requirements.txt" -e .
```

## Task

Create tests into `tests/test_utils.py`. Create two tests to verify the functionality of `demo_package.utils.is_categorical`
and `demo_package.utils.get_categorical_cols`.

The tests for `is_categorical` should test for multiple thresholds and input Series.

The tests for `get_categorical_cols` should mock calling `is_categorical` because we don't want to test the
functionality of `is_categorical` in this test.

## Clean up

```sh
deactivate
rm -rf venv/
rm -rf src/demo_package/__pycache__
rm -rf src/demo_package/demo_package.egg-info
rm -rf .pytest_cache/
rm -rf tests/__pycache__
```