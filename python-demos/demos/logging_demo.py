import logging
import time
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "app.log"


def get_logger(name: str = "ROOT") -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter(
            fmt=(
                "%(asctime)s [%(levelname)s] [%(name)s] "
                "[%(module)s::%(funcName)s] [%(filename)s:%(lineno)d] "
                "[%(process)d-%(threadName)s] %(message)s"
            ),
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        formatter.converter = time.gmtime

        file_handler = TimedRotatingFileHandler(
            LOG_FILE, when="midnight", interval=1, backupCount=7, encoding="utf-8", utc=True
        )
        file_handler.suffix = "%Y-%m-%d_%H:%M:%S"
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
    return logger


def main() -> None:  # pragma: no cover
    logger = get_logger(__name__)
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
    logger.debug("This is a debug message")


if __name__ == "__main__":
    main()
