"""
This is the ``docutils.parsers.rst.states`` module, the core of
the reStructuredText parser.  It defines the following:

:Classes:
    - `RSTStateMachine`: reStructuredText parser's entry point.
    - `NestedStateMachine`: recursive StateMachine.
    - `RSTState`: reStructuredText State superclass.
    - `Inliner`: For parsing inline markup.
    - `Body`: Generic classifier of the first line of a block.
    - `SpecializedBody`: Superclass for compound element members.
    - `BulletList`: Second and subsequent bullet_list list_items
    - `DefinitionList`: Second+ definition_list_items.
    - `EnumeratedList`: Second+ enumerated_list list_items.
    - `FieldList`: Second+ fields.
    - `OptionList`: Second+ option_list_items.
    - `RFC2822List`: Second+ RFC2822-style fields.
    - `ExtensionOptions`: Parses directive option fields.
    - `Explicit`: Second+ explicit markup constructs.
    - `SubstitutionDef`: For embedded directives in substitution definitions.
    - `Text`: Classifier of second line of a text block.
    - `SpecializedText`: Superclass for continuation lines of Text-variants.
    - `Definition`: Second line of potential definition_list_item.
    - `Line`: Second line of overlined section title or transition marker.
    - `Struct`: An auxiliary collection class.

:Exception classes:
    - `MarkupError`
    - `ParserError`
    - `MarkupMismatch`

:Functions:
    - `escape2null()`: Return a string, escape-backslashes converted to nulls.
    - `unescape()`: Return a string, nulls removed or restored to backslashes.

:Attributes:
    - `state_classes`: set of State classes used with `RSTStateMachine`.

Parser Overview
===============

The reStructuredText parser is implemented as a recursive state machine,
examining its input one line at a time.  To understand how the parser works,
please first become familiar with the `docutils.statemachine` module.  In the
description below, references are made to classes defined in this module;
please see the individual classes for details.

Parsing proceeds as follows:

1. The state machine examines each line of input, checking each of the
   transition patterns of the state `Body`, in order, looking for a match.
   The implicit transitions (blank lines and indentation) are checked before
   any others.  The 'text' transition is a catch-all (matches anything).

2. The method associated with the matched transition pattern is called.

   A. Some transition methods are self-contained, appending elements to the
      document tree (`Body.doctest` parses a doctest block).  The parser's
      current line index is advanced to the end of the element, and parsing
      continues with step 1.

   B. Other transition methods trigger the creation of a nested state machine,
      whose job is to parse a compound construct ('indent' does a block quote,
      'bullet' does a bullet list, 'overline' does a section [first checking
      for a valid section header], etc.).

      - In the case of lists and explicit markup, a one-off state machine is
        created and run to parse contents of the first item.

      - A new state machine is created and its initial state is set to the
        appropriate specialized state (`BulletList` in the case of the
        'bullet' transition; see `SpecializedBody` for more detail).  This
        state machine is run to parse the compound element (or series of
        explicit markup elements), and returns as soon as a non-member element
        is encountered.  For example, the `BulletList` state machine ends as
        soon as it encounters an element which is not a list item of that
        bullet list.  The optional omission of inter-element blank lines is
        enabled by this nested state machine.

      - The current line index is advanced to the end of the elements parsed,
        and parsing continues with step 1.

   C. The result of the 'text' transition depends on the next line of text.
      The current state is changed to `Text`, under which the second line is
      examined.  If the second line is:

      - Indented: The element is a definition list item, and parsing proceeds
        similarly to step 2.B, using the `DefinitionList` state.

      - A line of uniform punctuation characters: The element is a section
        header; again, parsing proceeds as in step 2.B, and `Body` is still
        used.

      - Anything else: The element is a paragraph, which is examined for
        inline markup and appended to the parent element.  Processing
        continues with step 1.
"""

from _typeshed import Incomplete
from collections.abc import Callable, Iterable, Sequence
from re import Match, Pattern
from types import ModuleType
from typing import Any, ClassVar, Final, NoReturn
from typing_extensions import TypeAlias

