from pathlib import Path
import click
import argparse

from demo_package.dataset import load_titanic


@click.version_option()
@click.group()
def cli():
    pass

# Praser
parser = argparse.ArgumentParser
@click.command("prepare-dataset")
@click.argument("out-dir", type=click.Path())
@click.option("--test-size", default=0.33, type=click.FloatRange(0, 1), help="Test size of the train/test split.")
@click.option("--seed", default=42, type=click.IntRange(min=0),
              help="Seed to help eliminate the randomness of the split.")
def prepare_dataset(out_dir, test_size: float, seed: int):
    """
    Prepares titanic dataset into OUT_DIR directory.
    """
    out_dir = Path(out_dir)
    X_train, X_test, y_train, y_test = load_titanic(test_size, random_state=seed)
    X_train.to_csv(out_dir / "X_train.csv", index=False)
    X_test.to_csv(out_dir / "X_test.csv", index=False)
    y_train.to_csv(out_dir / "y_train.csv", index=False)
    y_test.to_csv(out_dir / "y_test.csv", index=False)


def train():
    """
    This should be a click function under group cli.

    It should:

    1. Load train X and y.
    2. Perform training.
    """
    pass


def test():
    """
    This should be click function under group cli.

    It should:

    1. Load train X and y.
    2. Perform test.
    """
    pass


cli.add_command(prepare_dataset)
