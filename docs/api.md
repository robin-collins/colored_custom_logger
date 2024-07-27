# API Reference

This document provides a detailed reference for all public classes, methods, and attributes in the `colored_custom_logger` module.

## Table of Contents

1. [CustomLogger](#customlogger)
2. [ColoredFormatter](#coloredformatter)
3. [Utility Functions](#utility-functions)

## CustomLogger

`CustomLogger` is the main class you'll interact with. It's a subclass of `logging.Logger` that uses a `ColoredFormatter` by default.

### Class Definition

```python
class CustomLogger(logging.Logger):
    def __init__(self, name: str, level: int = logging.DEBUG)
```

### Class Methods

#### `get_logger`

```python
@classmethod
def get_logger(cls, name: str, level: int = logging.DEBUG) -> CustomLogger
```

Creates and returns a `CustomLogger` instance.

**Parameters:**
- `name` (str): The name of the logger.
- `level` (int, optional): The logging level. Defaults to `logging.DEBUG`.

**Returns:**
- `CustomLogger`: An instance of the CustomLogger.

**Example:**
```python
logger = CustomLogger.get_logger("my_app")
```

### Instance Methods

#### `setup_logger`

```python
def setup_logger(self) -> None
```

Sets up the logger with a `ColoredFormatter` and console handler.

**Example:**
```python
logger = CustomLogger("my_app")
logger.setup_logger()
```

#### Standard Logging Methods

The `CustomLogger` class inherits all standard logging methods from `logging.Logger`. These include:

- `debug(msg, *args, **kwargs)`
- `info(msg, *args, **kwargs)`
- `warning(msg, *args, **kwargs)`
- `error(msg, *args, **kwargs)`
- `critical(msg, *args, **kwargs)`
- `exception(msg, *args, exc_info=True, **kwargs)`

Each of these methods logs a message with the corresponding severity level.

**Parameters:**
- `msg` (str): The message to log.
- `*args`: Variable positional arguments to be merged into `msg`.
- `**kwargs`: Keyword arguments. These can include `exc_info` (a boolean, exception, or tuple) and `stack_info` (a boolean).

**Example:**
```python
logger.debug("Debug message")
logger.info("Info message with %s", "formatting")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")
logger.exception("Exception message", exc_info=True)
```

## ColoredFormatter

`ColoredFormatter` is a custom formatter that applies colors to log messages based on their level.

### Class Definition

```python
class ColoredFormatter(logging.Formatter):
    def __init__(self, fmt: Optional[str] = None, datefmt: Optional[str] = None, style: str = '%')
```

### Class Attributes

#### `COLORS`

A dictionary mapping log levels to color codes.

```python
COLORS = {
    "DEBUG": Fore.BLUE,
    "INFO": Fore.GREEN,
    "WARNING": Fore.YELLOW,
    "ERROR": Fore.RED,
    "CRITICAL": Fore.RED + Style.BRIGHT,
}
```

### Instance Methods

#### `format`

```python
def format(self, record: logging.LogRecord) -> str
```

Formats the log record with appropriate colors.

**Parameters:**
- `record` (logging.LogRecord): The log record to format.

**Returns:**
- `str`: The formatted log message with color codes.

**Example:**
```python
formatter = ColoredFormatter("%(asctime)s - %(levelname)s - %(message)s")
formatted_message = formatter.format(log_record)
```

## Utility Functions

### `init_logger`

```python
def init_logger(name: str, level: int = logging.DEBUG) -> CustomLogger
```

A convenience function to initialize and return a `CustomLogger`.

**Parameters:**
- `name` (str): The name of the logger.
- `level` (int, optional): The logging level. Defaults to `logging.DEBUG`.

**Returns:**
- `CustomLogger`: An initialized CustomLogger instance.

**Example:**
```python
logger = init_logger("my_app", level=logging.INFO)
```

## Constants

### Log Levels

The module uses standard Python logging levels:

- `DEBUG = 10`
- `INFO = 20`
- `WARNING = 30`
- `ERROR = 40`
- `CRITICAL = 50`

These can be imported from the `logging` module or accessed via `logging.DEBUG`, `logging.INFO`, etc.

## Best Practices

1. Use meaningful logger names, typically `__name__` or the name of the component.
2. Set appropriate log levels for different environments (e.g., DEBUG for development, INFO for production).
3. Use log messages to provide context, not just to state what code is executing.
4. When adding custom colors to messages, always reset the color afterwards using `Style.RESET_ALL`.

## Thread Safety

The `CustomLogger` and `ColoredFormatter` classes are thread-safe, inheriting this property from the standard `logging` module. However, be cautious when modifying global state (like changing log levels) in a multi-threaded environment.

## Performance Considerations

Logging can impact performance, especially at DEBUG level. In production environments, consider setting the log level to INFO or higher for optimal performance.

## Extending the Module

To extend the functionality of `colored_custom_logger`:

1. Subclass `CustomLogger` or `ColoredFormatter` to add new features.
2. Create custom handlers if you need special output behavior.
3. Modify the `COLORS` dictionary in `ColoredFormatter` to change default colors.

Remember to maintain backwards compatibility if you're extending the public API.

---

This API reference provides a comprehensive overview of the `colored_custom_logger` module. For usage examples and more context, please refer to the [Usage Guide](usage.md).