from docutils import ApplicationError, DataError, nodes
from docutils.parsers.rst.languages import _RstLanguageModule
from docutils.statemachine import StateMachine, StateMachineWS, StateWS, StringList
from docutils.utils import Reporter

__docformat__: Final = "reStructuredText"

class MarkupError(DataError): ...
class UnknownInterpretedRoleError(DataError): ...
class InterpretedRoleNotImplementedError(DataError): ...
class ParserError(ApplicationError): ...
class MarkupMismatch(Exception): ...

class Struct:
    """Stores data attributes for dotted-attribute access."""
    def __init__(self, **keywordargs) -> None: ...

class RSTStateMachine(StateMachineWS[list[str]]):
    language: _RstLanguageModule
    match_titles: bool
    memo: Struct | None
    document: nodes.document
    reporter: Reporter
    node: nodes.document | None
    def run(  # type: ignore[override]
        self,
        input_lines: Sequence[str] | StringList,
        document: nodes.document,
        input_offset: int = 0,
        match_titles: bool = True,
        inliner: Inliner | None = None,
    ) -> None: ...

class NestedStateMachine(StateMachineWS[list[str]]):
    match_titles: bool
    memo: Incomplete
    document: nodes.document
    reporter: Reporter
    language: Incomplete
    node: Incomplete
    def run(  # type: ignore[override]
        self, input_lines: Sequence[str] | StringList, input_offset: int, memo, node, match_titles: bool = True
    ) -> list[str]: ...

class RSTState(StateWS[list[str]]):
    nested_sm: type[NestedStateMachine]
    nested_sm_cache: list[StateMachine[Incomplete]]
    def __init__(self, state_machine, debug: bool = False) -> None: ...
    memo: Incomplete
    reporter: Reporter
    inliner: Inliner
    document: nodes.document
    parent: Incomplete
    def runtime_init(self) -> None: ...
    def goto_line(self, abs_line_offset: int) -> None:
        """Jump to input line `abs_line_offset`, ignoring jumps past the end."""
        ...
    def no_match(self, context: list[str], transitions):
        """
        Override `StateWS.no_match` to generate a system message.

        This code should never be run.
        """
        ...
    def bof(self, context: list[str]):
        """Called at beginning of file."""
        ...
    def nested_parse(
        self,
        block,
        input_offset: int,
        node,
        match_titles: bool = False,
        state_machine_class: type[StateMachine[list[str]]] | None = None,
        state_machine_kwargs=None,
    ):
        """
        Create a new StateMachine rooted at `node` and run it over the input
        `block`.
        """
        ...
    def nested_list_parse(
        self,
        block,
        input_offset: int,
        node,
        initial_state,
        blank_finish,
        blank_finish_state=None,
        extra_settings={},
        match_titles: bool = False,
        state_machine_class=None,
        state_machine_kwargs=None,
    ):
        """
        Create a new StateMachine rooted at `node` and run it over the input
        `block`. Also keep track of optional intermediate blank lines and the
        required final one.
        """
        ...
    def section(self, title: str, source, style, lineno: int, messages) -> None:
        """Check for a valid subsection and create one if it checks out."""
        ...
    def check_subsection(self, source, style, lineno: int):
        """
        Check for a valid subsection header.  Return True or False.

        When a new section is reached that isn't a subsection of the current
        section, back up the line count (use ``previous_line(-x)``), then
        ``raise EOFError``.  The current StateMachine will finish, then the
        calling StateMachine can re-examine the title.  This will work its way
        back up the calling chain until the correct section level isreached.

        @@@ Alternative: Evaluate the title, store the title info & level, and
        back up the chain until that level is reached.  Store in memo? Or
        return in results?

        :Exception: `EOFError` when a sibling or supersection encountered.
        """
        ...
    def title_inconsistent(self, sourcetext: str, lineno: int): ...
    def new_subsection(self, title: str, lineno: int, messages) -> None:
        """Append new subsection to document tree. On return, check level."""
        ...
    def paragraph(self, lines: Iterable[str], lineno: int):
        """Return a list (paragraph & messages) & a boolean: literal_block next?"""
        ...
    def inline_text(self, text: str, lineno: int):
        """Return 2 lists: nodes (text and inline elements), and system_messages."""
        ...
    def unindent_warning(self, node_name: str): ...

