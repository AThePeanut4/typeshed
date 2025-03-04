import socket
import sys
from _typeshed import Incomplete, ReadableBuffer
from collections.abc import Iterable
from types import TracebackType
from typing import Any, Generic, SupportsIndex, TypeVar
from typing_extensions import Self, TypeAlias

__all__ = ["Client", "Listener", "Pipe", "wait"]

# https://docs.python.org/3/library/multiprocessing.html#address-formats
_Address: TypeAlias = str | tuple[str, int]

# Defaulting to Any to avoid forcing generics on a lot of pre-existing code
_SendT_contra = TypeVar("_SendT_contra", contravariant=True, default=Any)
_RecvT_co = TypeVar("_RecvT_co", covariant=True, default=Any)

class _ConnectionBase(Generic[_SendT_contra, _RecvT_co]):
    def __init__(self, handle: SupportsIndex, readable: bool = True, writable: bool = True) -> None: ...
    @property
    def closed(self) -> bool:
        """True if the connection is closed"""
        ...
    @property
    def readable(self) -> bool:
        """True if the connection is readable"""
        ...
    @property
    def writable(self) -> bool: ...  # undocumented
    def fileno(self) -> int: ...
    def close(self) -> None: ...
    def send_bytes(self, buf: ReadableBuffer, offset: int = 0, size: int | None = None) -> None: ...
    def send(self, obj: _SendT_contra) -> None: ...
    def recv_bytes(self, maxlength: int | None = None) -> bytes: ...
    def recv_bytes_into(self, buf: Any, offset: int = 0) -> int: ...
    def recv(self) -> _RecvT_co: ...
    def poll(self, timeout: float | None = 0.0) -> bool: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_value: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...
    def __del__(self) -> None: ...

class Connection(_ConnectionBase[_SendT_contra, _RecvT_co]): ...

if sys.platform == "win32":
    class PipeConnection(_ConnectionBase[_SendT_contra, _RecvT_co]): ...

class Listener:
    """
    Returns a listener object.

    This is a wrapper for a bound socket which is 'listening' for
    connections, or for a Windows named pipe.
    """
    def __init__(
        self, address: _Address | None = None, family: str | None = None, backlog: int = 1, authkey: bytes | None = None
    ) -> None: ...
    def accept(self) -> Connection[Incomplete, Incomplete]:
        """
        Accept a connection on the bound socket or named pipe of `self`.

        Returns a `Connection` object.
        """
        ...
    def close(self) -> None:
        """Close the bound socket or named pipe of `self`."""
        ...
    @property
    def address(self) -> _Address: ...
    @property
    def last_accepted(self) -> _Address | None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_value: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...

# Any: send and recv methods unused
if sys.version_info >= (3, 12):
    def deliver_challenge(connection: Connection[Any, Any], authkey: bytes, digest_name: str = "sha256") -> None: ...

else:
    def deliver_challenge(connection: Connection[Any, Any], authkey: bytes) -> None: ...

def answer_challenge(connection: Connection[Any, Any], authkey: bytes) -> None: ...
def wait(
    object_list: Iterable[Connection[_SendT_contra, _RecvT_co] | socket.socket | int], timeout: float | None = None
) -> list[Connection[_SendT_contra, _RecvT_co] | socket.socket | int]: ...
def Client(address: _Address, family: str | None = None, authkey: bytes | None = None) -> Connection[Any, Any]: ...

# N.B. Keep this in sync with multiprocessing.context.BaseContext.Pipe.
# _ConnectionBase is the common base class of Connection and PipeConnection
# and can be used in cross-platform code.
#
# The two connections should have the same generic types but inverted (Connection[_T1, _T2], Connection[_T2, _T1]).
# However, TypeVars scoped entirely within a return annotation is unspecified in the spec.
if sys.platform != "win32":
    def Pipe(duplex: bool = True) -> tuple[Connection[Any, Any], Connection[Any, Any]]:
        """Returns pair of connection objects at either end of a pipe"""
        ...

else:
    def Pipe(duplex: bool = True) -> tuple[PipeConnection[Any, Any], PipeConnection[Any, Any]]: ...
