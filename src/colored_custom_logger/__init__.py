__version__ = "1.6.0"

import logging
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

class ColoredFormatter(logging.Formatter):
    """
    A custom logging formatter that applies colors to log level names.

    This formatter extends the standard logging.Formatter to add color-coding
    to the entire log line, except for the log message, in the output.
    It uses the colorama library to apply different colors to different log levels.

    Attributes:
        COLORS (dict): A dictionary mapping log level names to colorama color codes.
            - DEBUG: Blue
            - INFO: Green
            - WARNING: Yellow
            - ERROR: Red
            - CRITICAL: Light Magenta
    """

    COLORS = {
        "DEBUG": Fore.BLUE,
        "INFO": Fore.GREEN,
        "WARNING": Fore.YELLOW,
        "ERROR": Fore.RED,
        "CRITICAL": Fore.LIGHTMAGENTA_EX,
    }

    def __init__(self, fmt=None, datefmt=None):
        """
        Initialize the ColoredFormatter.

        This method sets up the formatter with the given format string and date format.
        If no format string is provided, it uses a default format.

        Args:
            fmt (str, optional): A format string for log messages.
                                 Defaults to "%(asctime)s - %(levelname)s - %(name)s - %(message)s".
            datefmt (str, optional): A format string for dates in log messages.
                                     Defaults to None.
        """
        super().__init__(fmt or "%(asctime)s - %(levelname)s - %(name)s - %(message)s", datefmt)

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the specified record as text with colored log level and prefix.

        This method overrides the standard format method to add color to the log level
        and the prefix of the log line. It applies the specified color to the prefix
        and formats the record using the base formatter.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The formatted log record as a string, with the prefix colored
                 according to the COLORS dictionary.
        """
        # Apply color to the prefix (everything before the log message)
        color = self.COLORS.get(record.levelname, '')
        prefix = f"{color}%(asctime)s - %(levelname)s - %(name)s{Style.RESET_ALL} - %(message)s"
        formatter = logging.Formatter(prefix, self.datefmt)
        
        formatted_message = formatter.format(record)

        # Handle exception information if present
        if record.exc_info:
            if not record.exc_text:
                record.exc_text = self.formatException(record.exc_info)
            if record.exc_text:
                formatted_message += "\n" + record.exc_text

        return formatted_message

class CustomLogger:
    """
    A custom logger class to provide colored logging functionality.

    This class wraps the standard logging.Logger class to provide a more user-friendly interface
    for creating and configuring loggers. It also adds color-coding to log level names in the output.

    Attributes:
        DEBUG (int): Logging level for debugging messages.
        INFO (int): Logging level for informational messages.
        WARNING (int): Logging level for warning messages.
        ERROR (int): Logging level for error messages.
        CRITICAL (int): Logging level for critical messages.
        _default_level (int): The default logging level for new loggers.
                               Defaults to logging.INFO.
        _loggers (dict): A dictionary storing created loggers, keyed by their names.
    """

    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

    _default_level = INFO
    _loggers = {}

    @classmethod
    def get_logger(cls, name: str, level: str = None) -> logging.Logger:
        """
        Get a logger with the specified name and level.

        If a logger with the given name already exists, it is returned. Otherwise, a new logger
        is created with the specified name and level, and added to the _loggers dictionary.

        Args:
            name (str): The name of the logger.
            level (str, optional): The logging level for the logger.
                                   Defaults to the default level set by set_default_level.

        Returns:
            logging.Logger: The logger with the specified name and level.
        """
        if name not in cls._loggers:
            logger = logging.getLogger(name)

            # Determine the log level
            log_level = getattr(cls, level.upper(), cls._default_level) if level else cls._default_level

            # Set the logger's level
            logger.setLevel(log_level)

            formatter = ColoredFormatter()

            ch = logging.StreamHandler()
            ch.setLevel(log_level)
            ch.setFormatter(formatter)

            logger.addHandler(ch)

            cls._loggers[name] = logger

        return cls._loggers[name]

    @classmethod
    def set_default_level(cls, level: int):
        """
        Set the default logging level for all loggers.

        This method sets the default logging level that will be used for new loggers
        created using the get_logger method. It also updates the level of existing loggers.

        Args:
            level (int): The new default logging level.
        """
        cls._default_level = level
        # Update existing loggers
        for logger in cls._loggers.values():
            logger.setLevel(level)
            for handler in logger.handlers:
                handler.setLevel(level)
            logger.info("Logger '%s' level set to %s", logger.name, logging.getLevelName(level))

        logging.info("Default logging level set to %s", logging.getLevelName(level))

