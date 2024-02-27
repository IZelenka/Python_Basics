import platform
import os
import pandas as pd
import seaborn.objects as so
import seaborn as sns

assert platform.python_version() == "3.10.10", "Incorrect version of Python."
assert pd.__version__ == "1.5.3", "Incorrect version of pandas."
assert sns.__version__ == "0.12.2", "Incorrect version of seaborn."

data = sns.load_dataset("titanic")

(
    so.Plot(data=data[lambda x: x["age"].pipe(pd.notna)][lambda x: x["fare"].pipe(pd.notna)], x="age", y="fare")
    .add(so.Dots())
    .add(so.Line(), so.PolyFit(order=1))
    .label(
        x="Věk",
        y="Jízdné",
        title="Vztah mezi jízdným a věkem cestujícího na Titanicu"
    )
    .save("plot.png")
)

assert os.path.exists("plot.png"), "Plot wasn't successfully generated."
