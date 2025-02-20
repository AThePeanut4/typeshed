import threading
from collections.abc import Iterator
from types import TracebackType
from typing import Literal, Protocol
from typing_extensions import Self

__version__: str

class _Stream(Protocol):
    def isatty(self) -> bool: ...
    def flush(self) -> None: ...
    def write(self, s: str, /) -> int: ...

class Spinner:
    spinner_cycle: Iterator[str]
    disable: bool
    beep: bool
    force: bool
    stream: _Stream
    stop_running: threading.Event | None
    spin_thread: threading.Thread | None
    def __init__(self, beep: bool = False, disable: bool = False, force: bool = False, stream: _Stream = ...) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def init_spin(self) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> Literal[False]: ...

def spinner(beep: bool = False, disable: bool = False, force: bool = False, stream: _Stream = ...) -> Spinner:
    """
    This function creates a context manager that is used to display a
    spinner on stdout as long as the context has not exited.

    The spinner is created only if stdout is not redirected, or if the spinner
    is forced using the `force` parameter.

    Parameters
    ----------
    beep : bool
        Beep when spinner finishes.
    disable : bool
        Hide spinner.
    force : bool
        Force creation of spinner even when stdout is redirected.

    Example
    -------

        with spinner():
            do_something()
            do_something_else()
    """
    ...