def build_regexp(definition, compile: bool = True):
    """
    Build, compile and return a regular expression based on `definition`.

    :Parameter: `definition`: a 4-tuple (group name, prefix, suffix, parts),
        where "parts" is a list of regular expressions and/or regular
        expression definitions to be joined into an or-group.
    """
    ...

_BasicDefinition: TypeAlias = tuple[str, str, str, list[Pattern[str]]]
_DefinitionParts: TypeAlias = tuple[str, str, str, list[Pattern[str] | _BasicDefinition]]
_DefinitionType: TypeAlias = tuple[str, str, str, list[Pattern[str] | _DefinitionParts]]

class Inliner:
    """Parse inline markup; call the `parse()` method."""
    implicit_dispatch: list[tuple[Pattern[str], Callable[[Match[str], int], Sequence[nodes.Node]]]]
    def __init__(self) -> None: ...
    start_string_prefix: str
    end_string_suffix: str
    parts: _DefinitionType
    patterns: Struct
    def init_customizations(self, settings: Any) -> None: ...
    reporter: Reporter
    document: nodes.document
    language: ModuleType
    parent: nodes.Element
    def parse(
        self, text: str, lineno: int, memo: Struct, parent: nodes.Element
    ) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        """
        Return 2 lists: nodes (text and inline elements), and system_messages.

        Using `self.patterns.initial`, a pattern which matches start-strings
        (emphasis, strong, interpreted, phrase reference, literal,
        substitution reference, and inline target) and complete constructs
        (simple reference, footnote reference), search for a candidate.  When
        one is found, check for validity (e.g., not a quoted '*' character).
        If valid, search for the corresponding end string if applicable, and
        check it for validity.  If not found or invalid, generate a warning
        and ignore the start-string.  Implicit inline markup (e.g. standalone
        URIs) is found last.

        :text: source string
        :lineno: absolute line number (cf. statemachine.get_source_and_line())
        """
        ...
    non_whitespace_before: str
    non_whitespace_escape_before: str
    non_unescaped_whitespace_escape_before: str
    non_whitespace_after: str
    simplename: str
    uric: str
    uri_end_delim: str
    urilast: str
    uri_end: str
    emailc: str
    email_pattern: str
    def quoted_start(self, match: Match[str]) -> bool:
        """
        Test if inline markup start-string is 'quoted'.

        'Quoted' in this context means the start-string is enclosed in a pair
        of matching opening/closing delimiters (not necessarily quotes)
        or at the end of the match.
        """
        ...
    def inline_obj(
        self,
        match: Match[str],
        lineno: int,
        end_pattern: Pattern[str],
        nodeclass: nodes.TextElement,
        restore_backslashes: bool = False,
    ) -> tuple[str, list[nodes.problematic], str, list[nodes.system_message], str]: ...
    def problematic(self, text: str, rawsource: str, message: nodes.system_message) -> nodes.problematic: ...
    def emphasis(
        self, match: Match[str], lineno: int
    ) -> tuple[str, list[nodes.problematic], str, list[nodes.system_message]]: ...
    def strong(self, match: Match[str], lineno: int) -> tuple[str, list[nodes.problematic], str, list[nodes.system_message]]: ...
    def interpreted_or_phrase_ref(
        self, match: Match[str], lineno: int
    ) -> tuple[str, list[nodes.problematic], str, list[nodes.system_message]]: ...
    def phrase_ref(
        self, before: str, after: str, rawsource: str, escaped: str, text: str | None = None
    ) -> tuple[str, list[nodes.Node], str, list[nodes.Node]]: ...
    def adjust_uri(self, uri: str) -> str: ...
    def interpreted(
        self, rawsource: str, text: str, role: str, lineno: int
    ) -> tuple[list[nodes.Node], list[nodes.system_message]]: ...
    def literal(self, match: Match[str], lineno: int) -> tuple[str, list[nodes.problematic], str, list[nodes.system_message]]: ...
    def inline_internal_target(
        self, match: Match[str], lineno: int
    ) -> tuple[str, list[nodes.problematic], str, list[nodes.system_message]]: ...
    def substitution_reference(
        self, match: Match[str], lineno: int
    ) -> tuple[str, list[nodes.problematic], str, list[nodes.system_message]]: ...
    def footnote_reference(
        self, match: Match[str], lineno: int
    ) -> tuple[str, list[nodes.problematic], str, list[nodes.system_message]]:
        """
        Handles `nodes.footnote_reference` and `nodes.citation_reference`
        elements.
        """
        ...
    def reference(
        self, match: Match[str], lineno: int, anonymous: bool = False
    ) -> tuple[str, list[nodes.problematic], str, list[nodes.system_message]]: ...
    def anonymous_reference(
        self, match: Match[str], lineno: int
    ) -> tuple[str, list[nodes.problematic], str, list[nodes.system_message]]: ...
    def standalone_uri(
        self, match: Match[str], lineno: int
    ) -> list[tuple[str, list[nodes.problematic], str, list[nodes.system_message]]]: ...
    def pep_reference(
        self, match: Match[str], lineno: int
    ) -> list[tuple[str, list[nodes.problematic], str, list[nodes.system_message]]]: ...
    rfc_url: str = ...
    def rfc_reference(
        self, match: Match[str], lineno: int
    ) -> list[tuple[str, list[nodes.problematic], str, list[nodes.system_message]]]: ...
    def implicit_inline(self, text: str, lineno: int) -> list[nodes.Text]:
        """
        Check each of the patterns in `self.implicit_dispatch` for a match,
        and dispatch to the stored method for the pattern.  Recursively check
        the text before and after the match.  Return a list of `nodes.Text`
        and inline element nodes.
        """
        ...
    dispatch: dict[str, Callable[[Match[str], int], tuple[str, list[nodes.problematic], str, list[nodes.system_message]]]] = ...

