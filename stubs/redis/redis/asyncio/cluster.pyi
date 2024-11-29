from _typeshed import Incomplete
from collections.abc import Awaitable, Callable, Mapping
from types import TracebackType
from typing import Any, Generic, TypeVar
from typing_extensions import Self

from redis.asyncio.client import ResponseCallbackT
from redis.asyncio.connection import AbstractConnection, BaseParser, Connection, Encoder
from redis.asyncio.parser import CommandsParser
from redis.client import AbstractRedis
from redis.cluster import AbstractRedisCluster, LoadBalancer

# TODO: add  AsyncRedisClusterCommands stubs
# from redis.commands import AsyncRedisClusterCommands
from redis.commands.core import _StrType
from redis.credentials import CredentialProvider
from redis.exceptions import ResponseError
from redis.retry import Retry
from redis.typing import AnyKeyT, EncodableT, KeyT

TargetNodesT = TypeVar("TargetNodesT", str, ClusterNode, list[ClusterNode], dict[Any, ClusterNode])  # noqa: Y001

# It uses `DefaultParser` in real life, but it is a dynamic base class.
class ClusterParser(BaseParser):
    def on_disconnect(self) -> None:
        """Called when the stream disconnects"""
        ...
    def on_connect(self, connection: AbstractConnection) -> None:
        """Called when the stream connects"""
        ...
    async def can_read_destructive(self) -> bool: ...
    async def read_response(self, disable_decoding: bool = False) -> EncodableT | ResponseError | list[EncodableT] | None: ...

