import asyncio
import socket
from _typeshed import Incomplete, Unused
from _typeshed.wsgi import WSGIEnvironment
from collections.abc import Awaitable, Callable
from ssl import SSLContext
from typing import Any, Literal, TypedDict, type_check_only

from wsproto import ConnectionType, WSConnection
from wsproto.events import Request
from wsproto.frame_protocol import CloseReason

from .asgi import WebSocketASGI, _SocketDataBase, _SocketDataBytes, _SocketDataProtocol, _SocketDataStr

class AioBase:
    subprotocol: str | None
    connection_type: ConnectionType
    receive_bytes: int
    ping_interval: float | None
    max_message_size: int | None
    pong_received: bool
    input_buffer: list[bytes | str]
    incoming_message: bytes | str | None
    incoming_message_len: int
    connected: bool
    is_server: bool
    close_reason: CloseReason
    close_message: str
    rsock: asyncio.StreamReader
    wsock: asyncio.StreamWriter
    event: asyncio.Event
    ws: WSConnection | None
    task: asyncio.Task[None]
    def __init__(
        self,
        connection_type: ConnectionType | None = None,
        receive_bytes: int = 4096,
        ping_interval: float | None = None,
        max_message_size: int | None = None,
    ) -> None: ...
    async def connect(self) -> None: ...
    async def handshake(self) -> None: ...
    # data can be antyhing. a special case is made for `bytes`, anything else is converted to `str`.
    async def send(self, data: bytes | Any) -> None:
        """
        Send data over the WebSocket connection.

        :param data: The data to send. If ``data`` is of type ``bytes``, then
                     a binary message is sent. Else, the message is sent in
                     text format.
        """
        ...
    async def receive(self, timeout: float | None = None) -> bytes | str | None:
        """
        Receive data over the WebSocket connection.

        :param timeout: Amount of time to wait for the data, in seconds. Set
                        to ``None`` (the default) to wait indefinitely. Set
                        to 0 to read without blocking.

        The data received is returned, as ``bytes`` or ``str``, depending on
        the type of the incoming message.
        """
        ...
    async def close(self, reason: CloseReason | None = None, message: str | None = None) -> None:
        """
        Close the WebSocket connection.

        :param reason: A numeric status code indicating the reason of the
                       closure, as defined by the WebSocket specification. The
                       default is 1000 (normal closure).
        :param message: A text message to be sent to the other side.
        """
        ...
    def choose_subprotocol(self, request: Request) -> str | None: ...

@type_check_only
class _AioServerRequest(TypedDict):
    # this is `aiohttp.web.Request`
    aiohttp: Incomplete
    sock: None
    headers: None

class AioServer(AioBase):
    """
    This class implements a WebSocket server.

    Instead of creating an instance of this class directly, use the
    ``accept()`` class method to create individual instances of the server,
    each bound to a client request.
    """
    request: _AioServerRequest
    headers: dict[str, Any]
    subprotocols: list[str]
    is_server: Literal[True]
    mode: str
    connected: bool
    def __init__(
        self,
        request: _AioServerRequest,
        subprotocols: list[str] | None = None,
        receive_bytes: int = 4096,
        ping_interval: float | None = None,
        max_message_size: int | None = None,
    ) -> None: ...
    @classmethod
    async def accept(
        cls,
        # this is `aiohttp.web.Request`
        aiohttp=None,
        asgi: (
            tuple[
                WSGIEnvironment,
                Callable[[], Awaitable[_SocketDataBytes | _SocketDataStr]],
                Callable[[_SocketDataBase | _SocketDataProtocol | _SocketDataBytes | _SocketDataStr], Awaitable[None]],
            ]
            | None
        ) = None,
        sock: socket.socket | None = None,
        headers: dict[str, Any] | None = None,
        subprotocols: list[str] | None = None,
        receive_bytes: int = 4096,
        ping_interval: float | None = None,
        max_message_size: int | None = None,
    ) -> WebSocketASGI | AioServer:
        """
        Accept a WebSocket connection from a client.

        :param aiohttp: The request object from aiohttp. If this argument is
                        provided, ``asgi``, ``sock`` and ``headers`` must not
                        be set.
        :param asgi: A (scope, receive, send) tuple from an ASGI request. If
                     this argument is provided, ``aiohttp``, ``sock`` and
                     ``headers`` must not be set.
        :param sock: A connected socket to use. If this argument is provided,
                     ``aiohttp`` and ``asgi`` must not be set. The ``headers``
                     argument must be set with the incoming request headers.
        :param headers: A dictionary with the incoming request headers, when
                        ``sock`` is used.
        :param subprotocols: A list of supported subprotocols, or ``None`` (the
                             default) to disable subprotocol negotiation.
        :param receive_bytes: The size of the receive buffer, in bytes. The
                              default is 4096.
        :param ping_interval: Send ping packets to clients at the requested
                              interval in seconds. Set to ``None`` (the
                              default) to disable ping/pong logic. Enable to
                              prevent disconnections when the line is idle for
                              a certain amount of time, or to detect
                              unresponsive clients and disconnect them. A
                              recommended interval is 25 seconds.
        :param max_message_size: The maximum size allowed for a message, in
                                 bytes, or ``None`` for no limit. The default
                                 is ``None``.
        """
        ...
    async def handshake(self) -> None: ...
    def choose_subprotocol(self, request: Request) -> str | None:
        """
        Choose a subprotocol to use for the WebSocket connection.

        The default implementation selects the first protocol requested by the
        client that is accepted by the server. Subclasses can override this
        method to implement a different subprotocol negotiation algorithm.

        :param request: A ``Request`` object.

        The method should return the subprotocol to use, or ``None`` if no
        subprotocol is chosen.
        """
        ...

