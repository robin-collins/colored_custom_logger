import logging

from colored_custom_logger import CustomLogger

logger = CustomLogger.get_logger(__name__, level=logging.INFO)

logger.debug("This debug message won't be displayed")
logger.info("This info message will be displayed")
logger.warning("This warning message will be displayed")

logger.setLevel(logging.DEBUG)
logger.debug("Now this debug message will be displayed")
