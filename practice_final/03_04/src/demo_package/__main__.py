import platform
import logging
import yaml
import logging.config

from demo_package.utils import process_titanic_ds, process_w_error
config_path = "config"

with open(config_path, "r") as file:
    config = yaml.safe_load(file)
logging.config.dictConfig(config)

logging.debug(f"Python: {platform.python_version()}")
process_titanic_ds(output_path="survivors.xlsx")

try:
    process_w_error()
except ValueError as exc:
    logging.debug(exc)