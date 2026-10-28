from __future__ import annotations

import importlib
from types import ModuleType
from typing import TYPE_CHECKING, Callable, cast
from typing_extensions import override

from ..._utils._proxy import LazyProxy

__all__ = [
    "check_installed",
    "Image",
    "ImageOps",
    "ImageSequence",
    "JpegImagePlugin",
    "LazyModule",
    "pdfium",
    "pdfium_c",
    "register_heif",
]


class LazyModule(LazyProxy[ModuleType]):
    """Imports the module on first use, so `import reducto` never loads it.
    A missing module raises ImportError with the extra that installs it."""

    def __init__(self, name: str, package: str, extra: str) -> None:
        self._name = name
        self._package = package
        self._extra = extra

    @override
    def __load__(self) -> ModuleType:
        try:
            return importlib.import_module(self._name)
        except ImportError as error:
            raise ImportError(
                f'{self._package} is not installed. Install it with: pip install "reductoai[{self._extra}]"'
            ) from error


if TYPE_CHECKING:
    import pypdfium2 as pdfium  # pyright: ignore[reportMissingTypeStubs]
    import pypdfium2.raw as pdfium_c  # pyright: ignore[reportMissingTypeStubs]
    from PIL import Image, ImageOps, ImageSequence, JpegImagePlugin
else:
    pdfium = LazyModule("pypdfium2", "pypdfium2", "sagemaker")
    pdfium_c = LazyModule("pypdfium2.raw", "pypdfium2", "sagemaker")
    Image = LazyModule("PIL.Image", "Pillow", "sagemaker")
    ImageOps = LazyModule("PIL.ImageOps", "Pillow", "sagemaker")
    ImageSequence = LazyModule("PIL.ImageSequence", "Pillow", "sagemaker")
    JpegImagePlugin = LazyModule("PIL.JpegImagePlugin", "Pillow", "sagemaker")

_pi_heif = LazyModule("pi_heif", "pi-heif", "heic")


def register_heif() -> None:
    """Lets Pillow open HEIC and HEIF files."""
    register = cast(Callable[[], None], _pi_heif.register_heif_opener)
    register()


def check_installed() -> None:
    """Imports pypdfium2 and Pillow now, so that a missing package raises the install hint when the client is
    built, not later in a worker thread."""
    for name, package in (("pypdfium2", "pypdfium2"), ("pypdfium2.raw", "pypdfium2"), ("PIL.Image", "Pillow")):
        LazyModule(name, package, "sagemaker").__load__()
