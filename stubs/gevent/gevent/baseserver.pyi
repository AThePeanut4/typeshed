"""Base class for implementing servers"""

from collections.abc import Callable, Container
from types import TracebackType
from typing import Generic, Literal, Protocol, type_check_only
from typing_extensions import ParamSpec, Self, TypeAlias, TypeVarTuple, Unpack

from gevent._types import _Loop
from gevent.pool import Pool
from gevent.socket import socket as _GeventSocket
from greenlet import greenlet

_Ts = TypeVarTuple("_Ts")
_P = ParamSpec("_P")

@type_check_only
class _SpawnFunc(Protocol):
    def __call__(self, func: Callable[_P, object], /, *args: _P.args, **kwargs: _P.kwargs) -> greenlet: ...

_Spawner: TypeAlias = Pool | _SpawnFunc | int | Literal["default"] | None

class BaseServer(Generic[Unpack[_Ts]]):
    min_delay: float
    max_delay: float
    max_accept: int
    stop_timeout: float
    fatal_errors: Container[int]
    pool: Pool | None
    delay: float
    loop: _Loop
    family: int
    address: str | tuple[str, int]
    socket: _GeventSocket
    handle: Callable[[Unpack[_Ts]], object]
    def __init__(
        self,
        listener: _GeventSocket | tuple[str, int] | str,
        handle: Callable[[Unpack[_Ts]], object] | None = None,
        spawn: _Spawner = "default",
    ) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, typ: type[BaseException] | None, value: BaseException | None, tb: TracebackType | None, /) -> None: ...
    def set_listener(self, listener: _GeventSocket | tuple[str, int] | str) -> None: ...
    def set_spawn(self, spawn: _Spawner) -> None: ...
    def set_handle(self, handle: Callable[[Unpack[_Ts]], object]) -> None: ...
    def start_accepting(self) -> None: ...
    def stop_accepting(self) -> None: ...
    def do_handle(self, *args: Unpack[_Ts]) -> None: ...
    def do_close(self, *args: Unpack[_Ts]) -> None: ...
    def do_read(self) -> tuple[Unpack[_Ts]] | None: ...
    def full(self) -> bool: ...
    @property
    def server_host(self) -> str | None:
        """IP address that the server is bound to (string)."""
        ...
    @property
    def server_port(self) -> int | None:
        """Port that the server is bound to (an integer)."""
        ...
    def init_socket(self) -> None:
        """
        If the user initialized the server with an address rather than
        socket, then this function must create a socket, bind it, and
        put it into listening mode.

        It is not supposed to be called by the user, it is called by :meth:`start` before starting
        the accept loop.
        """
        ...
    @property
    def started(self) -> bool: ...
    def start(self) -> None:
        """
        Start accepting the connections.

        If an address was provided in the constructor, then also create a socket,
        bind it and put it into the listening mode.
        """
        ...
    def close(self) -> None:
        """Close the listener socket and stop accepting."""
        ...
    @property
    def closed(self) -> bool: ...
    def stop(self, timeout: float | None = None) -> None:
        """
        Stop accepting the connections and close the listening socket.

        If the server uses a pool to spawn the requests, then
        :meth:`stop` also waits for all the handlers to exit. If there
        are still handlers executing after *timeout* has expired
        (default 1 second, :attr:`stop_timeout`), then the currently
        running handlers in the pool are killed.

        If the server does not use a pool, then this merely stops accepting connections;
        any spawned greenlets that are handling requests continue running until
        they naturally complete.
        """
        ...
    def serve_forever(self, stop_timeout: float | None = None) -> None:
        """Start the server if it hasn't been already started and wait until it's stopped."""
        ...
    def is_fatal_error(self, ex: BaseException) -> bool: ...

__all__ = ["BaseServer"]
