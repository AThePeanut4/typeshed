"""
Calling the ``publish_*`` convenience functions (or instantiating a
`Publisher` object) with component names will result in default
behavior.  For custom behavior (setting component options), create
custom component objects first, and pass *them* to
``publish_*``/`Publisher`.  See `The Docutils Publisher`_.

.. _The Docutils Publisher:
    https://docutils.sourceforge.io/docs/api/publisher.html
"""

from _typeshed import Incomplete
from typing import Final
from typing_extensions import deprecated

from docutils import SettingsSpec
from docutils.frontend import OptionParser
from docutils.io import FileInput, Input, Output, StringInput
from docutils.parsers import Parser
from docutils.readers import Reader
from docutils.utils import SystemMessage
from docutils.writers import Writer, _WriterParts

__docformat__: Final = "reStructuredText"

class Publisher:
    document: Incomplete | None
    reader: Reader[Incomplete]
    parser: Parser
    writer: Writer[Incomplete]
    source: Input[Incomplete]
    source_class: Incomplete
    destination: Output | None
    destination_class: Incomplete
    settings: dict[str, Incomplete]
    def __init__(
        self,
        reader: Reader[Incomplete] | None = None,
        parser: Parser | None = None,
        writer: Writer[Incomplete] | None = None,
        source: Input[Incomplete] | None = None,
        source_class=...,
        destination: Output | None = None,
        destination_class=...,
        settings: dict[str, Incomplete] | None = None,
    ) -> None: ...
    def set_reader(self, reader_name: str, parser: Parser | None, parser_name: str | None) -> None: ...
    def set_writer(self, writer_name: str) -> None: ...
    def set_components(self, reader_name: str, parser_name: str, writer_name: str) -> None: ...
    @deprecated("Publisher.setup_option_parser is deprecated, and will be removed in Docutils 0.21.")
    def setup_option_parser(
        self,
        usage: str | None = None,
        description: str | None = None,
        settings_spec: SettingsSpec | None = None,
        config_section: str | None = None,
        **defaults,
    ) -> OptionParser: ...
    def get_settings(
        self,
        usage: str | None = None,
        description: str | None = None,
        settings_spec: SettingsSpec | None = None,
        config_section: str | None = None,
        **defaults,
    ):
        """
        Return settings from components and config files.

        Please set components first (`self.set_reader` & `self.set_writer`).
        Use keyword arguments to override component defaults
        (before updating from configuration files).

        Calling this function also sets `self.settings` which makes
        `self.publish()` skip parsing command line options.
        """
        ...
    def process_programmatic_settings(self, settings_spec, settings_overrides, config_section) -> None: ...
    def process_command_line(
        self,
        argv: list[str] | None = None,
        usage=None,
        description: str | None = None,
        settings_spec=None,
        config_section=None,
        **defaults,
    ) -> None: ...
    def set_io(self, source_path=None, destination_path=None) -> None: ...
    def set_source(self, source=None, source_path=None) -> None: ...
    def set_destination(self, destination=None, destination_path=None) -> None: ...
    def apply_transforms(self) -> None: ...
    def publish(
        self,
        argv: list[str] | None = None,
        usage: str | None = None,
        description: str | None = None,
        settings_spec=None,
        settings_overrides=None,
        config_section: str | None = None,
        enable_exit_status: bool = False,
    ):
        """
        Process command line options and arguments (if `self.settings` not
        already set), run `self.reader` and then `self.writer`.  Return
        `self.writer`'s output.
        """
        ...
    def debugging_dumps(self) -> None: ...
    def prompt(self) -> None: ...
    def report_Exception(self, error: BaseException) -> None: ...
    def report_SystemMessage(self, error: SystemMessage) -> None: ...
    def report_UnicodeError(self, error: UnicodeEncodeError) -> None: ...

default_usage: Final[str]
default_description: Final[str]

def publish_cmdline(
    reader: Reader[Incomplete] | None = None,
    reader_name: str = "standalone",
    parser: Parser | None = None,
    parser_name: str = "restructuredtext",
    writer: Writer[Incomplete] | None = None,
    writer_name: str = "pseudoxml",
    settings=None,
    settings_spec=None,
    settings_overrides=None,
    config_section: str | None = None,
    enable_exit_status: bool = True,
    argv: list[str] | None = None,
    usage: str = ...,
    description: str = ...,
): ...
def publish_file(
    source=None,
    source_path: FileInput | StringInput | None = None,
    destination=None,
    destination_path: FileInput | StringInput | None = None,
    reader=None,
    reader_name: str = "standalone",
    parser=None,
    parser_name: str = "restructuredtext",
    writer=None,
    writer_name: str = "pseudoxml",
    settings=None,
    settings_spec=None,
    settings_overrides=None,
    config_section: str | None = None,
    enable_exit_status: bool = False,
):
    """
    Set up & run a `Publisher` for programmatic use with file-like I/O.
    Also return the output as `str` or `bytes` (for binary output document
    formats).

    Parameters: see `publish_programmatically()`.
    """
    ...
