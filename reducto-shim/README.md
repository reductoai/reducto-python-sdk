# reducto (PyPI alias)

This directory builds the `reducto` package on PyPI, which is an alias for [`reductoai`](https://pypi.org/project/reductoai/) — the official Reducto Python SDK.

`pip install reducto` installs `reductoai` as a dependency. The import name is `reducto` either way:

```python
import reducto
```

## Prefer installing reductoai directly

```
pip install reductoai
```

The `reducto` alias exists for discoverability; new projects should depend on `reductoai` explicitly.

## How this builds

This directory is published by `.github/workflows/publish-shim-pypi.yml`, which runs after the main `Publish PyPI` workflow succeeds. The workflow reads the canonical version from `src/reducto/_version.py`, substitutes `VERSION_PLACEHOLDER` in `pyproject.toml`, and publishes. The shim is always pinned to the exact `reductoai` version from the same release.

`pyproject.toml` contains `VERSION_PLACEHOLDER` on disk; it is not installable locally without CI substitution (and there's no reason to — use the main package).
