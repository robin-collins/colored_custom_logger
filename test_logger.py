__version__ = "0.1.1"

import logging
from colored_custom_logger import CustomLogger

def test_logger(test_logger: CustomLogger, number: int):
    test_logger.debug(f"This is a debug message #{number}")
    test_logger.info(f"This is an info message #{number}")
    test_logger.warning(f"This is a warning message #{number}")
    test_logger.error(f"This is an error message #{number}")
    test_logger.critical(f"This is a critical message #{number}")
    print("\n\n")

logger = CustomLogger.get_logger('test')
print(f"Initial logger level: {logging.getLevelName(logger.level)}")

test_logger(logger, 1)

print("\nSetting default level to DEBUG")
CustomLogger.set_default_level(CustomLogger.DEBUG)

print(f"\nLogger level after set_default_level: {logging.getLevelName(logger.level)}")
print(f"Handler levels after set_default_level: {[logging.getLevelName(h.level) for h in logger.handlers]}")

test_logger(logger, 2)

print("\nCreating a new logger")
new_logger = CustomLogger.get_logger('new_test')

test_logger(new_logger, 1)

print("\nSetting default level back to INFO")
CustomLogger.set_default_level(CustomLogger.INFO)

test_logger(logger, 3)
test_logger(new_logger, 2)

print("\nSetting default level to WARNING")
CustomLogger.set_default_level(CustomLogger.WARNING)

test_logger(logger, 4)
test_logger(new_logger, 3)

