"""Miscellaneous utilities for the documentation utilities."""

import optparse
from _typeshed import StrPath, SupportsWrite
from collections.abc import Callable, Iterable, Mapping, Sequence
from re import Pattern
from typing import Any, Final, Literal, TypeVar
from typing_extensions import TypeAlias, deprecated

from docutils import ApplicationError, DataError, nodes
from docutils.frontend import Values
from docutils.io import ErrorOutput, FileOutput
from docutils.nodes import document, unescape as unescape

_T = TypeVar("_T")
_Observer: TypeAlias = Callable[[nodes.system_message], object]
_SystemMessageLevel: TypeAlias = Literal[0, 1, 2, 3, 4]

__docformat__: Final = "reStructuredText"

class DependencyList:
    """
    List of dependencies, with file recording support.

    Note that the output file is not automatically closed.  You have
    to explicitly call the close() method.
    """
    list: list[str]
    file: FileOutput | None
    def __init__(self, output_file: str | None = None, dependencies: Iterable[str] = ()) -> None:
        """
        Initialize the dependency list, automatically setting the
        output file to `output_file` (see `set_output()`) and adding
        all supplied dependencies.

        If output_file is None, no file output is done when calling add().
        """
        ...
    def set_output(self, output_file: str | None) -> None:
        """
        Set the output file and clear the list of already added
        dependencies.

        `output_file` must be a string.  The specified file is
        immediately overwritten.

        If output_file is '-', the output will be written to stdout.
        """
        ...
    def add(self, *paths: str) -> None:
        """
        Append `path` to `self.list` unless it is already there.

        Also append to `self.file` unless it is already there
        or `self.file is `None`.
        """
        ...
    def close(self) -> None:
        """Close the output file."""
        ...

class SystemMessagePropagation(ApplicationError): ...

class Reporter:
    get_source_and_line: Callable[[int | None], tuple[StrPath | None, int | None]]
    levels: Final[Sequence[str]]

    DEBUG_LEVEL: Final = 0
    INFO_LEVEL: Final = 1
    WARNING_LEVEL: Final = 2
    ERROR_LEVEL: Final = 3
    SEVERE_LEVEL: Final = 4

    stream: ErrorOutput
    encoding: str
    observers: list[_Observer]
    max_level: int
    def __init__(
        self,
        source: str,
        report_level: int,
        halt_level: int,
        stream: SupportsWrite[str] | SupportsWrite[bytes] | str | bool | None = None,
        debug: bool = False,
        encoding: str | None = None,
        error_handler: str = "backslashreplace",
    ) -> None:
        """
        :Parameters:
            - `source`: The path to or description of the source data.
            - `report_level`: The level at or above which warning output will
              be sent to `stream`.
            - `halt_level`: The level at or above which `SystemMessage`
              exceptions will be raised, halting execution.
            - `debug`: Show debug (level=0) system messages?
            - `stream`: Where warning output is sent.  Can be file-like (has a
              ``.write`` method), a string (file name, opened for writing),
              '' (empty string) or `False` (for discarding all stream messages)
              or `None` (implies `sys.stderr`; default).
            - `encoding`: The output encoding.
            - `error_handler`: The error handler for stderr output encoding.
        """
        ...

    source: str
    error_handler: str
    debug_flag: bool
    report_level: _SystemMessageLevel
    halt_level: int
    def attach_observer(self, observer: _Observer) -> None: ...
    def detach_observer(self, observer: _Observer) -> None: ...
    def notify_observers(self, message: nodes.system_message) -> None: ...
    def system_message(
        self,
        level: int,
        message: str | Exception,
        *children: nodes.Node,
        base_node: nodes.Node = ...,
        source: str = ...,
        **kwargs,
    ) -> nodes.system_message:
        """
        Return a system_message object.

        Raise an exception or generate a warning if appropriate.
        """
        ...
    def debug(
        self, message: str | Exception, *children: nodes.Node, base_node: nodes.Node = ..., source: str = ..., **kwargs
    ) -> nodes.system_message:
        """
        Level-0, "DEBUG": an internal reporting issue. Typically, there is no
        effect on the processing. Level-0 system messages are handled
        separately from the others.
        """
        ...
    def info(
        self, message: str | Exception, *children: nodes.Node, base_node: nodes.Node = ..., source: str = ..., **kwargs
    ) -> nodes.system_message:
        """
        Level-1, "INFO": a minor issue that can be ignored. Typically there is
        no effect on processing, and level-1 system messages are not reported.
        """
        ...
    def warning(
        self, message: str | Exception, *children: nodes.Node, base_node: nodes.Node = ..., source: str = ..., **kwargs
    ) -> nodes.system_message:
        """
        Level-2, "WARNING": an issue that should be addressed. If ignored,
        there may be unpredictable problems with the output.
        """
        ...
    def error(
        self, message: str | Exception, *children: nodes.Node, base_node: nodes.Node = ..., source: str = ..., **kwargs
    ) -> nodes.system_message:
        """
        Level-3, "ERROR": an error that should be addressed. If ignored, the
        output will contain errors.
        """
        ...
    def severe(
        self, message: str | Exception, *children: nodes.Node, base_node: nodes.Node = ..., source: str = ..., **kwargs
    ) -> nodes.system_message:
        """
        Level-4, "SEVERE": a severe error that must be addressed. If ignored,
        the output will contain severe errors. Typically level-4 system
        messages are turned into exceptions which halt processing.
        """
        ...

