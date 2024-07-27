from setuptools import find_packages, setup

setup(
    name="colored_custom_logger",
    version="1.5.2",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
