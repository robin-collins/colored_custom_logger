__version__ = "1.5.16"

import logging
# from typing import Dict

from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

class ColoredFormatter(logging.Formatter):
    """
    A custom logging formatter that applies colors to log level names.

    This formatter extends the standard logging.Formatter to add color-coding
    to log level names in the output. It uses the colorama library to apply
    different colors to different log levels.

    Attributes:
        COLORS (dict): A dictionary mapping log level names to colorama color codes.
            - DEBUG: Blue
            - INFO: Green
            - WARNING: Yellow
            - ERROR: Red
            - CRITICAL: Bright Red
    """

    COLORS = {
        "DEBUG": Fore.BLUE,
        "INFO": Fore.GREEN,
        "WARNING": Fore.YELLOW,
        "ERROR": Fore.RED,
        "CRITICAL": Fore.LIGHTRED_EX,
    }

    def __init__(self, fmt=None, datefmt=None, style="%"):
        """
        Initialize the ColoredFormatter.

        This method sets up the formatter with the given format string, date format, and style.
        If no format string is provided, it uses a default format.

        Args:
            fmt (str, optional): A format string for log messages. If None default format is used.
            datefmt (str, optional): A format string for dates in log messages.
                                     If None default date format is used.
            style (str, optional): The style of the format string. Can be '%', '{', or '$'.
                                   Defaults to '%'.

        Returns:
            None
        """
        super().__init__(fmt, datefmt, style)

        self.COLORS = {
            'DEBUG': '\033[96m',  # Light Cyan
            'INFO': '\033[92m',  # Light Green
            'WARNING': '\033[93m',  # Light Yellow
            'ERROR': '\033[91m',  # Light Red
            'CRITICAL': '\033[95m',  # Light Magenta
        }
        self.RESET = '\033[0m'

        self._base_fmt = fmt or "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        self._colored_fmt = "%(asctime)s - %(levelname)s - %(name)s -"
        self._plain_fmt = " %(message)s"

    def format(self, record):
        """
        Format the specified record as text.

        This method overrides the standard format method to add color to the log level.
        It creates a new Formatter instance with a colored format string for each record,
        ensuring that the original formatter remains unchanged.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The formatted log record as a string, with the log level colored according
                to the COLORS dictionary.
        """
        # Format the colored part
        colored_parts = self._colored_fmt % {
            "asctime": self.formatTime(record, self.datefmt),
            "levelname": record.levelname,
            "name": record.name,
        }

        # Apply color to the formatted colored parts
        color = self.COLORS.get(record.levelname, "")
        colored_parts = f"{color}{colored_parts}{Style.RESET_ALL}"

        # Format the plain part
        plain_parts = self._plain_fmt % {"message": record.getMessage()}

        # Combine colored and plain parts
        formatted_message = colored_parts + plain_parts

        # Handle exception information if present
        if record.exc_info:
            if not record.exc_text:
                record.exc_text = self.formatException(record.exc_info)
        if record.exc_text:
            formatted_message += "\n" + record.exc_text

        return formatted_message



class CustomLogger:
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

    _default_level = INFO
    _loggers = {}

    @classmethod
    def get_logger(cls, name: str, level: str = None) -> logging.Logger:
        if name not in cls._loggers:
            logger = logging.getLogger(name)

            # Determine the log level
            if level:
                log_level = getattr(cls, level.upper(), cls._default_level)
            else:
                log_level = cls._default_level

            # Set the logger's level
            logger.setLevel(log_level)

            formatter = ColoredFormatter(
                '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
            )

            ch = logging.StreamHandler()
            ch.setLevel(log_level)  # Set the handler's level to match the logger's level
            ch.setFormatter(formatter)

            logger.addHandler(ch)

            cls._loggers[name] = logger

        return cls._loggers[name]

    @classmethod
    def set_default_level(cls, level: int):
        cls._default_level = level
        logger = logging.getLogger(__name__)
        logger.info("Logger '%s' level set to %s", __name__, logging.getLevelName(level))

        # Update existing loggers
        for logger in cls._loggers.values():
            logger.setLevel(level)
            for handler in logger.handlers:
                handler.setLevel(level)
            logger.info("Logger '%s' level set to %s", logger.name, logging.getLevelName(level))

        # Update default logging level
        # logging.basicConfig(level=level)
        logger.info("Default logging level set to %s", logging.getLevelName(level))
