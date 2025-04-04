"""This includes some demos of platypus for use in the API proposal"""

from _typeshed import Incomplete
from typing import Final

from reportlab.platypus import Flowable

__version__: Final[str]
captionStyle: Incomplete

class Figure(Flowable):
    width: Incomplete
    figureHeight: Incomplete
    caption: Incomplete
    captionFont: Incomplete
    captionSize: Incomplete
    captionTextColor: Incomplete
    captionBackColor: Incomplete
    captionGap: Incomplete
    captionAlign: Incomplete
    captionPosition: Incomplete
    captionHeight: int
    background: Incomplete
    border: Incomplete
    spaceBefore: Incomplete
    spaceAfter: Incomplete
    hAlign: Incomplete
    def __init__(
        self,
        width,
        height,
        caption: str = "",
        captionFont="Helvetica-Oblique",
        captionSize: int = 12,
        background: Incomplete | None = None,
        captionTextColor=...,
        captionBackColor: Incomplete | None = None,
        border: Incomplete | None = None,
        spaceBefore: int = 12,
        spaceAfter: int = 12,
        captionGap: Incomplete | None = None,
        captionAlign: str = "centre",
        captionPosition: str = "bottom",
        hAlign: str = "CENTER",
    ) -> None: ...
    height: Incomplete
    dx: Incomplete
    def wrap(self, availWidth, availHeight): ...
    def draw(self) -> None: ...
    def drawBorder(self) -> None: ...
    def drawBackground(self) -> None:
        """
        For use when using a figure on a differently coloured background.
        Allows you to specify a colour to be used as a background for the figure.
        """
        ...
    def drawCaption(self) -> None: ...
    def drawFigure(self) -> None: ...

def drawPage(canvas, x, y, width, height) -> None: ...

class PageFigure(Figure):
    """
    Shows a blank page in a frame, and draws on that.  Used in
    illustrations of how PLATYPUS works.
    """
    caption: str
    captionStyle: Incomplete
    background: Incomplete
    def __init__(self, background: Incomplete | None = None) -> None: ...
    def drawVirtualPage(self) -> None: ...
    def drawFigure(self) -> None: ...

class PlatPropFigure1(PageFigure):
    """This shows a page with a frame on it"""
    caption: str
    def __init__(self) -> None: ...
    def drawVirtualPage(self) -> None: ...

class FlexFigure(Figure):
    """Base for a figure class with a caption. Can grow or shrink in proportion"""
    shrinkToFit: Incomplete
    growToFit: Incomplete
    scaleFactor: Incomplete
    background: Incomplete
    def __init__(
        self,
        width,
        height,
        caption,
        background: Incomplete | None = None,
        captionFont: str = "Helvetica-Oblique",
        captionSize: int = 8,
        captionTextColor=...,
        shrinkToFit: int = 1,
        growToFit: int = 1,
        spaceBefore: int = 12,
        spaceAfter: int = 12,
        captionGap: int = 9,
        captionAlign: str = "centre",
        captionPosition: str = "top",
        scaleFactor: Incomplete | None = None,
        hAlign: str = "CENTER",
        border: int = 1,
    ) -> None: ...
    def wrap(self, availWidth, availHeight): ...
    def split(self, availWidth, availHeight): ...

class ImageFigure(FlexFigure):
    """Image with a caption below it"""
    filename: Incomplete
    def __init__(
        self,
        filename,
        caption,
        background: Incomplete | None = None,
        scaleFactor: Incomplete | None = None,
        hAlign: str = "CENTER",
        border: Incomplete | None = None,
    ) -> None: ...
    def drawFigure(self) -> None: ...

class DrawingFigure(FlexFigure):
    """Drawing with a caption below it.  Clunky, scaling fails."""
    drawing: Incomplete
    growToFit: int
    def __init__(
        self, modulename, classname, caption, baseDir: Incomplete | None = None, background: Incomplete | None = None
    ) -> None: ...
    def drawFigure(self) -> None: ...

def demo1(canvas) -> None: ...
def test1() -> None: ...
