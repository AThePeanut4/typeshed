import html
from typing import Any

HTMLunescape = html.unescape
ESCAPED_CHAR: Any
rePunctuation: Any
reLinkTitle: Any
reLinkDestinationBraces: Any
reEscapable: Any
reEntityHere: Any
reTicks: Any
reTicksHere: Any
reEllipses: Any
reDash: Any
reEmailAutolink: Any
reAutolink: Any
reSpnl: Any
reWhitespaceChar: Any
reWhitespace: Any
reUnicodeWhitespaceChar: Any
reFinalSpace: Any
reInitialSpace: Any
reSpaceAtEndOfLine: Any
reLinkLabel: Any
reMain: Any

def text(s): ...
def smart_dashes(chars): ...

class InlineParser:
    """
    INLINE PARSER

    These are methods of an InlineParser class, defined below.
    An InlineParser keeps track of a subject (a string to be
    parsed) and a position in that subject.
    """
    subject: str
    brackets: Any
    pos: int
    refmap: Any
    options: Any
    def __init__(self, options=...) -> None: ...
    def match(self, regexString):
        """
        If regexString matches at current position in the subject, advance
        position in subject and return the match; otherwise return None.
        """
        ...
    def peek(self):
        """
        Returns the character at the current subject position, or None if
        there are no more characters.
        """
        ...
    def spnl(self):
        """
        Parse zero or more space characters, including at
        most one newline.
        """
        ...
    def parseBackticks(self, block):
        """
        Attempt to parse backticks, adding either a backtick code span or a
        literal sequence of backticks to the 'inlines' list.
        """
        ...
    def parseBackslash(self, block):
        """
        Parse a backslash-escaped special character, adding either the
        escaped character, a hard line break (if the backslash is followed
        by a newline), or a literal backslash to the block's children.
        Assumes current character is a backslash.
        """
        ...
    def parseAutolink(self, block):
        """Attempt to parse an autolink (URL or email in pointy brackets)."""
        ...
    def parseHtmlTag(self, block):
        """Attempt to parse a raw HTML tag."""
        ...
    def scanDelims(self, c):
        """
        Scan a sequence of characters == c, and return information about
        the number of delimiters and whether they are positioned such that
        they can open and/or close emphasis or strong emphasis.  A utility
        function for strong/emph parsing.
        """
        ...
    delimiters: Any
    def handleDelim(self, cc, block):
        """Handle a delimiter marker for emphasis or a quote."""
        ...
    def removeDelimiter(self, delim) -> None: ...
    @staticmethod
    def removeDelimitersBetween(bottom, top) -> None: ...
    def processEmphasis(self, stack_bottom) -> None: ...
    def parseLinkTitle(self):
        """
        Attempt to parse link title (sans quotes), returning the string
        or None if no match.
        """
        ...
    def parseLinkDestination(self):
        """
        Attempt to parse link destination, returning the string or
        None if no match.
        """
        ...
    def parseLinkLabel(self):
        """
        Attempt to parse a link label, returning number of
        characters parsed.
        """
        ...
    def parseOpenBracket(self, block):
        """
        Add open bracket to delimiter stack and add a text node to
        block's children.
        """
        ...
    def parseBang(self, block):
        """
        If next character is [, and ! delimiter to delimiter stack and
        add a text node to block's children. Otherwise just add a text
        node.
        """
        ...
    def parseCloseBracket(self, block):
        """
        Try to match close bracket against an opening in the delimiter
        stack. Add either a link or image, or a plain [ character,
        to block's children. If there is a matching delimiter,
        remove it from the delimiter stack.
        """
        ...
    def addBracket(self, node, index, image) -> None: ...
    def removeBracket(self) -> None: ...
    def parseEntity(self, block):
        """Attempt to parse an entity."""
        ...
    def parseString(self, block):
        """
        Parse a run of ordinary characters, or a single character with
        a special meaning in markdown, as a plain string.
        """
        ...
    def parseNewline(self, block):
        """
        Parse a newline.  If it was preceded by two spaces, return a hard
        line break; otherwise a soft line break.
        """
        ...
    def parseReference(self, s, refmap):
        """Attempt to parse a link reference, modifying refmap."""
        ...
    def parseInline(self, block):
        """
        Parse the next inline element in subject, advancing subject
        position.

        On success, add the result to block's children and return True.
        On failure, return False.
        """
        ...
    def parseInlines(self, block) -> None:
        """
        Parse string content in block into inline children,
        using refmap to resolve references.
        """
        ...
    parse: Any