class RedisCluster(AbstractRedis, AbstractRedisCluster, Generic[_StrType]):  # TODO: AsyncRedisClusterCommands
    """
    Create a new RedisCluster client.

    Pass one of parameters:

      - `host` & `port`
      - `startup_nodes`

    | Use ``await`` :meth:`initialize` to find cluster nodes & create connections.
    | Use ``await`` :meth:`close` to disconnect connections & close client.

    Many commands support the target_nodes kwarg. It can be one of the
    :attr:`NODE_FLAGS`:

      - :attr:`PRIMARIES`
      - :attr:`REPLICAS`
      - :attr:`ALL_NODES`
      - :attr:`RANDOM`
      - :attr:`DEFAULT_NODE`

    Note: This client is not thread/process/fork safe.

    :param host:
        | Can be used to point to a startup node
    :param port:
        | Port used if **host** is provided
    :param startup_nodes:
        | :class:`~.ClusterNode` to used as a startup node
    :param require_full_coverage:
        | When set to ``False``: the client will not require a full coverage of
          the slots. However, if not all slots are covered, and at least one node
          has ``cluster-require-full-coverage`` set to ``yes``, the server will throw
          a :class:`~.ClusterDownError` for some key-based commands.
        | When set to ``True``: all slots must be covered to construct the cluster
          client. If not all slots are covered, :class:`~.RedisClusterException` will be
          thrown.
        | See:
          https://redis.io/docs/manual/scaling/#redis-cluster-configuration-parameters
    :param read_from_replicas:
        | Enable read from replicas in READONLY mode. You can read possibly stale data.
          When set to true, read commands will be assigned between the primary and
          its replications in a Round-Robin manner.
    :param reinitialize_steps:
        | Specifies the number of MOVED errors that need to occur before reinitializing
          the whole cluster topology. If a MOVED error occurs and the cluster does not
          need to be reinitialized on this current error handling, only the MOVED slot
          will be patched with the redirected node.
          To reinitialize the cluster on every MOVED error, set reinitialize_steps to 1.
          To avoid reinitializing the cluster on moved errors, set reinitialize_steps to
          0.
    :param cluster_error_retry_attempts:
        | Number of times to retry before raising an error when :class:`~.TimeoutError`
          or :class:`~.ConnectionError` or :class:`~.ClusterDownError` are encountered
    :param connection_error_retry_attempts:
        | Number of times to retry before reinitializing when :class:`~.TimeoutError`
          or :class:`~.ConnectionError` are encountered.
          The default backoff strategy will be set if Retry object is not passed (see
          default_backoff in backoff.py). To change it, pass a custom Retry object
          using the "retry" keyword.
    :param max_connections:
        | Maximum number of connections per node. If there are no free connections & the
          maximum number of connections are already created, a
          :class:`~.MaxConnectionsError` is raised. This error may be retried as defined
          by :attr:`connection_error_retry_attempts`
    :param address_remap:
        | An optional callable which, when provided with an internal network
          address of a node, e.g. a `(host, port)` tuple, will return the address
          where the node is reachable.  This can be used to map the addresses at
          which the nodes _think_ they are, to addresses at which a client may
          reach them, such as when they sit behind a proxy.

    | Rest of the arguments will be passed to the
      :class:`~redis.asyncio.connection.Connection` instances when created

    :raises RedisClusterException:
        if any arguments are invalid or unknown. Eg:

        - `db` != 0 or None
        - `path` argument for unix socket connection
        - none of the `host`/`port` & `startup_nodes` were provided
    """
    @classmethod
    def from_url(
        cls,
        url: str,
        *,
        host: str | None = None,
        port: str | int = 6379,
        # Cluster related kwargs
        startup_nodes: list[ClusterNode] | None = None,
        require_full_coverage: bool = True,
        read_from_replicas: bool = False,
        reinitialize_steps: int = 5,
        cluster_error_retry_attempts: int = 3,
        connection_error_retry_attempts: int = 3,
        max_connections: int = 2147483648,
        # Client related kwargs
        db: str | int = 0,
        path: str | None = None,
        credential_provider: CredentialProvider | None = None,
        username: str | None = None,
        password: str | None = None,
        client_name: str | None = None,
        # Encoding related kwargs
        encoding: str = "utf-8",
        encoding_errors: str = "strict",
        decode_responses: bool = False,
        # Connection related kwargs
        health_check_interval: float = 0,
        socket_connect_timeout: float | None = None,
        socket_keepalive: bool = False,
        socket_keepalive_options: Mapping[int, int | bytes] | None = None,
        socket_timeout: float | None = None,
        retry: Retry | None = None,
        retry_on_error: list[Exception] | None = None,
        # SSL related kwargs
        ssl: bool = False,
        ssl_ca_certs: str | None = None,
        ssl_ca_data: str | None = None,
        ssl_cert_reqs: str = "required",
        ssl_certfile: str | None = None,
        ssl_check_hostname: bool = False,
        ssl_keyfile: str | None = None,
        address_remap: Callable[[str, int], tuple[str, int]] | None = None,
    ) -> Self:
        """
        Return a Redis client object configured from the given URL.

        For example::

            redis://[[username]:[password]]@localhost:6379/0
            rediss://[[username]:[password]]@localhost:6379/0

        Three URL schemes are supported:

        - `redis://` creates a TCP socket connection. See more at:
          <https://www.iana.org/assignments/uri-schemes/prov/redis>
        - `rediss://` creates a SSL wrapped TCP socket connection. See more at:
          <https://www.iana.org/assignments/uri-schemes/prov/rediss>

        The username, password, hostname, path and all querystring values are passed
        through ``urllib.parse.unquote`` in order to replace any percent-encoded values
        with their corresponding characters.

        All querystring options are cast to their appropriate Python types. Boolean
        arguments can be specified with string values "True"/"False" or "Yes"/"No".
        Values that cannot be properly cast cause a ``ValueError`` to be raised. Once
        parsed, the querystring arguments and keyword arguments are passed to
        :class:`~redis.asyncio.connection.Connection` when created.
        In the case of conflicting arguments, querystring arguments are used.
        """
        ...

    retry: Retry | None
    connection_kwargs: dict[str, Any]
    nodes_manager: NodesManager
    encoder: Encoder
    read_from_replicas: bool
    reinitialize_steps: int
    cluster_error_retry_attempts: int
    reinitialize_counter: int
    commands_parser: CommandsParser
    node_flags: set[str]
    command_flags: dict[str, str]
    response_callbacks: Incomplete
    result_callbacks: dict[str, Callable[[Incomplete, Incomplete], Incomplete]]

    def __init__(
        self,
        host: str | None = None,
        port: str | int = 6379,
        # Cluster related kwargs
        startup_nodes: list[ClusterNode] | None = None,
        require_full_coverage: bool = True,
        read_from_replicas: bool = False,
        reinitialize_steps: int = 5,
        cluster_error_retry_attempts: int = 3,
        connection_error_retry_attempts: int = 3,
        max_connections: int = 2147483648,
        # Client related kwargs
        db: str | int = 0,
        path: str | None = None,
        credential_provider: CredentialProvider | None = None,
        username: str | None = None,
        password: str | None = None,
        client_name: str | None = None,
        # Encoding related kwargs
        encoding: str = "utf-8",
        encoding_errors: str = "strict",
        decode_responses: bool = False,
        # Connection related kwargs
        health_check_interval: float = 0,
        socket_connect_timeout: float | None = None,
        socket_keepalive: bool = False,
        socket_keepalive_options: Mapping[int, int | bytes] | None = None,
        socket_timeout: float | None = None,
        retry: Retry | None = None,
        retry_on_error: list[Exception] | None = None,
        # SSL related kwargs
        ssl: bool = False,
        ssl_ca_certs: str | None = None,
        ssl_ca_data: str | None = None,
        ssl_cert_reqs: str = "required",
        ssl_certfile: str | None = None,
        ssl_check_hostname: bool = False,
        ssl_keyfile: str | None = None,
        address_remap: Callable[[str, int], tuple[str, int]] | None = None,
    ) -> None: ...
    async def initialize(self) -> Self:
        """Get all nodes from startup nodes & creates connections if not initialized."""
        ...
    async def close(self) -> None:
        """Close all connections & client if initialized."""
        ...
    async def __aenter__(self) -> Self: ...
    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None
    ) -> None: ...
    def __await__(self) -> Awaitable[Self]: ...
    def __del__(self) -> None: ...
    async def on_connect(self, connection: Connection) -> None: ...
    def get_nodes(self) -> list[ClusterNode]:
        """Get all nodes of the cluster."""
        ...
    def get_primaries(self) -> list[ClusterNode]:
        """Get the primary nodes of the cluster."""
        ...
    def get_replicas(self) -> list[ClusterNode]:
        """Get the replica nodes of the cluster."""
        ...
    def get_random_node(self) -> ClusterNode:
        """Get a random node of the cluster."""
        ...
    def get_default_node(self) -> ClusterNode:
        """Get the default node of the client."""
        ...
    def set_default_node(self, node: ClusterNode) -> None:
        """
        Set the default node of the client.

        :raises DataError: if None is passed or node does not exist in cluster.
        """
        ...
    def get_node(self, host: str | None = None, port: int | None = None, node_name: str | None = None) -> ClusterNode | None:
        """Get node by (host, port) or node_name."""
        ...
    def get_node_from_key(self, key: str, replica: bool = False) -> ClusterNode | None:
        """
        Get the cluster node corresponding to the provided key.

        :param key:
        :param replica:
            | Indicates if a replica should be returned
            |
              None will returned if no replica holds this key

        :raises SlotNotCoveredError: if the key is not covered by any slot.
        """
        ...
    def keyslot(self, key: EncodableT) -> int:
        """
        Find the keyslot for a given key.

        See: https://redis.io/docs/manual/scaling/#redis-cluster-data-sharding
        """
        ...
    def get_encoder(self) -> Encoder:
        """Get the encoder object of the client."""
        ...
    def get_connection_kwargs(self) -> dict[str, Any | None]:
        """Get the kwargs passed to :class:`~redis.asyncio.connection.Connection`."""
        ...
    def set_response_callback(self, command: str, callback: ResponseCallbackT) -> None:
        """Set a custom response callback."""
        ...
    async def execute_command(self, *args: EncodableT, **kwargs: Any) -> Any:
        """
        Execute a raw command on the appropriate cluster node or target_nodes.

        It will retry the command as specified by :attr:`cluster_error_retry_attempts` &
        then raise an exception.

        :param args:
            | Raw command args
        :param kwargs:

            - target_nodes: :attr:`NODE_FLAGS` or :class:`~.ClusterNode`
              or List[:class:`~.ClusterNode`] or Dict[Any, :class:`~.ClusterNode`]
            - Rest of the kwargs are passed to the Redis connection

        :raises RedisClusterException: if target_nodes is not provided & the command
            can't be mapped to a slot
        """
        ...
    def pipeline(self, transaction: Any | None = None, shard_hint: Any | None = None) -> ClusterPipeline[_StrType]:
        """
        Create & return a new :class:`~.ClusterPipeline` object.

        Cluster implementation of pipeline does not support transaction or shard_hint.

        :raises RedisClusterException: if transaction or shard_hint are truthy values
        """
        ...

