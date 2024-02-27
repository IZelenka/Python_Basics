# Configuration and Logging

## Task

1. Create virtual environment and install packages in the `requirements.txt` file + install demo_package.
    - Check out `Makefile`, you can use that to speed up the process, e.g. `make install`.
2. Rewrite the Python files to use `logging` instead of `print`.
    - User appropriate logging level for each message.
3. Use `config/app.dev.yaml` to configure the logging. Utilize `demo_package.logs.load_log_config` function.
4. Create a new configuration for production environment, store it into `config/app.prod.yaml`, and:
  - Use `demo_package.logs.JsonFormatter` as its formatter.
    - https://docs.python.org/3/library/logging.config.html#user-defined-objects
  - Won't output `DEBUG` messages.
5. Allow programmers to run the program like `LOGS_CONFIG=path/to/logs/config python -m demo_package`.
  - Allow specifying `LOGS_CONFIG` environment variable that will contain path to the yaml configuration file.

## Clean up

```sh
deactivate
rm -rf venv/
rm -rf src/demo_package/__pycache__
rm -rf src/demo_package/demo_package.egg-info
```
