import re
from typing import Any, Final, Literal

from .inlines import InlineParser
from .node import Node

CODE_INDENT: Final[int]
reHtmlBlockOpen: Final[list[re.Pattern[str]]]
reHtmlBlockClose: Final[list[re.Pattern[str]]]
reThematicBreak: Final[re.Pattern[str]]
reMaybeSpecial: Final[re.Pattern[str]]
reNonSpace: Final[re.Pattern[str]]
reBulletListMarker: Final[re.Pattern[str]]
reOrderedListMarker: Final[re.Pattern[str]]
reATXHeadingMarker: Final[re.Pattern[str]]
reCodeFence: Final[re.Pattern[str]]
reClosingCodeFence: Final[re.Pattern[str]]
reSetextHeadingLine: Final[re.Pattern[str]]
reLineEnding: Final[re.Pattern[str]]

def is_blank(s: str) -> bool:
    """Returns True if string contains only space characters."""
    ...
def is_space_or_tab(s: str) -> bool: ...
def peek(ln: str, pos: int) -> str | None: ...
def ends_with_blank_line(block: Node) -> bool:
    """
    Returns true if block ends with a blank line,
    descending if needed into lists and sublists.
    """
    ...
def parse_list_marker(parser: Parser, container: Node) -> dict[str, Any] | None:
    """
    Parse a list marker and return data on the marker (type,
    start, delimiter, bullet character, padding) or None.
    """
    ...
def lists_match(list_data: dict[str, Any], item_data: dict[str, Any]) -> bool:
    """
    Returns True if the two list items are of the same type,
    with the same delimiter and bullet character.  This is used
    in agglomerating list items into lists.
    """
    ...

class Block:
    accepts_lines: bool | None
    @staticmethod
    def continue_(parser: Parser | None = None, container: Node | None = None) -> int | None: ...
    @staticmethod
    def finalize(parser: Parser | None = None, block: Node | None = None) -> None: ...
    @staticmethod
    def can_contain(t: str) -> bool | None: ...

class Document(Block):
    accepts_lines: Literal[False]
    @staticmethod
    def continue_(parser: Parser | None = None, container: Node | None = None) -> Literal[0]: ...
    @staticmethod
    def finalize(parser: Parser | None = None, block: Node | None = None) -> None: ...
    @staticmethod
    def can_contain(t: str) -> bool: ...

class List(Block):
    accepts_lines: Literal[False]
    @staticmethod
    def continue_(parser: Parser | None = None, container: Node | None = None) -> Literal[0]: ...
    @staticmethod
    def finalize(parser: Parser | None = None, block: Node | None = None) -> None: ...
    @staticmethod
    def can_contain(t: str) -> bool: ...

class BlockQuote(Block):
    accepts_lines: Literal[False]
    @staticmethod
    def continue_(parser: Parser | None = None, container: Node | None = None) -> Literal[0, 1]: ...
    @staticmethod
    def finalize(parser: Parser | None = None, block: Node | None = None) -> None: ...
    @staticmethod
    def can_contain(t: str) -> bool: ...

class Item(Block):
    accepts_lines: Literal[False]
    @staticmethod
    def continue_(parser: Parser | None = None, container: Node | None = None) -> Literal[0, 1]: ...
    @staticmethod
    def finalize(parser: Parser | None = None, block: Node | None = None) -> None: ...
    @staticmethod
    def can_contain(t: str) -> bool: ...

class Heading(Block):
    accepts_lines: Literal[False]
    @staticmethod
    def continue_(parser: Parser | None = None, container: Node | None = None) -> Literal[1]: ...
    @staticmethod
    def finalize(parser: Parser | None = None, block: Node | None = None) -> None: ...
    @staticmethod
    def can_contain(t: str) -> Literal[False]: ...

class ThematicBreak(Block):
    accepts_lines: Literal[False]
    @staticmethod
    def continue_(parser: Parser | None = None, container: Node | None = None) -> Literal[1]: ...
    @staticmethod
    def finalize(parser: Parser | None = None, block: Node | None = None) -> None: ...
    @staticmethod
    def can_contain(t: str) -> Literal[False]: ...

