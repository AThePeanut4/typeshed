"""
new experimental paragraph implementation

Intended to allow support for paragraphs in paragraphs, hotlinks,
embedded flowables, and underlining.  The main entry point is the
function

def Paragraph(text, style, bulletText=None, frags=None)

Which is intended to be plug compatible with the "usual" platypus
paragraph except that it supports more functionality.

In this implementation you may embed paragraphs inside paragraphs
to create hierarchically organized documents.

This implementation adds the following paragraph-like tags (which
support the same attributes as paragraphs, for font specification, etc).

- Unnumberred lists (ala html)::

    <ul>
        <li>first one</li>
        <li>second one</li>
    </ul>


Also <ul type="disc"> (default) or <ul type="circle">, <ul type="square">.

- Numberred lists (ala html)::

    <ol>
        <li>first one</li>
        <li>second one</li>
    </ol>

Also <ul type="1"> (default) or <ul type="a">, <ul type="A">.

- Display lists (ala HTML):

For example

<dl bulletFontName="Helvetica-BoldOblique" spaceBefore="10" spaceAfter="10">
<dt>frogs</dt> <dd>Little green slimy things. Delicious with <b>garlic</b></dd>
<dt>kittens</dt> <dd>cute, furry, not edible</dd>
<dt>bunnies</dt> <dd>cute, furry,. Delicious with <b>garlic</b></dd>
</dl>

ALSO the following additional internal paragraph markup tags are supported

<u>underlined text</u>

<a href="http://www.reportlab.com">hyperlinked text</a>
<a href="http://www.reportlab.com" color="blue">hyperlinked text</a>

<link destination="end" >Go to the end (go to document internal destination)</link>
<link destination="start" color="cyan">Go to the beginning</link>

<setLink destination="start" color="magenta">This is the document start
  (define document destination inside paragraph, color is optional)</setLink>
"""

from _typeshed import Incomplete, Unused
from collections.abc import Callable, Mapping
from typing import Any, Final, Literal, Protocol, TypedDict, TypeVar, overload
from typing_extensions import TypeAlias, Unpack

from reportlab.lib.colors import Color
from reportlab.lib.styles import ParagraphStyle, PropertySet, StyleSheet1
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfgen.textobject import PDFTextObject, _Color
from reportlab.platypus.flowables import Flowable

_T = TypeVar("_T")
_BoolInt: TypeAlias = Literal[0, 1]
_Op: TypeAlias = _SupportsWidthAndExecute | str | float | tuple[str, Unpack[tuple[Any, ...]]]
# NOTE: Output from pyRXP xml parser
_ParsedText: TypeAlias = tuple[str, dict[str, Any], list[_ParsedText], Any] | list[_ParsedText] | str

class _LineOpHandler(Protocol):
    def start_at(self, x: float, y: float, para: paragraphEngine, canvas: Canvas, textobject: PDFTextObject) -> None: ...
    def end_at(self, x: float, y: float, para: paragraphEngine, canvas: Canvas, textobject: PDFTextObject) -> None: ...

class _SupportsWidthAndExecute(Protocol):
    def width(self, engine) -> float: ...
    def execute(self, engine, textobject: PDFTextObject, canvas: Canvas) -> object: ...

class _SimpleStyleKwargs(TypedDict, total=False):
    fontName: str
    fontSize: float
    leading: float
    leftIndent: float
    rightIndent: float
    firstLineIndent: float
    alignment: Literal[0, 1, 2, 4]
    spaceBefore: float
    spaceAfter: float
    bulletFontName: str
    bulletFontSize: float
    bulletIndent: float
    textColor: _Color
    backColor: _Color | None

debug: int
DUMPPROGRAM: int
TOOSMALLSPACE: float

class paragraphEngine:
    TEXT_STATE_VARIABLES: Final[tuple[str, ...]]
    lineOpHandlers: list[_LineOpHandler]
    program: list[_Op]
    indent: float
    baseindent: float
    fontName: str
    fontSize: float
    leading: float
    fontColor: _Color
    x: float
    y: float
    alignment: Literal[0, 1, 2, 4]
    # NOTE: The inner list matches TEXT_STATE_VARIABLES
    textStateStack: list[list[Any]]
    def __init__(self, program: list[_Op] | None = None) -> None: ...
    def pushTextState(self) -> list[Any]: ...
    def popTextState(self) -> None: ...
    def format(
        self, maxwidth: float, maxheight: float, program: list[_Op], leading: float = 0
    ) -> tuple[list[_Op], str, dict[str, Any], float]:
        """return program with line operations added if at least one line fits"""
        ...
    def getState(self) -> dict[str, Any]: ...
    def resetState(self, state: dict[str, Any]) -> None: ...
    def fitLine(
        self, program: list[_Op], totalLength: float
    ) -> tuple[Literal[0, 1], list[_Op], int, float, float, float, Literal[0, 1]]:
        """fit words (and other things) onto a line"""
        ...
    def centerAlign(self, line: list[_Op], lineLength: float, maxLength: float) -> list[_Op]: ...
    def rightAlign(self, line: list[_Op], lineLength: float, maxLength: float) -> list[_Op]: ...
    def insertShift(self, line: list[_Op], shift: float) -> list[_Op]: ...
    def justifyAlign(self, line: list[_Op], lineLength: float, maxLength: float) -> list[_Op]: ...
    def shrinkWrap(self, line: list[_Op]) -> list[_Op]: ...
    def cleanProgram(self, line: list[_Op]) -> list[_Op]:
        """collapse adjacent spacings"""
        ...
    def runOpCodes(self, program: list[_Op], canvas: Canvas, textobject: PDFTextObject) -> dict[str, Any]:
        """render the line(s)"""
        ...

