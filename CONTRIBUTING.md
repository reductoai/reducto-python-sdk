## Setting up the environment

We use [uv](https://docs.astral.sh/uv/) to manage dependencies. It provisions a Python environment with the version in `.python-version`. To set it up, run:

```sh
$ ./scripts/bootstrap
```

Or [install uv manually](https://docs.astral.sh/uv/getting-started/installation/) and run:

```sh
$ uv sync --all-extras
```

You can then run scripts with `uv run python script.py` or activate the virtual environment:

```sh
# Activate the virtual environment - https://docs.python.org/3/library/venv.html#how-venvs-work
$ source .venv/bin/activate

# now you can omit the `uv run` prefix
$ python script.py
```

## Adding and running examples

All files in the `examples/` directory can be freely edited or added to.

```py
# add an example to examples/<your-example>.py

#!/usr/bin/env -S uv run python
…
```

```sh
$ chmod +x examples/<your-example>.py
# run the example against your api
$ ./examples/<your-example>.py
```

## Using the repository from source

If you'd like to use the repository from source, you can either install from git or link to a cloned repository:

To install via git:

```sh
$ pip install git+ssh://git@github.com/reductoai/reducto-python-sdk.git
```

Alternatively, you can build from source and install the wheel file:

Building this package will create two files in the `dist/` directory, a `.tar.gz` containing the source files and a `.whl` that can be used to install the package efficiently.

To create a distributable version of the library, run this command:

```sh
$ uv build
```

Then to install:

```sh
$ pip install ./path-to-wheel-file.whl
```

## Running tests

```sh
$ ./scripts/test
```

## Linting and formatting

This repository uses [ruff](https://github.com/astral-sh/ruff) to format the code.

To lint:

```sh
$ ./scripts/lint
```

To format and fix all ruff issues automatically:

```sh
$ ./scripts/format
```

## Publishing and releases

Releases are manual.

1. Bump the version in `pyproject.toml` and `src/reducto/_version.py`. Both must match.
2. Add a section to `CHANGELOG.md`.
3. Merge to `main`, then create a GitHub release with tag `vX.Y.Z`.

Publishing the release triggers [the `Publish PyPI` GitHub action](https://www.github.com/reductoai/reducto-python-sdk/actions/workflows/publish-pypi.yml). It needs the `REDUCTO_PYPI_TOKEN` (or `PYPI_TOKEN`) repository secret. You can also run it by hand from the Actions tab.

The `reducto` alias package publishes automatically after `Publish PyPI` succeeds.

### Publish from your machine

Run `bin/publish-pypi` with `PYPI_TOKEN` set in the environment.
