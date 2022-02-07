"""setup the package."""
import sys

import setuptools

needs_pytest = {"ptr", "pytest", "test"}.intersection(sys.argv)
pytest_runner = ["pytest-runner"] if needs_pytest else []

setuptools.setup(
    name="cleaning-utils",
    version="0.1.0",
    author="Maani Beigy",
    author_email="beygi.ma@iums.ac.ir",
    url="https://github.com/rezashabrang/cleaning-utils",
    description="""cleaning-utils is a collection of small Python functions \
and classes for formatting persian texts.""",
    license="MIT",
    packages=setuptools.find_packages(
        exclude=["_cleaning_utils_tests", "*.__pycache__"]),
    python_requires=">=3.8",
    install_requires=["python-dateutil", "datetime", "khayyam", "pytz"],
    tests_require=["pytest"],
    extras_require={
        "tests": [
            "flake8",
            "pytest",
            "pytest-cov",
            "pytest-flake8",
            "pip",
            "bandit",
            "black",
            "coverage",
            "coverage-badge",
            "darglint",
            "isort",
            "mypy",
            "mypy-extensions",
            "pre-commit",
            "pydocstyle",
            "pylint",
            "pytest-html",
            "pyupgrade",
            "safety",
            "radon",
            "docstr-coverage",
        ],
    },
    setup_requires=[] + pytest_runner,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
