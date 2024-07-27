import logging

from colored_custom_logger import ColoredFormatter, CustomLogger

logging.basicConfig(level=logging.INFO)

colored_formatter = ColoredFormatter()

root_logger = logging.getLogger()
console_handler = logging.StreamHandler()
console_handler.setFormatter(colored_formatter)
root_logger.addHandler(console_handler)

logger = logging.getLogger(__name__)
logger.info("This message will be colored")

custom_logger = CustomLogger.get_logger("custom_module")
custom_logger.warning("This warning uses CustomLogger directly")
