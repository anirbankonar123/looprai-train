from setuptools import setup
import pathlib


setup(
    name="looprai-train",  # Required
    version="1.0.0",  # Required
    description="A sample Python project for LOOPR AI",  # Optional
    long_description="A sample Python project for LOOPR AI",
    license="MIT",
    package_dir={"": "src"},
    packages=["looprai_train"],  # Required
    python_requires="==3.9",
    install_requires=["mlflow"],  # Optional
)
