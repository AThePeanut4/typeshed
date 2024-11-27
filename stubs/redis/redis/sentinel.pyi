from collections.abc import Iterable, Iterator
from typing import Any, Literal, TypeVar, overload
from typing_extensions import TypeAlias

from redis.client import Redis
from redis.commands.sentinel import SentinelCommands
from redis.connection import Connection, ConnectionPool, SSLConnection
from redis.exceptions import ConnectionError

_RedisT = TypeVar("_RedisT", bound=Redis[Any])
_AddressAndPort: TypeAlias = tuple[str, int]
_SentinelState: TypeAlias = dict[str, Any]  # TODO: this can be a TypedDict

class MasterNotFoundError(ConnectionError): ...
class SlaveNotFoundError(ConnectionError): ...

class SentinelManagedConnection(Connection):
    connection_pool: SentinelConnectionPool
    def __init__(self, *, connection_pool: SentinelConnectionPool, **kwargs) -> None: ...
    def connect_to(self, address: _AddressAndPort) -> None: ...
    def connect(self) -> None: ...
    # The result can be either `str | bytes` or `list[str | bytes]`
    def read_response(self, disable_decoding: bool = False, *, disconnect_on_error: bool = False) -> Any: ...

class SentinelManagedSSLConnection(SentinelManagedConnection, SSLConnection): ...

class SentinelConnectionPool(ConnectionPool):
    """
    Sentinel backed connection pool.

    If ``check_connection`` flag is set to True, SentinelManagedConnection
    sends a PING command right after establishing the connection.
    """
    is_master: bool
    check_connection: bool
    service_name: str
    sentinel_manager: Sentinel
    def __init__(self, service_name: str, sentinel_manager: Sentinel, **kwargs) -> None: ...
    def reset(self) -> None: ...
    def owns_connection(self, connection: Connection) -> bool: ...
    def get_master_address(self) -> _AddressAndPort: ...
    def rotate_slaves(self) -> Iterator[_AddressAndPort]:
        """Round-robin slave balancer"""
        ...

class Sentinel(SentinelCommands):
    """
    Redis Sentinel cluster client

    >>> from redis.sentinel import Sentinel
    >>> sentinel = Sentinel([('localhost', 26379)], socket_timeout=0.1)
    >>> master = sentinel.master_for('mymaster', socket_timeout=0.1)
    >>> master.set('foo', 'bar')
    >>> slave = sentinel.slave_for('mymaster', socket_timeout=0.1)
    >>> slave.get('foo')
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
    sentinel_kwargs: dict[str, Any]
    sentinels: list[Redis[Any]]
    min_other_sentinels: int
    connection_kwargs: dict[str, Any]
    def __init__(
        self,
        sentinels: Iterable[_AddressAndPort],
        min_other_sentinels: int = 0,
        sentinel_kwargs: dict[str, Any] | None = None,
        **connection_kwargs,
    ) -> None: ...
    def check_master_state(self, state: _SentinelState, service_name: str) -> bool: ...
    def discover_master(self, service_name: str) -> _AddressAndPort:
        """
        Asks sentinel servers for the Redis master's address corresponding
        to the service labeled ``service_name``.

        Returns a pair (address, port) or raises MasterNotFoundError if no
        master is found.
        """
        ...
    def filter_slaves(self, slaves: Iterable[_SentinelState]) -> list[_AddressAndPort]:
        """Remove slaves that are in an ODOWN or SDOWN state"""
        ...
    def discover_slaves(self, service_name: str) -> list[_AddressAndPort]:
        """Returns a list of alive slaves for service ``service_name``"""
        ...
    @overload
    def master_for(self, service_name: str, *, connection_pool_class=..., **kwargs) -> Redis[Any]:
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
    def master_for(self, service_name: str, redis_class: type[_RedisT], connection_pool_class=..., **kwargs) -> _RedisT:
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
    def slave_for(self, service_name: str, *, connection_pool_class=..., **kwargs) -> Redis[Any]:
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
    def slave_for(self, service_name: str, redis_class: type[_RedisT], connection_pool_class=..., **kwargs) -> _RedisT:
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
    def execute_command(self, *args, **kwargs) -> Literal[True]:
        """
        Execute Sentinel command in sentinel nodes.
        once - If set to True, then execute the resulting command on a single
        node at random, rather than across the entire sentinel cluster.
        """
        ...
