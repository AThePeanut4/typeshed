from _typeshed import Incomplete, Unused
from abc import abstractmethod
from collections.abc import Callable, Iterable, Mapping
from queue import Queue
from socket import socket
from typing import Any, ClassVar
from typing_extensions import Self, TypeAlias

from .credentials import CredentialProvider
from .retry import Retry

ssl_available: bool
SYM_STAR: bytes
SYM_DOLLAR: bytes
SYM_CRLF: bytes
SYM_EMPTY: bytes
SERVER_CLOSED_CONNECTION_ERROR: str
NONBLOCKING_EXCEPTIONS: tuple[type[Exception], ...]
NONBLOCKING_EXCEPTION_ERROR_NUMBERS: dict[type[Exception], int]
SENTINEL: object
MODULE_LOAD_ERROR: str
NO_SUCH_MODULE_ERROR: str
MODULE_UNLOAD_NOT_POSSIBLE_ERROR: str
MODULE_EXPORTS_DATA_TYPES_ERROR: str
FALSE_STRINGS: tuple[str, ...]
URL_QUERY_ARGUMENT_PARSERS: dict[str, Callable[[Any], Any]]

# Options as passed to Pool.get_connection().
_ConnectionPoolOptions: TypeAlias = Any
_ConnectFunc: TypeAlias = Callable[[Connection], object]

class BaseParser:
    EXCEPTION_CLASSES: ClassVar[dict[str, type[Exception] | dict[str, type[Exception]]]]
    @classmethod
    def parse_error(cls, response: str) -> Exception:
        """Parse an error response"""
        ...

class SocketBuffer:
    socket_read_size: int
    bytes_written: int
    bytes_read: int
    socket_timeout: float | None
    def __init__(self, socket: socket, socket_read_size: int, socket_timeout: float | None) -> None: ...
    def unread_bytes(self) -> int:
        """Remaining unread length of buffer"""
        ...
    def can_read(self, timeout: float | None) -> bool: ...
    def read(self, length: int) -> bytes: ...
    def readline(self) -> bytes: ...
    def get_pos(self) -> int:
        """Get current read position"""
        ...
    def rewind(self, pos: int) -> None:
        """Rewind the buffer to a specific position, to re-start reading"""
        ...
    def purge(self) -> None:
        """After a successful read, purge the read part of buffer"""
        ...
    def close(self) -> None: ...

class PythonParser(BaseParser):
    """Plain Python parsing class"""
    encoding: str
    socket_read_size: int
    encoder: Encoder | None
    def __init__(self, socket_read_size: int) -> None: ...
    def __del__(self) -> None: ...
    def on_connect(self, connection: Connection) -> None:
        """Called when the socket connects"""
        ...
    def on_disconnect(self) -> None:
        """Called when the socket disconnects"""
        ...
    def can_read(self, timeout: float | None) -> bool: ...
    def read_response(self, disable_decoding: bool = False) -> Any: ...  # `str | bytes` or `list[str | bytes]`

class HiredisParser(BaseParser):
    """Parser class for connections using Hiredis"""
    socket_read_size: int
    def __init__(self, socket_read_size: int) -> None: ...
    def __del__(self) -> None: ...
    def on_connect(self, connection: Connection, **kwargs) -> None: ...
    def on_disconnect(self) -> None: ...
    def can_read(self, timeout: float | None) -> bool: ...
    def read_from_socket(self, timeout: float | None = ..., raise_on_timeout: bool = True) -> bool: ...
    def read_response(self, disable_decoding: bool = False) -> Any: ...  # `str | bytes` or `list[str | bytes]`

DefaultParser: type[BaseParser]  # Hiredis or PythonParser

_Encodable: TypeAlias = str | bytes | memoryview | bool | float

class Encoder:
    """Encode strings to bytes-like and decode bytes-like to strings"""
    encoding: str
    encoding_errors: str
    decode_responses: bool
    def __init__(self, encoding: str, encoding_errors: str, decode_responses: bool) -> None: ...
    def encode(self, value: _Encodable) -> bytes:
        """Return a bytestring or bytes-like representation of the value"""
        ...
    def decode(self, value: str | bytes | memoryview, force: bool = False) -> str:
        """Return a unicode string from the bytes-like representation"""
        ...

