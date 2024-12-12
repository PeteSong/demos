## Setup Python environment on macOS

First install [Homebrew](https://brew.sh/)

Then install [pyenv](https://github.com/pyenv/pyenv)

```shell
brew install pyenv
```

Install specific Python

```shell
pyenv install 3.12
```

Then install [uv](https://docs.astral.sh/uv/getting-started/).

```shell
brew install uv
```

Install uv-managed python even if there's already a Python installation on your system.
Once Python is installed, it will be used by `uv` command automatically
When Python is installed by `uv`, it will not be available globally.

```shell
uv install 3.12.8
```

Created a new project.

```shell
uv init python-demos
```

Add a dependency

```shell
uv add pre-commit
```

Configure the `pre-commit` with tools

`.pre-commit-config.yaml`
```yaml
repos:
- repo: https://github.com/psf/black
  rev: 24.10.0
  hooks:
  - id: black

- repo: https://github.com/PyCQA/isort
  rev: 5.13.2
  hooks:
  - id: isort

- repo: https://github.com/PyCQA/flake8
  rev: 7.1.1
  hooks:
  - id: flake8
```

Then install the git hooks.

```shell
uv run pre-commit install
```

now when you run `git commit`, it will run those tools automatically.

## run a file

```shell
cd python-demos
uv run ./leetcode_solutions/lc2235.py
```
