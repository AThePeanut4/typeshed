from collections.abc import AsyncIterator, Iterable, Mapping
from typing import Any, Literal, TypedDict, TypeVar, overload

from redis.asyncio.client import Redis
from redis.asyncio.connection import (
    BaseParser,
    ConnectCallbackT,
    Connection,
    ConnectionPool,
    Encoder,
    SSLConnection,
    _ConnectionT,
    _Sentinel,
)
from redis.asyncio.retry import Retry
from redis.commands import AsyncSentinelCommands
from redis.credentials import CredentialProvider
from redis.exceptions import ConnectionError, RedisError

_RedisT = TypeVar("_RedisT", bound=Redis[Any])

class MasterNotFoundError(ConnectionError): ...
class SlaveNotFoundError(ConnectionError): ...

class SentinelManagedConnection(Connection):
    connection_pool: ConnectionPool[Any] | None
    def __init__(
        self,
        *,
        connection_pool: ConnectionPool[Any] | None,
        # **kwargs forwarded to Connection.
        host: str = "localhost",
        port: str | int = 6379,
        socket_keepalive: bool = False,
        socket_keepalive_options: Mapping[int, int | bytes] | None = None,
        socket_type: int = 0,
        db: str | int = 0,
        password: str | None = None,
        socket_timeout: float | None = None,
        socket_connect_timeout: float | None = None,
        retry_on_timeout: bool = False,
        retry_on_error: list[type[RedisError]] | _Sentinel = ...,
        encoding: str = "utf-8",
        encoding_errors: str = "strict",
        decode_responses: bool = False,
        parser_class: type[BaseParser] = ...,
        socket_read_size: int = 65536,
        health_check_interval: float = 0,
        client_name: str | None = None,
        username: str | None = None,
        retry: Retry | None = None,
        redis_connect_func: ConnectCallbackT | None = None,
        encoder_class: type[Encoder] = ...,
        credential_provider: CredentialProvider | None = None,
    ) -> None: ...
    async def connect_to(self, address: tuple[str, int]) -> None: ...
    async def connect(self) -> None: ...

class SentinelManagedSSLConnection(SentinelManagedConnection, SSLConnection): ...

class SentinelConnectionPool(ConnectionPool[_ConnectionT]):
    """
    Sentinel backed connection pool.

    If ``check_connection`` flag is set to True, SentinelManagedConnection
    sends a PING command right after establishing the connection.
    """
    is_master: bool
    check_connection: bool
    service_name: str
    sentinel_manager: Sentinel
    master_address: tuple[str, int] | None
    slave_rr_counter: int | None

    def __init__(
        self,
        service_name: str,
        sentinel_manager: Sentinel,
        *,
        ssl: bool = False,
        connection_class: type[SentinelManagedConnection] = ...,
        is_master: bool = True,
        check_connection: bool = False,
        # **kwargs ultimately forwarded to construction Connection instances.
        host: str = "localhost",
        port: str | int = 6379,
        socket_keepalive: bool = False,
        socket_keepalive_options: Mapping[int, int | bytes] | None = None,
        socket_type: int = 0,
        db: str | int = 0,
        password: str | None = None,
        socket_timeout: float | None = None,
        socket_connect_timeout: float | None = None,
        retry_on_timeout: bool = False,
        retry_on_error: list[type[RedisError]] | _Sentinel = ...,
        encoding: str = "utf-8",
        encoding_errors: str = "strict",
        decode_responses: bool = False,
        parser_class: type[BaseParser] = ...,
        socket_read_size: int = 65536,
        health_check_interval: float = 0,
        client_name: str | None = None,
        username: str | None = None,
        retry: Retry | None = None,
        redis_connect_func: ConnectCallbackT | None = None,
        encoder_class: type[Encoder] = ...,
        credential_provider: CredentialProvider | None = None,
    ) -> None: ...
    async def get_master_address(self) -> tuple[str, int]: ...
    async def rotate_slaves(self) -> AsyncIterator[tuple[str, int]]:
        """Round-robin slave balancer"""
        ...

_State = TypedDict(
    "_State", {"ip": str, "port": int, "is_master": bool, "is_sdown": bool, "is_odown": bool, "num-other-sentinels": int}
)

