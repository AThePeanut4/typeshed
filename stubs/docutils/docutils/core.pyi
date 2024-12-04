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

from docutils.writers import _WriterParts

__docformat__: str

class Publisher:
    """A facade encapsulating the high-level logic of a Docutils system."""
    document: Incomplete
    reader: Incomplete
    parser: Incomplete
    writer: Incomplete
    source: Incomplete
    source_class: Incomplete
    destination: Incomplete
    destination_class: Incomplete
    settings: Incomplete
    def __init__(
        self,
        reader: Incomplete | None = None,
        parser: Incomplete | None = None,
        writer: Incomplete | None = None,
        source: Incomplete | None = None,
        source_class=...,
        destination: Incomplete | None = None,
        destination_class=...,
        settings: Incomplete | None = None,
    ) -> None:
        """
        Initial setup.  If any of `reader`, `parser`, or `writer` are not
        specified, ``set_components()`` or the corresponding ``set_...()``
        method should be called with component names
        (`set_reader` sets the parser as well).
        """
        ...
    def set_reader(self, reader_name, parser, parser_name) -> None:
        """Set `self.reader` by name."""
        ...
    def set_writer(self, writer_name) -> None:
        """Set `self.writer` by name."""
        ...
    def set_components(self, reader_name, parser_name, writer_name) -> None: ...
    def setup_option_parser(
        self,
        usage: Incomplete | None = None,
        description: Incomplete | None = None,
        settings_spec: Incomplete | None = None,
        config_section: Incomplete | None = None,
        **defaults,
    ): ...
    def get_settings(
        self,
        usage: Incomplete | None = None,
        description: Incomplete | None = None,
        settings_spec: Incomplete | None = None,
        config_section: Incomplete | None = None,
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
        argv: Incomplete | None = None,
        usage: Incomplete | None = None,
        description: Incomplete | None = None,
        settings_spec: Incomplete | None = None,
        config_section: Incomplete | None = None,
        **defaults,
    ) -> None:
        """
        Parse command line arguments and set ``self.settings``.

        Pass an empty sequence to `argv` to avoid reading `sys.argv`
        (the default behaviour).

        Set components first (`self.set_reader` & `self.set_writer`).
        """
        ...
    def set_io(self, source_path: Incomplete | None = None, destination_path: Incomplete | None = None) -> None: ...
    def set_source(self, source: Incomplete | None = None, source_path: Incomplete | None = None) -> None: ...
    def set_destination(self, destination: Incomplete | None = None, destination_path: Incomplete | None = None) -> None: ...
    def apply_transforms(self) -> None: ...
    def publish(
        self,
        argv: Incomplete | None = None,
        usage: Incomplete | None = None,
        description: Incomplete | None = None,
        settings_spec: Incomplete | None = None,
        settings_overrides: Incomplete | None = None,
        config_section: Incomplete | None = None,
        enable_exit_status: bool = False,
    ):
        """
        Process command line options and arguments (if `self.settings` not
        already set), run `self.reader` and then `self.writer`.  Return
        `self.writer`'s output.
        """
        ...
    def debugging_dumps(self) -> None: ...
    def prompt(self) -> None:
        """Print info and prompt when waiting for input from a terminal."""
        ...
    def report_Exception(self, error) -> None: ...
    def report_SystemMessage(self, error) -> None: ...
    def report_UnicodeError(self, error) -> None: ...

default_usage: str
default_description: str

def publish_cmdline(
    reader: Incomplete | None = None,
    reader_name: str = "standalone",
    parser: Incomplete | None = None,
    parser_name: str = "restructuredtext",
    writer: Incomplete | None = None,
    writer_name: str = "pseudoxml",
    settings: Incomplete | None = None,
    settings_spec: Incomplete | None = None,
    settings_overrides: Incomplete | None = None,
    config_section: Incomplete | None = None,
    enable_exit_status: bool = True,
    argv: Incomplete | None = None,
    usage=...,
    description=...,
):
    """
    Set up & run a `Publisher` for command-line-based file I/O (input and
    output file paths taken automatically from the command line).
    Also return the output as `str` or `bytes` (for binary output document
    formats).

    Parameters: see `publish_programmatically()` for the remainder.

    - `argv`: Command-line argument list to use instead of ``sys.argv[1:]``.
    - `usage`: Usage string, output if there's a problem parsing the command
      line.
    - `description`: Program description, output for the "--help" option
      (along with command-line option descriptions).
    """
    ...
