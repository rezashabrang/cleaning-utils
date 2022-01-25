<div align="center">

# cleaning-utils


[![cleaning-utils version](assets/images/cleaning-utils.svg)](https://github.com/rezashabrang/cleaning-utils)
[![Python Version](https://img.shields.io/pypi/pyversions/cleaning-utils.svg)](https://pypi.org/project/cleaning-utils/)
[![coverage report](assets/images/coverage.svg)](.logs/coverage.txt)
[![static analysis](assets/images/mypy.svg)](.logs/mypy.txt)
[![vulnerabilities](assets/images/vulnerabilities.svg)](.logs/safety.txt)
[![lint report](assets/images/pylint.svg)](.logs/pylint-log.txt)
[![Dependencies Status](assets/images/dependencies.svg)](.logs/dependencies.txt)

[![interrogate](assets/images/interrogate_badge.svg)](.logs/docstring.txt)
[![maintainability](assets/images/maintainability.svg)](.logs/maintainability.txt)
[![complexity](assets/images/complexity.svg)](.logs/complexity.txt)
[![Code style: black](assets/images/codestyle.svg)](https://github.com/psf/black)
[![Security: bandit](assets/images/security.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](assets/images/precommits.svg)](.pre-commit-config.yaml)
[![License](https://img.shields.io/github/license/rezashabrang/cleaning-utils)](https://github.com/rezashabrang/cleaning-utils/blob/master/LICENSE)

cleaning-utils is a collection of small Python functions and classes which make
cleaning pipelines shorter and easier.

</div>

## Install


```bash
pip3 install cleaning-utils
```

## Contributing

### Testing:

```bash
make install
make test && make coverage && make check-codestyle && make mypy && make check-safety && make extrabadges
```

### Checks on various versions:

```bash
python3.8 -m venv .venv_38
. .venv_38/bin/activate
python3 -m pip install --upgrade pip
make install
make test && make coverage && make check-codestyle && make mypy && make check-safety
deactivate

python3.9 -m venv .venv_39
. .venv_39/bin/activate
python3 -m pip install --upgrade pip
make install
make test && make coverage && make check-codestyle && make mypy && make check-safety
deactivate
```


### Build Package:

```BASH
pre-commit run --all-files
```

First, change the `version` in [`setup.py`](setup.py),  [`pyproject.toml`](pyproject.toml), and change the
`__version__` in [`__init__.py`](cleaning_utils/__init__.py). Then:

```bash
python3 setup.py sdist bdist_wheel
```

### Commit Changes:

```bash
pre-commit run --all-files
git add .
git commit -m ":sparkles: new feature"
git pull
git push -u origin master
```

### Make a release:

```bash
git tag -a <write the version e.g., v0.1.2> -m "message of release"
git push --tags
make release
```

### Commit Changes to [`README.md`](README.md):

```bash
pre-commit run --all-files
git add .
git commit -m ":books: README.md updated"
git pull
git push -u origin master
```

<div>
Icon made from
<a href="http://www.onlinewebfonts.com/icon">
Icon Fonts
</a>
is licensed by CC BY 3.0
</div>



## Credits [![🚀 Your next Python package needs a bleeding-edge project structure.](https://img.shields.io/badge/python--package--template-%F0%9F%9A%80-brightgreen)](https://github.com/TezRomacH/python-package-template)

This project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template)
