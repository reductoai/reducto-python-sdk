from __future__ import annotations

import sys
import subprocess

_HEAVY = ("PIL", "pypdfium2", "pi_heif", "boto3", "botocore")


def _run(code: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, check=False)


def test_import_reducto_loads_no_provider_dependency() -> None:
    """Catches a top-level import that makes every hosted user install Pillow, pypdfium2, or boto3."""
    result = _run(
        "import sys, reducto, reducto.lib._page_parse, reducto.lib.sagemaker; reducto.ReductoSageMaker; "
        f"print(sorted(name for name in {_HEAVY!r} if name in sys.modules))"
    )
    assert result.returncode == 0, result.stderr
    assert result.stdout.strip() == "[]"


def test_import_reducto_loads_no_provider_module() -> None:
    """Catches an eager import of the page parse modules, which slows every hosted `import reducto`."""
    result = _run(
        "import sys, reducto; "
        "print(sorted(name for name in sys.modules if name.startswith('reducto.lib') or name.startswith('boto')))"
    )
    assert result.returncode == 0, result.stderr
    assert result.stdout.strip() == "[]"


def test_missing_dependency_names_the_install_command() -> None:
    """Catches a bare ModuleNotFoundError that does not tell the user which extra to install."""
    result = _run(
        "import sys; sys.modules['pypdfium2'] = None; "
        "from reducto.lib._page_parse.documents import open_document; "
        "open_document(b'%PDF-1.7', None)"
    )
    assert 'pip install "reductoai[sagemaker]"' in result.stderr


def test_missing_heic_dependency_names_its_extra() -> None:
    """Catches a HEIC photo that fails with a bare import error when the heic extra is missing."""
    result = _run(
        "import sys; sys.modules['pi_heif'] = None; "
        "from reducto.lib._page_parse.documents import open_document; "
        "open_document(b'\\x00\\x00\\x00\\x1cftypheic\\x00\\x00\\x00\\x00mif1heic', None)"
    )
    assert 'pip install "reductoai[heic]"' in result.stderr


def test_provider_clients_resolve_from_reducto() -> None:
    """Catches a lazy export that breaks `from reducto import ...`, `dir(reducto)`, or the public module name."""
    result = _run(
        "import reducto; listed = 'ReductoSageMaker' in dir(reducto); "
        "from reducto import AsyncReductoSageMaker; "
        "print(listed, reducto.ReductoSageMaker.__module__, AsyncReductoSageMaker.__module__)"
    )
    assert result.returncode == 0, result.stderr
    assert result.stdout.strip() == "True reducto reducto"


def test_provider_names_are_the_same_class_from_both_public_paths() -> None:
    """Catches an error class that differs between `reducto` and `reducto.lib.sagemaker`, so `except` misses it."""
    import reducto
    import reducto.lib.sagemaker as sagemaker

    for name in ("ReductoSageMaker", "AsyncReductoSageMaker", "PageParseError", "UnsupportedOnProviderError"):
        assert getattr(reducto, name) is getattr(sagemaker, name)
    assert issubclass(sagemaker.PageParseError, reducto.ReductoError)
