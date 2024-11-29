import abc
from typing import Literal

from PIL import Image, ImageDraw

from ...._types import Box
from ....main import ActiveWithNeighbors
from ...styledpil import StyledPilImage
from .base import QRModuleDrawer

ANTIALIASING_FACTOR: int

class StyledPilQRModuleDrawer(QRModuleDrawer, metaclass=abc.ABCMeta):
    """
    A base class for StyledPilImage module drawers.

    NOTE: the color that this draws in should be whatever is equivalent to
    black in the color space, and the specified QRColorMask will handle adding
    colors as necessary to the image
    """
    img: StyledPilImage

class SquareModuleDrawer(StyledPilQRModuleDrawer):
    """Draws the modules as simple squares"""
    imgDraw: ImageDraw.ImageDraw
    def drawrect(self, box: Box, is_active: bool) -> None: ...  # type: ignore[override]

class GappedSquareModuleDrawer(StyledPilQRModuleDrawer):
    """
    Draws the modules as simple squares that are not contiguous.

    The size_ratio determines how wide the squares are relative to the width of
    the space they are printed in
    """
    size_ratio: float
    def __init__(self, size_ratio: float = 0.8) -> None: ...
    imgDraw: ImageDraw.ImageDraw
    delta: float
    def drawrect(self, box: Box, is_active: bool) -> None: ...  # type: ignore[override]

class CircleModuleDrawer(StyledPilQRModuleDrawer):
    """Draws the modules as circles"""
    circle: Image.Image
    def drawrect(self, box: Box, is_active: bool) -> None: ...  # type: ignore[override]

class RoundedModuleDrawer(StyledPilQRModuleDrawer):
    """
    Draws the modules with all 90 degree corners replaced with rounded edges.

    radius_ratio determines the radius of the rounded edges - a value of 1
    means that an isolated module will be drawn as a circle, while a value of 0
    means that the radius of the rounded edge will be 0 (and thus back to 90
    degrees again).
    """
    needs_neighbors: Literal[True]
    radius_ratio: float
    def __init__(self, radius_ratio: float = 1) -> None: ...
    corner_width: int
    SQUARE: Image.Image
    NW_ROUND: Image.Image
    SW_ROUND: Image.Image
    SE_ROUND: Image.Image
    NE_ROUND: Image.Image
    def setup_corners(self) -> None: ...
    def drawrect(self, box: Box, is_active: ActiveWithNeighbors) -> None: ...  # type: ignore[override]

class VerticalBarsDrawer(StyledPilQRModuleDrawer):
    """
    Draws vertically contiguous groups of modules as long rounded rectangles,
    with gaps between neighboring bands (the size of these gaps is inversely
    proportional to the horizontal_shrink).
    """
    needs_neighbors: Literal[True]
    horizontal_shrink: float
    def __init__(self, horizontal_shrink: float = 0.8) -> None: ...
    half_height: int
    delta: int
    SQUARE: Image.Image
    ROUND_TOP: Image.Image
    ROUND_BOTTOM: Image.Image
    def setup_edges(self) -> None: ...
    def drawrect(self, box: Box, is_active: ActiveWithNeighbors) -> None: ...  # type: ignore[override]

class HorizontalBarsDrawer(StyledPilQRModuleDrawer):
    """
    Draws horizontally contiguous groups of modules as long rounded rectangles,
    with gaps between neighboring bands (the size of these gaps is inversely
    proportional to the vertical_shrink).
    """
    needs_neighbors: Literal[True]
    vertical_shrink: float
    def __init__(self, vertical_shrink: float = 0.8) -> None: ...
    half_width: int
    delta: int
    SQUARE: Image.Image
    ROUND_LEFT: Image.Image
    ROUND_RIGHT: Image.Image
    def setup_edges(self) -> None: ...
    def drawrect(self, box: Box, is_active: ActiveWithNeighbors) -> None: ...  # type: ignore[override]
