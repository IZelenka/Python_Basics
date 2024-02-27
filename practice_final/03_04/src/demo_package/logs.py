import yaml
import logging
import logging.config
import json


class JsonFormatter(logging.Formatter):
    def format(self, record) -> str:
        result = {
            "ts": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "name": record.name,
            "message": record.getMessage()
        }

        if record.exc_info:
            result["exc_info"] = self.formatException(record.exc_info)

        return json.dumps(result, ensure_ascii=False)


def load_log_config(config_path: str):
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    logging.config.dictConfig(config)