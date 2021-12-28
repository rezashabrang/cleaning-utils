#!/bin/bash
echo make release badge
export version=$(git describe --abbrev=0)
echo $version
find . -name 'cleaning-utils.svg' -delete
poetry run python3 -m pybadges --left-text="cleaning-utils" --right-text=${version} --whole-link="https://github.com/rezashabrang/cleaning-utils" --logo=assets/images/utility.svg --embed-logo >>assets/images/cleaning-utils.svg
