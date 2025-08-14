"""This package contains Docutils Writer modules."""

from _typeshed import StrPath
from pathlib import Path
from typing import Any, Final, Generic, TypedDict, TypeVar, type_check_only
from typing_extensions import Required

from docutils import Component, nodes
from docutils.frontend import Values
from docutils.io import Output
from docutils.languages import LanguageImporter

_S = TypeVar("_S")

__docformat__: Final = "reStructuredText"

# It would probably be better to specialize writers for subclasses,
# but this gives us all possible Writer items w/o instance checks
@type_check_only
class _WriterParts(TypedDict, total=False):
    # Parts Provided by All Writers https://docutils.sourceforge.io/docs/api/publisher.html#parts-provided-by-all-writers

    # See Writer.assemble_parts
    whole: Required[str | bytes]
    encoding: Required[str]
    errors: Required[str]
    version: Required[str]

    # Parts Provided by the HTML Writers https://docutils.sourceforge.io/docs/api/publisher.html#parts-provided-by-the-html-writers

    # HTML4 Writer https://docutils.sourceforge.io/docs/api/publisher.html#html4-writer
    # + HTML5 Writer https://docutils.sourceforge.io/docs/api/publisher.html#html5-writer
    body: str
    body_prefix: str
    body_pre_docinfo: str
    body_suffix: str
    docinfo: str
    footer: str
    fragment: str
    head: str
    head_prefix: str
    header: str
    html_body: str
    html_head: str
    html_prolog: str
    html_subtitle: str
    html_title: str
    meta: str
    stylesheet: str
    subtitle: str
    title: str
    # PEP/HTML Writer https://docutils.sourceforge.io/docs/api/publisher.html#pep-html-writer
    # + S5/HTML Writer https://docutils.sourceforge.io/docs/api/publisher.html#s5-html-writer
    pepnum: str

    # Parts Provided by the (Xe)LaTeX Writers https://docutils.sourceforge.io/docs/api/publisher.html#parts-provided-by-the-xe-latex-writers

    # (commenting out those already included)
    abstract: str
    # body: str
    # body_pre_docinfo: str
    dedication: str
    # docinfo: str
    fallbacks: str
    # head_prefix: str
    latex_preamble: str
    pdfsetup: str
    requirements: str
    # stylesheet: str
    # subtitle: str
    # title: str
    titledata: str

class Writer(Component, Generic[_S]):
    """
    Abstract base class for docutils Writers.

    Each writer module or package must export a subclass also called 'Writer'.
    Each writer must support all standard node types listed in
    `docutils.nodes.node_class_names`.

    The `write()` method is the main entry point.
    """
    parts: _WriterParts
    language: LanguageImporter | None = None
    document: nodes.document | None = None
    destination: Output | None = None
    output: _S | None = None
    def __init__(self) -> None: ...
    def write(self, document: nodes.document, destination: Output) -> str | bytes | None:
        """
        Process a document into its final form.

        Translate `document` (a Docutils document tree) into the Writer's
        native format, and write it out to its `destination` (a
        `docutils.io.Output` subclass object).

        Normally not overridden or extended in subclasses.
        """
        ...
    def translate(self) -> None:
        """
        Do final translation of `self.document` into `self.output`.  Called
        from `write`.  Override in subclasses.

        Usually done with a `docutils.nodes.NodeVisitor` subclass, in
        combination with a call to `docutils.nodes.Node.walk()` or
        `docutils.nodes.Node.walkabout()`.  The ``NodeVisitor`` subclass must
        support all standard elements (listed in
        `docutils.nodes.node_class_names`) and possibly non-standard elements
        used by the current Reader as well.
        """
        ...
    def assemble_parts(self) -> None:
        """
        Assemble the `self.parts` dictionary.  Extend in subclasses.

        See <https://docutils.sourceforge.io/docs/api/publisher.html>.
        """
        ...

class UnfilteredWriter(Writer[_S]):
    """
    A writer that passes the document tree on unchanged (e.g. a
    serializer.)

    Documents written by UnfilteredWriters are typically reused at a
    later date using a subclass of `readers.ReReader`.
    """
    ...

class DoctreeTranslator(nodes.NodeVisitor):
    """
    Generic Docutils document tree translator base class.

    Adds auxiliary methods and attributes that are used by several
    Docutils writers to the `nodes.NodeVisitor` abstract superclass.
    """
    settings: Values
    def __init__(self, document: nodes.document) -> None: ...
    def uri2path(self, uri: str, output_path: StrPath | None = None) -> Path:
        """
        Return filesystem path corresponding to a `URI reference`__.

        The `root_prefix`__ setting` is applied to URI references starting
        with "/" (but not to absolute Windows paths or "file" URIs).

        If `output_path` (defaults to the `output_path`__ setting) is
        not empty, relative paths are adjusted.
        (To work in the output document, URI references with relative path
        relate to the output directory.  For access by the writer, paths
        must be relative to the working directory.)

        Use case:
          The <image> element refers to the image via a "URI reference".
          The corresponding filesystem path is required to read the
          image size from the file or to embed the image in the output.

          A filesystem path is also expected by the "LaTeX" output format
          (with relative paths unchanged, relating to the output directory,
          set `output_path` to the empty string).

        Provisional: the function's location, interface and behaviour
        may change without advance warning.

        __ https://www.rfc-editor.org/rfc/rfc3986.html#section-4.1
        __ https://docutils.sourceforge.io/docs/user/config.html#root-prefix
        __ https://docutils.sourceforge.io/docs/user/config.html#output-path
        """
        ...

WRITER_ALIASES: Final[dict[str, str]]

def get_writer_class(writer_name: str) -> type[Writer[Any]]:
    """Return the Writer class from the `writer_name` module."""
    ...
