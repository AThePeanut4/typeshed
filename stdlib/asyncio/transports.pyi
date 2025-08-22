"""Abstract Transport class."""

from asyncio.events import AbstractEventLoop
from asyncio.protocols import BaseProtocol
from collections.abc import Iterable, Mapping
from socket import _Address
from typing import Any

# Keep asyncio.__all__ updated with any changes to __all__ here
__all__ = ("BaseTransport", "ReadTransport", "WriteTransport", "Transport", "DatagramTransport", "SubprocessTransport")

class BaseTransport:
    __slots__ = ("_extra",)
    def __init__(self, extra: Mapping[str, Any] | None = None) -> None: ...
    def get_extra_info(self, name: str, default: Any = None) -> Any:
        """Get optional transport information."""
        ...
    def is_closing(self) -> bool:
        """Return True if the transport is closing or closed."""
        ...
    def close(self) -> None:
        """
        Close the transport.

        Buffered data will be flushed asynchronously.  No more data
        will be received.  After all buffered data is flushed, the
        protocol's connection_lost() method will (eventually) be
        called with None as its argument.
        """
        ...
    def set_protocol(self, protocol: BaseProtocol) -> None:
        """Set a new protocol."""
        ...
    def get_protocol(self) -> BaseProtocol:
        """Return the current protocol."""
        ...

class ReadTransport(BaseTransport):
    __slots__ = ()
    def is_reading(self) -> bool: ...
    def pause_reading(self) -> None: ...
    def resume_reading(self) -> None: ...

class WriteTransport(BaseTransport):
    __slots__ = ()
    def set_write_buffer_limits(self, high: int | None = None, low: int | None = None) -> None: ...
    def get_write_buffer_size(self) -> int: ...
    def get_write_buffer_limits(self) -> tuple[int, int]: ...
    def write(self, data: bytes | bytearray | memoryview[Any]) -> None: ...  # any memoryview format or shape
    def writelines(
        self, list_of_data: Iterable[bytes | bytearray | memoryview[Any]]
    ) -> None:
        """
        Write a list (or any iterable) of data bytes to the transport.

class Transport(ReadTransport, WriteTransport):
    __slots__ = ()

class DatagramTransport(BaseTransport):
    __slots__ = ()
    def sendto(self, data: bytes | bytearray | memoryview, addr: _Address | None = None) -> None: ...
    def abort(self) -> None: ...

class SubprocessTransport(BaseTransport):
    __slots__ = ()
    def get_pid(self) -> int: ...
    def get_returncode(self) -> int | None: ...
    def get_pipe_transport(self, fd: int) -> BaseTransport | None: ...
    def send_signal(self, signal: int) -> None: ...
    def terminate(self) -> None: ...
    def kill(self) -> None: ...

class _FlowControlMixin(Transport):
    __slots__ = ("_loop", "_protocol_paused", "_high_water", "_low_water")
    def __init__(self, extra: Mapping[str, Any] | None = None, loop: AbstractEventLoop | None = None) -> None: ...