def publish_file(
    source: Incomplete | None = None,
    source_path: Incomplete | None = None,
    destination: Incomplete | None = None,
    destination_path: Incomplete | None = None,
    reader: Incomplete | None = None,
    reader_name: str = "standalone",
    parser: Incomplete | None = None,
    parser_name: str = "restructuredtext",
    writer: Incomplete | None = None,
    writer_name: str = "pseudoxml",
    settings: Incomplete | None = None,
    settings_spec: Incomplete | None = None,
    settings_overrides: Incomplete | None = None,
    config_section: Incomplete | None = None,
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
    source_path: Incomplete | None = None,
    destination_path: Incomplete | None = None,
    reader: Incomplete | None = None,
    reader_name: str = "standalone",
    parser: Incomplete | None = None,
    parser_name: str = "restructuredtext",
    writer: Incomplete | None = None,
    writer_name: str = "pseudoxml",
    settings: Incomplete | None = None,
    settings_spec: Incomplete | None = None,
    settings_overrides: Incomplete | None = None,
    config_section: Incomplete | None = None,
    enable_exit_status: bool = False,
):
    'Set up & run a `Publisher` for programmatic use with string I/O.\n\nAccepts a `bytes` or `str` instance as `source`.\n\nThe output is encoded according to the `output_encoding`_ setting;\nthe return value is a `bytes` instance (unless `output_encoding`_ is\n"unicode", cf. `docutils.io.StringOutput.write()`).\n\nParameters: see `publish_programmatically()`.\n\nThis function is provisional because in Python\xa03 name and behaviour\nno longer match.\n\n.. _output_encoding:\n    https://docutils.sourceforge.io/docs/user/config.html#output-encoding'
    ...
def publish_parts(
    source,
    source_path: Incomplete | None = None,
    source_class=...,
    destination_path: Incomplete | None = None,
    reader: Incomplete | None = None,
    reader_name: str = "standalone",
    parser: Incomplete | None = None,
    parser_name: str = "restructuredtext",
    writer: Incomplete | None = None,
    writer_name: str = "pseudoxml",
    settings: Incomplete | None = None,
    settings_spec: Incomplete | None = None,
    settings_overrides: Incomplete | None = None,
    config_section: Incomplete | None = None,
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
    source_path: Incomplete | None = None,
    source_class=...,
    reader: Incomplete | None = None,
    reader_name: str = "standalone",
    parser: Incomplete | None = None,
    parser_name: str = "restructuredtext",
    settings: Incomplete | None = None,
    settings_spec: Incomplete | None = None,
    settings_overrides: Incomplete | None = None,
    config_section: Incomplete | None = None,
    enable_exit_status: bool = False,
):
    """
    Set up & run a `Publisher` for programmatic use. Return a document tree.

    Parameters: see `publish_programmatically()`.
    """
    ...
def publish_from_doctree(
    document,
    destination_path: Incomplete | None = None,
    writer: Incomplete | None = None,
    writer_name: str = "pseudoxml",
    settings: Incomplete | None = None,
    settings_spec: Incomplete | None = None,
    settings_overrides: Incomplete | None = None,
    config_section: Incomplete | None = None,
    enable_exit_status: bool = False,
):
    'Set up & run a `Publisher` to render from an existing document tree\ndata structure. For programmatic use with string output\n(`bytes` or `str`, cf. `publish_string()`).\n\nNote that ``document.settings`` is overridden; if you want to use the\nsettings of the original `document`, pass ``settings=document.settings``.\n\nAlso, new `document.transformer` and `document.reporter` objects are\ngenerated.\n\nParameters: `document` is a `docutils.nodes.document` object, an existing\ndocument tree.\n\nOther parameters: see `publish_programmatically()`.\n\nThis function is provisional because in Python\xa03 name and behaviour\nof the `io.StringOutput` class no longer match.'
    ...
