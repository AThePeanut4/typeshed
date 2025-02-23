from collections.abc import Iterable, Iterator, Mapping
from types import FrameType, TracebackType
from typing import Any, Generic, Literal, TypeVar
from typing_extensions import Self

class Callpoint:
    """
    The Callpoint is a lightweight object used to represent a single
    entry in the code of a call stack. It stores the code-related
    metadata of a given frame. Available attributes are the same as
    the parameters below.

    Args:
        func_name (str): the function name
        lineno (int): the line number
        module_name (str): the module name
        module_path (str): the filesystem path of the module
        lasti (int): the index of bytecode execution
        line (str): the single-line code content (if available)
    """
    func_name: str
    lineno: int
    module_name: str
    module_path: str
    lasti: int
    line: str
    def __init__(
        self, module_name: str, module_path: str, func_name: str, lineno: int, lasti: int, line: str | None = None
    ) -> None: ...
    def to_dict(self) -> dict[str, Any]: ...
    @classmethod
    def from_current(cls, level: int = 1) -> Self:
        """Creates a Callpoint from the location of the calling function."""
        ...
    @classmethod
    def from_frame(cls, frame: FrameType) -> Self:
        """Create a Callpoint object from data extracted from the given frame."""
        ...
    @classmethod
    def from_tb(cls, tb: TracebackType) -> Self:
        """
        Create a Callpoint from the traceback of the current
        exception. Main difference with :meth:`from_frame` is that
        ``lineno`` and ``lasti`` come from the traceback, which is to
        say the line that failed in the try block, not the line
        currently being executed (in the except block).
        """
        ...
    def tb_frame_str(self) -> str:
        """
        Render the Callpoint as it would appear in a standard printed
        Python traceback. Returns a string with filename, line number,
        function name, and the actual code line of the error on up to
        two lines.
        """
        ...

_CallpointT = TypeVar("_CallpointT", bound=Callpoint, covariant=True, default=Callpoint)

class TracebackInfo(Generic[_CallpointT]):
    callpoint_type: type[_CallpointT]
    frames: list[_CallpointT]
    def __init__(self, frames: list[_CallpointT]) -> None: ...
    @classmethod
    def from_frame(cls, frame: FrameType | None = None, level: int = 1, limit: int | None = None) -> Self:
        """
        Create a new TracebackInfo *frame* by recurring up in the stack a
        max of *limit* times. If *frame* is unset, get the frame from
        :func:`sys._getframe` using *level*.

        Args:
            frame (types.FrameType): frame object from
                :func:`sys._getframe` or elsewhere. Defaults to result
                of :func:`sys.get_frame`.
            level (int): If *frame* is unset, the desired frame is
                this many levels up the stack from the invocation of
                this method. Default ``1`` (i.e., caller of this method).
            limit (int): max number of parent frames to extract
                (defaults to :data:`sys.tracebacklimit`)
        """
        ...
    @classmethod
    def from_traceback(cls, tb: TracebackType | None = None, limit: int | None = None) -> Self:
        """
        Create a new TracebackInfo from the traceback *tb* by recurring
        up in the stack a max of *limit* times. If *tb* is unset, get
        the traceback from the currently handled exception. If no
        exception is being handled, raise a :exc:`ValueError`.

        Args:

            frame (types.TracebackType): traceback object from
                :func:`sys.exc_info` or elsewhere. If absent or set to
                ``None``, defaults to ``sys.exc_info()[2]``, and
                raises a :exc:`ValueError` if no exception is
                currently being handled.
            limit (int): max number of parent frames to extract
                (defaults to :data:`sys.tracebacklimit`)
        """
        ...
    @classmethod
    def from_dict(cls, d: Mapping[Literal["frames"], list[_CallpointT]]) -> Self: ...
    def to_dict(self) -> dict[str, list[dict[str, _CallpointT]]]: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_CallpointT]: ...
    def get_formatted(self) -> str: ...

_TracebackInfoT = TypeVar("_TracebackInfoT", bound=TracebackInfo, covariant=True, default=TracebackInfo)

