import sys
from _typeshed import SupportsWrite
from collections.abc import Callable, Sequence
from re import Pattern
from types import TracebackType
from typing import Any, ClassVar, TextIO
from typing_extensions import TypeAlias

if sys.platform == "win32":
    from .winterm import WinTerm

    winterm: WinTerm
else:
    winterm: None

class StreamWrapper:
    """
    Wraps a stream (such as stdout), acting as a transparent proxy for all
    attribute access apart from method 'write()', which is delegated to our
    Converter instance.
    """
    def __init__(self, wrapped: TextIO, converter: SupportsWrite[str]) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    def __enter__(self, *args: object, **kwargs: object) -> TextIO: ...
    def __exit__(
        self, t: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None, /, **kwargs: Any
    ) -> None: ...
    def write(self, text: str) -> None: ...
    def isatty(self) -> bool: ...
    @property
    def closed(self) -> bool: ...

_WinTermCall: TypeAlias = Callable[[int | None, bool, bool], None]
_WinTermCallDict: TypeAlias = dict[int, tuple[_WinTermCall] | tuple[_WinTermCall, int] | tuple[_WinTermCall, int, bool]]

class AnsiToWin32:
    """
    Implements a 'write()' method which, on Windows, will strip ANSI character
    sequences from the text, and if outputting to a tty, will convert them into
    win32 function calls.
    """
    ANSI_CSI_RE: ClassVar[Pattern[str]]
    ANSI_OSC_RE: ClassVar[Pattern[str]]
    wrapped: TextIO
    autoreset: bool
    stream: StreamWrapper
    strip: bool
    convert: bool
    win32_calls: _WinTermCallDict
    on_stderr: bool
    def __init__(
        self, wrapped: TextIO, convert: bool | None = None, strip: bool | None = None, autoreset: bool = False
    ) -> None: ...
    def should_wrap(self) -> bool:
        """
        True if this class is actually needed. If false, then the output
        stream will not be affected, nor will win32 calls be issued, so
        wrapping stdout is not actually required. This will generally be
        False on non-Windows platforms, unless optional functionality like
        autoreset has been requested using kwargs to init()
        """
        ...
    def get_win32_calls(self) -> _WinTermCallDict: ...
    def write(self, text: str) -> None: ...
    def reset_all(self) -> None: ...
    def write_and_convert(self, text: str) -> None:
        """
        Write the given text to our wrapped stream, stripping any ANSI
        sequences from the text, and optionally converting them into win32
        calls.
        """
        ...
    def write_plain_text(self, text: str, start: int, end: int) -> None: ...
    def convert_ansi(self, paramstring: str, command: str) -> None: ...
    def extract_params(self, command: str, paramstring: str) -> tuple[int, ...]: ...
    def call_win32(self, command: str, params: Sequence[int]) -> None: ...
    def convert_osc(self, text: str) -> str: ...
    def flush(self) -> None: ...
