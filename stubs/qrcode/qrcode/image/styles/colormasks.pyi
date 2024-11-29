from _typeshed import SupportsRead
from pathlib import Path

from PIL import Image

from ..._types import Ink
from ..styledpil import StyledPilImage

class QRColorMask:
    """
    QRColorMask is used to color in the QRCode.

    By the time apply_mask is called, the QRModuleDrawer of the StyledPilImage
    will have drawn all of the modules on the canvas (the color of these
    modules will be mostly black, although antialiasing may result in
    gradients) In the base class, apply_mask is implemented such that the
    background color will remain, but the foreground pixels will be replaced by
    a color determined by a call to get_fg_pixel. There is additional
    calculation done to preserve the gradient artifacts of antialiasing.

    All QRColorMask objects should be careful about RGB vs RGBA color spaces.

    For examples of what these look like, see doc/color_masks.png
    """
    back_color: Ink
    has_transparency: bool
    paint_color: Ink
    # image is not actually used by any of the initialize implementations in this project.
    def initialize(self, styledPilImage: StyledPilImage, image: Image.Image) -> None: ...
    def apply_mask(self, image: Image.Image) -> None: ...
    def get_fg_pixel(self, image: Image.Image, x: int, y: int) -> Ink: ...
    def get_bg_pixel(self, image: Image.Image, x: int, y: int) -> Ink: ...
    def interp_num(self, n1: int, n2: int, norm: float) -> int: ...
    def interp_color(self, col1: Ink, col2: Ink, norm: float) -> Ink: ...
    def extrap_num(self, n1: int, n2: int, interped_num: int) -> float | None: ...
    def extrap_color(self, col1: Ink, col2: Ink, interped_color: Ink) -> float | None: ...

class SolidFillColorMask(QRColorMask):
    """Just fills in the background with one color and the foreground with another"""
    front_color: Ink
    def __init__(self, back_color: Ink = (255, 255, 255), front_color: Ink = (0, 0, 0)) -> None: ...

class RadialGradiantColorMask(QRColorMask):
    """Fills in the foreground with a radial gradient from the center to the edge"""
    center_color: Ink
    edge_color: Ink
    def __init__(
        self, back_color: Ink = (255, 255, 255), center_color: Ink = (0, 0, 0), edge_color: Ink = (0, 0, 255)
    ) -> None: ...

class SquareGradiantColorMask(QRColorMask):
    """Fills in the foreground with a square gradient from the center to the edge"""
    center_color: Ink
    edge_color: Ink
    def __init__(
        self, back_color: Ink = (255, 255, 255), center_color: Ink = (0, 0, 0), edge_color: Ink = (0, 0, 255)
    ) -> None: ...

class HorizontalGradiantColorMask(QRColorMask):
    """Fills in the foreground with a gradient sweeping from the left to the right"""
    left_color: Ink
    right_color: Ink
    def __init__(
        self, back_color: Ink = (255, 255, 255), left_color: Ink = (0, 0, 0), right_color: Ink = (0, 0, 255)
    ) -> None: ...

class VerticalGradiantColorMask(QRColorMask):
    """Fills in the forefround with a gradient sweeping from the top to the bottom"""
    top_color: Ink
    bottom_color: Ink
    def __init__(
        self, back_color: Ink = (255, 255, 255), top_color: Ink = (0, 0, 0), bottom_color: Ink = (0, 0, 255)
    ) -> None: ...

class ImageColorMask(QRColorMask):
    """
    Fills in the foreground with pixels from another image, either passed by
    path or passed by image object.
    """
    color_img: Ink
    def __init__(
        self,
        back_color: Ink = (255, 255, 255),
        color_mask_path: str | bytes | Path | SupportsRead[bytes] | None = None,
        color_mask_image: Image.Image | None = None,
    ) -> None: ...
    paint_color: Ink
