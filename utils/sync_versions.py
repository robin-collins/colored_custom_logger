"""
sync_versions.py

This script synchronizes the version numbers in setup.py and pyproject.toml
with the version specified in src/colored_custom_logger/__init__.py.

Version: 1.0.0
"""

import os
import re
import sys

# Import colored_custom_logger from src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import src.colored_custom_logger as colored_custom_logger

from colored_custom_logger import CustomLogger

logger = CustomLogger.get_logger(__name__, level="DEBUG")


def read_version_from_logger():
    """Read the version from src/colored_custom_logger/__init__.py."""
    try:
        return colored_custom_logger.__version__
    except AttributeError:
        logger.error("__version__ attribute not found in src/colored_custom_logger.")
        return None


def update_setup_py(version):
    """Update the version in setup.py."""
    try:
        with open("setup.py", "r", encoding="utf-8") as f:
            content = f.read()

        pattern = r'(version\s*=\s*["\'])(\d+\.\d+\.\d+)(["\'])'
        if re.search(pattern, content):
            updated_content = re.sub(
                pattern, lambda m: f"{m.group(1)}{version}{m.group(3)}", content
            )

            with open("setup.py", "w", encoding="utf-8") as f:
                f.write(updated_content)

            logger.info("Updated version in setup.py to %s", version)
        else:
            logger.error("Version pattern not found in setup.py")
    except FileNotFoundError:
        logger.error("setup.py not found")
    except IOError as e:
        logger.error("Error updating setup.py: %s", e)


def update_pyproject_toml(version):
    """Update the version in pyproject.toml."""
    try:
        with open("pyproject.toml", "r", encoding="utf-8") as f:
            content = f.read()

        pattern = r'(version\s*=\s*["\'])(\d+\.\d+\.\d+)(["\'])'
        if re.search(pattern, content):
            updated_content = re.sub(
                pattern, lambda m: f"{m.group(1)}{version}{m.group(3)}", content
            )

            with open("pyproject.toml", "w", encoding="utf-8") as f:
                f.write(updated_content)

            logger.info("Updated version in pyproject.toml to %s", version)
        else:
            logger.error("Version pattern not found in pyproject.toml")
    except FileNotFoundError:
        logger.error("pyproject.toml not found")
    except IOError as e:
        logger.error("Error updating pyproject.toml: %s", e)


def main():
    """Main function to synchronize versions."""
    version = read_version_from_logger()
    if version:
        print("Found Version:", version)
        update_setup_py(version)
        update_pyproject_toml(version)
    else:
        logger.error("Failed to synchronize versions due to errors.")
        sys.exit(1)


if __name__ == "__main__":
    main()
