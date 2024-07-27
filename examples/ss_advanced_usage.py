import logging
import os
from contextlib import contextmanager

from colored_custom_logger import ColoredFormatter, CustomLogger

# Create a custom logger
logger = CustomLogger.get_logger("advanced_example")

# 1. Changing log levels dynamically
print("1. Changing log levels dynamically:")
logger.setLevel(logging.INFO)
logger.debug("This debug message won't be displayed")
logger.info("This info message will be displayed")

logger.setLevel(logging.DEBUG)
logger.debug("Now this debug message will be displayed")

# 2. Adding a file handler
log_file = "advanced_example.log"
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

print("\n2. Logging to both console and file:")
logger.info("This message goes to both console and file")
print(f"Check {log_file} for the logged message")

# 3. Custom log format
custom_formatter = ColoredFormatter(
    fmt="%(asctime)s | %(levelname)8s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
console_handler = logger.handlers[
    0
]  # Assuming the first handler is the console handler
console_handler.setFormatter(custom_formatter)

print("\n3. Using a custom log format:")
logger.info("This message uses the custom format")


# 4. Context manager for temporary logging changes
@contextmanager
def temporary_loglevel(temp_level):
    original_level = logger.level
    logger.setLevel(temp_level)
    try:
        yield
    finally:
        logger.setLevel(original_level)


print("\n4. Using a context manager for temporary logging changes:")
logger.setLevel(logging.INFO)
logger.debug("This debug message won't appear")
with temporary_loglevel(logging.DEBUG):
    logger.debug("This debug message will appear")
logger.debug("This debug message won't appear again")

# Clean up
logger.removeHandler(file_handler)
os.remove(log_file)
