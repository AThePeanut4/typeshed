import threading
from _typeshed import Incomplete, SupportsItems, Unused
from collections.abc import Callable, Iterable, Iterator, Mapping, Sequence
from datetime import datetime, timedelta
from re import Pattern
from types import TracebackType
from typing import Any, ClassVar, Literal, TypeVar, overload
from typing_extensions import Self, TypeAlias

from redis import RedisError

from .commands import CoreCommands, RedisModuleCommands, SentinelCommands
from .connection import ConnectionPool, _ConnectFunc, _ConnectionPoolOptions
from .credentials import CredentialProvider
from .lock import Lock
from .retry import Retry
from .typing import ChannelT, EncodableT, KeyT, PatternT

_Value: TypeAlias = bytes | float | int | str
_Key: TypeAlias = str | bytes

# Lib returns str or bytes depending on value of decode_responses
_StrType = TypeVar("_StrType", bound=str | bytes)

_VT = TypeVar("_VT")
_T = TypeVar("_T")

# Keyword arguments that are passed to Redis.parse_response().
_ParseResponseOptions: TypeAlias = Any
# Keyword arguments that are passed to Redis.execute_command().
_CommandOptions: TypeAlias = _ConnectionPoolOptions | _ParseResponseOptions

SYM_EMPTY: bytes
EMPTY_RESPONSE: str
NEVER_DECODE: str

class CaseInsensitiveDict(dict[_StrType, _VT]):
    """Case insensitive dict implementation. Assumes string keys only."""
    def __init__(self, data: SupportsItems[_StrType, _VT]) -> None: ...
    def update(self, data: SupportsItems[_StrType, _VT]) -> None: ...  # type: ignore[override]
    @overload
    def get(self, k: _StrType, default: None = None) -> _VT | None: ...
    @overload
    def get(self, k: _StrType, default: _VT | _T) -> _VT | _T: ...
    # Overrides many other methods too, but without changing signature

def list_or_args(keys, args): ...
def timestamp_to_datetime(response):
    """Converts a unix timestamp to a Python datetime object"""
    ...
def string_keys_to_dict(key_string, callback): ...
def parse_debug_object(response):
    """Parse the results of Redis's DEBUG OBJECT command into a Python dict"""
    ...
def parse_object(response, infotype):
    """Parse the results of an OBJECT command"""
    ...
def parse_info(response):
    """Parse the result of Redis's INFO command into a Python dict"""
    ...

SENTINEL_STATE_TYPES: dict[str, type[int]]

def parse_sentinel_state(item): ...
def parse_sentinel_master(response): ...
def parse_sentinel_masters(response): ...
def parse_sentinel_slaves_and_sentinels(response): ...
def parse_sentinel_get_master(response): ...
def pairs_to_dict(response, decode_keys: bool = False, decode_string_values: bool = False):
    """Create a dict given a list of key/value pairs"""
    ...
def pairs_to_dict_typed(response, type_info): ...
def zset_score_pairs(response, **options):
    """
    If ``withscores`` is specified in the options, return the response as
    a list of (value, score) pairs
    """
    ...
def sort_return_tuples(response, **options):
    """
    If ``groups`` is specified, return the response as a list of
    n-element tuples with n being the value found in options['groups']
    """
    ...
def int_or_none(response): ...
def float_or_none(response): ...
def bool_ok(response): ...
def parse_client_list(response, **options): ...
def parse_config_get(response, **options): ...
def parse_scan(response, **options): ...
def parse_hscan(response, **options): ...
def parse_zscan(response, **options): ...
def parse_slowlog_get(response, **options): ...

_LockType = TypeVar("_LockType")

class AbstractRedis:
    RESPONSE_CALLBACKS: dict[str, Any]

