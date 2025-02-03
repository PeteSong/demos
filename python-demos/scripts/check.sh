#!/usr/bin/env bash

echo ==== Running black
uvx black --check $1
echo && echo

echo ==== Running isort
uvx isort --check-only $1
echo && echo

echo ==== Running flake8
uvx flake8 $1
echo && echo

echo ==== Running pylint
uvx pylint $1
echo && echo

echo ==== Running mypy
uvx mypy $1
echo && echo

echo ==== Running pyright
uvx pyright $1
echo && echo

echo ==== Running radon
uvx radon cc $1
echo && echo

echo ==== Running bandit
uvx bandit -r $1
echo && echo
