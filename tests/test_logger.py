import logging
import unittest
from io import StringIO

from colorama import Fore, Style
from colored_custom_logger import CustomLogger, ColoredFormatter


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

    def test_set_default_level(self):
        CustomLogger.set_default_level(logging.WARNING)
        new_logger = CustomLogger.get_logger("new_test_logger")
        self.assertEqual(new_logger.level, logging.WARNING)

        # Reset default level to DEBUG for other tests
        CustomLogger.set_default_level(logging.DEBUG)

    def test_get_logger_with_specific_level(self):
        info_logger = CustomLogger.get_logger("info_logger", logging.INFO)
        self.assertEqual(info_logger.level, logging.INFO)

        debug_logger = CustomLogger.get_logger("debug_logger", logging.DEBUG)
        self.assertEqual(debug_logger.level, logging.DEBUG)

    def test_multiple_loggers_with_different_levels(self):
        CustomLogger.set_default_level(logging.INFO)
        
        info_logger = CustomLogger.get_logger("info_logger")
        debug_logger = CustomLogger.get_logger("debug_logger", logging.DEBUG)
        warning_logger = CustomLogger.get_logger("warning_logger", logging.WARNING)

        self.assertEqual(info_logger.level, logging.INFO)
        self.assertEqual(debug_logger.level, logging.DEBUG)
        self.assertEqual(warning_logger.level, logging.WARNING)

        # Reset default level to DEBUG for other tests
        CustomLogger.set_default_level(logging.DEBUG)

    def test_lazy_formatting(self):
        test_value = "lazy"
        self.logger.info("This is a %s formatted log message", test_value)
        log_output = self.log_capture.getvalue()
        self.assertIn("This is a lazy formatted log message", log_output)

    def test_change_log_level_dynamically(self):
        logger = CustomLogger.get_logger("dynamic_level_logger", logging.INFO)
        self.assertEqual(logger.level, logging.INFO)
        logger.setLevel(logging.DEBUG)
        self.assertEqual(logger.level, logging.DEBUG)

    def test_multiple_handlers(self):
        logger = CustomLogger.get_logger("multi_handler_logger")
        file_handler = logging.FileHandler("test.log")
        logger.addHandler(file_handler)
        self.assertEqual(len(logger.handlers), 2)
        logger.removeHandler(file_handler)

    def test_logger_name(self):
        logger_name = "test_name_logger"
        logger = CustomLogger.get_logger(logger_name)
        self.assertEqual(logger.name, logger_name)

    def test_logger_propagation(self):
        logger = CustomLogger.get_logger("propagation_logger")
        self.assertFalse(logger.propagate)

    def test_exception_logging(self):
        try:
            raise ValueError("Test exception")
        except ValueError:
            self.logger.exception("An error occurred")
        log_output = self.log_capture.getvalue()
        self.assertIn("An error occurred", log_output)
        self.assertIn("ValueError: Test exception", log_output)
        self.assertIn("Traceback (most recent call last):", log_output)

    def test_custom_log_levels(self):
        CUSTOM_LEVEL = 25
        logging.addLevelName(CUSTOM_LEVEL, "CUSTOM")
        self.logger.log(CUSTOM_LEVEL, "Custom level message")
        log_output = self.log_capture.getvalue()
        self.assertIn("CUSTOM", log_output)
        self.assertIn("Custom level message", log_output)

    def test_default_level_persistence(self):
        CustomLogger.set_default_level(logging.WARNING)
        logger1 = CustomLogger.get_logger("logger1")
        logger2 = CustomLogger.get_logger("logger2")
        self.assertEqual(logger1.level, logging.WARNING)
        self.assertEqual(logger2.level, logging.WARNING)
        CustomLogger.set_default_level(logging.DEBUG)  # Reset for other tests

if __name__ == "__main__":
    unittest.main()
