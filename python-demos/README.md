## Install `uv`
Use [Homebrew](https://brew.sh/) to install [uv](https://docs.astral.sh/uv/getting-started/).

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
uv add numpy
```

Remove a dependency

```shell
uv remove numpy
```
