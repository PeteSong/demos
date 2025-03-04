This is a demo project for the "Selenium + Python(uv) + Pytest".

There are tests on the [TodoMVC website](https://todomvc.com/examples/react/dist/).

1. Go to `python` directory

```
cd demos/selenium-demos/python
```

2. Run all the tests

```
uv run pytest
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
