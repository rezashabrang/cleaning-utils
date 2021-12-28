#!/bin/bash
find . -name 'docstring.txt' -delete
interrogate -v cleaning_utils >>.logs/docstring.txt
poetry run interrogate cleaning_utils