class ExceptionInfo(Generic[_TracebackInfoT]):
    tb_info_type: type[_TracebackInfoT]
    exc_type: str
    exc_msg: str
    tb_info: _TracebackInfoT
    def __init__(self, exc_type: str, exc_msg: str, tb_info: _TracebackInfoT) -> None: ...
    @classmethod
    def from_exc_info(cls, exc_type: type[BaseException], exc_value: BaseException, traceback: TracebackType) -> Self: ...
    @classmethod
    def from_current(cls) -> Self:
        """
        Create an :class:`ExceptionInfo` object from the current exception
        being handled, by way of :func:`sys.exc_info`. Will raise an
        exception if no exception is currently being handled.
        """
        ...
    def to_dict(self) -> dict[str, str | dict[str, list[FrameType]]]:
        """
        Get a :class:`dict` representation of the ExceptionInfo, suitable
        for JSON serialization.
        """
        ...
    def get_formatted(self) -> str:
        """
        Returns a string formatted in the traditional Python
        built-in style observable when an exception is not caught. In
        other words, mimics :func:`traceback.format_exception`.
        """
        ...
    def get_formatted_exception_only(self) -> str: ...

class ContextualCallpoint(Callpoint):
    """
    The ContextualCallpoint is a :class:`Callpoint` subtype with the
    exact same API and storing two additional values:

      1. :func:`repr` outputs for local variables from the Callpoint's scope
      2. A number of lines before and after the Callpoint's line of code

    The ContextualCallpoint is used by the :class:`ContextualTracebackInfo`.
    """
    local_reprs: dict[Any, Any]
    pre_lines: list[str]
    post_lines: list[str]
    def __init__(self, *a, **kw) -> None: ...
    @classmethod
    def from_frame(cls, frame: FrameType) -> Self:
        """Identical to :meth:`Callpoint.from_frame`"""
        ...
    @classmethod
    def from_tb(cls, tb: TracebackType) -> Self:
        """Identical to :meth:`Callpoint.from_tb`"""
        ...
    def to_dict(self) -> dict[str, Any]:
        """
        Same principle as :meth:`Callpoint.to_dict`, but with the added
        contextual values. With ``ContextualCallpoint.to_dict()``,
        each frame will now be represented like::

          {'func_name': 'print_example',
           'lineno': 0,
           'module_name': 'example_module',
           'module_path': '/home/example/example_module.pyc',
           'lasti': 0,
           'line': 'print "example"',
           'locals': {'variable': '"value"'},
           'pre_lines': ['variable = "value"'],
           'post_lines': []}

        The locals dictionary and line lists are copies and can be mutated
        freely.
        """
        ...

class ContextualTracebackInfo(TracebackInfo[ContextualCallpoint]):
    callpoint_type: type[ContextualCallpoint]

class ContextualExceptionInfo(ExceptionInfo[ContextualTracebackInfo]):
    tb_info_type: type[ContextualTracebackInfo]

def print_exception(
    etype: type[BaseException] | None,
    value: BaseException | None,
    tb: TracebackType | None,
    limit: int | None = None,
    file: str | None = None,
) -> None: ...

class ParsedException:
    """
    Stores a parsed traceback and exception as would be typically
    output by :func:`sys.excepthook` or
    :func:`traceback.print_exception`.

    .. note:

       Does not currently store SyntaxError details such as column.
    """
    exc_type: str
    exc_msg: str
    frames: list[FrameType]
    def __init__(self, exc_type_name: str, exc_msg: str, frames: Iterable[Mapping[str, Any]] | None = None) -> None: ...
    @property
    def source_file(self) -> str | None:
        """
        The file path of module containing the function that raised the
        exception, or None if not available.
        """
        ...
    def to_dict(self) -> dict[str, str | list[FrameType]]:
        """Get a copy as a JSON-serializable :class:`dict`."""
        ...
    def to_string(self) -> str:
        """
        Formats the exception and its traceback into the standard format,
        as returned by the traceback module.

        ``ParsedException.from_string(text).to_string()`` should yield
        ``text``.

        .. note::

           Note that this method does not output "anchors" (e.g.,
           ``~~~~~^^``), as were added in Python 3.13. See the built-in
           ``traceback`` module if these are necessary.
        """
        ...
    @classmethod
    def from_string(cls, tb_str: str) -> Self:
        """
        Parse a traceback and exception from the text *tb_str*. This text
        is expected to have been decoded, otherwise it will be
        interpreted as UTF-8.

        This method does not search a larger body of text for
        tracebacks. If the first line of the text passed does not
        match one of the known patterns, a :exc:`ValueError` will be
        raised. This method will ignore trailing text after the end of
        the first traceback.

        Args:
            tb_str (str): The traceback text (:class:`unicode` or UTF-8 bytes)
        """
        ...

ParsedTB = ParsedException