class CodeBlock(Block):
    accepts_lines: Literal[True]
    @staticmethod
    def continue_(parser: Parser | None = None, container: Node | None = None) -> Literal[0, 1, 2]: ...
    @staticmethod
    def finalize(parser: Parser | None = None, block: Node | None = None) -> None: ...
    @staticmethod
    def can_contain(t: str) -> Literal[False]: ...

class HtmlBlock(Block):
    accepts_lines: Literal[True]
    @staticmethod
    def continue_(parser: Parser | None = None, container: Node | None = None) -> Literal[0, 1]: ...
    @staticmethod
    def finalize(parser: Parser | None = None, block: Node | None = None) -> None: ...
    @staticmethod
    def can_contain(t: str) -> Literal[False]: ...

class Paragraph(Block):
    accepts_lines: Literal[True]
    @staticmethod
    def continue_(parser: Parser | None = None, container: Node | None = None) -> Literal[0, 1]: ...
    @staticmethod
    def finalize(parser: Parser | None = None, block: Node | None = None) -> None: ...
    @staticmethod
    def can_contain(t: str) -> Literal[False]: ...

class BlockStarts:
    """
    Block start functions.

    Return values:
    0 = no match
    1 = matched container, keep going
    2 = matched leaf, no more block starts
    """
    METHODS: list[str]
    @staticmethod
    def block_quote(parser: Parser, container: Node | None = None) -> Literal[0, 1]: ...
    @staticmethod
    def atx_heading(parser: Parser, container: Node | None = None) -> Literal[0, 2]: ...
    @staticmethod
    def fenced_code_block(parser: Parser, container: Node | None = None) -> Literal[0, 2]: ...
    @staticmethod
    def html_block(parser: Parser, container: Node | None = None) -> Literal[0, 2]: ...
    @staticmethod
    def setext_heading(parser: Parser, container: Node | None = None) -> Literal[0, 2]: ...
    @staticmethod
    def thematic_break(parser: Parser, container: Node | None = None) -> Literal[0, 2]: ...
    @staticmethod
    def list_item(parser: Parser, container: Node | None = None) -> Literal[0, 1]: ...
    @staticmethod
    def indented_code_block(parser: Parser, container: Node | None = None) -> Literal[0, 2]: ...

class Parser:
    doc: Node
    block_starts: BlockStarts
    tip: Node
    oldtip: Node
    current_line: str
    line_number: int
    offset: int
    column: int
    next_nonspace: int
    next_nonspace_column: int
    indent: int
    indented: bool
    blank: bool
    partially_consumed_tab: bool
    all_closed: bool
    last_matched_container: Node
    refmap: dict[str, Any]
    last_line_length: int
    inline_parser: InlineParser
    options: dict[str, Any]
    blocks: dict[str, Block]
    def __init__(self, options: dict[str, Any] = {}) -> None: ...
    def add_line(self) -> None:
        """
        Add a line to the block at the tip.  We assume the tip
        can accept lines -- that check should be done before calling this.
        """
        ...
    def add_child(self, tag: str, offset: int) -> Node:
        """
        Add block of type tag as a child of the tip.  If the tip can't
        accept children, close and finalize it and try its parent,
        and so on til we find a block that can accept children.
        """
        ...
    def close_unmatched_blocks(self) -> None:
        """Finalize and close any unmatched blocks."""
        ...
    def find_next_nonspace(self) -> None: ...
    def advance_next_nonspace(self) -> None: ...
    def advance_offset(self, count: int, columns: bool) -> None: ...
    def incorporate_line(self, ln: str) -> None:
        """
        Analyze a line of text and update the document appropriately.

        We parse markdown text by calling this on each line of input,
        then finalizing the document.
        """
        ...
    def finalize(self, block: Node, line_number: int) -> None:
        """
        Finalize a block.  Close it and do any necessary postprocessing,
        e.g. creating string_content from strings, setting the 'tight'
        or 'loose' status of a list, and parsing the beginnings
        of paragraphs for reference definitions.  Reset the tip to the
        parent of the closed block.
        """
        ...
    def process_inlines(self, block: Node) -> None:
        """
        Walk through a block & children recursively, parsing string content
        into inline content where appropriate.
        """
        ...
    def parse(self, my_input: str) -> Node:
        """The main parsing function.  Returns a parsed document AST."""
        ...

CAMEL_RE: Final[re.Pattern[str]]