class SystemMessage(ApplicationError):
    level: _SystemMessageLevel
    def __init__(self, system_message: object, level: _SystemMessageLevel): ...

def new_reporter(source_path: str, settings: optparse.Values) -> Reporter:
    """
    Return a new Reporter object.

    :Parameters:
        `source` : string
            The path to or description of the source text of the document.
        `settings` : optparse.Values object
            Runtime settings.
    """
    ...
def new_document(source_path: str, settings: optparse.Values | None = None) -> document:
    """
    Return a new empty document object.

    :Parameters:
        `source_path` : string
            The path to or description of the source text of the document.
        `settings` : optparse.Values object
            Runtime settings.  If none are provided, a default core set will
            be used.  If you will use the document object with any Docutils
            components, you must provide their default settings as well.

            For example, if parsing rST, at least provide the rst-parser
            settings, obtainable as follows:

            Defaults for parser component::

                settings = docutils.frontend.get_default_settings(
                               docutils.parsers.rst.Parser)

            Defaults and configuration file customizations::

                settings = docutils.core.Publisher(
                    parser=docutils.parsers.rst.Parser).get_settings()
    """
    ...

class ExtensionOptionError(DataError): ...
class BadOptionError(ExtensionOptionError): ...
class BadOptionDataError(ExtensionOptionError): ...
class DuplicateOptionError(ExtensionOptionError): ...

def extract_extension_options(
    field_list: nodes.field_list, options_spec: Mapping[str, Callable[[str], Any]]
) -> dict[str, Any]:
    """
    Return a dictionary mapping extension option names to converted values.

    :Parameters:
        - `field_list`: A flat field list without field arguments, where each
          field body consists of a single paragraph only.
        - `options_spec`: Dictionary mapping known option names to a
          conversion function such as `int` or `float`.

    :Exceptions:
        - `KeyError` for unknown option names.
        - `ValueError` for invalid option values (raised by the conversion
           function).
        - `TypeError` for invalid option value types (raised by conversion
           function).
        - `DuplicateOptionError` for duplicate options.
        - `BadOptionError` for invalid fields.
        - `BadOptionDataError` for invalid option data (missing name,
          missing data, bad quotes, etc.).
    """
    ...
def extract_options(field_list: nodes.field_list) -> list[tuple[str, str]]:
    """
    Return a list of option (name, value) pairs from field names & bodies.

    :Parameter:
        `field_list`: A flat field list, where each field name is a single
        word and each field body consists of a single paragraph only.

    :Exceptions:
        - `BadOptionError` for invalid fields.
        - `BadOptionDataError` for invalid option data (missing name,
          missing data, bad quotes, etc.).
    """
    ...
def assemble_option_dict(
    option_list: Iterable[tuple[str, str]], options_spec: Mapping[str, Callable[[str], Any]]
) -> dict[str, Any]:
    """
    Return a mapping of option names to values.

    :Parameters:
        - `option_list`: A list of (name, value) pairs (the output of
          `extract_options()`).
        - `options_spec`: Dictionary mapping known option names to a
          conversion function such as `int` or `float`.

    :Exceptions:
        - `KeyError` for unknown option names.
        - `DuplicateOptionError` for duplicate options.
        - `ValueError` for invalid option values (raised by conversion
           function).
        - `TypeError` for invalid option value types (raised by conversion
           function).
    """
    ...

class NameValueError(DataError): ...

@deprecated("Deprecated and will be removed in Docutils 1.0.")
def decode_path(path: str) -> str: ...
def extract_name_value(line: str) -> list[tuple[str, str]]: ...
def clean_rcs_keywords(paragraph: nodes.paragraph, keyword_substitutions: Iterable[tuple[Pattern[str], str]]) -> None: ...
def relative_path(source: StrPath | None, target: StrPath) -> str: ...
@deprecated("Deprecated and will be removed in Docutils 1.0. Use `get_stylesheet_list()` instead.")
def get_stylesheet_reference(settings: Values, relative_to: StrPath | None = None) -> str: ...
def get_stylesheet_list(settings: Values) -> list[str]: ...
def find_file_in_dirs(path: StrPath, dirs: Iterable[StrPath]) -> str: ...
def get_trim_footnote_ref_space(settings: Values) -> bool: ...
def get_source_line(node: nodes.Node) -> tuple[str, int]: ...
def escape2null(text: str) -> str: ...
def split_escaped_whitespace(text: str) -> list[str]: ...
def strip_combining_chars(text: str) -> str: ...
def find_combining_chars(text: str) -> list[int]:
    """
    Return indices of all combining chars in  Unicode string `text`.

    >>> from docutils.utils import find_combining_chars
    >>> find_combining_chars('A t̆ab̆lĕ')
    [3, 6, 9]
    """
    ...
def column_indices(text: str) -> list[int]:
    """
    Indices of Unicode string `text` when skipping combining characters.

    >>> from docutils.utils import column_indices
    >>> column_indices('A t̆ab̆lĕ')
    [0, 1, 2, 4, 5, 7, 8]
    """
    ...

east_asian_widths: dict[str, int]

def column_width(text: str) -> int:
    """
    Return the column width of text.

    Correct ``len(text)`` for wide East Asian and combining Unicode chars.
    """
    ...
def uniq(L: list[_T]) -> list[_T]: ...
def normalize_language_tag(tag: str) -> list[str]: ...
def xml_declaration(encoding: str | None = None) -> str: ...
