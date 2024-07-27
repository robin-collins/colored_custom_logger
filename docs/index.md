# Welcome to Colored Custom Logger

Colored Custom Logger is a Python module that extends the functionality of the built-in `logging` module to provide colorized log output. It's designed to make log messages more readable and distinguishable, especially when working with console output.

## Features

- Colorized log output for improved readability
- Easy to integrate with existing Python projects
- Customizable color schemes
- Support for both console and file logging
- Compatible with Python's built-in logging module

## Quick Start

Get started with Colored Custom Logger in just a few lines of code:

```python
from colored_custom_logger import CustomLogger

logger = CustomLogger.get_logger(__name__)

logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
```

## Navigation

Use the navigation menu to explore different sections of the documentation:

- [Installation](installation.md): Learn how to install Colored Custom Logger
- [Usage](usage.md): Detailed guide on how to use the module
- [API Reference](api.md): Complete API documentation

## Getting Help

If you encounter any issues or have questions, please check our [Troubleshooting](troubleshooting.md) section or open an issue on our [GitHub repository](https://github.com/robin-collins/colored_custom_logger).

Thank you for using Colored Custom Logger!