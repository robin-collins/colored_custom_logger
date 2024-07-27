from colorama import Back, Fore, Style
from colored_custom_logger import CustomLogger

# Basic usage
print("Default color setup:")
logger = CustomLogger.get_logger("basic_example")

logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")

print("\nCustom colors:")
logger.info(
    f"This message has {Fore.BLUE}blue text{Style.RESET_ALL} and {Back.YELLOW}yellow background{Style.RESET_ALL}"
)
logger.warning(f"This is a {Fore.MAGENTA}magenta warning{Style.RESET_ALL}")

print("\nMultiple loggers:")
main_logger = CustomLogger.get_logger("main")
db_logger = CustomLogger.get_logger("database")
api_logger = CustomLogger.get_logger("api")

main_logger.info("Application starting")
db_logger.debug("Connecting to database")
api_logger.warning("API rate limit approaching")
main_logger.error("An error occurred in the main process")
db_logger.critical("Database connection lost")
