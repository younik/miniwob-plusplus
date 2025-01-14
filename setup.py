"""Setups the project."""
from setuptools import setup

setup(
    name="miniwob_plusplus",
    version="0.0.1",
    python_requires=">=3.7, <3.11",
    packages=["miniwob"],
    install_requires=[
        "Gymnasium==0.26.3",
        "Pillow>=9.0.0",
        "selenium>=4.5.0",
        "numpy>=1.18.0",
    ],
    extras_require={
        "testing": [
            "pytest>=7.0.0",
            "pytest-timeout>=2.1.0",
        ]
    },
)
