#!/bin/bash
find . -name 'coverage.txt' -delete
poetry run pytest --cov-report term --cov cleaning_utils tests/ >>.logs/coverage.txt