class Redis(AbstractRedis, RedisModuleCommands, CoreCommands[_StrType], SentinelCommands):
    """
    Implementation of the Redis protocol.

    This abstract class provides a Python interface to all Redis commands
    and an implementation of the Redis protocol.

    Pipelines derive from this, implementing how
    the commands are sent and received to the Redis server. Based on
    configuration, an instance will either use a ConnectionPool, or
    Connection object to talk to redis.

    It is not safe to pass PubSub or Pipeline objects between threads.
    """
    @overload
    @classmethod
    def from_url(
        cls,
        url: str,
        *,
        host: str | None = ...,
        port: int | None = ...,
        db: int | None = ...,
        password: str | None = ...,
        socket_timeout: float | None = ...,
        socket_connect_timeout: float | None = ...,
        socket_keepalive: bool | None = ...,
        socket_keepalive_options: Mapping[str, int | str] | None = ...,
        connection_pool: ConnectionPool | None = ...,
        unix_socket_path: str | None = ...,
        encoding: str = ...,
        encoding_errors: str = ...,
        charset: str | None = ...,
        errors: str | None = ...,
        decode_responses: Literal[True],
        retry_on_timeout: bool = ...,
        retry_on_error: list[type[RedisError]] | None = ...,
        ssl: bool = ...,
        ssl_keyfile: str | None = ...,
        ssl_certfile: str | None = ...,
        ssl_cert_reqs: str | int | None = ...,
        ssl_ca_certs: str | None = ...,
        ssl_ca_path: Incomplete | None = None,
        ssl_ca_data: Incomplete | None = None,
        ssl_check_hostname: bool = ...,
        ssl_password: Incomplete | None = None,
        ssl_validate_ocsp: bool = False,
        ssl_validate_ocsp_stapled: bool = False,  # added in 4.1.1
        ssl_ocsp_context: Incomplete | None = None,  # added in 4.1.1
        ssl_ocsp_expected_cert: Incomplete | None = None,  # added in 4.1.1
        max_connections: int | None = ...,
        single_connection_client: bool = ...,
        health_check_interval: float = ...,
        client_name: str | None = ...,
        username: str | None = ...,
        retry: Retry | None = ...,
        redis_connect_func: _ConnectFunc | None = None,
        credential_provider: CredentialProvider | None = None,
    ) -> Redis[str]:
        """
        Return a Redis client object configured from the given URL

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
    @overload
    @classmethod
    def from_url(
        cls,
        url: str,
        *,
        host: str | None = ...,
        port: int | None = ...,
        db: int | None = ...,
        password: str | None = ...,
        socket_timeout: float | None = ...,
        socket_connect_timeout: float | None = ...,
        socket_keepalive: bool | None = ...,
        socket_keepalive_options: Mapping[str, int | str] | None = ...,
        connection_pool: ConnectionPool | None = ...,
        unix_socket_path: str | None = ...,
        encoding: str = ...,
        encoding_errors: str = ...,
        charset: str | None = ...,
        errors: str | None = ...,
        decode_responses: Literal[False] = False,
        retry_on_timeout: bool = ...,
        retry_on_error: list[type[RedisError]] | None = ...,
        ssl: bool = ...,
        ssl_keyfile: str | None = ...,
        ssl_certfile: str | None = ...,
        ssl_cert_reqs: str | int | None = ...,
        ssl_ca_certs: str | None = ...,
        ssl_ca_path: Incomplete | None = None,
        ssl_ca_data: Incomplete | None = None,
        ssl_check_hostname: bool = ...,
        ssl_password: Incomplete | None = None,
        ssl_validate_ocsp: bool = False,
        ssl_validate_ocsp_stapled: bool = False,  # added in 4.1.1
        ssl_ocsp_context: Incomplete | None = None,  # added in 4.1.1
        ssl_ocsp_expected_cert: Incomplete | None = None,  # added in 4.1.1
        max_connections: int | None = ...,
        single_connection_client: bool = ...,
        health_check_interval: float = ...,
        client_name: str | None = ...,
        username: str | None = ...,
        retry: Retry | None = ...,
        redis_connect_func: _ConnectFunc | None = None,
        credential_provider: CredentialProvider | None = None,
    ) -> Redis[bytes]:
        """
        Return a Redis client object configured from the given URL

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
    connection_pool: Any
    response_callbacks: Any
    @overload
    def __init__(
        self: Redis[str],
        host: str,
        port: int,
        db: int,
        password: str | None,
        socket_timeout: float | None,
        socket_connect_timeout: float | None,
        socket_keepalive: bool | None,
        socket_keepalive_options: Mapping[str, int | str] | None,
        connection_pool: ConnectionPool | None,
        unix_socket_path: str | None,
        encoding: str,
        encoding_errors: str,
        charset: str | None,
        errors: str | None,
        decode_responses: Literal[True],
        retry_on_timeout: bool = False,
        retry_on_error: list[type[RedisError]] | None = None,
        ssl: bool = False,
        ssl_keyfile: str | None = None,
        ssl_certfile: str | None = None,
        ssl_cert_reqs: str | int | None = "required",
        ssl_ca_certs: str | None = None,
        ssl_ca_path: Incomplete | None = None,
        ssl_ca_data: Incomplete | None = None,
        ssl_check_hostname: bool = False,
        ssl_password: Incomplete | None = None,
        ssl_validate_ocsp: bool = False,
        ssl_validate_ocsp_stapled: bool = False,  # added in 4.1.1
        ssl_ocsp_context: Incomplete | None = None,  # added in 4.1.1
        ssl_ocsp_expected_cert: Incomplete | None = None,  # added in 4.1.1
        max_connections: int | None = None,
        single_connection_client: bool = False,
        health_check_interval: float = 0,
        client_name: str | None = None,
        username: str | None = None,
        retry: Retry | None = None,
        redis_connect_func: _ConnectFunc | None = None,
        credential_provider: CredentialProvider | None = None,
    ) -> None:
        """
        Initialize a new Redis client.
        To specify a retry policy for specific errors, first set
        `retry_on_error` to a list of the error/s to retry on, then set
        `retry` to a valid `Retry` object.
        To retry on TimeoutError, `retry_on_timeout` can also be set to `True`.

        Args:

        single_connection_client:
            if `True`, connection pool is not used. In that case `Redis`
            instance use is not thread safe.
        """
        ...
    @overload
    def __init__(
        self: Redis[str],
        host: str = "localhost",
        port: int = 6379,
        db: int = 0,
        password: str | None = None,
        socket_timeout: float | None = None,
        socket_connect_timeout: float | None = None,
        socket_keepalive: bool | None = None,
        socket_keepalive_options: Mapping[str, int | str] | None = None,
        connection_pool: ConnectionPool | None = None,
        unix_socket_path: str | None = None,
        encoding: str = "utf-8",
        encoding_errors: str = "strict",
        charset: str | None = None,
        errors: str | None = None,
        *,
        decode_responses: Literal[True],
        retry_on_timeout: bool = False,
        retry_on_error: list[type[RedisError]] | None = None,
        ssl: bool = False,
        ssl_keyfile: str | None = None,
        ssl_certfile: str | None = None,
        ssl_cert_reqs: str | int | None = "required",
        ssl_ca_certs: str | None = None,
        ssl_ca_data: Incomplete | None = None,
        ssl_check_hostname: bool = False,
        ssl_password: Incomplete | None = None,
        ssl_validate_ocsp: bool = False,
        ssl_validate_ocsp_stapled: bool = False,  # added in 4.1.1
        ssl_ocsp_context: Incomplete | None = None,  # added in 4.1.1
        ssl_ocsp_expected_cert: Incomplete | None = None,  # added in 4.1.1
        max_connections: int | None = None,
        single_connection_client: bool = False,
        health_check_interval: float = 0,
        client_name: str | None = None,
        username: str | None = None,
        retry: Retry | None = None,
        redis_connect_func: _ConnectFunc | None = None,
        credential_provider: CredentialProvider | None = None,
    ) -> None:
        """
        Initialize a new Redis client.
        To specify a retry policy for specific errors, first set
        `retry_on_error` to a list of the error/s to retry on, then set
        `retry` to a valid `Retry` object.
        To retry on TimeoutError, `retry_on_timeout` can also be set to `True`.

        Args:

        single_connection_client:
            if `True`, connection pool is not used. In that case `Redis`
            instance use is not thread safe.
        """
        ...
    @overload
    def __init__(
        self: Redis[bytes],
        host: str = "localhost",
        port: int = 6379,
        db: int = 0,
        password: str | None = None,
        socket_timeout: float | None = None,
        socket_connect_timeout: float | None = None,
        socket_keepalive: bool | None = None,
        socket_keepalive_options: Mapping[str, int | str] | None = None,
        connection_pool: ConnectionPool | None = None,
        unix_socket_path: str | None = None,
        encoding: str = "utf-8",
        encoding_errors: str = "strict",
        charset: str | None = None,
        errors: str | None = None,
        decode_responses: Literal[False] = False,
        retry_on_timeout: bool = False,
        retry_on_error: list[type[RedisError]] | None = None,
        ssl: bool = False,
        ssl_keyfile: str | None = None,
        ssl_certfile: str | None = None,
        ssl_cert_reqs: str | int | None = "required",
        ssl_ca_certs: str | None = None,
        ssl_ca_data: Incomplete | None = None,
        ssl_check_hostname: bool = False,
        ssl_password: Incomplete | None = None,
        ssl_validate_ocsp: bool = False,
        ssl_validate_ocsp_stapled: bool = False,  # added in 4.1.1
        ssl_ocsp_context: Incomplete | None = None,  # added in 4.1.1
        ssl_ocsp_expected_cert: Incomplete | None = None,  # added in 4.1.1
        max_connections: int | None = None,
        single_connection_client: bool = False,
        health_check_interval: float = 0,
        client_name: str | None = None,
        username: str | None = None,
        retry: Retry | None = None,
        redis_connect_func: _ConnectFunc | None = None,
        credential_provider: CredentialProvider | None = None,
    ) -> None:
        """
        Initialize a new Redis client.
        To specify a retry policy for specific errors, first set
        `retry_on_error` to a list of the error/s to retry on, then set
        `retry` to a valid `Retry` object.
        To retry on TimeoutError, `retry_on_timeout` can also be set to `True`.

        Args:

        single_connection_client:
            if `True`, connection pool is not used. In that case `Redis`
            instance use is not thread safe.
        """
        ...
    def get_encoder(self):
        """Get the connection pool's encoder"""
        ...
    def get_connection_kwargs(self):
        """Get the connection's key-word arguments"""
        ...
    def set_response_callback(self, command, callback):
        """Set a custom Response Callback"""
        ...
    def pipeline(self, transaction: bool = True, shard_hint: Any = None) -> Pipeline[_StrType]:
        """
        Return a new pipeline object that can queue multiple commands for
        later execution. ``transaction`` indicates whether all commands
        should be executed atomically. Apart from making a group of operations
        atomic, pipelines are useful for reducing the back-and-forth overhead
        between the client and server.
        """
        ...
    def transaction(self, func, *watches, **kwargs):
        """
        Convenience method for executing the callable `func` as a transaction
        while watching all keys specified in `watches`. The 'func' callable
        should expect a single argument which is a Pipeline object.
        """
        ...
    @overload
    def lock(
        self,
        name: _Key,
        timeout: float | None = None,
        sleep: float = 0.1,
        blocking: bool = True,
        blocking_timeout: float | None = None,
        lock_class: None = None,
        thread_local: bool = True,
    ) -> Lock:
        """
        Return a new Lock object using key ``name`` that mimics
        the behavior of threading.Lock.

        If specified, ``timeout`` indicates a maximum life for the lock.
        By default, it will remain locked until release() is called.

        ``sleep`` indicates the amount of time to sleep per loop iteration
        when the lock is in blocking mode and another client is currently
        holding the lock.

        ``blocking`` indicates whether calling ``acquire`` should block until
        the lock has been acquired or to fail immediately, causing ``acquire``
        to return False and the lock not being acquired. Defaults to True.
        Note this value can be overridden by passing a ``blocking``
        argument to ``acquire``.

        ``blocking_timeout`` indicates the maximum amount of time in seconds to
        spend trying to acquire the lock. A value of ``None`` indicates
        continue trying forever. ``blocking_timeout`` can be specified as a
        float or integer, both representing the number of seconds to wait.

        ``lock_class`` forces the specified lock implementation. Note that as
        of redis-py 3.0, the only lock class we implement is ``Lock`` (which is
        a Lua-based lock). So, it's unlikely you'll need this parameter, unless
        you have created your own custom lock class.

        ``thread_local`` indicates whether the lock token is placed in
        thread-local storage. By default, the token is placed in thread local
        storage so that a thread only sees its token, not a token set by
        another thread. Consider the following timeline:

            time: 0, thread-1 acquires `my-lock`, with a timeout of 5 seconds.
                     thread-1 sets the token to "abc"
            time: 1, thread-2 blocks trying to acquire `my-lock` using the
                     Lock instance.
            time: 5, thread-1 has not yet completed. redis expires the lock
                     key.
            time: 5, thread-2 acquired `my-lock` now that it's available.
                     thread-2 sets the token to "xyz"
            time: 6, thread-1 finishes its work and calls release(). if the
                     token is *not* stored in thread local storage, then
                     thread-1 would see the token value as "xyz" and would be
                     able to successfully release the thread-2's lock.

        In some use cases it's necessary to disable thread local storage. For
        example, if you have code where one thread acquires a lock and passes
        that lock instance to a worker thread to release later. If thread
        local storage isn't disabled in this case, the worker thread won't see
        the token set by the thread that acquired the lock. Our assumption
        is that these cases aren't common and as such default to using
        thread local storage.
        """
        ...
    @overload
    def lock(
        self,
        name: _Key,
        timeout: float | None,
        sleep: float,
        blocking: bool,
        blocking_timeout: float | None,
        lock_class: type[_LockType],
        thread_local: bool = True,
    ) -> _LockType:
        """
        Return a new Lock object using key ``name`` that mimics
        the behavior of threading.Lock.

        If specified, ``timeout`` indicates a maximum life for the lock.
        By default, it will remain locked until release() is called.

        ``sleep`` indicates the amount of time to sleep per loop iteration
        when the lock is in blocking mode and another client is currently
        holding the lock.

        ``blocking`` indicates whether calling ``acquire`` should block until
        the lock has been acquired or to fail immediately, causing ``acquire``
        to return False and the lock not being acquired. Defaults to True.
        Note this value can be overridden by passing a ``blocking``
        argument to ``acquire``.

        ``blocking_timeout`` indicates the maximum amount of time in seconds to
        spend trying to acquire the lock. A value of ``None`` indicates
        continue trying forever. ``blocking_timeout`` can be specified as a
        float or integer, both representing the number of seconds to wait.

        ``lock_class`` forces the specified lock implementation. Note that as
        of redis-py 3.0, the only lock class we implement is ``Lock`` (which is
        a Lua-based lock). So, it's unlikely you'll need this parameter, unless
        you have created your own custom lock class.

        ``thread_local`` indicates whether the lock token is placed in
        thread-local storage. By default, the token is placed in thread local
        storage so that a thread only sees its token, not a token set by
        another thread. Consider the following timeline:

            time: 0, thread-1 acquires `my-lock`, with a timeout of 5 seconds.
                     thread-1 sets the token to "abc"
            time: 1, thread-2 blocks trying to acquire `my-lock` using the
                     Lock instance.
            time: 5, thread-1 has not yet completed. redis expires the lock
                     key.
            time: 5, thread-2 acquired `my-lock` now that it's available.
                     thread-2 sets the token to "xyz"
            time: 6, thread-1 finishes its work and calls release(). if the
                     token is *not* stored in thread local storage, then
                     thread-1 would see the token value as "xyz" and would be
                     able to successfully release the thread-2's lock.

        In some use cases it's necessary to disable thread local storage. For
        example, if you have code where one thread acquires a lock and passes
        that lock instance to a worker thread to release later. If thread
        local storage isn't disabled in this case, the worker thread won't see
        the token set by the thread that acquired the lock. Our assumption
        is that these cases aren't common and as such default to using
        thread local storage.
        """
        ...
    @overload
    def lock(
        self,
        name: _Key,
        timeout: float | None = None,
        sleep: float = 0.1,
        blocking: bool = True,
        blocking_timeout: float | None = None,
        *,
        lock_class: type[_LockType],
        thread_local: bool = True,
    ) -> _LockType:
        """
        Return a new Lock object using key ``name`` that mimics
        the behavior of threading.Lock.

        If specified, ``timeout`` indicates a maximum life for the lock.
        By default, it will remain locked until release() is called.

        ``sleep`` indicates the amount of time to sleep per loop iteration
        when the lock is in blocking mode and another client is currently
        holding the lock.

        ``blocking`` indicates whether calling ``acquire`` should block until
        the lock has been acquired or to fail immediately, causing ``acquire``
        to return False and the lock not being acquired. Defaults to True.
        Note this value can be overridden by passing a ``blocking``
        argument to ``acquire``.

        ``blocking_timeout`` indicates the maximum amount of time in seconds to
        spend trying to acquire the lock. A value of ``None`` indicates
        continue trying forever. ``blocking_timeout`` can be specified as a
        float or integer, both representing the number of seconds to wait.

        ``lock_class`` forces the specified lock implementation. Note that as
        of redis-py 3.0, the only lock class we implement is ``Lock`` (which is
        a Lua-based lock). So, it's unlikely you'll need this parameter, unless
        you have created your own custom lock class.

        ``thread_local`` indicates whether the lock token is placed in
        thread-local storage. By default, the token is placed in thread local
        storage so that a thread only sees its token, not a token set by
        another thread. Consider the following timeline:

            time: 0, thread-1 acquires `my-lock`, with a timeout of 5 seconds.
                     thread-1 sets the token to "abc"
            time: 1, thread-2 blocks trying to acquire `my-lock` using the
                     Lock instance.
            time: 5, thread-1 has not yet completed. redis expires the lock
                     key.
            time: 5, thread-2 acquired `my-lock` now that it's available.
                     thread-2 sets the token to "xyz"
            time: 6, thread-1 finishes its work and calls release(). if the
                     token is *not* stored in thread local storage, then
                     thread-1 would see the token value as "xyz" and would be
                     able to successfully release the thread-2's lock.

        In some use cases it's necessary to disable thread local storage. For
        example, if you have code where one thread acquires a lock and passes
        that lock instance to a worker thread to release later. If thread
        local storage isn't disabled in this case, the worker thread won't see
        the token set by the thread that acquired the lock. Our assumption
        is that these cases aren't common and as such default to using
        thread local storage.
        """
        ...
    def pubsub(self, *, shard_hint: Any = ..., ignore_subscribe_messages: bool = ...) -> PubSub:
        """
        Return a Publish/Subscribe object. With this object, you can
        subscribe to channels and listen for messages that get published to
        them.
        """
        ...
    def execute_command(self, *args, **options: _CommandOptions):
        """Execute a command and return a parsed response"""
        ...
    def parse_response(self, connection, command_name, **options: _ParseResponseOptions):
        """Parses a response from the Redis server"""
        ...
    def monitor(self) -> Monitor: ...
    def __enter__(self) -> Redis[_StrType]: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None
    ) -> None: ...
    def __del__(self) -> None: ...
    def close(self) -> None: ...
    def client(self) -> Redis[_StrType]: ...

StrictRedis = Redis

