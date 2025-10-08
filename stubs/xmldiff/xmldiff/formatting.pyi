from _typeshed import Incomplete
from collections.abc import Generator
from typing import Final, NamedTuple

DIFF_NS: Final[str]
DIFF_PREFIX: Final[str]
INSERT_NAME: Final[Incomplete]
DELETE_NAME: Final[Incomplete]
REPLACE_NAME: Final[Incomplete]
RENAME_NAME: Final[Incomplete]
WS_BOTH: Final[int]
WS_TEXT: Final[int]
WS_TAGS: Final[int]
WS_NONE: Final[int]
T_OPEN: Final[int]
T_CLOSE: Final[int]
T_SINGLE: Final[int]
PLACEHOLDER_START: Final[int]

class BaseFormatter:
    def __init__(self, normalize=1, pretty_print: bool = False) -> None:
        """
        Formatters must as a minimum have a normalize parameter

        This is used by the main API to decide is whitespace between the
        tags should be stripped (the remove_blank_text flag in lxml) and
        if tags that are known texts tags should be normalized before
        comparing. String content in non-text tags will not be
        normalized with the included formatters.

        pretty_print is used to choose between a compact and a pretty output.
        This is currently only used by the XML and HTML formatters.

        Formatters may of course have more options than these, but these
        two are the ones that can be set from the command-line.
        """
        ...
    def prepare(self, left_tree, right_tree) -> None:
        """
        Allows the formatter to prepare the trees before diffing

        That preparing may need some "unpreparing", but it's then done
        by the formatters format() method, and is not a part of the
        public interface.
        """
        ...
    def format(self, diff, orig_tree) -> None:
        """
        Formats the diff and returns a unicode string

        A formatter that returns XML with diff markup will need the original
        tree available to do it's job, so there is an orig_tree parameter,
        but it may be ignored by differs that don't need it.
        """
        ...

class PlaceholderEntry(NamedTuple):
    """PlaceholderEntry(element, ttype, close_ph)"""
    element: Incomplete
    ttype: Incomplete
    close_ph: Incomplete

class PlaceholderMaker:
    """
    Replace tags with unicode placeholders

    This class searches for certain tags in an XML tree and replaces them
    with unicode placeholders. The idea is to replace structured content
    (in this case XML elements) with unicode characters which then
    participate in the regular text diffing algorithm. This makes text
    diffing easier and faster.

    The code can then unreplace the unicode placeholders with the tags.
    """
    text_tags: Incomplete
    formatting_tags: Incomplete
    placeholder2tag: Incomplete
    tag2placeholder: Incomplete
    placeholder: Incomplete
    diff_tags: Incomplete
    def __init__(self, text_tags=(), formatting_tags=()) -> None: ...
    def get_placeholder(self, element, ttype, close_ph): ...
    def is_placeholder(self, char): ...
    def is_formatting(self, element): ...
    def do_element(self, element) -> None: ...
    def do_tree(self, tree) -> None: ...
    def split_string(self, text): ...
    def undo_string(self, text): ...
    def undo_element(self, elem) -> None: ...
    def undo_tree(self, tree) -> None: ...
    def mark_diff(self, ph, action, attributes=None): ...
    def wrap_diff(self, text, action, attributes=None): ...

class XMLFormatter(BaseFormatter):
    """
    A formatter that also replaces formatting tags with unicode characters

    The idea of this differ is to replace structured content (in this case XML
    elements) with unicode characters which then participate in the regular
    text diffing algorithm. This is done in the prepare() step.

    Each identical XML element will get a unique unicode character. If the
    node is changed for any reason, a new unicode character is assigned to the
    node. This allows identity detection of structured content between the
    two text versions while still allowing customization during diffing time,
    such as marking a new formatting node. The latter feature allows for
    granular style change detection independently of text changes.

    In order for the algorithm to not go crazy and convert entire XML
    documents to text (though that is perfectly doable), a few rules have been
    defined.

    - The `textTags` attribute lists all the XML nodes by name which can
      contain text. All XML nodes within those text nodes are converted to
      unicode placeholders. If you want better control over which parts of
      your XML document are considered text, you can simply override the
      ``insert_placeholders(tree)`` function. It is purposefully kept small to
      allow easy subclassing.

    - By default, all tags inside text tags are treated as immutable
      units. That means the node itself including its entire sub-structure is
      assigned one unicode character.

    - The ``formattingTags`` attribute is used to specify tags that format the
      text. For these tags, the opening and closing tags receive unique
      unicode characters, allowing for sub-structure change detection and
      formatting changes. During the diff markup phase, formatting notes are
      annotated to mark them as inserted or deleted allowing for markup
      specific to those formatting changes.

    The diffed version of the structural tree is passed into the
    ``finalize(tree)`` method to convert all the placeholders back into
    structural content before formatting.

    The ``normalize`` parameter decides how to normalize whitespace.
    WS_TEXT normalizes only inside text_tags, WS_TAGS will remove ignorable
    whitespace between tags, WS_BOTH do both, and WS_NONE will preserve
    all whitespace.

    The ``use_replace`` flag decides, if a replace tag (with the old text
    as an attribute) should be used instead of one delete and one insert tag.
    """
    normalize: Incomplete
    pretty_print: Incomplete
    text_tags: Incomplete
    formatting_tags: Incomplete
    use_replace: Incomplete
    placeholderer: Incomplete
    def __init__(
        self, normalize=0, pretty_print: bool = True, text_tags=(), formatting_tags=(), use_replace: bool = False
    ) -> None: ...
    def prepare(self, left_tree, right_tree) -> None:
        """
        prepare() is run on the trees before diffing

        This is so the formatter can apply magic before diffing.
        """
        ...
    def finalize(self, result_tree) -> None:
        """
        finalize() is run on the resulting tree before returning it

        This is so the formatter cab apply magic after diffing.
        """
        ...
    def format(self, diff, orig_tree, differ=None): ...
    def render(self, result): ...
    def handle_action(self, action, result) -> None: ...

class DiffFormatter(BaseFormatter):
    normalize: Incomplete
    def __init__(self, normalize=1, pretty_print: bool = False) -> None: ...
    def prepare(self, left, right) -> None: ...
    def finalize(self, left, right) -> None: ...
    def format(self, diff, orig_tree): ...
    def handle_action(self, action): ...

class XmlDiffFormatter(BaseFormatter):
    """A formatter for an output trying to be xmldiff 0.6 compatible"""
    normalize: Incomplete
    def __init__(self, normalize=1, pretty_print: bool = False) -> None: ...
    def prepare(self, left, right) -> None: ...
    def finalize(self, left, right) -> None: ...
    def format(self, diff, orig_tree): ...
    def handle_action(self, action, orig_tree) -> Generator[Incomplete, Incomplete]: ...