class ClusterNode:
    """
    Create a new ClusterNode.

    Each ClusterNode manages multiple :class:`~redis.asyncio.connection.Connection`
    objects for the (host, port).
    """
    host: str
    port: str | int
    name: str
    server_type: str | None
    max_connections: int
    connection_class: type[Connection]
    connection_kwargs: dict[str, Any]
    response_callbacks: dict[Incomplete, Incomplete]
    def __init__(
        self,
        host: str,
        port: str | int,
        server_type: str | None = None,
        *,
        max_connections: int = 2147483648,
        connection_class: type[Connection] = ...,
        **connection_kwargs: Any,
    ) -> None: ...
    def __eq__(self, obj: object) -> bool: ...
    def __del__(self) -> None: ...
    async def disconnect(self) -> None: ...
    def acquire_connection(self) -> Connection: ...
    async def parse_response(self, connection: Connection, command: str, **kwargs: Any) -> Any: ...
    async def execute_command(self, *args: Any, **kwargs: Any) -> Any: ...
    async def execute_pipeline(self, commands: list[PipelineCommand]) -> bool: ...

class NodesManager:
    startup_nodes: dict[str, ClusterNode]
    require_full_coverage: bool
    connection_kwargs: dict[str, Any]
    default_node: ClusterNode | None
    nodes_cache: dict[str, ClusterNode]
    slots_cache: dict[int, list[ClusterNode]]
    read_load_balancer: LoadBalancer
    address_remap: Callable[[str, int], tuple[str, int]] | None
    def __init__(
        self,
        startup_nodes: list[ClusterNode],
        require_full_coverage: bool,
        connection_kwargs: dict[str, Any],
        address_remap: Callable[[str, int], tuple[str, int]] | None = None,
    ) -> None: ...
    def get_node(self, host: str | None = None, port: int | None = None, node_name: str | None = None) -> ClusterNode | None: ...
    def set_nodes(self, old: dict[str, ClusterNode], new: dict[str, ClusterNode], remove_old: bool = False) -> None: ...
    def get_node_from_slot(self, slot: int, read_from_replicas: bool = False) -> ClusterNode: ...
    def get_nodes_by_server_type(self, server_type: str) -> list[ClusterNode]: ...
    async def initialize(self) -> None: ...
    async def close(self, attr: str = "nodes_cache") -> None: ...
    def remap_host_port(self, host: str, port: int) -> tuple[str, int]:
        """
        Remap the host and port returned from the cluster to a different
        internal value.  Useful if the client is not connecting directly
        to the cluster.
        """
        ...