def stringLine(line: list[_Op], length: float) -> list[_Op]:
    """simple case: line with just strings and spacings which can be ignored"""
    ...
def simpleJustifyAlign(line: list[_Op], currentLength: float, maxLength: float) -> list[_Op]:
    """simple justification with only strings"""
    ...
def readBool(text: str) -> _BoolInt: ...
def readAlignment(text: str) -> Literal[0, 1, 2, 4] | None: ...
def readLength(text: str) -> float:
    """
    Read a dimension measurement: accept "3in", "5cm",
    "72 pt" and so on.
    """
    ...
@overload
def lengthSequence(s: str, converter: Callable[[str], float] = ...) -> list[float]:
    """from "(2, 1)" or "2,1" return [2,1], for example"""
    ...
@overload
def lengthSequence(s: str, converter: Callable[[str], _T]) -> list[_T]:
    """from "(2, 1)" or "2,1" return [2,1], for example"""
    ...
def readColor(text: str | None) -> Color | None:
    """Read color names or tuples, RGB or CMYK, and return a Color object."""
    ...

class StyleAttributeConverters:
    fontSize: list[Callable[[str], float]]
    leading: list[Callable[[str], float]]
    leftIndent: list[Callable[[str], float]]
    rightIndent: list[Callable[[str], float]]
    firstLineIndent: list[Callable[[str], float]]
    alignment: list[Callable[[str], Literal[0, 1, 2, 4] | None]]
    spaceBefore: list[Callable[[str], float]]
    spaceAfter: list[Callable[[str], float]]
    bulletFontSize: list[Callable[[str], float]]
    bulletIndent: list[Callable[[str], float]]
    textColor: list[Callable[[str], Color | None]]
    backColor: list[Callable[[str], Color | None]]

class SimpleStyle:
    """simplified paragraph style without all the fancy stuff"""
    name: str
    fontName: str
    fontSize: float
    leading: float
    leftIndent: float
    rightIndent: float
    firstLineIndent: float
    alignment: Literal[0, 1, 2, 4]
    spaceBefore: float
    spaceAfter: float
    bulletFontName: str
    bulletFontSize: float
    bulletIndent: float
    textColor: _Color
    backColor: _Color | None
    # NOTE: We are being generous by allowing PropertySet i.e. ParagraphStyle here
    #       technically SimpleStyle is more strict and doesn't allow string alignments
    def __init__(self, name: str, parent: SimpleStyle | PropertySet | None = None, **kw: Unpack[_SimpleStyleKwargs]) -> None: ...
    def addAttributes(self, dictionary: Mapping[str, str | None]) -> None: ...

DEFAULT_ALIASES: Final[dict[str, str]]

class FastPara(Flowable):
    """paragraph with no special features (not even a single ampersand!)"""
    style: SimpleStyle | ParagraphStyle
    simpletext: str
    lines: list[str] | None
    # NOTE: We are being generous by allowing PropertySet i.e. ParagraphStyle here
    #       technically SimpleStyle is more strict and doesn't allow string alignments
    def __init__(self, style: SimpleStyle | PropertySet, simpletext: str) -> None: ...
    def draw(self) -> None: ...

def defaultContext() -> dict[str, PropertySet]: ...
def buildContext(stylesheet: StyleSheet1 | None = None) -> dict[str, PropertySet]: ...

