# Installation Guide

This guide will walk you through the process of installing the `colored_custom_logger` module in your Python environment.

## Prerequisites

Before installing `colored_custom_logger`, ensure you have the following:

- Python 3.7 or higher installed on your system
- pip (Python package installer) installed

You can check your Python version by running:

```bash
python --version
```

## Installation Steps

### 1. Install using pip

The easiest way to install `colored_custom_logger` is using pip. Open your terminal or command prompt and run:

```bash
pip install colored-custom-logger
```

This command will download and install the latest version of `colored_custom_logger` along with its dependencies.

### 2. Verify the Installation

After the installation is complete, you can verify it by importing the module in Python:

```python
from colored_custom_logger import CustomLogger

# If no error occurs, the installation was successful
```

## Installing from Source

If you prefer to install from source or want to contribute to the development:

1. Clone the repository:

   ```bash
   git clone https://github.com/robin-collins/colored_custom_logger.git
   ```

2. Navigate to the project directory:

   ```bash
   cd colored_custom_logger
   ```

3. Install the package in editable mode:

   ```bash
   pip install -e .
   ```

## Dependencies

`colored_custom_logger` depends on the following packages:

- colorama

These dependencies will be automatically installed when you install `colored_custom_logger` using pip.

## Troubleshooting

If you encounter any issues during installation:

1. Ensure you have the latest version of pip:

   ```bash
   pip install --upgrade pip
   ```

2. If you're using a virtual environment, make sure it's activated before installation.

3. On some systems, you might need to use `pip3` instead of `pip` to ensure you're using Python 3.

   ```bash
   pip3 install colored-custom-logger
   ```

4. If you encounter permission errors, you may need to use `sudo` (on Unix-based systems) or run your command prompt as administrator (on Windows).

## Next Steps

After installation, you're ready to start using `colored_custom_logger` in your projects. Check out the [Usage Guide](usage.md) for examples and best practices.

For any further issues or questions, please [open an issue](https://github.com/robin-collins/colored_custom_logger/issues) on our GitHub repository.