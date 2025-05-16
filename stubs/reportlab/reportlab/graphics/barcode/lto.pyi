from _typeshed import Incomplete

from reportlab.graphics.barcode.code39 import Standard39

class BaseLTOLabel(Standard39):
    """
    Base class for LTO labels.

    Specification taken from "IBM LTO Ultrium Cartridge Label Specification, Revision 3"
    available on  May 14th 2008 from :
    http://www-1.ibm.com/support/docview.wss?rs=543&context=STCVQ6R&q1=ssg1*&uid=ssg1S7000429&loc=en_US&cs=utf-8&lang=en+en
    """
    LABELWIDTH: Incomplete
    LABELHEIGHT: Incomplete
    LABELROUND: Incomplete
    CODERATIO: float
    CODENOMINALWIDTH: Incomplete
    CODEBARHEIGHT: Incomplete
    CODEBARWIDTH: Incomplete
    CODEGAP = CODEBARWIDTH
    CODELQUIET: Incomplete
    CODERQUIET: Incomplete
    height: Incomplete
    border: Incomplete
    label: Incomplete
    def __init__(
        self, prefix: str = "", number=None, subtype: str = "1", border=None, checksum: bool = False, availheight=None
    ) -> None: ...
    def drawOn(self, canvas, x, y) -> None: ...

class VerticalLTOLabel(BaseLTOLabel):
    """A class for LTO labels with rectangular blocks around the tape identifier."""
    LABELFONT: Incomplete
    BLOCKWIDTH: Incomplete
    BLOCKHEIGHT: Incomplete
    LINEWIDTH: float
    NBBLOCKS: int
    COLORSCHEME: Incomplete
    colored: Incomplete
    def __init__(self, *args, **kwargs) -> None:
        """
        Initializes the label.

        colored : boolean to determine if blocks have to be colorized.
        """
        ...
    def drawOn(self, canvas, x, y) -> None:
        """Draws some blocks around the identifier's characters."""
        ...

def test() -> None:
    """Test this."""
    ...
