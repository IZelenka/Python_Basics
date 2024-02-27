# Command-Line Interface (CLI)

## Installation

```shell
python -m venv "venv"
source venv/bin/activate 
python -m pip install -r "requirements.txt" -e .
```

## Experimenting

Let's check out the following commands.

```shell
# the two commands below are identical
python -m demo_package --help
demo_package --help
# how to call prepare dataset
demo_package prepare-dataset --help
```

Then we can call the `prepare-dataset` (with default options).

```shell
demo_package prepare-dataset data/
```


## Task

Our task is to create CLI for training and testing, similarly how it is prepared for the `prepare-dataset` function.

We create two functions `train` and `test` and add them to the CLI. They will internally use `demo_package.model.train` and `demo_package.model.test` resp.

**Training**

```shell
# logic of the commands: PACKAGE COMMAND INPUT_PARAM OUTPUT_PARAM OUT_MODEL
demo_package train "data/X_train.csv" "data/y_train.csv" "out/model.pkl" -v 10
```

Arguments:
- x input.
- y input.
- Path to the output, where the model will be serialized by pickle (binary serialization).

**Note: use only small letters for the argument names.**

Options:
- `--seed`: Seed that eliminates randomness from the training. Default value should be 42.
- `--verbose` (or `-v`): level of verbosity. Higher number leads to more logs. Min 0, max 10. Default 0.

**Testing**

```shell
demo_package test "out/model.pkl" "data/X_test.csv" "data/y_test.csv" "out/roc_auc.csv"
```

Arguments:
- Model path (from training step).
- X input.
- y input.
- Path to the output with the model test score.

## Clean Up

```sh
deactivate
rm -rf venv
rm -rf src/demo_package/__pycache__
rm -rf src/demo_package.egg-info
rm -rf data/ && mkdir data && touch data/.gitkeep
rm -rf out/ && mkdir out && touch out/.gitkeep
```