class ClusterPipeline(AbstractRedis, AbstractRedisCluster, Generic[_StrType]):  # TODO: AsyncRedisClusterCommands
    """
    Create a new ClusterPipeline object.

    Usage::

        result = await (
            rc.pipeline()
            .set("A", 1)
            .get("A")
            .hset("K", "F", "V")
            .hgetall("K")
            .mset_nonatomic({"A": 2, "B": 3})
            .get("A")
            .get("B")
            .delete("A", "B", "K")
            .execute()
        )
        # result = [True, "1", 1, {"F": "V"}, True, True, "2", "3", 1, 1, 1]

    Note: For commands `DELETE`, `EXISTS`, `TOUCH`, `UNLINK`, `mset_nonatomic`, which
    are split across multiple nodes, you'll get multiple results for them in the array.

    Retryable errors:
        - :class:`~.ClusterDownError`
        - :class:`~.ConnectionError`
        - :class:`~.TimeoutError`

    Redirection errors:
        - :class:`~.TryAgainError`
        - :class:`~.MovedError`
        - :class:`~.AskError`

    :param client:
        | Existing :class:`~.RedisCluster` client
    """
    def __init__(self, client: RedisCluster[_StrType]) -> None: ...
    async def initialize(self) -> Self: ...
    async def __aenter__(self) -> Self: ...
    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None
    ) -> None: ...
    def __await__(self) -> Awaitable[Self]: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None
    ) -> None: ...
    def __bool__(self) -> bool: ...
    def __len__(self) -> int: ...
    def execute_command(self, *args: KeyT | EncodableT, **kwargs: Any) -> Self:
        """
        Append a raw command to the pipeline.

        :param args:
            | Raw command args
        :param kwargs:

            - target_nodes: :attr:`NODE_FLAGS` or :class:`~.ClusterNode`
              or List[:class:`~.ClusterNode`] or Dict[Any, :class:`~.ClusterNode`]
            - Rest of the kwargs are passed to the Redis connection
        """
        ...
    async def execute(self, raise_on_error: bool = True, allow_redirections: bool = True) -> list[Any]:
        """
        Execute the pipeline.

        It will retry the commands as specified by :attr:`cluster_error_retry_attempts`
        & then raise an exception.

        :param raise_on_error:
            | Raise the first error if there are any errors
        :param allow_redirections:
            | Whether to retry each failed command individually in case of redirection
              errors

        :raises RedisClusterException: if target_nodes is not provided & the command
            can't be mapped to a slot
        """
        ...
    def mset_nonatomic(self, mapping: Mapping[AnyKeyT, EncodableT]) -> Self: ...

class PipelineCommand:
    args: Any
    kwargs: Any
    position: int
    result: Exception | None | Any
    def __init__(self, position: int, *args: Any, **kwargs: Any) -> None: ...
