#!/usr/bin/env bash

echo Running black
uvx black --check $1
echo

echo Running isort
uvx isort --check-only $1
echo

echo Running flake8
uvx flake8 $1
echo

echo Running mypy
uvx mypy $1
echo

echo Running radon
uvx radon cc $1
echo
