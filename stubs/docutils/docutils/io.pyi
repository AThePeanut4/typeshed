"""
I/O classes provide a uniform API for low-level input and output.  Subclasses
exist for a variety of input/output mechanisms.
"""

from _typeshed import (
    Incomplete,
    OpenBinaryModeReading,
    OpenBinaryModeWriting,
    OpenTextModeReading,
    OpenTextModeWriting,
    SupportsWrite,
    Unused,
)
from re import Pattern
from typing import IO, Any, ClassVar, Generic, Literal, TypeVar

from docutils import TransformSpec, nodes

__docformat__: str

class InputError(OSError): ...
class OutputError(OSError): ...

def check_encoding(stream: Any, encoding: str) -> bool | None:
    """
    Test, whether the encoding of `stream` matches `encoding`.

    Returns

    :None:  if `encoding` or `stream.encoding` are not a valid encoding
            argument (e.g. ``None``) or `stream.encoding is missing.
    :True:  if the encoding argument resolves to the same value as `encoding`,
    :False: if the encodings differ.
    """
    ...
def error_string(err: BaseException) -> str:
    """
    Return string representation of Exception `err`.
    
    """
    ...

_S = TypeVar("_S")

class Input(TransformSpec, Generic[_S]):
    """
    Abstract base class for input wrappers.

    Docutils input objects must provide a `read()` method that
    returns the source, typically as `str` instance.

    Inheriting `TransformSpec` allows input objects to add
    "transforms" and "unknown_reference_resolvers" to the "Transformer".
    (Optional for custom input objects since Docutils 0.19.)
    """
    component_type: ClassVar[str]
    default_source_path: ClassVar[str | None]
    encoding: str | None
    error_handler: str
    source: _S | None
    source_path: str | None
    successful_encoding: str | None = None
    def __init__(
        self, source: _S | None = None, source_path: str | None = None, encoding: str | None = None, error_handler: str = "strict"
    ) -> None: ...
    def read(self) -> str:
        """Return input as `str`. Define in subclasses."""
        ...
    def decode(self, data: str | bytes | bytearray) -> str:
        """
        Decode `data` if required.

        Return Unicode `str` instances unchanged (nothing to decode).

        If `self.encoding` is None, determine encoding from data
        or try UTF-8 and the locale's preferred encoding.
        The client application should call ``locale.setlocale()`` at the
        beginning of processing::

            locale.setlocale(locale.LC_ALL, '')

        Raise UnicodeError if unsuccessful.

        Provisional: encoding detection will be removed in Docutils 1.0.
        """
        ...
    coding_slug: ClassVar[Pattern[bytes]]
    byte_order_marks: ClassVar[tuple[tuple[bytes, str], ...]]
    def determine_encoding_from_data(self, data: str | bytes | bytearray) -> str | None:
        """
        Try to determine the encoding of `data` by looking *in* `data`.
        Check for a byte order mark (BOM) or an encoding declaration.
        """
        ...
    def isatty(self) -> bool:
        """Return True, if the input source is connected to a TTY device."""
        ...

class Output(TransformSpec):
    """
    Abstract base class for output wrappers.

    Docutils output objects must provide a `write()` method that
    expects and handles one argument (the output).

    Inheriting `TransformSpec` allows output objects to add
    "transforms" and "unknown_reference_resolvers" to the "Transformer".
    (Optional for custom output objects since Docutils 0.19.)
    """
    component_type: ClassVar[str]
    default_destination_path: ClassVar[str | None]
    def __init__(
        self,
        destination: Incomplete | None = None,
        destination_path: Incomplete | None = None,
        encoding: str | None = None,
        error_handler: str = "strict",
    ) -> None: ...
    def write(self, data: str) -> Any:
        """Write `data`. Define in subclasses."""
        ...
    def encode(self, data: str) -> Any:
        """
        Encode and return `data`.

        If `data` is a `bytes` instance, it is returned unchanged.
        Otherwise it is encoded with `self.encoding`.

        Provisional: If `self.encoding` is set to the pseudo encoding name
        "unicode", `data` must be a `str` instance and is returned unchanged.
        """
        ...

class ErrorOutput:
    """
    Wrapper class for file-like error streams with
    failsafe de- and encoding of `str`, `bytes`, `unicode` and
    `Exception` instances.
    """
    def __init__(
        self,
        destination: str | SupportsWrite[str] | SupportsWrite[bytes] | Literal[False] | None = None,
        encoding: str | None = None,
        encoding_errors: str = "backslashreplace",
        decoding_errors: str = "replace",
    ) -> None:
        """
        :Parameters:
            - `destination`: a file-like object,
                        a string (path to a file),
                        `None` (write to `sys.stderr`, default), or
                        evaluating to `False` (write() requests are ignored).
            - `encoding`: `destination` text encoding. Guessed if None.
            - `encoding_errors`: how to treat encoding errors.
        """
        ...
    def write(self, data: str | bytes | Exception) -> None:
        """
        Write `data` to self.destination. Ignore, if self.destination is False.

        `data` can be a `bytes`, `str`, or `Exception` instance.
        """
        ...
    def close(self) -> None:
        """
        Close the error-output stream.

        Ignored if the destination is` sys.stderr` or `sys.stdout` or has no
        close() method.
        """
        ...
    def isatty(self) -> bool:
        """Return True, if the destination is connected to a TTY device."""
        ...

class FileInput(Input[IO[str]]):
    """Input for single, simple file-like objects."""
    def __init__(
        self,
        source: Incomplete | None = None,
        source_path: Incomplete | None = None,
        encoding: str | None = None,
        error_handler: str = "strict",
        autoclose: bool = True,
        mode: OpenTextModeReading | OpenBinaryModeReading = "r",
    ) -> None:
        """
        :Parameters:
            - `source`: either a file-like object (which is read directly), or
              `None` (which implies `sys.stdin` if no `source_path` given).
            - `source_path`: a path to a file, which is opened for reading.
            - `encoding`: the expected text encoding of the input file.
            - `error_handler`: the encoding error handler to use.
            - `autoclose`: close automatically after read (except when
              `sys.stdin` is the source).
            - `mode`: how the file is to be opened (see standard function
              `open`). The default is read only ('r').
        """
        ...
    def read(self) -> str:
        """Read and decode a single file, return as `str`."""
        ...
    def readlines(self) -> list[str]:
        """Return lines of a single file as list of strings."""
        ...
    def close(self) -> None: ...

class FileOutput(Output):
    """Output for single, simple file-like objects."""
    mode: ClassVar[OpenTextModeWriting | OpenBinaryModeWriting]
    def __getattr__(self, name: str) -> Incomplete: ...

class BinaryFileOutput(FileOutput):
    """A version of docutils.io.FileOutput which writes to a binary file."""
    ...

class StringInput(Input[str]):
    """Input from a `str` or `bytes` instance."""
    default_source_path: ClassVar[str]

class StringOutput(Output):
    """
    Output to a `bytes` or `str` instance.

    Provisional.
    """
    default_destination_path: ClassVar[str]
    destination: str | bytes  # only defined after call to write()

class NullInput(Input[Any]):
    """Degenerate input: read nothing."""
    default_source_path: ClassVar[str]
    def read(self) -> str:
        """Return an empty string."""
        ...

class NullOutput(Output):
    """Degenerate output: write nothing."""
    default_destination_path: ClassVar[str]
    def write(self, data: Unused) -> None:
        """Do nothing, return None."""
        ...

class DocTreeInput(Input[nodes.document]):
    """
    Adapter for document tree input.

    The document tree must be passed in the ``source`` parameter.
    """
    default_source_path: ClassVar[str]
