"""
version_sync.py

This script synchronizes the version numbers in setup.py and pyproject.toml
with the version specified in src/colored_custom_logger/logger.py.

Version: 1.0.0
"""

import logging
import re
import sys

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def read_version_from_logger():
    """Read the version from src/colored_custom_logger/logger.py."""
    try:
        with open("src/colored_custom_logger/logger.py", "r", encoding="utf-8") as f:
            content = f.read()
            match = re.search(r"Version:\s*(\d+\.\d+\.\d+)", content)
            if match:
                return match.group(1)
            else:
                logger.error("Version not found in logger.py")
                return None
    except FileNotFoundError:
        logger.error("logger.py not found in src/colored_custom_logger/")
        return None
    except IOError as e:
        logger.error(f"Error reading logger.py: {e}")
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

            logger.info(f"Updated version in setup.py to {version}")
        else:
            logger.error("Version pattern not found in setup.py")
    except FileNotFoundError:
        logger.error("setup.py not found")
    except IOError as e:
        logger.error(f"Error updating setup.py: {e}")


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

            logger.info(f"Updated version in pyproject.toml to {version}")
        else:
            logger.error("Version pattern not found in pyproject.toml")
    except FileNotFoundError:
        logger.error("pyproject.toml not found")
    except IOError as e:
        logger.error(f"Error updating pyproject.toml: {e}")


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