class AbstractConnection:
    """Manages communication to and from a Redis server"""
    pid: int
    db: int
    client_name: str | None
    credential_provider: CredentialProvider | None
    password: str | None
    username: str | None
    socket_timeout: float | None
    socket_connect_timeout: float | None
    retry_on_timeout: bool
    retry_on_error: list[type[Exception]]
    retry: Retry
    health_check_interval: int
    next_health_check: int
    redis_connect_func: _ConnectFunc | None
    encoder: Encoder

    def __init__(
        self,
        db: int = 0,
        password: str | None = None,
        socket_timeout: float | None = None,
        socket_connect_timeout: float | None = None,
        retry_on_timeout: bool = False,
        retry_on_error: list[type[Exception]] = ...,
        encoding: str = "utf-8",
        encoding_errors: str = "strict",
        decode_responses: bool = False,
        parser_class: type[BaseParser] = ...,
        socket_read_size: int = 65536,
        health_check_interval: int = 0,
        client_name: str | None = None,
        username: str | None = None,
        retry: Retry | None = None,
        redis_connect_func: _ConnectFunc | None = None,
        credential_provider: CredentialProvider | None = None,
        command_packer: Incomplete | None = None,
    ) -> None:
        """
        Initialize a new Connection.
        To specify a retry policy for specific errors, first set
        `retry_on_error` to a list of the error/s to retry on, then set
        `retry` to a valid `Retry` object.
        To retry on TimeoutError, `retry_on_timeout` can also be set to `True`.
        """
        ...
    @abstractmethod
    def repr_pieces(self) -> list[tuple[str, Any]]: ...
    def register_connect_callback(self, callback: _ConnectFunc) -> None: ...
    def clear_connect_callbacks(self) -> None: ...
    def set_parser(self, parser_class: type[BaseParser]) -> None:
        """
        Creates a new instance of parser_class with socket size:
        _socket_read_size and assigns it to the parser for the connection
        :param parser_class: The required parser class
        """
        ...
    def connect(self) -> None:
        """Connects to the Redis server if not already connected"""
        ...
    def on_connect(self) -> None:
        """Initialize the connection, authenticate and select a database"""
        ...
    def disconnect(self, *args: Unused) -> None:
        """Disconnects from the Redis server"""
        ...
    def check_health(self) -> None:
        """Check the health of the connection with a PING/PONG"""
        ...
    def send_packed_command(self, command: str | Iterable[str], check_health: bool = True) -> None:
        """Send an already packed command to the Redis server"""
        ...
    def send_command(self, *args, **kwargs) -> None:
        """Pack and send a command to the Redis server"""
        ...
    def can_read(self, timeout: float | None = 0) -> bool:
        """Poll the socket to see if there's data that can be read."""
        ...
    def read_response(
        self, disable_decoding: bool = False, *, disconnect_on_error: bool = True
    ) -> Any:
        """Read the response from a previously sent command"""
        ...
    def pack_command(self, *args) -> list[bytes]:
        """Pack a series of arguments into the Redis protocol"""
        ...
    def pack_commands(self, commands: Iterable[Iterable[Incomplete]]) -> list[bytes]:
        """Pack multiple commands into the Redis protocol"""
        ...

class Connection(AbstractConnection):
    """Manages TCP communication to and from a Redis server"""
    host: str
    port: int
    socket_keepalive: bool
    socket_keepalive_options: Mapping[str, int | str]
    socket_type: int
    def __init__(
        self,
        host: str = "localhost",
        port: int = 6379,
        socket_keepalive: bool = False,
        socket_keepalive_options: Mapping[str, int | str] | None = None,
        socket_type: int = 0,
        *,
        db: int = 0,
        password: str | None = None,
        socket_timeout: float | None = None,
        socket_connect_timeout: float | None = None,
        retry_on_timeout: bool = False,
        retry_on_error: list[type[Exception]] = ...,
        encoding: str = "utf-8",
        encoding_errors: str = "strict",
        decode_responses: bool = False,
        parser_class: type[BaseParser] = ...,
        socket_read_size: int = 65536,
        health_check_interval: int = 0,
        client_name: str | None = None,
        username: str | None = None,
        retry: Retry | None = None,
        redis_connect_func: _ConnectFunc | None = None,
        credential_provider: CredentialProvider | None = None,
        command_packer: Incomplete | None = None,
    ) -> None: ...
    def repr_pieces(self) -> list[tuple[str, Any]]: ...