class PubSub:
    """
    PubSub provides publish, subscribe and listen support to Redis channels.

    After subscribing to one or more channels, the listen() method will block
    until a message arrives on one of the subscribed channels. That message
    will be returned and it's safe to start listening again.
    """
    PUBLISH_MESSAGE_TYPES: ClassVar[tuple[str, str]]
    UNSUBSCRIBE_MESSAGE_TYPES: ClassVar[tuple[str, str]]
    HEALTH_CHECK_MESSAGE: ClassVar[str]
    connection_pool: Any
    shard_hint: Any
    ignore_subscribe_messages: Any
    connection: Any
    subscribed_event: threading.Event
    encoder: Any
    health_check_response_b: bytes
    health_check_response: list[str] | list[bytes]
    def __init__(
        self,
        connection_pool,
        shard_hint: Incomplete | None = None,
        ignore_subscribe_messages: bool = False,
        encoder: Incomplete | None = None,
    ) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None
    ) -> None: ...
    def __del__(self): ...
    channels: Any
    patterns: Any
    def reset(self): ...
    def close(self) -> None: ...
    def on_connect(self, connection):
        """Re-subscribe to any channels and patterns previously subscribed to"""
        ...
    @property
    def subscribed(self):
        """Indicates if there are subscriptions to any channels or patterns"""
        ...
    def execute_command(self, *args):
        """Execute a publish/subscribe command"""
        ...
    def clean_health_check_responses(self) -> None:
        """If any health check responses are present, clean them"""
        ...
    def parse_response(self, block: bool = True, timeout: float = 0):
        """Parse the response from a publish/subscribe command"""
        ...
    def is_health_check_response(self, response) -> bool:
        """
        Check if the response is a health check response.
        If there are no subscriptions redis responds to PING command with a
        bulk response, instead of a multi-bulk with "pong" and the response.
        """
        ...
    def check_health(self) -> None: ...
    def psubscribe(self, *args: _Key, **kwargs: Callable[[Any], None]):
        """
        Subscribe to channel patterns. Patterns supplied as keyword arguments
        expect a pattern name as the key and a callable as the value. A
        pattern's callable will be invoked automatically when a message is
        received on that pattern rather than producing a message via
        ``listen()``.
        """
        ...
    def punsubscribe(self, *args: _Key) -> None:
        """
        Unsubscribe from the supplied patterns. If empty, unsubscribe from
        all patterns.
        """
        ...
    def subscribe(self, *args: _Key, **kwargs: Callable[[Any], None]) -> None:
        """
        Subscribe to channels. Channels supplied as keyword arguments expect
        a channel name as the key and a callable as the value. A channel's
        callable will be invoked automatically when a message is received on
        that channel rather than producing a message via ``listen()`` or
        ``get_message()``.
        """
        ...
    def unsubscribe(self, *args: _Key) -> None:
        """
        Unsubscribe from the supplied channels. If empty, unsubscribe from
        all channels
        """
        ...
    def listen(self):
        """Listen for messages on channels this client has been subscribed to"""
        ...
    def get_message(self, ignore_subscribe_messages: bool = False, timeout: float = 0.0) -> dict[str, Any] | None:
        """
        Get the next message if one is available, otherwise None.

        If timeout is specified, the system will wait for `timeout` seconds
        before returning. Timeout should be specified as a floating point
        number, or None, to wait indefinitely.
        """
        ...
    def handle_message(self, response, ignore_subscribe_messages: bool = False) -> dict[str, Any] | None:
        """
        Parses a pub/sub message. If the channel or pattern was subscribed to
        with a message handler, the handler is invoked instead of a parsed
        message being returned.
        """
        ...
    def run_in_thread(self, sleep_time: float = 0, daemon: bool = False, exception_handler: Incomplete | None = None): ...
    def ping(self, message: _Value | None = None) -> None:
        """Ping the Redis server"""
        ...

class PubSubWorkerThread(threading.Thread):
    daemon: Any
    pubsub: Any
    sleep_time: Any
    exception_handler: Any
    def __init__(self, pubsub, sleep_time, daemon: bool = False, exception_handler: Incomplete | None = None) -> None: ...
    def run(self) -> None: ...
    def stop(self) -> None: ...