class Para(Flowable):
    baseindent: float
    context: dict[str, PropertySet]
    parsedText: _ParsedText
    bulletText: str | None
    style1: SimpleStyle | PropertySet
    program: list[_Op]
    formattedProgram: list[_Op]
    remainder: _ParsedText
    state: dict[str, Any]
    bold: _BoolInt
    italic: _BoolInt
    face: str
    size: float
    def __init__(
        self,
        # NOTE: We are being generous by allowing PropertySet i.e. ParagraphStyle here
        #       technically SimpleStyle is more strict and doesn't allow string alignments
        style: SimpleStyle | PropertySet,
        parsedText: tuple[Any, ...] | None = None,
        bulletText: str | None = None,
        state: dict[str, Any] | None = None,
        context: dict[str, PropertySet] | None = None,
        baseindent: float = 0,
    ) -> None: ...
    def draw(self) -> None: ...
    def compileProgram(self, parsedText: _ParsedText, program: list[_Op] | None = None) -> list[_Op]: ...
    def linearize(self, program: list[_Op] | None = None, parsedText: _ParsedText | None = None) -> None: ...
    def compileComponent(self, parsedText: _ParsedText, program: list[_Op]) -> None: ...
    def shiftfont(
        self, program: list[_Op], face: str | None = None, bold: _BoolInt | None = None, italic: _BoolInt | None = None
    ): ...
    def compile_(self, attdict, content, extra, program: list[_Op]) -> None: ...
    def compile_pageNumber(self, attdict, content, extra, program: list[_Op]) -> None: ...
    def compile_b(self, attdict, content, extra, program: list[_Op]) -> None: ...
    def compile_i(self, attdict, content, extra, program: list[_Op]) -> None: ...
    def compile_u(self, attdict, content, extra, program: list[_Op]) -> None: ...
    def compile_sub(self, attdict, content, extra, program: list[_Op]) -> None: ...
    def compile_ul(self, attdict, content, extra, program: list[_Op], tagname: str = "ul") -> None: ...
    def compile_ol(self, attdict, content, extra, program: list[_Op]): ...
    def compile_dl(self, attdict, content, extra, program: list[_Op]) -> None: ...
    def compile_super(self, attdict, content, extra, program: list[_Op]) -> None: ...
    def compile_font(self, attdict, content, extra, program: list[_Op]) -> None: ...
    def compile_a(self, attdict, content, extra, program: list[_Op]) -> None: ...
    def compile_link(self, attdict, content, extra, program: list[_Op]) -> None: ...
    def compile_setLink(self, attdict, content, extra, program: list[_Op]) -> None: ...
    def compile_bullet(self, attdict, content, extra, program: list[_Op]) -> None: ...
    def do_bullet(self, text: str, program: list[_Op]) -> None: ...
    def compile_tt(self, attdict, content, extra, program: list[_Op]) -> None: ...
    def compile_greek(self, attdict, content, extra, program: list[_Op]) -> None: ...
    def compile_evalString(self, attdict, content, extra, program: list[_Op]) -> None: ...
    def compile_name(self, attdict, content, extra, program: list[_Op]) -> None: ...
    def compile_getName(self, attdict, content, extra, program: list[_Op]) -> None: ...
    def compile_seq(self, attdict, content, extra, program: list[_Op]) -> None: ...
    def compile_seqReset(self, attdict, content, extra, program: list[_Op]) -> None: ...
    def compile_seqDefault(self, attdict, content, extra, program: list[_Op]) -> None: ...
    def compile_para(self, attdict, content, extra, program: list[_Op], stylename: str = "para.defaultStyle") -> None: ...

class bulletMaker:
    tagname: Literal["ul", "ol", "dl"]
    style: str
    typ: str
    count: int
    def __init__(self, tagname: Literal["ul", "ol", "dl"], atts, context) -> None: ...
    def makeBullet(self, atts, bl: str | None = None) -> None: ...

class EvalStringObject:
    """this will only work if rml2pdf is present"""
    tagname: str
    attdict: Incomplete
    content: str
    context: Incomplete
    extra: Incomplete
    op: Incomplete
    def __init__(self, attdict, content: str, extra, context) -> None: ...
    def getOp(self, tuple, engine): ...
    def width(self, engine) -> float: ...
    def execute(self, engine, textobject: PDFTextObject, canvas: Canvas) -> None: ...

class SeqObject(EvalStringObject): ...
class NameObject(EvalStringObject): ...
class SeqDefaultObject(NameObject): ...
class SeqResetObject(NameObject): ...
class GetNameObject(EvalStringObject): ...

class PageNumberObject:
    example: str
    def __init__(self, example: str = "XXX") -> None: ...
    def width(self, engine) -> float: ...
    def execute(self, engine, textobject: PDFTextObject, canvas: Canvas) -> None: ...

def EmbedInRml2pdf() -> None:
    """make the para the default para implementation in rml2pdf"""
    ...
def handleSpecialCharacters(engine, text: str, program: list[_Op] | None = None) -> list[_Op]: ...
def Paragraph(
    text: str,
    style: SimpleStyle | PropertySet,
    bulletText: str | None = None,
    frags: Unused | None = None,
    context: dict[str, PropertySet] | None = None,
) -> Para | FastPara:
    """
    Paragraph(text, style, bulletText=None)
    intended to be like a platypus Paragraph but better.
    """
    ...

class UnderLineHandler:
    color: _Color | None
    # NOTE: available after start_at
    xStart: float
    yStart: float
    def __init__(self, color: _Color | None = None) -> None: ...
    def start_at(self, x: float, y: float, para: paragraphEngine, canvas: Canvas, textobject: PDFTextObject) -> None: ...
    def end_at(self, x: float, y: float, para: paragraphEngine, canvas: Canvas, textobject: PDFTextObject) -> None: ...

UNDERLINE: Final[UnderLineHandler]

class HotLink(UnderLineHandler):
    url: str
    def __init__(self, url: str) -> None: ...
    def link(self, rect, canvas: Canvas) -> None: ...

class InternalLink(HotLink): ...

class DefDestination(HotLink):
    defined: _BoolInt

def splitspace(text: str) -> list[str]: ...

testparagraph: str
testparagraph1: str

def test2(canv, testpara) -> None: ...

testlink: Incomplete
test_program: Incomplete

def test() -> None: ...