class SSLConnection(Connection):
    """
    Manages SSL connections to and from the Redis server(s).
    This class extends the Connection class, adding SSL functionality, and making
    use of ssl.SSLContext (https://docs.python.org/3/library/ssl.html#ssl.SSLContext)
    """
    keyfile: Any
    certfile: Any
    cert_reqs: Any
    ca_certs: Any
    ca_path: Incomplete | None
    check_hostname: bool
    certificate_password: Incomplete | None
    ssl_validate_ocsp: bool
    ssl_validate_ocsp_stapled: bool  # added in 4.1.1
    ssl_ocsp_context: Incomplete | None  # added in 4.1.1
    ssl_ocsp_expected_cert: Incomplete | None  # added in 4.1.1
    def __init__(
        self,
        ssl_keyfile=None,
        ssl_certfile=None,
        ssl_cert_reqs="required",
        ssl_ca_certs=None,
        ssl_ca_data: Incomplete | None = None,
        ssl_check_hostname: bool = False,
        ssl_ca_path: Incomplete | None = None,
        ssl_password: Incomplete | None = None,
        ssl_validate_ocsp: bool = False,
        ssl_validate_ocsp_stapled: bool = False,  # added in 4.1.1
        ssl_ocsp_context: Incomplete | None = None,  # added in 4.1.1
        ssl_ocsp_expected_cert: Incomplete | None = None,  # added in 4.1.1
        *,
        host: str = "localhost",
        port: int = 6379,
        socket_timeout: float | None = None,
        socket_connect_timeout: float | None = None,
        socket_keepalive: bool = False,
        socket_keepalive_options: Mapping[str, int | str] | None = None,
        socket_type: int = 0,
        db: int = 0,
        password: str | None = None,
        retry_on_timeout: bool = False,
        retry_on_error: list[type[Exception]] = ...,
        encoding: str = "utf-8",
        encoding_errors: str = "strict",
        decode_responses: bool = False,
        parser_class: type[BaseParser] = ...,
        socket_read_size: int = 65536,
        health_check_interval: int = 0,
        client_name: str | None = None,
        username: str | None = None,
        retry: Retry | None = None,
        redis_connect_func: _ConnectFunc | None = None,
        credential_provider: CredentialProvider | None = None,
        command_packer: Incomplete | None = None,
    ) -> None:
        """
        Constructor

        Args:
            ssl_keyfile: Path to an ssl private key. Defaults to None.
            ssl_certfile: Path to an ssl certificate. Defaults to None.
            ssl_cert_reqs: The string value for the SSLContext.verify_mode (none, optional, required). Defaults to "required".
            ssl_ca_certs: The path to a file of concatenated CA certificates in PEM format. Defaults to None.
            ssl_ca_data: Either an ASCII string of one or more PEM-encoded certificates or a bytes-like object of DER-encoded certificates.
            ssl_check_hostname: If set, match the hostname during the SSL handshake. Defaults to False.
            ssl_ca_path: The path to a directory containing several CA certificates in PEM format. Defaults to None.
            ssl_password: Password for unlocking an encrypted private key. Defaults to None.

            ssl_validate_ocsp: If set, perform a full ocsp validation (i.e not a stapled verification)
            ssl_validate_ocsp_stapled: If set, perform a validation on a stapled ocsp response
            ssl_ocsp_context: A fully initialized OpenSSL.SSL.Context object to be used in verifying the ssl_ocsp_expected_cert
            ssl_ocsp_expected_cert: A PEM armoured string containing the expected certificate to be returned from the ocsp verification service.

        Raises:
            RedisError
        """
        ...

class UnixDomainSocketConnection(AbstractConnection):
    """Manages UDS communication to and from a Redis server"""
    path: str
    def __init__(
        self,
        path: str = "",
        *,
        db: int = 0,
        password: str | None = None,
        socket_timeout: float | None = None,
        socket_connect_timeout: float | None = None,
        retry_on_timeout: bool = False,
        retry_on_error: list[type[Exception]] = ...,
        encoding: str = "utf-8",
        encoding_errors: str = "strict",
        decode_responses: bool = False,
        parser_class: type[BaseParser] = ...,
        socket_read_size: int = 65536,
        health_check_interval: int = 0,
        client_name: str | None = None,
        username: str | None = None,
        retry: Retry | None = None,
        redis_connect_func: _ConnectFunc | None = None,
        credential_provider: CredentialProvider | None = None,
        command_packer: Incomplete | None = None,
    ) -> None: ...
    def repr_pieces(self) -> list[tuple[str, Any]]: ...