def publish_string(
    source,
    source_path: FileInput | StringInput | None = None,
    destination_path: FileInput | StringInput | None = None,
    reader=None,
    reader_name: str = "standalone",
    parser=None,
    parser_name: str = "restructuredtext",
    writer=None,
    writer_name: str = "pseudoxml",
    settings=None,
    settings_spec=None,
    settings_overrides=None,
    config_section: str | None = None,
    enable_exit_status: bool = False,
):
    'Set up & run a `Publisher` for programmatic use with string I/O.\n\nAccepts a `bytes` or `str` instance as `source`.\n\nThe output is encoded according to the `output_encoding`_ setting;\nthe return value is a `bytes` instance (unless `output_encoding`_ is\n"unicode", cf. `docutils.io.StringOutput.write()`).\n\nParameters: see `publish_programmatically()`.\n\nThis function is provisional because in Python\xa03 name and behaviour\nno longer match.\n\n.. _output_encoding:\n    https://docutils.sourceforge.io/docs/user/config.html#output-encoding'
    ...
def publish_parts(
    source,
    source_path: FileInput | StringInput | None = None,
    source_class=...,
    destination_path: FileInput | StringInput | None = None,
    reader=None,
    reader_name: str = "standalone",
    parser=None,
    parser_name: str = "restructuredtext",
    writer=None,
    writer_name: str = "pseudoxml",
    settings=None,
    settings_spec=None,
    settings_overrides: dict[str, Incomplete] | None = None,
    config_section: str | None = None,
    enable_exit_status: bool = False,
) -> _WriterParts:
    """
    Set up & run a `Publisher`, and return a dictionary of document parts.

    Dictionary keys are the names of parts.
    Dictionary values are `str` instances; encoding is up to the client,
    e.g.::

       parts = publish_parts(...)
       body = parts['body'].encode(parts['encoding'], parts['errors'])

    See the `API documentation`__ for details on the provided parts.

    Parameters: see `publish_programmatically()`.

    __ https://docutils.sourceforge.io/docs/api/publisher.html#publish-parts
    """
    ...
def publish_doctree(
    source,
    source_path: FileInput | StringInput | None = None,
    source_class=...,
    reader=None,
    reader_name: str = "standalone",
    parser=None,
    parser_name: str = "restructuredtext",
    settings=None,
    settings_spec=None,
    settings_overrides=None,
    config_section: str | None = None,
    enable_exit_status: bool = False,
):
    """
    Set up & run a `Publisher` for programmatic use. Return a document tree.

    Parameters: see `publish_programmatically()`.
    """
    ...
def publish_from_doctree(
    document,
    destination_path: FileInput | StringInput | None = None,
    writer=None,
    writer_name: str = "pseudoxml",
    settings=None,
    settings_spec=None,
    settings_overrides=None,
    config_section: str | None = None,
    enable_exit_status: bool = False,
):
    'Set up & run a `Publisher` to render from an existing document tree\ndata structure. For programmatic use with string output\n(`bytes` or `str`, cf. `publish_string()`).\n\nNote that ``document.settings`` is overridden; if you want to use the\nsettings of the original `document`, pass ``settings=document.settings``.\n\nAlso, new `document.transformer` and `document.reporter` objects are\ngenerated.\n\nParameters: `document` is a `docutils.nodes.document` object, an existing\ndocument tree.\n\nOther parameters: see `publish_programmatically()`.\n\nThis function is provisional because in Python\xa03 name and behaviour\nof the `io.StringOutput` class no longer match.'
    ...
def publish_cmdline_to_binary(
    reader=None,
    reader_name: str = "standalone",
    parser=None,
    parser_name: str = "restructuredtext",
    writer=None,
    writer_name: str = "pseudoxml",
    settings=None,
    settings_spec=None,
    settings_overrides=None,
    config_section: str | None = None,
    enable_exit_status: bool = True,
    argv: list[str] | None = None,
    usage: str = ...,
    description: str = ...,
    destination=None,
    destination_class=...,
):
    """
    Set up & run a `Publisher` for command-line-based file I/O (input and
    output file paths taken automatically from the command line).
    Also return the output as `bytes`.

    This is just like publish_cmdline, except that it uses
    io.BinaryFileOutput instead of io.FileOutput.

    Parameters: see `publish_programmatically()` for the remainder.

    - `argv`: Command-line argument list to use instead of ``sys.argv[1:]``.
    - `usage`: Usage string, output if there's a problem parsing the command
      line.
    - `description`: Program description, output for the "--help" option
      (along with command-line option descriptions).
    """
    ...
def publish_programmatically(
    source_class: type[FileInput],
    source,
    source_path: FileInput | StringInput,
    destination_class,
    destination,
    destination_path: FileInput | StringInput,
    reader,
    reader_name: str,
    parser,
    parser_name: str,
    writer,
    writer_name: str,
    settings,
    settings_spec,
    settings_overrides,
    config_section: str,
    enable_exit_status: bool,
) -> tuple[str | bytes | None, Publisher]: ...
def rst2something(writer: str, documenttype: str, doc_path: str = "") -> None: ...
def rst2html() -> None: ...
def rst2html4() -> None: ...
def rst2html5() -> None: ...
def rst2latex() -> None: ...
def rst2man() -> None: ...
def rst2odt() -> None: ...
def rst2pseudoxml() -> None: ...
def rst2s5() -> None: ...
def rst2xetex() -> None: ...
def rst2xml() -> None: ...
