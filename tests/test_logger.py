import logging
import unittest
from io import StringIO

from colorama import Fore, Style
from colored_custom_logger.logger import ColoredFormatter, CustomLogger


class TestColoredCustomLogger(unittest.TestCase):
    def setUp(self):
        self.logger = CustomLogger.get_logger("test_logger", level=logging.DEBUG)
        self.log_capture = StringIO()
        self.handler = logging.StreamHandler(self.log_capture)
        self.handler.setFormatter(ColoredFormatter())
        self.logger.addHandler(self.handler)

    def tearDown(self):
        self.logger.removeHandler(self.handler)
        self.log_capture.close()

    def test_logger_levels(self):
        test_messages = {
            "debug": "Debug message",
            "info": "Info message",
            "warning": "Warning message",
            "error": "Error message",
            "critical": "Critical message",
        }

        for level, message in test_messages.items():
            getattr(self.logger, level)(message)

        log_output = self.log_capture.getvalue()

        for level, message in test_messages.items():
            self.assertIn(message, log_output)
            self.assertIn(level.upper(), log_output)

    def test_colored_output(self):
        self.logger.info("Test colored output")
        log_output = self.log_capture.getvalue()

        self.assertIn(Fore.GREEN, log_output)
        self.assertIn(Style.RESET_ALL, log_output)

    def test_custom_formatter(self):
        formatter = ColoredFormatter()
        record = logging.LogRecord(
            name="test_logger",
            level=logging.INFO,
            pathname="",
            lineno=0,
            msg="Test message",
            args=(),
            exc_info=None,
        )
        formatted_record = formatter.format(record)

        self.assertIn(Fore.GREEN, formatted_record)
        self.assertIn(Style.RESET_ALL, formatted_record)
        self.assertIn("INFO", formatted_record)
        self.assertIn("test_logger", formatted_record)
        self.assertIn("Test message", formatted_record)

    # ... (keep other test methods unchanged)


if __name__ == "__main__":
    unittest.main()
