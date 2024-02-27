# Virtual Environment

## Task

1. Create Python virtual environment for this project. It should have version **3.10.10**. Place it into `venv` directory.
    - Use `python -m venv "venv"` for that.
2. Activate the environment.
3. Install packages `pandas` (version 1.5.3) and `seaborn` (version 0.12.2).
4. Check that correct versions of those packages are installed.
    - `pip list` command.
5. Install the local `demo_package` in an editable mode.
    - `-e` switch.
6. Save it into `requirements.txt` file. Exclude the editable install.
    - `pip freeze` command.
    - `--exclude-editable` switch.
7. Run the `__main__.py`.
8. Check your solution with the following command (you can copy-paste it into the terminal):

```sh
python -c '
import platform
import os
import pandas as pd
import seaborn.objects as so
import seaborn as sns

assert platform.python_version() == "3.10.10", "Incorrect version of Python."
assert pd.__version__ == "1.5.3", "Incorrect version of pandas."
assert sns.__version__ == "0.12.2", "Incorrect version of seaborn."
assert os.path.exists("plot.png"), "Plot wasnt successfully generated."
'
```

## Clean up

```sh
deactivate
rm -rf venv
rm plot.png requirements.txt
```