class Body(RSTState):
    double_width_pad_char: Incomplete
    enum: Incomplete
    grid_table_top_pat: Incomplete
    simple_table_top_pat: Incomplete
    simple_table_border_pat: Incomplete
    pats: Incomplete
    patterns: ClassVar[dict[str, str | Pattern[str]]]
    initial_transitions: ClassVar[tuple[str, ...]]
    def indent(self, match, context, next_state): ...
    def block_quote(self, indented, line_offset): ...
    attribution_pattern: Incomplete
    def split_attribution(self, indented, line_offset): ...
    def check_attribution(self, indented, attribution_start): ...
    def parse_attribution(self, indented, line_offset): ...
    def bullet(self, match, context, next_state): ...
    def list_item(self, indent): ...
    def enumerator(self, match, context, next_state): ...
    def parse_enumerator(self, match, expected_sequence=None): ...
    def is_enumerated_list_item(self, ordinal, sequence, format): ...
    def make_enumerator(self, ordinal, sequence, format): ...
    def field_marker(self, match, context, next_state): ...
    def field(self, match): ...
    def parse_field_marker(self, match): ...
    def parse_field_body(self, indented, offset, node) -> None: ...
    def option_marker(self, match, context, next_state): ...
    def option_list_item(self, match): ...
    def parse_option_marker(self, match): ...
    def doctest(self, match, context, next_state): ...
    def line_block(self, match, context, next_state): ...
    def line_block_line(self, match, lineno): ...
    def nest_line_block_lines(self, block) -> None: ...
    def nest_line_block_segment(self, block) -> None: ...
    def grid_table_top(self, match, context, next_state): ...
    def simple_table_top(self, match, context, next_state): ...
    def table_top(self, match, context, next_state, isolate_function, parser_class): ...
    def table(self, isolate_function, parser_class): ...
    def isolate_grid_table(self): ...
    def isolate_simple_table(self): ...
    def malformed_table(self, block, detail: str = "", offset: int = 0): ...
    def build_table(self, tabledata, tableline, stub_columns: int = 0, widths=None): ...
    def build_table_row(self, rowdata, tableline): ...
    explicit: Incomplete
    def footnote(self, match): ...
    def citation(self, match): ...
    def hyperlink_target(self, match): ...
    def make_target(self, block, block_text, lineno, target_name): ...
    def parse_target(self, block, block_text, lineno): ...
    def is_reference(self, reference): ...
    def add_target(self, targetname, refuri, target, lineno) -> None: ...
    def substitution_def(self, match): ...
    def disallowed_inside_substitution_definitions(self, node): ...
    def directive(self, match, **option_presets): ...
    def run_directive(self, directive, match, type_name, option_presets): ...
    def parse_directive_block(self, indented, line_offset, directive, option_presets): ...
    def parse_directive_options(self, option_presets, option_spec, arg_block): ...
    def parse_directive_arguments(self, directive, arg_block): ...
    def parse_extension_options(self, option_spec, datalines): ...
    def unknown_directive(self, type_name): ...
    def comment(self, match): ...
    def explicit_markup(self, match, context, next_state): ...
    def explicit_construct(self, match): ...
    def explicit_list(self, blank_finish) -> None: ...
    def anonymous(self, match: Match[str], context: list[str] | None, next_state: str): ...
    def anonymous_target(self, match): ...
    def line(self, match, context, next_state): ...
    def text(self, match, context, next_state): ...

