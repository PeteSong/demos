#!/usr/bin/env bash

echo Running black
black --check $1
echo

echo Running isort
isort --check-only $1
echo

echo Running flake8
flake8 $1
echo

echo Running radon
radon cc $1
echo
