from colored_custom_logger import CustomLogger

# Create loggers for different components
main_logger = CustomLogger.get_logger("main")
db_logger = CustomLogger.get_logger("database")
api_logger = CustomLogger.get_logger("api")

main_logger.info("Application starting")
db_logger.debug("Connecting to database")
api_logger.warning("API rate limit approaching")
main_logger.error("An error occurred in the main process")
db_logger.critical("Database connection lost")
