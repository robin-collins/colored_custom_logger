import logging

from colored_custom_logger import CustomLogger

logger = CustomLogger.get_logger(__name__)

file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.DEBUG)

file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)

logger.debug("This message will go to both console and file")
logger.info("So will this info message")
