import sys
from _typeshed import Incomplete, SupportsRead
from collections.abc import Sequence
from typing import Final, Literal
from typing_extensions import TypeAlias
from xml.dom.minidom import Document, DOMImplementation, Element, Text
from xml.sax.handler import ContentHandler
from xml.sax.xmlreader import XMLReader

START_ELEMENT: Final = "START_ELEMENT"
END_ELEMENT: Final = "END_ELEMENT"
COMMENT: Final = "COMMENT"
START_DOCUMENT: Final = "START_DOCUMENT"
END_DOCUMENT: Final = "END_DOCUMENT"
PROCESSING_INSTRUCTION: Final = "PROCESSING_INSTRUCTION"
IGNORABLE_WHITESPACE: Final = "IGNORABLE_WHITESPACE"
CHARACTERS: Final = "CHARACTERS"

_DocumentFactory: TypeAlias = DOMImplementation | None
_Node: TypeAlias = Document | Element | Text

_Event: TypeAlias = tuple[
    Literal[
        Literal["START_ELEMENT"],
        Literal["END_ELEMENT"],
        Literal["COMMENT"],
        Literal["START_DOCUMENT"],
        Literal["END_DOCUMENT"],
        Literal["PROCESSING_INSTRUCTION"],
        Literal["IGNORABLE_WHITESPACE"],
        Literal["CHARACTERS"],
    ],
    _Node,
]

class PullDOM(ContentHandler):
    document: Document | None
    documentFactory: _DocumentFactory
    firstEvent: Incomplete
    lastEvent: Incomplete
    elementStack: Sequence[Incomplete]
    pending_events: Sequence[Incomplete]
    def __init__(self, documentFactory: _DocumentFactory = None) -> None: ...
    def pop(self) -> Element: ...
    def setDocumentLocator(self, locator) -> None: ...
    def startPrefixMapping(self, prefix, uri) -> None: ...
    def endPrefixMapping(self, prefix) -> None: ...
    def startElementNS(self, name, tagName, attrs) -> None: ...
    def endElementNS(self, name, tagName) -> None: ...
    def startElement(self, name, attrs) -> None: ...
    def endElement(self, name) -> None: ...
    def comment(self, s) -> None: ...
    def processingInstruction(self, target, data) -> None: ...
    def ignorableWhitespace(self, chars) -> None: ...
    def characters(self, chars) -> None: ...
    def startDocument(self) -> None: ...
    def buildDocument(self, uri, tagname): ...
    def endDocument(self) -> None: ...
    def clear(self) -> None:
        """clear(): Explicitly release parsing structures"""
        ...

class ErrorHandler:
    def warning(self, exception) -> None: ...
    def error(self, exception) -> None: ...
    def fatalError(self, exception) -> None: ...

class DOMEventStream:
    stream: SupportsRead[bytes] | SupportsRead[str]
    parser: XMLReader
    bufsize: int
    def __init__(self, stream: SupportsRead[bytes] | SupportsRead[str], parser: XMLReader, bufsize: int) -> None: ...
    pulldom: Incomplete
    if sys.version_info < (3, 11):
        def __getitem__(self, pos): ...

    def __next__(self): ...
    def __iter__(self): ...
    def getEvent(self) -> _Event: ...
    def expandNode(self, node: _Node) -> None: ...
    def reset(self) -> None: ...
    def clear(self) -> None:
        """clear(): Explicitly release parsing objects"""
        ...

class SAX2DOM(PullDOM):
    def startElementNS(self, name, tagName, attrs) -> None: ...
    def startElement(self, name, attrs) -> None: ...
    def processingInstruction(self, target, data) -> None: ...
    def ignorableWhitespace(self, chars) -> None: ...
    def characters(self, chars) -> None: ...

default_bufsize: int

def parse(
    stream_or_string: str | SupportsRead[bytes] | SupportsRead[str], parser: XMLReader | None = None, bufsize: int | None = None
) -> DOMEventStream: ...
def parseString(string: str, parser: XMLReader | None = None) -> DOMEventStream: ...