class RFC2822Body(Body):
    patterns: ClassVar[dict[str, str | Pattern[str]]]
    initial_transitions: ClassVar[list[tuple[str | tuple[str, str], str]]]  # type: ignore[assignment]
    def rfc2822(self, match, context, next_state): ...
    def rfc2822_field(self, match): ...

class SpecializedBody(Body):
    def invalid_input(
        self, match: Match[str] | None = None, context: list[str] | None = None, next_state: str | None = None
    ) -> NoReturn: ...
    indent = invalid_input  # type: ignore[assignment]
    bullet = invalid_input
    enumerator = invalid_input
    field_marker = invalid_input
    option_marker = invalid_input
    doctest = invalid_input
    line_block = invalid_input
    grid_table_top = invalid_input
    simple_table_top = invalid_input
    explicit_markup = invalid_input
    anonymous = invalid_input  # type: ignore[assignment]
    line = invalid_input
    text = invalid_input

class BulletList(SpecializedBody):
    blank_finish: Incomplete
    def bullet(  # type: ignore[override]
        self, match: Match[str], context: list[str] | None, next_state: str | None
    ) -> tuple[list[str], str | None, list[str]]: ...

class DefinitionList(SpecializedBody):
    def text(self, match: Match[str], context: list[str] | None, next_state: str | None) -> tuple[list[str], str, list[str]]: ...  # type: ignore[override]

class EnumeratedList(SpecializedBody):
    auto: int
    blank_finish: Incomplete
    lastordinal: Incomplete
    def enumerator(  # type: ignore[override]
        self, match: Match[str], context: list[str] | None, next_state: str | None
    ) -> tuple[list[str], str | None, list[str]]: ...

class FieldList(SpecializedBody):
    blank_finish: Incomplete
    def field_marker(  # type: ignore[override]
        self, match: Match[str], context: list[str] | None, next_state: str | None
    ) -> tuple[list[str], str | None, list[str]]: ...

class OptionList(SpecializedBody):
    blank_finish: Incomplete
    def option_marker(  # type: ignore[override]
        self, match: Match[str], context: list[str] | None, next_state: str | None
    ) -> tuple[list[str], str | None, list[str]]: ...

class RFC2822List(SpecializedBody, RFC2822Body):
    patterns: ClassVar[dict[str, str | Pattern[str]]]
    initial_transitions: ClassVar[list[tuple[str | tuple[str, str], str]]]  # type: ignore[assignment]
    blank_finish: Incomplete
    def rfc2822(self, match, context, next_state): ...
    blank: Incomplete

