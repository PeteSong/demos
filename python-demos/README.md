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

Add dependencies

```shell
uv add pytest
uv add pytest-cov

uv add pre-commit
```

Add dependencies only for dev

```shell
uv add --dev ipython
uv add --dev jupyter
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
    args: [
      "--ignore=E203,W503,E266",
      --max-line-length=120
    ]
```

Then install the git hooks.

```shell
uv run pre-commit install
```

now when you run `git commit`, it will run those tools automatically.

## Run a file

```shell
cd python-demos

# check a file
source ./scripts/check.sh ./leetcode/lc2235.py

# run a file
uv run ./leetcode/lc2235.py

# run pytest
uv run pytest

# run pytest on one file
uv run pytest ./tests/test_leetcode_solutions/test_lc13.py
```
