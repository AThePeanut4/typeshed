from _typeshed import SupportsRead
from pathlib import Path
from typing import Any, Literal

from PIL import Image

from .._types import Ink, Writeable
from ..main import ModulesType
from . import base
from .styles.colormasks import QRColorMask
from .styles.moduledrawers import SquareModuleDrawer
from .styles.moduledrawers.base import QRModuleDrawer

class StyledPilImage(base.BaseImageWithDrawer):
    """
    Styled PIL image builder, default format is PNG.

    This differs from the PilImage in that there is a module_drawer, a
    color_mask, and an optional image

    The module_drawer should extend the QRModuleDrawer class and implement the
    drawrect_context(self, box, active, context), and probably also the
    initialize function. This will draw an individual "module" or square on
    the QR code.

    The color_mask will extend the QRColorMask class and will at very least
    implement the get_fg_pixel(image, x, y) function, calculating a color to
    put on the image at the pixel location (x,y) (more advanced functionality
    can be gotten by instead overriding other functions defined in the
    QRColorMask class)

    The Image can be specified either by path or with a Pillow Image, and if it
    is there will be placed in the middle of the QR code. No effort is done to
    ensure that the QR code is still legible after the image has been placed
    there; Q or H level error correction levels are recommended to maintain
    data integrity A resampling filter can be specified (defaulting to
    PIL.Image.Resampling.LANCZOS) for resizing; see PIL.Image.resize() for possible
    options for this parameter.
    The image size can be controlled by `embeded_image_ratio` which is a ratio
    between 0 and 1 that's set in relation to the overall width of the QR code.
    """
    kind: Literal["PNG"]
    color_mask: QRColorMask
    default_drawer_class: type[SquareModuleDrawer]
    embeded_image: Image.Image
    embeded_image_resample: Image.Resampling
    paint_color: Ink
    # the class accepts arbitrary additional positional arguments to accommodate
    # subclasses with additional arguments. kwargs are forwarded to the `new_image()` call
    # via the BaseImage.__init__ method.
    def __init__(
        self,
        border: int,
        width: int,
        box_size: int,
        *args: Any,
        qrcode_modules: ModulesType | None,
        module_drawer: QRModuleDrawer | str | None = None,
        eye_drawer: QRModuleDrawer | str | None = None,
        color_mask: QRColorMask = ...,
        embeded_image_path: str | bytes | Path | SupportsRead[bytes] | None = None,
        embeded_image: Image.Image | None = None,
        embeded_image_resample: Image.Resampling = ...,
        **kwargs: Any,
    ) -> None: ...
    # the new_image method accepts arbitrary keyword arguments to accommodate
    # subclasses with additional arguments.
    def new_image(self, **kwargs: Any) -> Image.Image: ...
    def draw_embeded_image(self) -> None: ...
    # kwargs are passed on to PIL.Image.save, which also accepts arbitrary keyword arguments.
    def save(  # type: ignore[override]
        self,
        stream: str | bytes | Path | Writeable,
        format: str | None = None,
        *,
        kind: str | None = None,
        save_all: bool = ...,
        bitmap_format: Literal["bmp", "png"] = ...,
        optimize: bool = ...,
        **kwargs: Any,
    ) -> None: ...
    # attribute access is forwarded to the wrapped PIL.Image.Image instance.
    def __getattr__(self, name: str) -> Any: ...
