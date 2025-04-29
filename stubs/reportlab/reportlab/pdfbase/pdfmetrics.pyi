from _typeshed import Incomplete, StrOrBytesPath
from typing import Final

from reportlab.lib.rl_accel import unicode2T1 as unicode2T1

__version__: Final[str]
standardFonts: Incomplete
standardEncodings: Incomplete

class FontError(Exception): ...
class FontNotFoundError(Exception): ...

def parseAFMFile(afmFileName: StrOrBytesPath) -> tuple[dict[Incomplete, Incomplete], list[Incomplete]]: ...

class TypeFace:
    name: Incomplete
    glyphNames: Incomplete
    glyphWidths: Incomplete
    ascent: int
    descent: int
    familyName: Incomplete
    bold: int
    italic: int
    requiredEncoding: str
    builtIn: int
    def __init__(self, name) -> None: ...
    def getFontFiles(self):
        """Info function, return list of the font files this depends on."""
        ...
    def findT1File(self, ext: str = ".pfb"): ...

def bruteForceSearchForFile(fn, searchPath: Incomplete | None = None): ...
def bruteForceSearchForAFM(faceName):
    """
    Looks in all AFM files on path for face with given name.

    Returns AFM file name or None.  Ouch!
    """
    ...

class Encoding:
    """Object to help you create and refer to encodings."""
    name: Incomplete
    frozen: int
    baseEncodingName: Incomplete
    vector: Incomplete
    def __init__(self, name, base: Incomplete | None = None) -> None: ...
    def __getitem__(self, index):
        """Return glyph name for that code point, or None"""
        ...
    def __setitem__(self, index, value) -> None: ...
    def freeze(self) -> None: ...
    def isEqual(self, other): ...
    def modifyRange(self, base, newNames) -> None:
        """Set a group of character names starting at the code point 'base'."""
        ...
    def getDifferences(self, otherEnc):
        """
        Return a compact list of the code points differing between two encodings

        This is in the Adobe format: list of
           [[b1, name1, name2, name3],
           [b2, name4]]
   
        where b1...bn is the starting code point, and the glyph names following
        are assigned consecutive code points.
        """
        ...
    def makePDFObject(self):
        """Returns a PDF Object representing self"""
        ...

standardT1SubstitutionFonts: Incomplete

class Font:
    """
    Represents a font (i.e combination of face and encoding).

    Defines suitable machinery for single byte fonts.  This is
    a concrete class which can handle the basic built-in fonts;
    not clear yet if embedded ones need a new font class or
    just a new typeface class (which would do the job through
    composition)
    """
    fontName: Incomplete
    encoding: Incomplete
    encName: Incomplete
    substitutionFonts: Incomplete
    shapable: bool
    def __init__(self, name, faceName, encName, substitutionFonts: Incomplete | None = None) -> None: ...
    def stringWidth(self, text: str | bytes, size: float, encoding: str = "utf8") -> float: ...
    def addObjects(self, doc) -> None: ...

PFB_MARKER: Final[str]
PFB_ASCII: Final[str]
PFB_BINARY: Final[str]
PFB_EOF: Final[str]

class EmbeddedType1Face(TypeFace):
    """
    A Type 1 font other than one of the basic 14.

    Its glyph data will be embedded in the PDF file.
    """
    afmFileName: Incomplete
    pfbFileName: Incomplete
    requiredEncoding: Incomplete
    def __init__(self, afmFileName, pfbFileName) -> None: ...
    def getFontFiles(self): ...
    def addObjects(self, doc):
        """Add whatever needed to PDF file, and return a FontDescriptor reference"""
        ...

def registerTypeFace(face) -> None: ...
def registerEncoding(enc) -> None: ...
def registerFontFamily(
    family,
    normal: Incomplete | None = None,
    bold: Incomplete | None = None,
    italic: Incomplete | None = None,
    boldItalic: Incomplete | None = None,
) -> None: ...
def registerFont(font) -> None: ...
def getTypeFace(faceName): ...
def getEncoding(encName): ...
def findFontAndRegister(fontName: str) -> Font: ...
def getFont(fontName: str) -> Font: ...
def getAscentDescent(fontName: str, fontSize: float | None = None): ...
def getAscent(fontName: str, fontSize: float | None = None): ...
def getDescent(fontName: str, fontSize: float | None = None): ...
def getRegisteredFontNames() -> list[Incomplete]: ...
def stringWidth(text: str | bytes, fontName: str, fontSize: float, encoding: str = "utf8") -> float: ...
def dumpFontData() -> None: ...
def test3widths(texts) -> None: ...
def testStringWidthAlgorithms() -> None: ...
def test() -> None: ...
