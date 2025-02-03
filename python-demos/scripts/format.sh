#!/usr/bin/env bash

echo ==== Running black
uvx black $1
echo && echo

echo ==== Running isort
uvx isort $1
echo && echo
