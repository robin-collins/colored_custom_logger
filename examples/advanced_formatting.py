from colored_custom_logger import ColoredFormatter, CustomLogger

logger = CustomLogger.get_logger(__name__)

custom_formatter = ColoredFormatter(
    fmt="%(asctime)s | %(levelname)8s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

console_handler = logger.handlers[0]
console_handler.setFormatter(custom_formatter)

logger.info("This message uses the custom format")
logger.warning("So does this warning message")
