"""
logger.py - A module for setting up consistent, partially colorful logging across multiple modules.

This module provides a CustomLogger class that can be used directly for logging with colorful date
and log level, while leaving the rest of the output in plain text.

Version: 1.5.2
"""

import logging

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
        "CRITICAL": Fore.RED + Style.BRIGHT,
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


class CustomLogger(logging.Logger):
    """
    A custom logger class that extends the standard logging.Logger.

    This logger is configured with a colored formatter and console handler.
    """

    def __init__(self, name: str, level: int = logging.DEBUG):
        """
        Initialize the CustomLogger.

        Args:
            name (str): The name of the logger.
            level (int): The logging level. Defaults to logging.INFO.
        """
        super().__init__(name, level)
        self.setup_logger()

    def setup_logger(self):
        """
        Set up the logger with a colored formatter and console handler.

        This method configures the logger by:
        1. Removing any existing handlers.
        2. Creating a new console handler with DEBUG level.
        3. Creating a ColoredFormatter.
        4. Adding the formatter to the console handler.
        5. Adding the console handler to the logger.
        6. Disabling propagation to the root logger.
        """
        # Remove all handlers associated with the logger object
        for handler in self.handlers[:]:
            self.removeHandler(handler)

        # Create console handler and set level to debug
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        # Create formatter
        formatter = ColoredFormatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        )

        # Add formatter to console handler
        console_handler.setFormatter(formatter)

        # Add console handler to logger
        self.addHandler(console_handler)

        # Prevent the logger from propagating messages to the root logger
        self.propagate = False

    @classmethod
    def get_logger(cls, name: str, level: int = logging.DEBUG):
        """
        Get a CustomLogger instance.

        Args:
            name (str): The name of the logger.
            level (int): The logging level. Defaults to logging.INFO.

        Returns:
            CustomLogger: A configured logger instance.
        """
        return cls(name, level)