class Pipeline(Redis[_StrType]):
    """
    Pipelines provide a way to transmit multiple commands to the Redis server
    in one transmission.  This is convenient for batch processing, such as
    saving all the values in a list to Redis.

    All commands executed within a pipeline are wrapped with MULTI and EXEC
    calls. This guarantees all commands executed in the pipeline will be
    executed atomically.

    Any command raising an exception does *not* halt the execution of
    subsequent commands in the pipeline. Instead, the exception is caught
    and its instance is placed into the response list returned by execute().
    Code iterating over the response list should be able to deal with an
    instance of an exception as a potential value. In general, these will be
    ResponseError exceptions, such as those raised when issuing a command
    on a key of a different datatype.
    """
    UNWATCH_COMMANDS: Any
    connection_pool: Any
    connection: Any
    response_callbacks: Any
    transaction: bool
    shard_hint: Any
    watching: bool

    command_stack: Any
    scripts: Any
    explicit_transaction: Any
    def __init__(self, connection_pool, response_callbacks, transaction, shard_hint) -> None: ...
    def __enter__(self) -> Pipeline[_StrType]: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None
    ) -> None: ...
    def __del__(self) -> None: ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool:
        """Pipeline instances should always evaluate to True"""
        ...
    def discard(self) -> None:
        """
        Flushes all previously queued commands
        See: https://redis.io/commands/DISCARD
        """
        ...
    def reset(self) -> None: ...
    def multi(self) -> None:
        """
        Start a transactional block of the pipeline after WATCH commands
        are issued. End the transactional block with `execute`.
        """
        ...
    def execute_command(self, *args, **options): ...
    def immediate_execute_command(self, *args, **options):
        """
        Execute a command immediately, but don't auto-retry on a
        ConnectionError if we're already WATCHing a variable. Used when
        issuing WATCH or subsequent commands retrieving their values but before
        MULTI is called.
        """
        ...
    def pipeline_execute_command(self, *args, **options):
        """
        Stage a command to be executed when execute() is next called

        Returns the current Pipeline object back so commands can be
        chained together, such as:

        pipe = pipe.set('foo', 'bar').incr('baz').decr('bang')

        At some other point, you can then run: pipe.execute(),
        which will execute all commands queued in the pipe.
        """
        ...
    def raise_first_error(self, commands, response): ...
    def annotate_exception(self, exception, number, command): ...
    def parse_response(self, connection, command_name, **options): ...
    def load_scripts(self): ...
    def execute(self, raise_on_error: bool = True) -> list[Any]:
        """Execute all the commands in the current pipeline"""
        ...
    def watch(self, *names: _Key) -> bool:
        """Watches the values at keys ``names``"""
        ...
    def unwatch(self) -> bool:
        """Unwatches all previously specified keys"""
        ...
    # in the Redis implementation, the following methods are inherited from client.
    def set_response_callback(self, command, callback):
        """Set a custom Response Callback"""
        ...
    def pipeline(self, transaction: bool = True, shard_hint: Any = None) -> Pipeline[_StrType]:
        """
        Return a new pipeline object that can queue multiple commands for
        later execution. ``transaction`` indicates whether all commands
        should be executed atomically. Apart from making a group of operations
        atomic, pipelines are useful for reducing the back-and-forth overhead
        between the client and server.
        """
        ...
    def acl_cat(self, category: str | None = None) -> Pipeline[_StrType]:
        """
        Returns a list of categories or commands within a category.

        If ``category`` is not supplied, returns a list of all categories.
        If ``category`` is supplied, returns a list of all commands within
        that category.

        For more information see https://redis.io/commands/acl-cat
        """
        ...
    def acl_deluser(self, username: str) -> Pipeline[_StrType]:
        """
        Delete the ACL for the specified ``username``s

        For more information see https://redis.io/commands/acl-deluser
        """
        ...
    def acl_genpass(self, bits: int | None = None) -> Pipeline[_StrType]:
        """
        Generate a random password value.
        If ``bits`` is supplied then use this number of bits, rounded to
        the next multiple of 4.
        See: https://redis.io/commands/acl-genpass
        """
        ...
    def acl_getuser(self, username: str) -> Pipeline[_StrType]:
        """
        Get the ACL details for the specified ``username``.

        If ``username`` does not exist, return None

        For more information see https://redis.io/commands/acl-getuser
        """
        ...
    def acl_list(self) -> Pipeline[_StrType]:
        """
        Return a list of all ACLs on the server

        For more information see https://redis.io/commands/acl-list
        """
        ...
    def acl_load(self) -> Pipeline[_StrType]:
        """
        Load ACL rules from the configured ``aclfile``.

        Note that the server must be configured with the ``aclfile``
        directive to be able to load ACL rules from an aclfile.

        For more information see https://redis.io/commands/acl-load
        """
        ...
    def acl_setuser(  # type: ignore[override]
        self,
        username: str,
        enabled: bool = False,
        nopass: bool = False,
        passwords: Sequence[str] | None = None,
        hashed_passwords: Sequence[str] | None = None,
        categories: Sequence[str] | None = None,
        commands: Sequence[str] | None = None,
        keys: Sequence[str] | None = None,
        channels: Iterable[ChannelT] | None = None,
        selectors: Iterable[tuple[str, KeyT]] | None = None,
        reset: bool = False,
        reset_keys: bool = False,
        reset_channels: bool = False,
        reset_passwords: bool = False,
        **kwargs: _CommandOptions,
    ) -> Pipeline[_StrType]:
        """
        Create or update an ACL user.

        Create or update the ACL for ``username``. If the user already exists,
        the existing ACL is completely overwritten and replaced with the
        specified values.

        ``enabled`` is a boolean indicating whether the user should be allowed
        to authenticate or not. Defaults to ``False``.

        ``nopass`` is a boolean indicating whether the can authenticate without
        a password. This cannot be True if ``passwords`` are also specified.

        ``passwords`` if specified is a list of plain text passwords
        to add to or remove from the user. Each password must be prefixed with
        a '+' to add or a '-' to remove. For convenience, the value of
        ``passwords`` can be a simple prefixed string when adding or
        removing a single password.

        ``hashed_passwords`` if specified is a list of SHA-256 hashed passwords
        to add to or remove from the user. Each hashed password must be
        prefixed with a '+' to add or a '-' to remove. For convenience,
        the value of ``hashed_passwords`` can be a simple prefixed string when
        adding or removing a single password.

        ``categories`` if specified is a list of strings representing category
        permissions. Each string must be prefixed with either a '+' to add the
        category permission or a '-' to remove the category permission.

        ``commands`` if specified is a list of strings representing command
        permissions. Each string must be prefixed with either a '+' to add the
        command permission or a '-' to remove the command permission.

        ``keys`` if specified is a list of key patterns to grant the user
        access to. Keys patterns allow '*' to support wildcard matching. For
        example, '*' grants access to all keys while 'cache:*' grants access
        to all keys that are prefixed with 'cache:'. ``keys`` should not be
        prefixed with a '~'.

        ``reset`` is a boolean indicating whether the user should be fully
        reset prior to applying the new ACL. Setting this to True will
        remove all existing passwords, flags and privileges from the user and
        then apply the specified rules. If this is False, the user's existing
        passwords, flags and privileges will be kept and any new specified
        rules will be applied on top.

        ``reset_keys`` is a boolean indicating whether the user's key
        permissions should be reset prior to applying any new key permissions
        specified in ``keys``. If this is False, the user's existing
        key permissions will be kept and any new specified key permissions
        will be applied on top.

        ``reset_channels`` is a boolean indicating whether the user's channel
        permissions should be reset prior to applying any new channel permissions
        specified in ``channels``.If this is False, the user's existing
        channel permissions will be kept and any new specified channel permissions
        will be applied on top.

        ``reset_passwords`` is a boolean indicating whether to remove all
        existing passwords and the 'nopass' flag from the user prior to
        applying any new passwords specified in 'passwords' or
        'hashed_passwords'. If this is False, the user's existing passwords
        and 'nopass' status will be kept and any new specified passwords
        or hashed_passwords will be applied on top.

        For more information see https://redis.io/commands/acl-setuser
        """
        ...
    def acl_users(self) -> Pipeline[_StrType]:
        """
        Returns a list of all registered users on the server.

        For more information see https://redis.io/commands/acl-users
        """
        ...
    def acl_whoami(self) -> Pipeline[_StrType]:
        """
        Get the username for the current connection

        For more information see https://redis.io/commands/acl-whoami
        """
        ...
    def bgrewriteaof(self) -> Pipeline[_StrType]:
        """
        Tell the Redis server to rewrite the AOF file from data in memory.

        For more information see https://redis.io/commands/bgrewriteaof
        """
        ...
    def bgsave(self, schedule: bool = True) -> Pipeline[_StrType]:
        """
        Tell the Redis server to save its data to disk.  Unlike save(),
        this method is asynchronous and returns immediately.

        For more information see https://redis.io/commands/bgsave
        """
        ...
    def client_id(self) -> Pipeline[_StrType]:
        """
        Returns the current connection id

        For more information see https://redis.io/commands/client-id
        """
        ...
    def client_kill(self, address: str) -> Pipeline[_StrType]:
        """
        Disconnects the client at ``address`` (ip:port)

        For more information see https://redis.io/commands/client-kill
        """
        ...
    def client_list(self, _type: str | None = None, client_id: list[str] = []) -> Pipeline[_StrType]:
        """
        Returns a list of currently connected clients.
        If type of client specified, only that type will be returned.
        :param _type: optional. one of the client types (normal, master,
         replica, pubsub)
        :param client_id: optional. a list of client ids

        For more information see https://redis.io/commands/client-list
        """
        ...
    def client_getname(self) -> Pipeline[_StrType]:
        """
        Returns the current connection name

        For more information see https://redis.io/commands/client-getname
        """
        ...
    def client_setname(self, name: str) -> Pipeline[_StrType]:
        """
        Sets the current connection name

        For more information see https://redis.io/commands/client-setname

        .. note::
           This method sets client name only for **current** connection.

           If you want to set a common name for all connections managed
           by this client, use ``client_name`` constructor argument.
        """
        ...
    def readwrite(self) -> Pipeline[_StrType]:
        """
        Disables read queries for a connection to a Redis Cluster slave node.

        For more information see https://redis.io/commands/readwrite
        """
        ...
    def readonly(self) -> Pipeline[_StrType]:
        """
        Enables read queries for a connection to a Redis Cluster replica node.

        For more information see https://redis.io/commands/readonly
        """
        ...
    def config_get(self, pattern: PatternT = "*", *args: PatternT, **kwargs: _CommandOptions) -> Pipeline[_StrType]:
        """
        Return a dictionary of configuration based on the ``pattern``

        For more information see https://redis.io/commands/config-get
        """
        ...
    def config_set(
        self, name: KeyT, value: EncodableT, *args: KeyT | EncodableT, **kwargs: _CommandOptions
    ) -> Pipeline[_StrType]:
        """
        Set config item ``name`` with ``value``

        For more information see https://redis.io/commands/config-set
        """
        ...
    def config_resetstat(self) -> Pipeline[_StrType]:
        """
        Reset runtime statistics

        For more information see https://redis.io/commands/config-resetstat
        """
        ...
    def config_rewrite(self) -> Pipeline[_StrType]:
        """
        Rewrite config file with the minimal change to reflect running config.

        For more information see https://redis.io/commands/config-rewrite
        """
        ...
    def dbsize(self) -> Pipeline[_StrType]:
        """
        Returns the number of keys in the current database

        For more information see https://redis.io/commands/dbsize
        """
        ...
    def debug_object(self, key) -> Pipeline[_StrType]:
        """
        Returns version specific meta information about a given key

        For more information see https://redis.io/commands/debug-object
        """
        ...
    def echo(self, value) -> Pipeline[_StrType]:
        """
        Echo the string back from the server

        For more information see https://redis.io/commands/echo
        """
        ...
    def flushall(self, asynchronous: bool = False) -> Pipeline[_StrType]:
        """
        Delete all keys in all databases on the current host.

        ``asynchronous`` indicates whether the operation is
        executed asynchronously by the server.

        For more information see https://redis.io/commands/flushall
        """
        ...
    def flushdb(self, asynchronous: bool = False) -> Pipeline[_StrType]:
        """
        Delete all keys in the current database.

        ``asynchronous`` indicates whether the operation is
        executed asynchronously by the server.

        For more information see https://redis.io/commands/flushdb
        """
        ...
    def info(self, section: _Key | None = None, *args: _Key, **kwargs: _CommandOptions) -> Pipeline[_StrType]:
        """
        Returns a dictionary containing information about the Redis server

        The ``section`` option can be used to select a specific section
        of information

        The section option is not supported by older versions of Redis Server,
        and will generate ResponseError

        For more information see https://redis.io/commands/info
        """
        ...
    def lastsave(self) -> Pipeline[_StrType]:
        """
        Return a Python datetime object representing the last time the
        Redis database was saved to disk

        For more information see https://redis.io/commands/lastsave
        """
        ...
    def object(self, infotype, key) -> Pipeline[_StrType]:
        """Return the encoding, idletime, or refcount about the key"""
        ...
    def ping(self) -> Pipeline[_StrType]:
        """
        Ping the Redis server

        For more information see https://redis.io/commands/ping
        """
        ...
    def save(self) -> Pipeline[_StrType]:
        """
        Tell the Redis server to save its data to disk,
        blocking until the save is complete

        For more information see https://redis.io/commands/save
        """
        ...
    def sentinel_get_master_addr_by_name(self, service_name) -> Pipeline[_StrType]:
        """Returns a (host, port) pair for the given ``service_name``"""
        ...
    def sentinel_master(self, service_name) -> Pipeline[_StrType]:
        """Returns a dictionary containing the specified masters state."""
        ...
    def sentinel_masters(self) -> Pipeline[_StrType]:
        """Returns a list of dictionaries containing each master's state."""
        ...
    def sentinel_monitor(self, name, ip, port, quorum) -> Pipeline[_StrType]:
        """Add a new master to Sentinel to be monitored"""
        ...
    def sentinel_remove(self, name) -> Pipeline[_StrType]:
        """Remove a master from Sentinel's monitoring"""
        ...
    def sentinel_sentinels(self, service_name) -> Pipeline[_StrType]:
        """Returns a list of sentinels for ``service_name``"""
        ...
    def sentinel_set(self, name, option, value) -> Pipeline[_StrType]:
        """Set Sentinel monitoring parameters for a given master"""
        ...
    def sentinel_slaves(self, service_name) -> Pipeline[_StrType]:
        """Returns a list of slaves for ``service_name``"""
        ...
    def slaveof(self, host=None, port=None) -> Pipeline[_StrType]:
        """
        Set the server to be a replicated slave of the instance identified
        by the ``host`` and ``port``. If called without arguments, the
        instance is promoted to a master instead.

        For more information see https://redis.io/commands/slaveof
        """
        ...
    def slowlog_get(self, num=None) -> Pipeline[_StrType]:
        """
        Get the entries from the slowlog. If ``num`` is specified, get the
        most recent ``num`` items.

        For more information see https://redis.io/commands/slowlog-get
        """
        ...
    def slowlog_len(self) -> Pipeline[_StrType]:
        """
        Get the number of items in the slowlog

        For more information see https://redis.io/commands/slowlog-len
        """
        ...
    def slowlog_reset(self) -> Pipeline[_StrType]:
        """
        Remove all items in the slowlog

        For more information see https://redis.io/commands/slowlog-reset
        """
        ...
    def time(self) -> Pipeline[_StrType]:
        """
        Returns the server time as a 2-item tuple of ints:
        (seconds since epoch, microseconds into this second).

        For more information see https://redis.io/commands/time
        """
        ...
    def append(self, key, value) -> Pipeline[_StrType]:
        """
        Appends the string ``value`` to the value at ``key``. If ``key``
        doesn't already exist, create it with a value of ``value``.
        Returns the new length of the value at ``key``.

        For more information see https://redis.io/commands/append
        """
        ...
    def bitcount(  # type: ignore[override]
        self, key: _Key, start: int | None = None, end: int | None = None, mode: str | None = None
    ) -> Pipeline[_StrType]:
        """
        Returns the count of set bits in the value of ``key``.  Optional
        ``start`` and ``end`` parameters indicate which bytes to consider

        For more information see https://redis.io/commands/bitcount
        """
        ...
    def bitop(self, operation, dest, *keys) -> Pipeline[_StrType]:
        """
        Perform a bitwise operation using ``operation`` between ``keys`` and
        store the result in ``dest``.

        For more information see https://redis.io/commands/bitop
        """
        ...
    def bitpos(self, key, bit, start=None, end=None, mode: str | None = None) -> Pipeline[_StrType]:
        """
        Return the position of the first bit set to 1 or 0 in a string.
        ``start`` and ``end`` defines search range. The range is interpreted
        as a range of bytes and not a range of bits, so start=0 and end=2
        means to look at the first three bytes.

        For more information see https://redis.io/commands/bitpos
        """
        ...
    def decr(self, name, amount=1) -> Pipeline[_StrType]:
        """
        Decrements the value of ``key`` by ``amount``.  If no key exists,
        the value will be initialized as 0 - ``amount``

        For more information see https://redis.io/commands/decrby
        """
        ...
    def delete(self, *names: _Key) -> Pipeline[_StrType]:
        """Delete one or more keys specified by ``names``"""
        ...
    def __delitem__(self, _Key) -> None: ...
    def dump(self, name) -> Pipeline[_StrType]:
        """
        Return a serialized version of the value stored at the specified key.
        If key does not exist a nil bulk reply is returned.

        For more information see https://redis.io/commands/dump
        """
        ...
    def exists(self, *names: _Key) -> Pipeline[_StrType]:
        """
        Returns the number of ``names`` that exist

        For more information see https://redis.io/commands/exists
        """
        ...
    def __contains__(self, *names: _Key) -> Pipeline[_StrType]:
        """
        Returns the number of ``names`` that exist

        For more information see https://redis.io/commands/exists
        """
        ...
    def expire(  # type: ignore[override]
        self, name: _Key, time: int | timedelta, nx: bool = False, xx: bool = False, gt: bool = False, lt: bool = False
    ) -> Pipeline[_StrType]:
        """
        Set an expire flag on key ``name`` for ``time`` seconds with given
        ``option``. ``time`` can be represented by an integer or a Python timedelta
        object.

        Valid options are:
            NX -> Set expiry only when the key has no expiry
            XX -> Set expiry only when the key has an existing expiry
            GT -> Set expiry only when the new expiry is greater than current one
            LT -> Set expiry only when the new expiry is less than current one

        For more information see https://redis.io/commands/expire
        """
        ...
    def expireat(
        self, name, when, nx: bool = False, xx: bool = False, gt: bool = False, lt: bool = False
    ) -> Pipeline[_StrType]:
        """
        Set an expire flag on key ``name`` with given ``option``. ``when``
        can be represented as an integer indicating unix time or a Python
        datetime object.

        Valid options are:
            -> NX -- Set expiry only when the key has no expiry
            -> XX -- Set expiry only when the key has an existing expiry
            -> GT -- Set expiry only when the new expiry is greater than current one
            -> LT -- Set expiry only when the new expiry is less than current one

        For more information see https://redis.io/commands/expireat
        """
        ...
    def get(self, name: _Key) -> Pipeline[_StrType]:
        """
        Return the value at key ``name``, or None if the key doesn't exist

        For more information see https://redis.io/commands/get
        """
        ...
    def __getitem__(self, name) -> Pipeline[_StrType]:
        """
        Return the value at key ``name``, raises a KeyError if the key
        doesn't exist.
        """
        ...
    def getbit(self, name: _Key, offset: int) -> Pipeline[_StrType]:
        """
        Returns an integer indicating the value of ``offset`` in ``name``

        For more information see https://redis.io/commands/getbit
        """
        ...
    def getrange(self, key, start, end) -> Pipeline[_StrType]:
        """
        Returns the substring of the string value stored at ``key``,
        determined by the offsets ``start`` and ``end`` (both are inclusive)

        For more information see https://redis.io/commands/getrange
        """
        ...
    def getset(self, name, value) -> Pipeline[_StrType]:
        """
        Sets the value at key ``name`` to ``value``
        and returns the old value at key ``name`` atomically.

        As per Redis 6.2, GETSET is considered deprecated.
        Please use SET with GET parameter in new code.

        For more information see https://redis.io/commands/getset
        """
        ...
    def incr(self, name, amount=1) -> Pipeline[_StrType]:
        """
        Increments the value of ``key`` by ``amount``.  If no key exists,
        the value will be initialized as ``amount``

        For more information see https://redis.io/commands/incrby
        """
        ...
    def incrby(self, name, amount=1) -> Pipeline[_StrType]:
        """
        Increments the value of ``key`` by ``amount``.  If no key exists,
        the value will be initialized as ``amount``

        For more information see https://redis.io/commands/incrby
        """
        ...
    def incrbyfloat(self, name, amount=1.0) -> Pipeline[_StrType]:
        """
        Increments the value at key ``name`` by floating ``amount``.
        If no key exists, the value will be initialized as ``amount``

        For more information see https://redis.io/commands/incrbyfloat
        """
        ...
    def keys(self, pattern: _Key = "*") -> Pipeline[_StrType]:
        """
        Returns a list of keys matching ``pattern``

        For more information see https://redis.io/commands/keys
        """
        ...
    def mget(self, keys: _Key | Iterable[_Key], *args: _Key) -> Pipeline[_StrType]:
        """
        Returns a list of values ordered identically to ``keys``

        For more information see https://redis.io/commands/mget
        """
        ...
    def mset(self, mapping: Mapping[_Key, _Value]) -> Pipeline[_StrType]:
        """
        Sets key/values based on a mapping. Mapping is a dictionary of
        key/value pairs. Both keys and values should be strings or types that
        can be cast to a string via str().

        For more information see https://redis.io/commands/mset
        """
        ...
    def msetnx(self, mapping: Mapping[_Key, _Value]) -> Pipeline[_StrType]:
        """
        Sets key/values based on a mapping if none of the keys are already set.
        Mapping is a dictionary of key/value pairs. Both keys and values
        should be strings or types that can be cast to a string via str().
        Returns a boolean indicating if the operation was successful.

        For more information see https://redis.io/commands/msetnx
        """
        ...
    def move(self, name: _Key, db: int) -> Pipeline[_StrType]:
        """
        Moves the key ``name`` to a different Redis database ``db``

        For more information see https://redis.io/commands/move
        """
        ...
    def persist(self, name: _Key) -> Pipeline[_StrType]:
        """
        Removes an expiration on ``name``

        For more information see https://redis.io/commands/persist
        """
        ...
    def pexpire(  # type: ignore[override]
        self, name: _Key, time: int | timedelta, nx: bool = False, xx: bool = False, gt: bool = False, lt: bool = False
    ) -> Pipeline[_StrType]:
        """
        Set an expire flag on key ``name`` for ``time`` milliseconds
        with given ``option``. ``time`` can be represented by an
        integer or a Python timedelta object.

        Valid options are:
            NX -> Set expiry only when the key has no expiry
            XX -> Set expiry only when the key has an existing expiry
            GT -> Set expiry only when the new expiry is greater than current one
            LT -> Set expiry only when the new expiry is less than current one

        For more information see https://redis.io/commands/pexpire
        """
        ...
    def pexpireat(  # type: ignore[override]
        self, name: _Key, when: int | datetime, nx: bool = False, xx: bool = False, gt: bool = False, lt: bool = False
    ) -> Pipeline[_StrType]:
        """
        Set an expire flag on key ``name`` with given ``option``. ``when``
        can be represented as an integer representing unix time in
        milliseconds (unix time * 1000) or a Python datetime object.

        Valid options are:
            NX -> Set expiry only when the key has no expiry
            XX -> Set expiry only when the key has an existing expiry
            GT -> Set expiry only when the new expiry is greater than current one
            LT -> Set expiry only when the new expiry is less than current one

        For more information see https://redis.io/commands/pexpireat
        """
        ...
    def psetex(self, name, time_ms, value) -> Pipeline[_StrType]:
        """
        Set the value of key ``name`` to ``value`` that expires in ``time_ms``
        milliseconds. ``time_ms`` can be represented by an integer or a Python
        timedelta object

        For more information see https://redis.io/commands/psetex
        """
        ...
    def pttl(self, name) -> Pipeline[_StrType]:
        """
        Returns the number of milliseconds until the key ``name`` will expire

        For more information see https://redis.io/commands/pttl
        """
        ...
    def randomkey(self) -> Pipeline[_StrType]:
        """
        Returns the name of a random key

        For more information see https://redis.io/commands/randomkey
        """
        ...
    def rename(self, src, dst) -> Pipeline[_StrType]:
        """
        Rename key ``src`` to ``dst``

        For more information see https://redis.io/commands/rename
        """
        ...
    def renamenx(self, src, dst) -> Pipeline[_StrType]:
        """
        Rename key ``src`` to ``dst`` if ``dst`` doesn't already exist

        For more information see https://redis.io/commands/renamenx
        """
        ...
    def restore(
        self,
        name,
        ttl,
        value,
        replace: bool = False,
        absttl: bool = False,
        idletime: Incomplete | None = None,
        frequency: Incomplete | None = None,
    ) -> Pipeline[_StrType]:
        """
        Create a key using the provided serialized value, previously obtained
        using DUMP.

        ``replace`` allows an existing key on ``name`` to be overridden. If
        it's not specified an error is raised on collision.

        ``absttl`` if True, specified ``ttl`` should represent an absolute Unix
        timestamp in milliseconds in which the key will expire. (Redis 5.0 or
        greater).

        ``idletime`` Used for eviction, this is the number of seconds the
        key must be idle, prior to execution.

        ``frequency`` Used for eviction, this is the frequency counter of
        the object stored at the key, prior to execution.

        For more information see https://redis.io/commands/restore
        """
        ...
    def set(  # type: ignore[override]
        self,
        name: _Key,
        value: _Value,
        ex: None | int | timedelta = None,
        px: None | int | timedelta = None,
        nx: bool = False,
        xx: bool = False,
        keepttl: bool = False,
        get: bool = False,
        exat: Incomplete | None = None,
        pxat: Incomplete | None = None,
    ) -> Pipeline[_StrType]:
        """
        Set the value at key ``name`` to ``value``

        ``ex`` sets an expire flag on key ``name`` for ``ex`` seconds.

        ``px`` sets an expire flag on key ``name`` for ``px`` milliseconds.

        ``nx`` if set to True, set the value at key ``name`` to ``value`` only
            if it does not exist.

        ``xx`` if set to True, set the value at key ``name`` to ``value`` only
            if it already exists.

        ``keepttl`` if True, retain the time to live associated with the key.
            (Available since Redis 6.0)

        ``get`` if True, set the value at key ``name`` to ``value`` and return
            the old value stored at key, or None if the key did not exist.
            (Available since Redis 6.2)

        ``exat`` sets an expire flag on key ``name`` for ``ex`` seconds,
            specified in unix time.

        ``pxat`` sets an expire flag on key ``name`` for ``ex`` milliseconds,
            specified in unix time.

        For more information see https://redis.io/commands/set
        """
        ...
    def __setitem__(self, name, value) -> None: ...
    def setbit(self, name: _Key, offset: int, value: int) -> Pipeline[_StrType]:
        """
        Flag the ``offset`` in ``name`` as ``value``. Returns an integer
        indicating the previous value of ``offset``.

        For more information see https://redis.io/commands/setbit
        """
        ...
    def setex(self, name: _Key, time: int | timedelta, value: _Value) -> Pipeline[_StrType]:
        """
        Set the value of key ``name`` to ``value`` that expires in ``time``
        seconds. ``time`` can be represented by an integer or a Python
        timedelta object.

        For more information see https://redis.io/commands/setex
        """
        ...
    def setnx(self, name, value) -> Pipeline[_StrType]:
        """
        Set the value of key ``name`` to ``value`` if key doesn't exist

        For more information see https://redis.io/commands/setnx
        """
        ...
    def setrange(self, name, offset, value) -> Pipeline[_StrType]:
        """
        Overwrite bytes in the value of ``name`` starting at ``offset`` with
        ``value``. If ``offset`` plus the length of ``value`` exceeds the
        length of the original value, the new value will be larger than before.
        If ``offset`` exceeds the length of the original value, null bytes
        will be used to pad between the end of the previous value and the start
        of what's being injected.

        Returns the length of the new string.

        For more information see https://redis.io/commands/setrange
        """
        ...
    def strlen(self, name) -> Pipeline[_StrType]:
        """
        Return the number of bytes stored in the value of ``name``

        For more information see https://redis.io/commands/strlen
        """
        ...
    def substr(self, name, start, end=-1) -> Pipeline[_StrType]:
        """
        Return a substring of the string at key ``name``. ``start`` and ``end``
        are 0-based integers specifying the portion of the string to return.
        """
        ...
    def ttl(self, name: _Key) -> Pipeline[_StrType]:
        """
        Returns the number of seconds until the key ``name`` will expire

        For more information see https://redis.io/commands/ttl
        """
        ...
    def type(self, name) -> Pipeline[_StrType]:
        """
        Returns the type of key ``name``

        For more information see https://redis.io/commands/type
        """
        ...
    def unlink(self, *names: _Key) -> Pipeline[_StrType]:
        """
        Unlink one or more keys specified by ``names``

        For more information see https://redis.io/commands/unlink
        """
        ...
    def blmove(  # type: ignore[override]
        self,
        first_list: _Key,
        second_list: _Key,
        timeout: float,
        src: Literal["LEFT", "RIGHT"] = "LEFT",
        dest: Literal["LEFT", "RIGHT"] = "RIGHT",
    ) -> Pipeline[_StrType]:
        """
        Blocking version of lmove.

        For more information see https://redis.io/commands/blmove
        """
        ...
    def blpop(self, keys: _Value | Iterable[_Value], timeout: float = 0) -> Pipeline[_StrType]:
        """
        LPOP a value off of the first non-empty list
        named in the ``keys`` list.

        If none of the lists in ``keys`` has a value to LPOP, then block
        for ``timeout`` seconds, or until a value gets pushed on to one
        of the lists.

        If timeout is 0, then block indefinitely.

        For more information see https://redis.io/commands/blpop
        """
        ...
    def brpop(self, keys: _Value | Iterable[_Value], timeout: float = 0) -> Pipeline[_StrType]:
        """
        RPOP a value off of the first non-empty list
        named in the ``keys`` list.

        If none of the lists in ``keys`` has a value to RPOP, then block
        for ``timeout`` seconds, or until a value gets pushed on to one
        of the lists.

        If timeout is 0, then block indefinitely.

        For more information see https://redis.io/commands/brpop
        """
        ...
    def brpoplpush(self, src, dst, timeout=0) -> Pipeline[_StrType]:
        """
        Pop a value off the tail of ``src``, push it on the head of ``dst``
        and then return it.

        This command blocks until a value is in ``src`` or until ``timeout``
        seconds elapse, whichever is first. A ``timeout`` value of 0 blocks
        forever.

        For more information see https://redis.io/commands/brpoplpush
        """
        ...
    def lindex(self, name: _Key, index: int) -> Pipeline[_StrType]:
        """
        Return the item from list ``name`` at position ``index``

        Negative indexes are supported and will return an item at the
        end of the list

        For more information see https://redis.io/commands/lindex
        """
        ...
    def linsert(  # type: ignore[override]
        self, name: _Key, where: Literal["BEFORE", "AFTER", "before", "after"], refvalue: _Value, value: _Value
    ) -> Pipeline[_StrType]:
        """
        Insert ``value`` in list ``name`` either immediately before or after
        [``where``] ``refvalue``

        Returns the new length of the list on success or -1 if ``refvalue``
        is not in the list.

        For more information see https://redis.io/commands/linsert
        """
        ...
    def llen(self, name: _Key) -> Pipeline[_StrType]:
        """
        Return the length of the list ``name``

        For more information see https://redis.io/commands/llen
        """
        ...
    def lmove(  # type: ignore[override]
        self,
        first_list: _Key,
        second_list: _Key,
        src: Literal["LEFT", "RIGHT"] = "LEFT",
        dest: Literal["LEFT", "RIGHT"] = "RIGHT",
    ) -> Pipeline[_StrType]:
        """
        Atomically returns and removes the first/last element of a list,
        pushing it as the first/last element on the destination list.
        Returns the element being popped and pushed.

        For more information see https://redis.io/commands/lmove
        """
        ...
    def lpop(self, name, count: int | None = None) -> Pipeline[_StrType]:
        """
        Removes and returns the first elements of the list ``name``.

        By default, the command pops a single element from the beginning of
        the list. When provided with the optional ``count`` argument, the reply
        will consist of up to count elements, depending on the list's length.

        For more information see https://redis.io/commands/lpop
        """
        ...
    def lpush(self, name: _Value, *values: _Value) -> Pipeline[_StrType]:
        """
        Push ``values`` onto the head of the list ``name``

        For more information see https://redis.io/commands/lpush
        """
        ...
    def lpushx(self, name, value) -> Pipeline[_StrType]:
        """
        Push ``value`` onto the head of the list ``name`` if ``name`` exists

        For more information see https://redis.io/commands/lpushx
        """
        ...
    def lrange(self, name: _Key, start: int, end: int) -> Pipeline[_StrType]:
        """
        Return a slice of the list ``name`` between
        position ``start`` and ``end``

        ``start`` and ``end`` can be negative numbers just like
        Python slicing notation

        For more information see https://redis.io/commands/lrange
        """
        ...
    def lrem(self, name: _Key, count: int, value: _Value) -> Pipeline[_StrType]:
        """
        Remove the first ``count`` occurrences of elements equal to ``value``
        from the list stored at ``name``.

        The count argument influences the operation in the following ways:
            count > 0: Remove elements equal to value moving from head to tail.
            count < 0: Remove elements equal to value moving from tail to head.
            count = 0: Remove all elements equal to value.

            For more information see https://redis.io/commands/lrem
        """
        ...
    def lset(self, name: _Key, index: int, value: _Value) -> Pipeline[_StrType]:
        """
        Set element at ``index`` of list ``name`` to ``value``

        For more information see https://redis.io/commands/lset
        """
        ...
    def ltrim(self, name: _Key, start: int, end: int) -> Pipeline[_StrType]:
        """
        Trim the list ``name``, removing all values not within the slice
        between ``start`` and ``end``

        ``start`` and ``end`` can be negative numbers just like
        Python slicing notation

        For more information see https://redis.io/commands/ltrim
        """
        ...
    def rpop(self, name, count: int | None = None) -> Pipeline[_StrType]:
        """
        Removes and returns the last elements of the list ``name``.

        By default, the command pops a single element from the end of the list.
        When provided with the optional ``count`` argument, the reply will
        consist of up to count elements, depending on the list's length.

        For more information see https://redis.io/commands/rpop
        """
        ...
    def rpoplpush(self, src, dst) -> Pipeline[_StrType]:
        """
        RPOP a value off of the ``src`` list and atomically LPUSH it
        on to the ``dst`` list.  Returns the value.

        For more information see https://redis.io/commands/rpoplpush
        """
        ...
    def rpush(self, name: _Value, *values: _Value) -> Pipeline[_StrType]:
        """
        Push ``values`` onto the tail of the list ``name``

        For more information see https://redis.io/commands/rpush
        """
        ...
    def rpushx(self, name, value) -> Pipeline[_StrType]:
        """
        Push ``value`` onto the tail of the list ``name`` if ``name`` exists

        For more information see https://redis.io/commands/rpushx
        """
        ...
    def sort(  # type: ignore[override]
        self,
        name: _Key,
        start: int | None = None,
        num: int | None = None,
        by: _Key | None = None,
        get: _Key | Sequence[_Key] | None = None,
        desc: bool = False,
        alpha: bool = False,
        store: _Key | None = None,
        groups: bool = False,
    ) -> Pipeline[_StrType]:
        """
        Sort and return the list, set or sorted set at ``name``.

        ``start`` and ``num`` allow for paging through the sorted data

        ``by`` allows using an external key to weight and sort the items.
            Use an "*" to indicate where in the key the item value is located

        ``get`` allows for returning items from external keys rather than the
            sorted data itself.  Use an "*" to indicate where in the key
            the item value is located

        ``desc`` allows for reversing the sort

        ``alpha`` allows for sorting lexicographically rather than numerically

        ``store`` allows for storing the result of the sort into
            the key ``store``

        ``groups`` if set to True and if ``get`` contains at least two
            elements, sort will return a list of tuples, each containing the
            values fetched from the arguments to ``get``.

        For more information see https://redis.io/commands/sort
        """
        ...
    def scan(  # type: ignore[override]
        self, cursor: int = 0, match: _Key | None = None, count: int | None = None, _type: str | None = None
    ) -> Pipeline[_StrType]:
        """
        Incrementally return lists of key names. Also return a cursor
        indicating the scan position.

        ``match`` allows for filtering the keys by pattern

        ``count`` provides a hint to Redis about the number of keys to
            return per batch.

        ``_type`` filters the returned values by a particular Redis type.
            Stock Redis instances allow for the following types:
            HASH, LIST, SET, STREAM, STRING, ZSET
            Additionally, Redis modules can expose other types as well.

        For more information see https://redis.io/commands/scan
        """
        ...
    def scan_iter(self, match: _Key | None = None, count: int | None = None, _type: str | None = None) -> Iterator[Any]:
        """
        Make an iterator using the SCAN command so that the client doesn't
        need to remember the cursor position.

        ``match`` allows for filtering the keys by pattern

        ``count`` provides a hint to Redis about the number of keys to
            return per batch.

        ``_type`` filters the returned values by a particular Redis type.
            Stock Redis instances allow for the following types:
            HASH, LIST, SET, STREAM, STRING, ZSET
            Additionally, Redis modules can expose other types as well.
        """
        ...
    def sscan(self, name: _Key, cursor: int = 0, match: _Key | None = None, count: int | None = None) -> Pipeline[_StrType]:
        """
        Incrementally return lists of elements in a set. Also return a cursor
        indicating the scan position.

        ``match`` allows for filtering the keys by pattern

        ``count`` allows for hint the minimum number of returns

        For more information see https://redis.io/commands/sscan
        """
        ...
    def sscan_iter(self, name: _Key, match: _Key | None = None, count: int | None = None) -> Iterator[Any]:
        """
        Make an iterator using the SSCAN command so that the client doesn't
        need to remember the cursor position.

        ``match`` allows for filtering the keys by pattern

        ``count`` allows for hint the minimum number of returns
        """
        ...
    def hscan(self, name: _Key, cursor: int = 0, match: _Key | None = None, count: int | None = None) -> Pipeline[_StrType]:
        """
        Incrementally return key/value slices in a hash. Also return a cursor
        indicating the scan position.

        ``match`` allows for filtering the keys by pattern

        ``count`` allows for hint the minimum number of returns

        For more information see https://redis.io/commands/hscan
        """
        ...
    def hscan_iter(self, name, match: _Key | None = None, count: int | None = None) -> Iterator[Any]:
        """
        Make an iterator using the HSCAN command so that the client doesn't
        need to remember the cursor position.

        ``match`` allows for filtering the keys by pattern

        ``count`` allows for hint the minimum number of returns
        """
        ...
    def zscan_iter(
        self, name: _Key, match: _Key | None = None, count: int | None = None, score_cast_func: Callable[[_StrType], Any] = ...
    ) -> Iterator[Any]:
        """
        Make an iterator using the ZSCAN command so that the client doesn't
        need to remember the cursor position.

        ``match`` allows for filtering the keys by pattern

        ``count`` allows for hint the minimum number of returns

        ``score_cast_func`` a callable used to cast the score return value
        """
        ...
    def sadd(self, name: _Key, *values: _Value) -> Pipeline[_StrType]:
        """
        Add ``value(s)`` to set ``name``

        For more information see https://redis.io/commands/sadd
        """
        ...
    def scard(self, name: _Key) -> Pipeline[_StrType]:
        """
        Return the number of elements in set ``name``

        For more information see https://redis.io/commands/scard
        """
        ...
    def sdiff(self, keys: _Key | Iterable[_Key], *args: _Key) -> Pipeline[_StrType]:
        """
        Return the difference of sets specified by ``keys``

        For more information see https://redis.io/commands/sdiff
        """
        ...
    def sdiffstore(self, dest: _Key, keys: _Key | Iterable[_Key], *args: _Key) -> Pipeline[_StrType]:
        """
        Store the difference of sets specified by ``keys`` into a new
        set named ``dest``.  Returns the number of keys in the new set.

        For more information see https://redis.io/commands/sdiffstore
        """
        ...
    def sinter(self, keys: _Key | Iterable[_Key], *args: _Key) -> Pipeline[_StrType]:
        """
        Return the intersection of sets specified by ``keys``

        For more information see https://redis.io/commands/sinter
        """
        ...
    def sinterstore(self, dest: _Key, keys: _Key | Iterable[_Key], *args: _Key) -> Pipeline[_StrType]:
        """
        Store the intersection of sets specified by ``keys`` into a new
        set named ``dest``.  Returns the number of keys in the new set.

        For more information see https://redis.io/commands/sinterstore
        """
        ...
    def sismember(self, name: _Key, value: _Value) -> Pipeline[_StrType]:
        """
        Return a boolean indicating if ``value`` is a member of set ``name``

        For more information see https://redis.io/commands/sismember
        """
        ...
    def smembers(self, name: _Key) -> Pipeline[_StrType]:
        """
        Return all members of the set ``name``

        For more information see https://redis.io/commands/smembers
        """
        ...
    def smove(self, src: _Key, dst: _Key, value: _Value) -> Pipeline[_StrType]:
        """
        Move ``value`` from set ``src`` to set ``dst`` atomically

        For more information see https://redis.io/commands/smove
        """
        ...
    def spop(self, name: _Key, count: int | None = None) -> Pipeline[_StrType]:
        """
        Remove and return a random member of set ``name``

        For more information see https://redis.io/commands/spop
        """
        ...
    def srandmember(self, name: _Key, number: int | None = None) -> Pipeline[_StrType]:
        """
        If ``number`` is None, returns a random member of set ``name``.

        If ``number`` is supplied, returns a list of ``number`` random
        members of set ``name``. Note this is only available when running
        Redis 2.6+.

        For more information see https://redis.io/commands/srandmember
        """
        ...
    def srem(self, name: _Key, *values: _Value) -> Pipeline[_StrType]:
        """
        Remove ``values`` from set ``name``

        For more information see https://redis.io/commands/srem
        """
        ...
    def sunion(self, keys: _Key | Iterable[_Key], *args: _Key) -> Pipeline[_StrType]:
        """
        Return the union of sets specified by ``keys``

        For more information see https://redis.io/commands/sunion
        """
        ...
    def sunionstore(self, dest: _Key, keys: _Key | Iterable[_Key], *args: _Key) -> Pipeline[_StrType]:
        """
        Store the union of sets specified by ``keys`` into a new
        set named ``dest``.  Returns the number of keys in the new set.

        For more information see https://redis.io/commands/sunionstore
        """
        ...
    def xack(self, name, groupname, *ids) -> Pipeline[_StrType]:
        """
        Acknowledges the successful processing of one or more messages.
        name: name of the stream.
        groupname: name of the consumer group.
        *ids: message ids to acknowledge.

        For more information see https://redis.io/commands/xack
        """
        ...
    def xadd(
        self,
        name,
        fields,
        id="*",
        maxlen=None,
        approximate: bool = True,
        nomkstream: bool = False,
        minid: Incomplete | None = None,
        limit: int | None = None,
    ) -> Pipeline[_StrType]:
        """
        Add to a stream.
        name: name of the stream
        fields: dict of field/value pairs to insert into the stream
        id: Location to insert this record. By default it is appended.
        maxlen: truncate old stream members beyond this size.
        Can't be specified with minid.
        approximate: actual stream length may be slightly more than maxlen
        nomkstream: When set to true, do not make a stream
        minid: the minimum id in the stream to query.
        Can't be specified with maxlen.
        limit: specifies the maximum number of entries to retrieve

        For more information see https://redis.io/commands/xadd
        """
        ...
    def xclaim(
        self,
        name,
        groupname,
        consumername,
        min_idle_time,
        message_ids,
        idle=None,
        time=None,
        retrycount=None,
        force=False,
        justid=False,
    ) -> Pipeline[_StrType]:
        """
        Changes the ownership of a pending message.
        name: name of the stream.
        groupname: name of the consumer group.
        consumername: name of a consumer that claims the message.
        min_idle_time: filter messages that were idle less than this amount of
        milliseconds
        message_ids: non-empty list or tuple of message IDs to claim
        idle: optional. Set the idle time (last time it was delivered) of the
         message in ms
        time: optional integer. This is the same as idle but instead of a
         relative amount of milliseconds, it sets the idle time to a specific
         Unix time (in milliseconds).
        retrycount: optional integer. set the retry counter to the specified
         value. This counter is incremented every time a message is delivered
         again.
        force: optional boolean, false by default. Creates the pending message
         entry in the PEL even if certain specified IDs are not already in the
         PEL assigned to a different client.
        justid: optional boolean, false by default. Return just an array of IDs
         of messages successfully claimed, without returning the actual message

         For more information see https://redis.io/commands/xclaim
        """
        ...
    def xdel(self, name, *ids) -> Pipeline[_StrType]:
        """
        Deletes one or more messages from a stream.
        name: name of the stream.
        *ids: message ids to delete.

        For more information see https://redis.io/commands/xdel
        """
        ...
    def xgroup_create(self, name, groupname, id="$", mkstream=False, entries_read: int | None = None) -> Pipeline[_StrType]:
        """
        Create a new consumer group associated with a stream.
        name: name of the stream.
        groupname: name of the consumer group.
        id: ID of the last item in the stream to consider already delivered.

        For more information see https://redis.io/commands/xgroup-create
        """
        ...
    def xgroup_delconsumer(self, name, groupname, consumername) -> Pipeline[_StrType]:
        """
        Remove a specific consumer from a consumer group.
        Returns the number of pending messages that the consumer had before it
        was deleted.
        name: name of the stream.
        groupname: name of the consumer group.
        consumername: name of consumer to delete

        For more information see https://redis.io/commands/xgroup-delconsumer
        """
        ...
    def xgroup_destroy(self, name, groupname) -> Pipeline[_StrType]:
        """
        Destroy a consumer group.
        name: name of the stream.
        groupname: name of the consumer group.

        For more information see https://redis.io/commands/xgroup-destroy
        """
        ...
    def xgroup_setid(self, name, groupname, id, entries_read: int | None = None) -> Pipeline[_StrType]:
        """
        Set the consumer group last delivered ID to something else.
        name: name of the stream.
        groupname: name of the consumer group.
        id: ID of the last item in the stream to consider already delivered.

        For more information see https://redis.io/commands/xgroup-setid
        """
        ...
    def xinfo_consumers(self, name, groupname) -> Pipeline[_StrType]:
        """
        Returns general information about the consumers in the group.
        name: name of the stream.
        groupname: name of the consumer group.

        For more information see https://redis.io/commands/xinfo-consumers
        """
        ...
    def xinfo_groups(self, name) -> Pipeline[_StrType]:
        """
        Returns general information about the consumer groups of the stream.
        name: name of the stream.

        For more information see https://redis.io/commands/xinfo-groups
        """
        ...
    def xinfo_stream(self, name, full: bool = False) -> Pipeline[_StrType]:
        """
        Returns general information about the stream.
        name: name of the stream.
        full: optional boolean, false by default. Return full summary

        For more information see https://redis.io/commands/xinfo-stream
        """
        ...
    def xlen(self, name: _Key) -> Pipeline[_StrType]:
        """
        Returns the number of elements in a given stream.

        For more information see https://redis.io/commands/xlen
        """
        ...
    def xpending(self, name, groupname) -> Pipeline[_StrType]:
        """
        Returns information about pending messages of a group.
        name: name of the stream.
        groupname: name of the consumer group.

        For more information see https://redis.io/commands/xpending
        """
        ...
    def xpending_range(
        self, name: _Key, groupname, min, max, count: int, consumername: Incomplete | None = None, idle: int | None = None
    ) -> Pipeline[_StrType]:
        """
        Returns information about pending messages, in a range.

        name: name of the stream.
        groupname: name of the consumer group.
        idle: available from  version 6.2. filter entries by their
        idle-time, given in milliseconds (optional).
        min: minimum stream ID.
        max: maximum stream ID.
        count: number of messages to return
        consumername: name of a consumer to filter by (optional).
        """
        ...
    def xrange(self, name, min="-", max="+", count=None) -> Pipeline[_StrType]:
        """
        Read stream values within an interval.
        name: name of the stream.
        start: first stream ID. defaults to '-',
               meaning the earliest available.
        finish: last stream ID. defaults to '+',
                meaning the latest available.
        count: if set, only return this many items, beginning with the
               earliest available.

        For more information see https://redis.io/commands/xrange
        """
        ...
    def xread(self, streams, count=None, block=None) -> Pipeline[_StrType]:
        """
        Block and monitor multiple streams for new data.
        streams: a dict of stream names to stream IDs, where
                   IDs indicate the last ID already seen.
        count: if set, only return this many items, beginning with the
               earliest available.
        block: number of milliseconds to wait, if nothing already present.

        For more information see https://redis.io/commands/xread
        """
        ...
    def xreadgroup(self, groupname, consumername, streams, count=None, block=None, noack=False) -> Pipeline[_StrType]:
        """
        Read from a stream via a consumer group.
        groupname: name of the consumer group.
        consumername: name of the requesting consumer.
        streams: a dict of stream names to stream IDs, where
               IDs indicate the last ID already seen.
        count: if set, only return this many items, beginning with the
               earliest available.
        block: number of milliseconds to wait, if nothing already present.
        noack: do not add messages to the PEL

        For more information see https://redis.io/commands/xreadgroup
        """
        ...
    def xrevrange(self, name, max="+", min="-", count=None) -> Pipeline[_StrType]:
        """
        Read stream values within an interval, in reverse order.
        name: name of the stream
        start: first stream ID. defaults to '+',
               meaning the latest available.
        finish: last stream ID. defaults to '-',
                meaning the earliest available.
        count: if set, only return this many items, beginning with the
               latest available.

        For more information see https://redis.io/commands/xrevrange
        """
        ...
    def xtrim(
        self, name, maxlen: int | None = None, approximate: bool = True, minid: Incomplete | None = None, limit: int | None = None
    ) -> Pipeline[_StrType]:
        """
        Trims old messages from a stream.
        name: name of the stream.
        maxlen: truncate old stream messages beyond this size
        Can't be specified with minid.
        approximate: actual stream length may be slightly more than maxlen
        minid: the minimum id in the stream to query
        Can't be specified with maxlen.
        limit: specifies the maximum number of entries to retrieve

        For more information see https://redis.io/commands/xtrim
        """
        ...
    def zadd(  # type: ignore[override]
        self,
        name: _Key,
        mapping: Mapping[_Key, _Value],
        nx: bool = False,
        xx: bool = False,
        ch: bool = False,
        incr: bool = False,
        gt: Incomplete | None = False,
        lt: Incomplete | None = False,
    ) -> Pipeline[_StrType]:
        """
        Set any number of element-name, score pairs to the key ``name``. Pairs
        are specified as a dict of element-names keys to score values.

        ``nx`` forces ZADD to only create new elements and not to update
        scores for elements that already exist.

        ``xx`` forces ZADD to only update scores of elements that already
        exist. New elements will not be added.

        ``ch`` modifies the return value to be the numbers of elements changed.
        Changed elements include new elements that were added and elements
        whose scores changed.

        ``incr`` modifies ZADD to behave like ZINCRBY. In this mode only a
        single element/score pair can be specified and the score is the amount
        the existing score will be incremented by. When using this mode the
        return value of ZADD will be the new score of the element.

        ``LT`` Only update existing elements if the new score is less than
        the current score. This flag doesn't prevent adding new elements.

        ``GT`` Only update existing elements if the new score is greater than
        the current score. This flag doesn't prevent adding new elements.

        The return value of ZADD varies based on the mode specified. With no
        options, ZADD returns the number of new elements added to the sorted
        set.

        ``NX``, ``LT``, and ``GT`` are mutually exclusive options.

        See: https://redis.io/commands/ZADD
        """
        ...
    def zcard(self, name: _Key) -> Pipeline[_StrType]:
        """
        Return the number of elements in the sorted set ``name``

        For more information see https://redis.io/commands/zcard
        """
        ...
    def zcount(self, name: _Key, min: _Value, max: _Value) -> Pipeline[_StrType]:
        """
        Returns the number of elements in the sorted set at key ``name`` with
        a score between ``min`` and ``max``.

        For more information see https://redis.io/commands/zcount
        """
        ...
    def zincrby(self, name: _Key, amount: float, value: _Value) -> Pipeline[_StrType]:
        """
        Increment the score of ``value`` in sorted set ``name`` by ``amount``

        For more information see https://redis.io/commands/zincrby
        """
        ...
    def zinterstore(  # type: ignore[override]
        self, dest: _Key, keys: Iterable[_Key], aggregate: Literal["SUM", "MIN", "MAX"] | None = None
    ) -> Pipeline[_StrType]:
        """
        Intersect multiple sorted sets specified by ``keys`` into a new
        sorted set, ``dest``. Scores in the destination will be aggregated
        based on the ``aggregate``. This option defaults to SUM, where the
        score of an element is summed across the inputs where it exists.
        When this option is set to either MIN or MAX, the resulting set will
        contain the minimum or maximum score of an element across the inputs
        where it exists.

        For more information see https://redis.io/commands/zinterstore
        """
        ...
    def zlexcount(self, name: _Key, min: _Value, max: _Value) -> Pipeline[_StrType]:
        """
        Return the number of items in the sorted set ``name`` between the
        lexicographical range ``min`` and ``max``.

        For more information see https://redis.io/commands/zlexcount
        """
        ...
    def zpopmax(self, name: _Key, count: int | None = None) -> Pipeline[_StrType]:
        """
        Remove and return up to ``count`` members with the highest scores
        from the sorted set ``name``.

        For more information see https://redis.io/commands/zpopmax
        """
        ...
    def zpopmin(self, name: _Key, count: int | None = None) -> Pipeline[_StrType]:
        """
        Remove and return up to ``count`` members with the lowest scores
        from the sorted set ``name``.

        For more information see https://redis.io/commands/zpopmin
        """
        ...
    def bzpopmax(self, keys: _Key | Iterable[_Key], timeout: float = 0) -> Pipeline[_StrType]:
        """
        ZPOPMAX a value off of the first non-empty sorted set
        named in the ``keys`` list.

        If none of the sorted sets in ``keys`` has a value to ZPOPMAX,
        then block for ``timeout`` seconds, or until a member gets added
        to one of the sorted sets.

        If timeout is 0, then block indefinitely.

        For more information see https://redis.io/commands/bzpopmax
        """
        ...
    def bzpopmin(self, keys: _Key | Iterable[_Key], timeout: float = 0) -> Pipeline[_StrType]:
        """
        ZPOPMIN a value off of the first non-empty sorted set
        named in the ``keys`` list.

        If none of the sorted sets in ``keys`` has a value to ZPOPMIN,
        then block for ``timeout`` seconds, or until a member gets added
        to one of the sorted sets.

        If timeout is 0, then block indefinitely.

        For more information see https://redis.io/commands/bzpopmin
        """
        ...
    def zrange(  # type: ignore[override]
        self,
        name: _Key,
        start: int,
        end: int,
        desc: bool = False,
        withscores: bool = False,
        score_cast_func: Callable[[_StrType], Any] = ...,
        byscore: bool = False,
        bylex: bool = False,
        offset: int | None = None,
        num: int | None = None,
    ) -> Pipeline[_StrType]:
        """
        Return a range of values from sorted set ``name`` between
        ``start`` and ``end`` sorted in ascending order.

        ``start`` and ``end`` can be negative, indicating the end of the range.

        ``desc`` a boolean indicating whether to sort the results in reversed
        order.

        ``withscores`` indicates to return the scores along with the values.
        The return type is a list of (value, score) pairs.

        ``score_cast_func`` a callable used to cast the score return value.

        ``byscore`` when set to True, returns the range of elements from the
        sorted set having scores equal or between ``start`` and ``end``.

        ``bylex`` when set to True, returns the range of elements from the
        sorted set between the ``start`` and ``end`` lexicographical closed
        range intervals.
        Valid ``start`` and ``end`` must start with ( or [, in order to specify
        whether the range interval is exclusive or inclusive, respectively.

        ``offset`` and ``num`` are specified, then return a slice of the range.
        Can't be provided when using ``bylex``.

        For more information see https://redis.io/commands/zrange
        """
        ...
    def zrangebylex(  # type: ignore[override]
        self, name: _Key, min: _Value, max: _Value, start: int | None = None, num: int | None = None
    ) -> Pipeline[_StrType]:
        """
        Return the lexicographical range of values from sorted set ``name``
        between ``min`` and ``max``.

        If ``start`` and ``num`` are specified, then return a slice of the
        range.

        For more information see https://redis.io/commands/zrangebylex
        """
        ...
    def zrangebyscore(  # type: ignore[override]
        self,
        name: _Key,
        min: _Value,
        max: _Value,
        start: int | None = None,
        num: int | None = None,
        withscores: bool = False,
        score_cast_func: Callable[[_StrType], Any] = ...,
    ) -> Pipeline[_StrType]:
        """
        Return a range of values from the sorted set ``name`` with scores
        between ``min`` and ``max``.

        If ``start`` and ``num`` are specified, then return a slice
        of the range.

        ``withscores`` indicates to return the scores along with the values.
        The return type is a list of (value, score) pairs

        `score_cast_func`` a callable used to cast the score return value

        For more information see https://redis.io/commands/zrangebyscore
        """
        ...
    def zrank(self, name: _Key, value: _Value, withscore: bool = False) -> Pipeline[_StrType]:
        """
        Returns a 0-based value indicating the rank of ``value`` in sorted set
        ``name``.
        The optional WITHSCORE argument supplements the command's
        reply with the score of the element returned.

        For more information see https://redis.io/commands/zrank
        """
        ...
    def zrem(self, name: _Key, *values: _Value) -> Pipeline[_StrType]:
        """
        Remove member ``values`` from sorted set ``name``

        For more information see https://redis.io/commands/zrem
        """
        ...
    def zremrangebylex(self, name: _Key, min: _Value, max: _Value) -> Pipeline[_StrType]:
        """
        Remove all elements in the sorted set ``name`` between the
        lexicographical range specified by ``min`` and ``max``.

        Returns the number of elements removed.

        For more information see https://redis.io/commands/zremrangebylex
        """
        ...
    def zremrangebyrank(self, name: _Key, min: _Value, max: _Value) -> Pipeline[_StrType]:
        """
        Remove all elements in the sorted set ``name`` with ranks between
        ``min`` and ``max``. Values are 0-based, ordered from smallest score
        to largest. Values can be negative indicating the highest scores.
        Returns the number of elements removed

        For more information see https://redis.io/commands/zremrangebyrank
        """
        ...
    def zremrangebyscore(self, name: _Key, min: _Value, max: _Value) -> Pipeline[_StrType]:
        """
        Remove all elements in the sorted set ``name`` with scores
        between ``min`` and ``max``. Returns the number of elements removed.

        For more information see https://redis.io/commands/zremrangebyscore
        """
        ...
    def zrevrange(  # type: ignore[override]
        self, name: _Key, start: int, end: int, withscores: bool = False, score_cast_func: Callable[[_StrType], Any] = ...
    ) -> Pipeline[_StrType]:
        """
        Return a range of values from sorted set ``name`` between
        ``start`` and ``end`` sorted in descending order.

        ``start`` and ``end`` can be negative, indicating the end of the range.

        ``withscores`` indicates to return the scores along with the values
        The return type is a list of (value, score) pairs

        ``score_cast_func`` a callable used to cast the score return value

        For more information see https://redis.io/commands/zrevrange
        """
        ...
    def zrevrangebyscore(  # type: ignore[override]
        self,
        name: _Key,
        max: _Value,
        min: _Value,
        start: int | None = None,
        num: int | None = None,
        withscores: bool = False,
        score_cast_func: Callable[[_StrType], Any] = ...,
    ) -> Pipeline[_StrType]:
        """
        Return a range of values from the sorted set ``name`` with scores
        between ``min`` and ``max`` in descending order.

        If ``start`` and ``num`` are specified, then return a slice
        of the range.

        ``withscores`` indicates to return the scores along with the values.
        The return type is a list of (value, score) pairs

        ``score_cast_func`` a callable used to cast the score return value

        For more information see https://redis.io/commands/zrevrangebyscore
        """
        ...
    def zrevrangebylex(  # type: ignore[override]
        self, name: _Key, max: _Value, min: _Value, start: int | None = None, num: int | None = None
    ) -> Pipeline[_StrType]:
        """
        Return the reversed lexicographical range of values from sorted set
        ``name`` between ``max`` and ``min``.

        If ``start`` and ``num`` are specified, then return a slice of the
        range.

        For more information see https://redis.io/commands/zrevrangebylex
        """
        ...
    def zrevrank(self, name: _Key, value: _Value, withscore: bool = False) -> Pipeline[_StrType]:
        """
        Returns a 0-based value indicating the descending rank of
        ``value`` in sorted set ``name``.
        The optional ``withscore`` argument supplements the command's
        reply with the score of the element returned.

        For more information see https://redis.io/commands/zrevrank
        """
        ...
    def zscore(self, name: _Key, value: _Value) -> Pipeline[_StrType]:
        """
        Return the score of element ``value`` in sorted set ``name``

        For more information see https://redis.io/commands/zscore
        """
        ...
    def zunionstore(  # type: ignore[override]
        self, dest: _Key, keys: Iterable[_Key], aggregate: Literal["SUM", "MIN", "MAX"] | None = None
    ) -> Pipeline[_StrType]:
        """
        Union multiple sorted sets specified by ``keys`` into
        a new sorted set, ``dest``. Scores in the destination will be
        aggregated based on the ``aggregate``, or SUM if none is provided.

        For more information see https://redis.io/commands/zunionstore
        """
        ...
    def pfadd(self, name: _Key, *values: _Value) -> Pipeline[_StrType]:
        """
        Adds the specified elements to the specified HyperLogLog.

        For more information see https://redis.io/commands/pfadd
        """
        ...
    def pfcount(self, name: _Key) -> Pipeline[_StrType]:
        """
        Return the approximated cardinality of
        the set observed by the HyperLogLog at key(s).

        For more information see https://redis.io/commands/pfcount
        """
        ...
    def pfmerge(self, dest: _Key, *sources: _Key) -> Pipeline[_StrType]:
        """
        Merge N different HyperLogLogs into a single one.

        For more information see https://redis.io/commands/pfmerge
        """
        ...
    def hdel(self, name: _Key, *keys: _Key) -> Pipeline[_StrType]:
        """
        Delete ``keys`` from hash ``name``

        For more information see https://redis.io/commands/hdel
        """
        ...
    def hexists(self, name: _Key, key: _Key) -> Pipeline[_StrType]:
        """
        Returns a boolean indicating if ``key`` exists within hash ``name``

        For more information see https://redis.io/commands/hexists
        """
        ...
    def hget(self, name: _Key, key: _Key) -> Pipeline[_StrType]:
        """
        Return the value of ``key`` within the hash ``name``

        For more information see https://redis.io/commands/hget
        """
        ...
    def hgetall(self, name: _Key) -> Pipeline[_StrType]:
        """
        Return a Python dict of the hash's name/value pairs

        For more information see https://redis.io/commands/hgetall
        """
        ...
    def hincrby(self, name: _Key, key: _Key, amount: int = 1) -> Pipeline[_StrType]:
        """
        Increment the value of ``key`` in hash ``name`` by ``amount``

        For more information see https://redis.io/commands/hincrby
        """
        ...
    def hincrbyfloat(self, name: _Key, key: _Key, amount: float = 1.0) -> Pipeline[_StrType]:
        """
        Increment the value of ``key`` in hash ``name`` by floating ``amount``

        For more information see https://redis.io/commands/hincrbyfloat
        """
        ...
    def hkeys(self, name: _Key) -> Pipeline[_StrType]:
        """
        Return the list of keys within hash ``name``

        For more information see https://redis.io/commands/hkeys
        """
        ...
    def hlen(self, name: _Key) -> Pipeline[_StrType]:
        """
        Return the number of elements in hash ``name``

        For more information see https://redis.io/commands/hlen
        """
        ...
    @overload  # type: ignore[override]
    def hset(
        self, name: _Key, key: _Key, value: _Value, mapping: Mapping[_Key, _Value] | None = None, items: Incomplete | None = None
    ) -> Pipeline[_StrType]:
        """
        Set ``key`` to ``value`` within hash ``name``,
        ``mapping`` accepts a dict of key/value pairs that will be
        added to hash ``name``.
        ``items`` accepts a list of key/value pairs that will be
        added to hash ``name``.
        Returns the number of fields that were added.

        For more information see https://redis.io/commands/hset
        """
        ...
    @overload
    def hset(
        self, name: _Key, key: None, value: None, mapping: Mapping[_Key, _Value], items: Incomplete | None = None
    ) -> Pipeline[_StrType]:
        """
        Set ``key`` to ``value`` within hash ``name``,
        ``mapping`` accepts a dict of key/value pairs that will be
        added to hash ``name``.
        ``items`` accepts a list of key/value pairs that will be
        added to hash ``name``.
        Returns the number of fields that were added.

        For more information see https://redis.io/commands/hset
        """
        ...
    @overload
    def hset(self, name: _Key, *, mapping: Mapping[_Key, _Value], items: Incomplete | None = None) -> Pipeline[_StrType]:
        """
        Set ``key`` to ``value`` within hash ``name``,
        ``mapping`` accepts a dict of key/value pairs that will be
        added to hash ``name``.
        ``items`` accepts a list of key/value pairs that will be
        added to hash ``name``.
        Returns the number of fields that were added.

        For more information see https://redis.io/commands/hset
        """
        ...
    def hsetnx(self, name: _Key, key: _Key, value: _Value) -> Pipeline[_StrType]:
        """
        Set ``key`` to ``value`` within hash ``name`` if ``key`` does not
        exist.  Returns 1 if HSETNX created a field, otherwise 0.

        For more information see https://redis.io/commands/hsetnx
        """
        ...
    def hmset(self, name: _Key, mapping: Mapping[_Key, _Value]) -> Pipeline[_StrType]:
        """
        Set key to value within hash ``name`` for each corresponding
        key and value from the ``mapping`` dict.

        For more information see https://redis.io/commands/hmset
        """
        ...
    def hmget(self, name: _Key, keys: _Key | Iterable[_Key], *args: _Key) -> Pipeline[_StrType]:
        """
        Returns a list of values ordered identically to ``keys``

        For more information see https://redis.io/commands/hmget
        """
        ...
    def hvals(self, name: _Key) -> Pipeline[_StrType]:
        """
        Return the list of values within hash ``name``

        For more information see https://redis.io/commands/hvals
        """
        ...
    def publish(self, channel: _Key, message: _Key) -> Pipeline[_StrType]:
        """
        Publish ``message`` on ``channel``.
        Returns the number of subscribers the message was delivered to.

        For more information see https://redis.io/commands/publish
        """
        ...
    def eval(self, script, numkeys, *keys_and_args) -> Pipeline[_StrType]:
        """
        Execute the Lua ``script``, specifying the ``numkeys`` the script
        will touch and the key names and argument values in ``keys_and_args``.
        Returns the result of the script.

        In practice, use the object returned by ``register_script``. This
        function exists purely for Redis API completion.

        For more information see  https://redis.io/commands/eval
        """
        ...
    def evalsha(self, sha, numkeys, *keys_and_args) -> Pipeline[_StrType]:
        """
        Use the ``sha`` to execute a Lua script already registered via EVAL
        or SCRIPT LOAD. Specify the ``numkeys`` the script will touch and the
        key names and argument values in ``keys_and_args``. Returns the result
        of the script.

        In practice, use the object returned by ``register_script``. This
        function exists purely for Redis API completion.

        For more information see  https://redis.io/commands/evalsha
        """
        ...
    def script_exists(self, *args) -> Pipeline[_StrType]:
        """
        Check if a script exists in the script cache by specifying the SHAs of
        each script as ``args``. Returns a list of boolean values indicating if
        if each already script exists in the cache.

        For more information see  https://redis.io/commands/script-exists
        """
        ...
    def script_flush(self, sync_type: Incomplete | None = None) -> Pipeline[_StrType]:
        """
        Flush all scripts from the script cache.
        ``sync_type`` is by default SYNC (synchronous) but it can also be
                      ASYNC.
        For more information see  https://redis.io/commands/script-flush
        """
        ...
    def script_kill(self) -> Pipeline[_StrType]:
        """
        Kill the currently executing Lua script

        For more information see https://redis.io/commands/script-kill
        """
        ...
    def script_load(self, script) -> Pipeline[_StrType]:
        """
        Load a Lua ``script`` into the script cache. Returns the SHA.

        For more information see https://redis.io/commands/script-load
        """
        ...
    def pubsub_channels(self, pattern: _Key = "*") -> Pipeline[_StrType]:
        """
        Return a list of channels that have at least one subscriber

        For more information see https://redis.io/commands/pubsub-channels
        """
        ...
    def pubsub_numsub(self, *args: _Key) -> Pipeline[_StrType]:
        """
        Return a list of (channel, number of subscribers) tuples
        for each channel given in ``*args``

        For more information see https://redis.io/commands/pubsub-numsub
        """
        ...
    def pubsub_numpat(self) -> Pipeline[_StrType]:
        """
        Returns the number of subscriptions to patterns

        For more information see https://redis.io/commands/pubsub-numpat
        """
        ...
    def monitor(self) -> Monitor: ...
    def cluster(self, cluster_arg: str, *args: Any) -> Pipeline[_StrType]: ...  # type: ignore[override]
    def client(self) -> Any: ...

class Monitor:
    """
    Monitor is useful for handling the MONITOR command to the redis server.
    next_command() method returns one command from monitor
    listen() method yields commands from monitor.
    """
    command_re: Pattern[str]
    monitor_re: Pattern[str]
    def __init__(self, connection_pool) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, *args: Unused) -> None: ...
    def next_command(self) -> dict[str, Any]:
        """Parse the response from a monitor command"""
        ...
    def listen(self) -> Iterable[dict[str, Any]]:
        """Listen for commands coming to the server."""
        ...