def publish_cmdline_to_binary(
    reader: Incomplete | None = None,
    reader_name: str = "standalone",
    parser: Incomplete | None = None,
    parser_name: str = "restructuredtext",
    writer: Incomplete | None = None,
    writer_name: str = "pseudoxml",
    settings: Incomplete | None = None,
    settings_spec: Incomplete | None = None,
    settings_overrides: Incomplete | None = None,
    config_section: Incomplete | None = None,
    enable_exit_status: bool = True,
    argv: Incomplete | None = None,
    usage=...,
    description=...,
    destination: Incomplete | None = None,
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
    source_class,
    source,
    source_path,
    destination_class,
    destination,
    destination_path,
    reader,
    reader_name,
    parser,
    parser_name,
    writer,
    writer_name,
    settings,
    settings_spec,
    settings_overrides,
    config_section,
    enable_exit_status,
):
    """
    Set up & run a `Publisher` for custom programmatic use.

    Return the output (as `str` or `bytes`, depending on `destination_class`,
    writer, and the "output_encoding" setting) and the Publisher object.

    Applications should not need to call this function directly.  If it does
    seem to be necessary to call this function directly, please write to the
    Docutils-develop mailing list
    <https://docutils.sourceforge.io/docs/user/mailing-lists.html#docutils-develop>.

    Parameters:

    * `source_class` **required**: The class for dynamically created source
      objects.  Typically `io.FileInput` or `io.StringInput`.

    * `source`: Type depends on `source_class`:

      - If `source_class` is `io.FileInput`: Either a file-like object
        (must have 'read' and 'close' methods), or ``None``
        (`source_path` is opened).  If neither `source` nor
        `source_path` are supplied, `sys.stdin` is used.

      - If `source_class` is `io.StringInput` **required**:
        The input as either a `bytes` object (ensure the 'input_encoding'
        setting matches its encoding) or a `str` object.

    * `source_path`: Type depends on `source_class`:

      - `io.FileInput`: Path to the input file, opened if no `source`
        supplied.

      - `io.StringInput`: Optional.  Path to the file or name of the
        object that produced `source`.  Only used for diagnostic output.

    * `destination_class` **required**: The class for dynamically created
      destination objects.  Typically `io.FileOutput` or `io.StringOutput`.

    * `destination`: Type depends on `destination_class`:

      - `io.FileOutput`: Either a file-like object (must have 'write' and
        'close' methods), or ``None`` (`destination_path` is opened).  If
        neither `destination` nor `destination_path` are supplied,
        `sys.stdout` is used.

      - `io.StringOutput`: Not used; pass ``None``.

    * `destination_path`: Type depends on `destination_class`:

      - `io.FileOutput`: Path to the output file.  Opened if no `destination`
        supplied.

      - `io.StringOutput`: Path to the file or object which will receive the
        output; optional.  Used for determining relative paths (stylesheets,
        source links, etc.).

    * `reader`: A `docutils.readers.Reader` object.

    * `reader_name`: Name or alias of the Reader class to be instantiated if
      no `reader` supplied.

    * `parser`: A `docutils.parsers.Parser` object.

    * `parser_name`: Name or alias of the Parser class to be instantiated if
      no `parser` supplied.

    * `writer`: A `docutils.writers.Writer` object.

    * `writer_name`: Name or alias of the Writer class to be instantiated if
      no `writer` supplied.

    * `settings`: A runtime settings (`docutils.frontend.Values`) object, for
      dotted-attribute access to runtime settings.  It's the end result of the
      `SettingsSpec`, config file, and option processing.  If `settings` is
      passed, it's assumed to be complete and no further setting/config/option
      processing is done.

    * `settings_spec`: A `docutils.SettingsSpec` subclass or object.  Provides
      extra application-specific settings definitions independently of
      components.  In other words, the application becomes a component, and
      its settings data is processed along with that of the other components.
      Used only if no `settings` specified.

    * `settings_overrides`: A dictionary containing application-specific
      settings defaults that override the defaults of other components.
      Used only if no `settings` specified.

    * `config_section`: A string, the name of the configuration file section
      for this application.  Overrides the ``config_section`` attribute
      defined by `settings_spec`.  Used only if no `settings` specified.

    * `enable_exit_status`: Boolean; enable exit status at end of processing?
    """
    ...
def rst2something(writer, documenttype, doc_path: str = "") -> None: ...
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
