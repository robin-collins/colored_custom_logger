from colored_custom_logger import CustomLogger

logger = CustomLogger.get_logger("exception_example")

try:
    1 / 0
except ZeroDivisionError:
    logger.exception("An error occurred:")
