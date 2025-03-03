#!/usr/bin/env bash
#
# use this script to format python files
#

echo ==== Running black
uvx black $1
echo && echo

echo ==== Running isort
uvx isort $1
echo && echo
