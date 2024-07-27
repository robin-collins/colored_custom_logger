from setuptools import find_packages, setup

setup(
    name="colored_custom_logger",
    version="1.5.3",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    project_urls={
        "Documentation": "https://robin-collins.github.io/colored_custom_logger/",
        "Source": "https://github.com/robin-collins/colored_custom_logger/",
    },
)
