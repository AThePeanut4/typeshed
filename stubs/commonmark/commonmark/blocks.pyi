from _typeshed import Incomplete
from typing import Any

CODE_INDENT: int
reHtmlBlockOpen: Any
reHtmlBlockClose: Any
reThematicBreak: Any
reMaybeSpecial: Any
reNonSpace: Any
reBulletListMarker: Any
reOrderedListMarker: Any
reATXHeadingMarker: Any
reCodeFence: Any
reClosingCodeFence: Any
reSetextHeadingLine: Any
reLineEnding: Any

def is_blank(s):
    """Returns True if string contains only space characters."""
    ...
def is_space_or_tab(s): ...
def peek(ln, pos): ...
def ends_with_blank_line(block):
    """
    Returns true if block ends with a blank line,
    descending if needed into lists and sublists.
    """
    ...
def parse_list_marker(parser, container):
    """
    Parse a list marker and return data on the marker (type,
    start, delimiter, bullet character, padding) or None.
    """
    ...
def lists_match(list_data, item_data):
    """
    Returns True if the two list items are of the same type,
    with the same delimiter and bullet character.  This is used
    in agglomerating list items into lists.
    """
    ...

class Block:
    accepts_lines: Any
    @staticmethod
    def continue_(parser: Incomplete | None = ..., container: Incomplete | None = ...) -> None: ...
    @staticmethod
    def finalize(parser: Incomplete | None = ..., block: Incomplete | None = ...) -> None: ...
    @staticmethod
    def can_contain(t) -> None: ...

class Document(Block):
    accepts_lines: bool
    @staticmethod
    def continue_(parser: Incomplete | None = ..., container: Incomplete | None = ...): ...
    @staticmethod
    def finalize(parser: Incomplete | None = ..., block: Incomplete | None = ...) -> None: ...
    @staticmethod
    def can_contain(t): ...

class List(Block):
    accepts_lines: bool
    @staticmethod
    def continue_(parser: Incomplete | None = ..., container: Incomplete | None = ...): ...
    @staticmethod
    def finalize(parser: Incomplete | None = ..., block: Incomplete | None = ...) -> None: ...
    @staticmethod
    def can_contain(t): ...

class BlockQuote(Block):
    accepts_lines: bool
    @staticmethod
    def continue_(parser: Incomplete | None = ..., container: Incomplete | None = ...): ...
    @staticmethod
    def finalize(parser: Incomplete | None = ..., block: Incomplete | None = ...) -> None: ...
    @staticmethod
    def can_contain(t): ...

class Item(Block):
    accepts_lines: bool
    @staticmethod
    def continue_(parser: Incomplete | None = ..., container: Incomplete | None = ...): ...
    @staticmethod
    def finalize(parser: Incomplete | None = ..., block: Incomplete | None = ...) -> None: ...
    @staticmethod
    def can_contain(t): ...

class Heading(Block):
    accepts_lines: bool
    @staticmethod
    def continue_(parser: Incomplete | None = ..., container: Incomplete | None = ...): ...
    @staticmethod
    def finalize(parser: Incomplete | None = ..., block: Incomplete | None = ...) -> None: ...
    @staticmethod
    def can_contain(t): ...

class ThematicBreak(Block):
    accepts_lines: bool
    @staticmethod
    def continue_(parser: Incomplete | None = ..., container: Incomplete | None = ...): ...
    @staticmethod
    def finalize(parser: Incomplete | None = ..., block: Incomplete | None = ...) -> None: ...
    @staticmethod
    def can_contain(t): ...

class CodeBlock(Block):
    accepts_lines: bool
    @staticmethod
    def continue_(parser: Incomplete | None = ..., container: Incomplete | None = ...): ...
    @staticmethod
    def finalize(parser: Incomplete | None = ..., block: Incomplete | None = ...) -> None: ...
    @staticmethod
    def can_contain(t): ...

class HtmlBlock(Block):
    accepts_lines: bool
    @staticmethod
    def continue_(parser: Incomplete | None = ..., container: Incomplete | None = ...): ...
    @staticmethod
    def finalize(parser: Incomplete | None = ..., block: Incomplete | None = ...) -> None: ...
    @staticmethod
    def can_contain(t): ...

class Paragraph(Block):
    accepts_lines: bool
    @staticmethod
    def continue_(parser: Incomplete | None = ..., container: Incomplete | None = ...): ...
    @staticmethod
    def finalize(parser: Incomplete | None = ..., block: Incomplete | None = ...) -> None: ...
    @staticmethod
    def can_contain(t): ...

class BlockStarts:
    """
    Block start functions.

    Return values:
    0 = no match
    1 = matched container, keep going
    2 = matched leaf, no more block starts
    """
    METHODS: Any
    @staticmethod
    def block_quote(parser, container: Incomplete | None = ...): ...
    @staticmethod
    def atx_heading(parser, container: Incomplete | None = ...): ...
    @staticmethod
    def fenced_code_block(parser, container: Incomplete | None = ...): ...
    @staticmethod
    def html_block(parser, container: Incomplete | None = ...): ...
    @staticmethod
    def setext_heading(parser, container: Incomplete | None = ...): ...
    @staticmethod
    def thematic_break(parser, container: Incomplete | None = ...): ...
    @staticmethod
    def list_item(parser, container: Incomplete | None = ...): ...
    @staticmethod
    def indented_code_block(parser, container: Incomplete | None = ...): ...

class Parser:
    doc: Any
    block_starts: Any
    tip: Any
    oldtip: Any
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
    last_matched_container: Any
    refmap: Any
    last_line_length: int
    inline_parser: Any
    options: Any
    def __init__(self, options=...) -> None: ...
    def add_line(self) -> None:
        """
        Add a line to the block at the tip.  We assume the tip
        can accept lines -- that check should be done before calling this.
        """
        ...
    def add_child(self, tag, offset):
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
    def advance_offset(self, count, columns) -> None: ...
    def incorporate_line(self, ln) -> None:
        """
        Analyze a line of text and update the document appropriately.

        We parse markdown text by calling this on each line of input,
        then finalizing the document.
        """
        ...
    def finalize(self, block, line_number) -> None:
        """
        Finalize a block.  Close it and do any necessary postprocessing,
        e.g. creating string_content from strings, setting the 'tight'
        or 'loose' status of a list, and parsing the beginnings
        of paragraphs for reference definitions.  Reset the tip to the
        parent of the closed block.
        """
        ...
    def process_inlines(self, block) -> None:
        """
        Walk through a block & children recursively, parsing string content
        into inline content where appropriate.
        """
        ...
    def parse(self, my_input):
        """The main parsing function.  Returns a parsed document AST."""
        ...

CAMEL_RE: Any
