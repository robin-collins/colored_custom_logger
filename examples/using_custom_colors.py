from colorama import Back, Fore, Style
from colored_custom_logger import CustomLogger

logger = CustomLogger.get_logger(__name__)

logger.info(f"This message has {Fore.BLUE}blue text{Style.RESET_ALL}")
logger.warning(f"This is a {Fore.MAGENTA}magenta warning{Style.RESET_ALL}")
logger.error(f"Error! {Back.WHITE}{Fore.RED}Something went wrong!{Style.RESET_ALL}")
