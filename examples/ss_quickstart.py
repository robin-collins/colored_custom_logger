from colored_custom_logger import CustomLogger

# Create your fabulous logger
logger = CustomLogger.get_logger(__name__)

# Let the colorful logging begin!
logger.debug("🔍 This is a debug message")
logger.info("ℹ️ Here's some info for you")
logger.warning("⚠️ Uh-oh, this is a warning")
logger.error("❌ Oops! We've got an error")
logger.critical("🚨 MAYDAY! MAYDAY! This is critical!")