class ExtensionOptions(FieldList):
    def parse_field_body(self, indented, offset, node) -> None: ...

class LineBlock(SpecializedBody):
    blank: Incomplete
    blank_finish: Incomplete
    def line_block(  # type: ignore[override]
        self, match: Match[str], context: list[str] | None, next_state: str | None
    ) -> tuple[list[str], str | None, list[str]]: ...

class Explicit(SpecializedBody):
    blank_finish: Incomplete
    blank: Incomplete
    def explicit_markup(  # type: ignore[override]
        self, match: Match[str], context: list[str] | None, next_state: str | None
    ) -> tuple[list[str], str | None, list[str]]: ...
    def anonymous(  # type: ignore[override]
        self, match: Match[str], context: list[str] | None, next_state: str | None
    ) -> tuple[list[str], str | None, list[str]]: ...

class SubstitutionDef(Body):
    patterns: ClassVar[dict[str, str | Pattern[str]]]
    initial_transitions: ClassVar[list[str]]  # type: ignore[assignment]
    blank_finish: Incomplete
    def embedded_directive(self, match, context, next_state) -> None: ...
    def text(self, match, context, next_state) -> None: ...

class Text(RSTState):
    patterns: ClassVar[dict[str, str | Pattern[str]]]
    initial_transitions: ClassVar[list[tuple[str, str]]]
    def blank(self, match, context, next_state): ...
    def eof(self, context): ...
    def indent(self, match, context, next_state): ...
    def underline(self, match, context, next_state): ...
    def text(self, match, context, next_state): ...
    def literal_block(self): ...
    def quoted_literal_block(self): ...
    def definition_list_item(self, termline): ...
    classifier_delimiter: Incomplete
    def term(self, lines, lineno): ...

class SpecializedText(Text):
    def eof(self, context): ...
    def invalid_input(
        self, match: Match[str] | None = None, context: list[str] | None = None, next_state: str | None = None
    ) -> NoReturn: ...
    blank = invalid_input
    indent = invalid_input
    underline = invalid_input
    text = invalid_input

class Definition(SpecializedText):
    def eof(self, context): ...
    blank_finish: Incomplete
    def indent(  # type: ignore[override]
        self, match: Match[str] | None, context: list[str], next_state: str | None
    ) -> tuple[list[str], str, list[str]]: ...

class Line(SpecializedText):
    eofcheck: int
    def eof(self, context: list[str]): ...
    def blank(self, match: Match[str] | None, context: list[str], next_state: str | None) -> tuple[list[str], str, list[str]]: ...  # type: ignore[override]
    def text(self, match: Match[str], context: list[str], next_state: str | None) -> tuple[list[str], str, list[str]]: ...  # type: ignore[override]
    indent = text  # type: ignore[assignment]
    def underline(  # type: ignore[override]
        self, match: Match[str] | None, context: list[str], next_state: str | None
    ) -> tuple[list[str], str, list[str]]: ...
    def short_overline(self, context, blocktext, lineno, lines: int = 1) -> None: ...
    def state_correction(self, context, lines: int = 1) -> None: ...

class QuotedLiteralBlock(RSTState):
    patterns: ClassVar[dict[str, str | Pattern[str]]]
    messages: Incomplete
    initial_lineno: Incomplete
    def __init__(self, state_machine, debug: bool = False) -> None: ...
    def blank(self, match, context, next_state): ...
    def eof(self, context): ...
    def indent(self, match: Match[str] | None, context: list[str], next_state: str | None) -> NoReturn: ...
    def initial_quoted(
        self, match: Match[str], context: list[str] | None, next_state: str | None
    ) -> tuple[list[str], str | None, list[str]]: ...
    def quoted(
        self, match: Match[str], context: list[str], next_state: str | None
    ) -> tuple[list[str], str | None, list[str]]: ...
    def text(self, match: Match[str] | None, context: list[str] | None, next_state: str | None) -> None: ...

state_classes: tuple[type[RSTState], ...]
