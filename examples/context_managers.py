import logging
from contextlib import contextmanager

from colored_custom_logger import CustomLogger

logger = CustomLogger.get_logger(__name__, level=logging.INFO)


@contextmanager
def temporary_loglevel(temp_level):
    original_level = logger.level
    logger.setLevel(temp_level)
    try:
        yield
    finally:
        logger.setLevel(original_level)


logger.debug("This debug message won't appear")

with temporary_loglevel(logging.DEBUG):
    logger.debug("This debug message will appear")

logger.debug("This debug message won't appear again")
