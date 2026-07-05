import logging
import os
from logging.handlers import RotatingFileHandler


def get_logger(name="bot"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.propagate = False

    if not logger.handlers:
        os.makedirs("logs", exist_ok=True)
        log_path = os.path.join("logs", "app.log")
        handler = RotatingFileHandler(log_path,
            "app.log",
            maxBytes=5 * 1024 * 1024,
            backupCount=5,
            encoding="utf-8"
        )

        formatter = logging.Formatter(
            "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
        )

        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger