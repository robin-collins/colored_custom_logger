from colored_custom_logger import CustomLogger

def main():
    # Example usage
    logger = CustomLogger.get_logger(__name__)
    
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
    
    # Example with manual color in the message
    from colorama import Fore, Back, Style
    logger.info(f"This is a message with {Fore.YELLOW}yellow text{Style.RESET_ALL} and {Back.BLUE}blue background{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