# TODO: make generic on `connection_class`
class ConnectionPool:
    """
    Create a connection pool. ``If max_connections`` is set, then this
    object raises :py:class:`~redis.exceptions.ConnectionError` when the pool's
    limit is reached.

    By default, TCP connections are created unless ``connection_class``
    is specified. Use class:`.UnixDomainSocketConnection` for
    unix sockets.

    Any additional keyword arguments are passed to the constructor of
    ``connection_class``.
    """
    connection_class: type[Connection]
    connection_kwargs: dict[str, Any]
    max_connections: int
    pid: int
    @classmethod
    def from_url(cls, url: str, *, db: int = ..., decode_components: bool = ..., **kwargs) -> Self:
        """
        Return a connection pool configured from the given URL.

        For example::

            redis://[[username]:[password]]@localhost:6379/0
            rediss://[[username]:[password]]@localhost:6379/0
            unix://[username@]/path/to/socket.sock?db=0[&password=password]

        Three URL schemes are supported:

        - `redis://` creates a TCP socket connection. See more at:
          <https://www.iana.org/assignments/uri-schemes/prov/redis>
        - `rediss://` creates a SSL wrapped TCP socket connection. See more at:
          <https://www.iana.org/assignments/uri-schemes/prov/rediss>
        - ``unix://``: creates a Unix Domain Socket connection.

        The username, password, hostname, path and all querystring values
        are passed through urllib.parse.unquote in order to replace any
        percent-encoded values with their corresponding characters.

        There are several ways to specify a database number. The first value
        found will be used:

            1. A ``db`` querystring option, e.g. redis://localhost?db=0
            2. If using the redis:// or rediss:// schemes, the path argument
               of the url, e.g. redis://localhost/0
            3. A ``db`` keyword argument to this function.

        If none of these options are specified, the default db=0 is used.

        All querystring options are cast to their appropriate Python types.
        Boolean arguments can be specified with string values "True"/"False"
        or "Yes"/"No". Values that cannot be properly cast cause a
        ``ValueError`` to be raised. Once parsed, the querystring arguments
        and keyword arguments are passed to the ``ConnectionPool``'s
        class initializer. In the case of conflicting arguments, querystring
        arguments always win.
        """
        ...
    def __init__(
        self, connection_class: type[AbstractConnection] = ..., max_connections: int | None = None, **connection_kwargs
    ) -> None: ...
    def reset(self) -> None: ...
    def get_connection(self, command_name: Unused, *keys, **options: _ConnectionPoolOptions) -> Connection:
        """Get a connection from the pool"""
        ...
    def make_connection(self) -> Connection:
        """Create a new connection"""
        ...
    def release(self, connection: Connection) -> None:
        """Releases the connection back to the pool"""
        ...
    def disconnect(self, inuse_connections: bool = True) -> None:
        """
        Disconnects connections in the pool

        If ``inuse_connections`` is True, disconnect connections that are
        current in use, potentially by other threads. Otherwise only disconnect
        connections that are idle in the pool.
        """
        ...
    def get_encoder(self) -> Encoder:
        """Return an encoder based on encoding settings"""
        ...
    def owns_connection(self, connection: Connection) -> bool: ...

class BlockingConnectionPool(ConnectionPool):
    """
    Thread-safe blocking connection pool::

        >>> from redis.client import Redis
        >>> client = Redis(connection_pool=BlockingConnectionPool())

    It performs the same function as the default
    :py:class:`~redis.ConnectionPool` implementation, in that,
    it maintains a pool of reusable connections that can be shared by
    multiple redis clients (safely across threads if required).

    The difference is that, in the event that a client tries to get a
    connection from the pool when all of connections are in use, rather than
    raising a :py:class:`~redis.ConnectionError` (as the default
    :py:class:`~redis.ConnectionPool` implementation does), it
    makes the client wait ("blocks") for a specified number of seconds until
    a connection becomes available.

    Use ``max_connections`` to increase / decrease the pool size::

        >>> pool = BlockingConnectionPool(max_connections=10)

    Use ``timeout`` to tell it either how many seconds to wait for a connection
    to become available, or to block forever:

        >>> # Block forever.
        >>> pool = BlockingConnectionPool(timeout=None)

        >>> # Raise a ``ConnectionError`` after five seconds if a connection is
        >>> # not available.
        >>> pool = BlockingConnectionPool(timeout=5)
    """
    queue_class: type[Queue[Any]]
    timeout: float
    pool: Queue[Connection | None]  # might not be defined
    def __init__(
        self,
        max_connections: int = 50,
        timeout: float = 20,
        connection_class: type[Connection] = ...,
        queue_class: type[Queue[Any]] = ...,
        **connection_kwargs,
    ) -> None: ...
    def disconnect(self) -> None:
        """Disconnects all connections in the pool."""
        ...

def to_bool(value: object) -> bool: ...
def parse_url(url: str) -> dict[str, Any]: ...
