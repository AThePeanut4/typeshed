import html
import re
from typing import Any, Final, Literal

from .node import Node

HTMLunescape = html.unescape
ESCAPED_CHAR: Final[str]
rePunctuation: Final[re.Pattern[str]]
reLinkTitle: Final[re.Pattern[str]]
reLinkDestinationBraces: Final[re.Pattern[str]]
reEscapable: Final[re.Pattern[str]]
reEntityHere: Final[re.Pattern[str]]
reTicks: Final[re.Pattern[str]]
reTicksHere: Final[re.Pattern[str]]
reEllipses: Final[re.Pattern[str]]
reDash: Final[re.Pattern[str]]
reEmailAutolink: Final[re.Pattern[str]]
reAutolink: Final[re.Pattern[str]]
reSpnl: Final[re.Pattern[str]]
reWhitespaceChar: Final[re.Pattern[str]]
reWhitespace: Final[re.Pattern[str]]
reUnicodeWhitespaceChar: Final[re.Pattern[str]]
reFinalSpace: Final[re.Pattern[str]]
reInitialSpace: Final[re.Pattern[str]]
reSpaceAtEndOfLine: Final[re.Pattern[str]]
reLinkLabel: Final[re.Pattern[str]]
reMain: Final[re.Pattern[str]]

def text(s: str) -> Node: ...
def smart_dashes(chars: str) -> str: ...

class InlineParser:
    """
    INLINE PARSER

    These are methods of an InlineParser class, defined below.
    An InlineParser keeps track of a subject (a string to be
    parsed) and a position in that subject.
    """
    subject: str
    brackets: dict[str, Any] | None
    pos: int
    refmap: dict[str, Any]
    options: dict[str, Any]
    def __init__(self, options: dict[str, Any] = {}) -> None: ...
    def match(self, regexString: str | re.Pattern[str]) -> str | None:
        """
        If regexString matches at current position in the subject, advance
        position in subject and return the match; otherwise return None.
        """
        ...
    def peek(self) -> str | None:
        """
        Returns the character at the current subject position, or None if
        there are no more characters.
        """
        ...
    def spnl(self) -> Literal[True]:
        """
        Parse zero or more space characters, including at
        most one newline.
        """
        ...
    def parseBackticks(self, block: Node) -> bool:
        """
        Attempt to parse backticks, adding either a backtick code span or a
        literal sequence of backticks to the 'inlines' list.
        """
        ...
    def parseBackslash(self, block: Node) -> Literal[True]:
        """
        Parse a backslash-escaped special character, adding either the
        escaped character, a hard line break (if the backslash is followed
        by a newline), or a literal backslash to the block's children.
        Assumes current character is a backslash.
        """
        ...
    def parseAutolink(self, block: Node) -> bool:
        """Attempt to parse an autolink (URL or email in pointy brackets)."""
        ...
    def parseHtmlTag(self, block: Node) -> bool:
        """Attempt to parse a raw HTML tag."""
        ...
    def scanDelims(self, c: str) -> dict[str, Any] | None:
        """
        Scan a sequence of characters == c, and return information about
        the number of delimiters and whether they are positioned such that
        they can open and/or close emphasis or strong emphasis.  A utility
        function for strong/emph parsing.
        """
        ...
    delimiters: dict[str, Any]
    def handleDelim(self, cc: str, block: Node) -> bool:
        """Handle a delimiter marker for emphasis or a quote."""
        ...
    def removeDelimiter(self, delim: dict[str, Any]) -> None: ...
    @staticmethod
    def removeDelimitersBetween(bottom: dict[str, Any], top: dict[str, Any]) -> None: ...
    def processEmphasis(self, stack_bottom: dict[str, Any]) -> None: ...
    def parseLinkTitle(self) -> str | None:
        """
        Attempt to parse link title (sans quotes), returning the string
        or None if no match.
        """
        ...
    def parseLinkDestination(self) -> str | None:
        """
        Attempt to parse link destination, returning the string or
        None if no match.
        """
        ...
    def parseLinkLabel(self) -> int:
        """
        Attempt to parse a link label, returning number of
        characters parsed.
        """
        ...
    def parseOpenBracket(self, block: Node) -> Literal[True]:
        """
        Add open bracket to delimiter stack and add a text node to
        block's children.
        """
        ...
    def parseBang(self, block: Node) -> Literal[True]:
        """
        If next character is [, and ! delimiter to delimiter stack and
        add a text node to block's children. Otherwise just add a text
        node.
        """
        ...
    def parseCloseBracket(self, block: Node) -> Literal[True]:
        """
        Try to match close bracket against an opening in the delimiter
        stack. Add either a link or image, or a plain [ character,
        to block's children. If there is a matching delimiter,
        remove it from the delimiter stack.
        """
        ...
    def addBracket(self, node: Node, index: int, image: bool | None) -> None: ...
    def removeBracket(self) -> None: ...
    def parseEntity(self, block: Node) -> bool:
        """Attempt to parse an entity."""
        ...
    def parseString(self, block: Node) -> bool:
        """
        Parse a run of ordinary characters, or a single character with
        a special meaning in markdown, as a plain string.
        """
        ...
    def parseNewline(self, block: Node) -> Literal[True]:
        """
        Parse a newline.  If it was preceded by two spaces, return a hard
        line break; otherwise a soft line break.
        """
        ...
    def parseReference(self, s: str, refmap: dict[str, Any]) -> int:
        """Attempt to parse a link reference, modifying refmap."""
        ...
    def parseInline(self, block: Node) -> bool:
        """
        Parse the next inline element in subject, advancing subject
        position.

        On success, add the result to block's children and return True.
        On failure, return False.
        """
        ...
    def parseInlines(self, block: Node) -> None:
        """
        Parse string content in block into inline children,
        using refmap to resolve references.
        """
        ...
    parse = parseInlines