class AioClient(AioBase):
    """
    This class implements a WebSocket client.

    Instead of creating an instance of this class directly, use the
    ``connect()`` class method to create an instance that is connected to a
    server.
    """
    url: str
    ssl_context: SSLContext | None
    is_secure: bool
    host: str
    port: int
    path: str
    subprotocols: list[str]
    extra_headeers: list[tuple[bytes, bytes]]
    subprotocol: str | None
    connected: bool
    def __init__(
        self,
        url: str,
        subprotocols: list[str] | None = None,
        headers: dict[str, Any] | None = None,
        receive_bytes: int = 4096,
        ping_interval: float | None = None,
        max_message_size: int | None = None,
        ssl_context: SSLContext | None = None,
    ) -> None: ...
    # the source code itself has this override
    @classmethod
    async def connect(  # type: ignore[override]
        cls,
        url: str,
        subprotocols: list[str] | None = None,
        headers: dict[str, Any] | None = None,
        receive_bytes: int = 4096,
        ping_interval: float | None = None,
        max_message_size: int | None = None,
        ssl_context: SSLContext | None = None,
        thread_class: Unused = None,
        event_class: Unused = None,
    ) -> AioClient:
        """
        Returns a WebSocket client connection.

        :param url: The connection URL. Both ``ws://`` and ``wss://`` URLs are
                    accepted.
        :param subprotocols: The name of the subprotocol to use, or a list of
                             subprotocol names in order of preference. Set to
                             ``None`` (the default) to not use a subprotocol.
        :param headers: A dictionary or list of tuples with additional HTTP
                        headers to send with the connection request. Note that
                        custom headers are not supported by the WebSocket
                        protocol, so the use of this parameter is not
                        recommended.
        :param receive_bytes: The size of the receive buffer, in bytes. The
                              default is 4096.
        :param ping_interval: Send ping packets to the server at the requested
                              interval in seconds. Set to ``None`` (the
                              default) to disable ping/pong logic. Enable to
                              prevent disconnections when the line is idle for
                              a certain amount of time, or to detect an
                              unresponsive server and disconnect. A recommended
                              interval is 25 seconds. In general it is
                              preferred to enable ping/pong on the server, and
                              let the client respond with pong (which it does
                              regardless of this setting).
        :param max_message_size: The maximum size allowed for a message, in
                                 bytes, or ``None`` for no limit. The default
                                 is ``None``.
        :param ssl_context: An ``SSLContext`` instance, if a default SSL
                            context isn't sufficient.
        """
        ...
    async def handshake(self) -> None: ...
    async def close(self, reason: CloseReason | None = None, message: str | None = None) -> None: ...
