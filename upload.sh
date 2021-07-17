#! /bin/bash

set -e

rm -rf build
rm -rf dist
python3 setup.py sdist
python3 setup.py bdist_wheel
twine upload dist/*