class Sentinel(AsyncSentinelCommands):
    """
    Redis Sentinel cluster client

    >>> from redis.sentinel import Sentinel
    >>> sentinel = Sentinel([('localhost', 26379)], socket_timeout=0.1)
    >>> master = sentinel.master_for('mymaster', socket_timeout=0.1)
    >>> await master.set('foo', 'bar')
    >>> slave = sentinel.slave_for('mymaster', socket_timeout=0.1)
    >>> await slave.get('foo')
    b'bar'

    ``sentinels`` is a list of sentinel nodes. Each node is represented by
    a pair (hostname, port).

    ``min_other_sentinels`` defined a minimum number of peers for a sentinel.
    When querying a sentinel, if it doesn't meet this threshold, responses
    from that sentinel won't be considered valid.

    ``sentinel_kwargs`` is a dictionary of connection arguments used when
    connecting to sentinel instances. Any argument that can be passed to
    a normal Redis connection can be specified here. If ``sentinel_kwargs`` is
    not specified, any socket_timeout and socket_keepalive options specified
    in ``connection_kwargs`` will be used.

    ``connection_kwargs`` are keyword arguments that will be used when
    establishing a connection to a Redis server.
    """
    sentinel_kwargs: Mapping[str, Any]
    sentinels: list[Redis[Any]]
    min_other_sentinels: int
    connection_kwargs: Mapping[str, Any]
    def __init__(
        self,
        sentinels: Iterable[tuple[str, int]],
        min_other_sentinels: int = 0,
        sentinel_kwargs: Mapping[str, Any] | None = None,
        **connection_kwargs: Any,
    ) -> None: ...
    async def execute_command(self, *args: Any, once: bool = False, **kwargs: Any) -> Literal[True]:
        """
        Execute Sentinel command in sentinel nodes.
        once - If set to True, then execute the resulting command on a single
               node at random, rather than across the entire sentinel cluster.
        """
        ...
    def check_master_state(self, state: _State, service_name: str) -> bool: ...
    async def discover_master(self, service_name: str) -> tuple[str, int]:
        """
        Asks sentinel servers for the Redis master's address corresponding
        to the service labeled ``service_name``.

        Returns a pair (address, port) or raises MasterNotFoundError if no
        master is found.
        """
        ...
    def filter_slaves(self, slaves: Iterable[_State]) -> list[tuple[str, int]]:
        """Remove slaves that are in an ODOWN or SDOWN state"""
        ...
    async def discover_slaves(self, service_name: str) -> list[tuple[str, int]]:
        """Returns a list of alive slaves for service ``service_name``"""
        ...
    @overload
    def master_for(
        self,
        service_name: str,
        redis_class: type[_RedisT],
        connection_pool_class: type[SentinelConnectionPool[Any]] = ...,
        # Forwarded to the connection pool constructor.
        **kwargs: Any,
    ) -> _RedisT:
        """
        Returns a redis client instance for the ``service_name`` master.

        A :py:class:`~redis.sentinel.SentinelConnectionPool` class is
        used to retrieve the master's address before establishing a new
        connection.

        NOTE: If the master's address has changed, any cached connections to
        the old master are closed.

        By default clients will be a :py:class:`~redis.Redis` instance.
        Specify a different class to the ``redis_class`` argument if you
        desire something different.

        The ``connection_pool_class`` specifies the connection pool to
        use.  The :py:class:`~redis.sentinel.SentinelConnectionPool`
        will be used by default.

        All other keyword arguments are merged with any connection_kwargs
        passed to this class and passed to the connection pool as keyword
        arguments to be used to initialize Redis connections.
        """
        ...
    @overload
    def master_for(
        self,
        service_name: str,
        *,
        connection_pool_class: type[SentinelConnectionPool[Any]] = ...,
        # Forwarded to the connection pool constructor.
        **kwargs: Any,
    ) -> Redis[Any]:
        """
        Returns a redis client instance for the ``service_name`` master.

        A :py:class:`~redis.sentinel.SentinelConnectionPool` class is
        used to retrieve the master's address before establishing a new
        connection.

        NOTE: If the master's address has changed, any cached connections to
        the old master are closed.

        By default clients will be a :py:class:`~redis.Redis` instance.
        Specify a different class to the ``redis_class`` argument if you
        desire something different.

        The ``connection_pool_class`` specifies the connection pool to
        use.  The :py:class:`~redis.sentinel.SentinelConnectionPool`
        will be used by default.

        All other keyword arguments are merged with any connection_kwargs
        passed to this class and passed to the connection pool as keyword
        arguments to be used to initialize Redis connections.
        """
        ...
    @overload
    def slave_for(
        self,
        service_name: str,
        redis_class: type[_RedisT],
        connection_pool_class: type[SentinelConnectionPool[Any]] = ...,
        # Forwarded to the connection pool constructor.
        **kwargs: Any,
    ) -> _RedisT:
        """
        Returns redis client instance for the ``service_name`` slave(s).

        A SentinelConnectionPool class is used to retrieve the slave's
        address before establishing a new connection.

        By default clients will be a :py:class:`~redis.Redis` instance.
        Specify a different class to the ``redis_class`` argument if you
        desire something different.

        The ``connection_pool_class`` specifies the connection pool to use.
        The SentinelConnectionPool will be used by default.

        All other keyword arguments are merged with any connection_kwargs
        passed to this class and passed to the connection pool as keyword
        arguments to be used to initialize Redis connections.
        """
        ...
    @overload
    def slave_for(
        self,
        service_name: str,
        *,
        connection_pool_class: type[SentinelConnectionPool[Any]] = ...,
        # Forwarded to the connection pool constructor.
        **kwargs: Any,
    ) -> Redis[Any]:
        """
        Returns redis client instance for the ``service_name`` slave(s).

        A SentinelConnectionPool class is used to retrieve the slave's
        address before establishing a new connection.

        By default clients will be a :py:class:`~redis.Redis` instance.
        Specify a different class to the ``redis_class`` argument if you
        desire something different.

        The ``connection_pool_class`` specifies the connection pool to use.
        The SentinelConnectionPool will be used by default.

        All other keyword arguments are merged with any connection_kwargs
        passed to this class and passed to the connection pool as keyword
        arguments to be used to initialize Redis connections.
        """
        ...
