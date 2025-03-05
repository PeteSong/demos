This is a demo project for the "Playwright + Python(uv) + Pytest".

There are tests on the [TodoMVC website](https://todomvc.com/examples/web-components/dist/).

1. Go to `python` directory

```
cd demos/playwright-demos/python
```

2. Run all the tests

```
uv run pytest
```

Or run the tests in parallel

```
uv run pytest -n auto
```

3. Run a specific test

```
uv run pytest path/to/test.py
```

4. check and format the code with `isort + black + flake8`

```
# format the file first
./scripts/format.sh path/to/file.py

# then check the file
./scripts/check.sh path/to/file.py
```
