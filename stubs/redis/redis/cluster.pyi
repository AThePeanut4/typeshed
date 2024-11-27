from _typeshed import Incomplete, Unused
from collections.abc import Callable, Iterable, Sequence
from threading import Lock
from types import TracebackType
from typing import Any, ClassVar, Literal, NoReturn, Protocol
from typing_extensions import Self

from redis.client import CaseInsensitiveDict, PubSub, Redis, _ParseResponseOptions
from redis.commands import CommandsParser, RedisClusterCommands
from redis.commands.core import _StrType
from redis.connection import BaseParser, Connection, ConnectionPool, Encoder, _ConnectionPoolOptions, _Encodable
from redis.exceptions import MovedError, RedisError
from redis.retry import Retry
from redis.typing import EncodableT

def get_node_name(host: str, port: str | int) -> str: ...
def get_connection(redis_node: Redis[Any], *args, **options: _ConnectionPoolOptions) -> Connection: ...
def parse_scan_result(command: Unused, res, **options): ...
def parse_pubsub_numsub(command: Unused, res, **options: Unused): ...
def parse_cluster_slots(resp, **options) -> dict[tuple[int, int], dict[str, Any]]: ...
def parse_cluster_myshardid(resp: bytes, **options: Unused) -> str:
    """Parse CLUSTER MYSHARDID response."""
    ...

PRIMARY: str
REPLICA: str
SLOT_ID: str
REDIS_ALLOWED_KEYS: tuple[str, ...]
KWARGS_DISABLED_KEYS: tuple[str, ...]
PIPELINE_BLOCKED_COMMANDS: tuple[str, ...]

def cleanup_kwargs(**kwargs: Any) -> dict[str, Any]:
    """Remove unsupported or disabled keys from kwargs"""
    ...

# It uses `DefaultParser` in real life, but it is a dynamic base class.
class ClusterParser(BaseParser): ...

class AbstractRedisCluster:
    RedisClusterRequestTTL: ClassVar[int]
    PRIMARIES: ClassVar[str]
    REPLICAS: ClassVar[str]
    ALL_NODES: ClassVar[str]
    RANDOM: ClassVar[str]
    DEFAULT_NODE: ClassVar[str]
    NODE_FLAGS: ClassVar[set[str]]
    COMMAND_FLAGS: ClassVar[dict[str, str]]
    CLUSTER_COMMANDS_RESPONSE_CALLBACKS: ClassVar[dict[str, Any]]
    RESULT_CALLBACKS: ClassVar[dict[str, Callable[[Incomplete, Incomplete], Incomplete]]]
    ERRORS_ALLOW_RETRY: ClassVar[tuple[type[RedisError], ...]]

class RedisCluster(AbstractRedisCluster, RedisClusterCommands[_StrType]):
    user_on_connect_func: Callable[[Connection], object] | None
    encoder: Encoder
    cluster_error_retry_attempts: int
    command_flags: dict[str, str]
    node_flags: set[str]
    read_from_replicas: bool
    reinitialize_counter: int
    reinitialize_steps: int
    nodes_manager: NodesManager
    cluster_response_callbacks: CaseInsensitiveDict[str, Callable[..., Incomplete]]
    result_callbacks: CaseInsensitiveDict[str, Callable[[Incomplete, Incomplete], Incomplete]]
    commands_parser: CommandsParser
    def __init__(  # TODO: make @overloads, either `url` or `host:port` can be passed
        self,
        host: str | None = None,
        port: int | None = 6379,
        startup_nodes: list[ClusterNode] | None = None,
        cluster_error_retry_attempts: int = 3,
        retry: Retry | None = None,
        require_full_coverage: bool = False,
        reinitialize_steps: int = 5,
        read_from_replicas: bool = False,
        dynamic_startup_nodes: bool = True,
        url: str | None = None,
        address_remap: Callable[[str, int], tuple[str, int]] | None = None,
        **kwargs,
    ) -> None:
        """
         Initialize a new RedisCluster client.

         :param startup_nodes:
             List of nodes from which initial bootstrapping can be done
         :param host:
             Can be used to point to a startup node
         :param port:
             Can be used to point to a startup node
         :param require_full_coverage:
            When set to False (default value): the client will not require a
            full coverage of the slots. However, if not all slots are covered,
            and at least one node has 'cluster-require-full-coverage' set to
            'yes,' the server will throw a ClusterDownError for some key-based
            commands. See -
            https://redis.io/topics/cluster-tutorial#redis-cluster-configuration-parameters
            When set to True: all slots must be covered to construct the
            cluster client. If not all slots are covered, RedisClusterException
            will be thrown.
        :param read_from_replicas:
             Enable read from replicas in READONLY mode. You can read possibly
             stale data.
             When set to true, read commands will be assigned between the
             primary and its replications in a Round-Robin manner.
         :param dynamic_startup_nodes:
             Set the RedisCluster's startup nodes to all of the discovered nodes.
             If true (default value), the cluster's discovered nodes will be used to
             determine the cluster nodes-slots mapping in the next topology refresh.
             It will remove the initial passed startup nodes if their endpoints aren't
             listed in the CLUSTER SLOTS output.
             If you use dynamic DNS endpoints for startup nodes but CLUSTER SLOTS lists
             specific IP addresses, it is best to set it to false.
        :param cluster_error_retry_attempts:
             Number of times to retry before raising an error when
             :class:`~.TimeoutError` or :class:`~.ConnectionError` or
             :class:`~.ClusterDownError` are encountered
        :param reinitialize_steps:
            Specifies the number of MOVED errors that need to occur before
            reinitializing the whole cluster topology. If a MOVED error occurs
            and the cluster does not need to be reinitialized on this current
            error handling, only the MOVED slot will be patched with the
            redirected node.
            To reinitialize the cluster on every MOVED error, set
            reinitialize_steps to 1.
            To avoid reinitializing the cluster on moved errors, set
            reinitialize_steps to 0.
        :param address_remap:
            An optional callable which, when provided with an internal network
            address of a node, e.g. a `(host, port)` tuple, will return the address
            where the node is reachable.  This can be used to map the addresses at
            which the nodes _think_ they are, to addresses at which a client may
            reach them, such as when they sit behind a proxy.

         :**kwargs:
             Extra arguments that will be sent into Redis instance when created
             (See Official redis-py doc for supported kwargs
         [https://github.com/andymccurdy/redis-py/blob/master/redis/client.py])
             Some kwargs are not supported and will raise a
             RedisClusterException:
                 - db (Redis do not support database SELECT in cluster mode)
        """
        ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, type: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None
    ) -> None: ...
    def __del__(self) -> None: ...
    def disconnect_connection_pools(self) -> None: ...
    @classmethod
    def from_url(cls, url: str, **kwargs) -> Self:
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
    def on_connect(self, connection: Connection) -> None:
        """
        Initialize the connection, authenticate and select a database and send
         READONLY if it is set during object initialization.
        """
        ...
    def get_redis_connection(self, node: ClusterNode) -> Redis[Any]: ...
    def get_node(
        self, host: str | None = None, port: str | int | None = None, node_name: str | None = None
    ) -> ClusterNode | None: ...
    def get_primaries(self) -> list[ClusterNode]: ...
    def get_replicas(self) -> list[ClusterNode]: ...
    def get_random_node(self) -> ClusterNode: ...
    def get_nodes(self) -> list[ClusterNode]: ...
    def get_node_from_key(self, key: _Encodable, replica: bool = False) -> ClusterNode | None:
        """
        Get the node that holds the key's slot.
        If replica set to True but the slot doesn't have any replicas, None is
        returned.
        """
        ...
    def get_default_node(self) -> ClusterNode | None:
        """Get the cluster's default node"""
        ...
    def set_default_node(self, node: ClusterNode | None) -> bool:
        """
        Set the default node of the cluster.
        :param node: 'ClusterNode'
        :return True if the default node was set, else False
        """
        ...
    def monitor(self, target_node: Incomplete | None = None):
        """
        Returns a Monitor object for the specified target node.
        The default cluster node will be selected if no target node was
        specified.
        Monitor is useful for handling the MONITOR command to the redis server.
        next_command() method returns one command from monitor
        listen() method yields commands from monitor.
        """
        ...
    def pubsub(
        self, node: Incomplete | None = None, host: Incomplete | None = None, port: Incomplete | None = None, **kwargs
    ):
        """
        Allows passing a ClusterNode, or host&port, to get a pubsub instance
        connected to the specified node
        """
        ...
    def pipeline(self, transaction: Incomplete | None = None, shard_hint: Incomplete | None = None):
        """
        Cluster impl:
            Pipelines do not work in cluster mode the same way they
            do in normal mode. Create a clone of this object so
            that simulating pipelines will work correctly. Each
            command will be called directly when used and
            when calling execute() will only return the result stack.
        """
        ...
    def lock(
        self,
        name: str,
        timeout: float | None = None,
        sleep: float = 0.1,
        blocking: bool = True,
        blocking_timeout: float | None = None,
        lock_class: type[Incomplete] | None = None,
        thread_local: bool = True,
    ):
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
    def keyslot(self, key: _Encodable) -> int:
        """
        Calculate keyslot for a given key.
        See Keys distribution model in https://redis.io/topics/cluster-spec
        """
        ...
    def determine_slot(self, *args):
        """
        Figure out what slot to use based on args.

        Raises a RedisClusterException if there's a missing key and we can't
            determine what slots to map the command to; or, if the keys don't
            all map to the same key slot.
        """
        ...
    def get_encoder(self) -> Encoder:
        """Get the connections' encoder"""
        ...
    def get_connection_kwargs(self) -> dict[str, Any]:
        """Get the connections' key-word arguments"""
        ...
    def execute_command(self, *args, **kwargs):
        """
        Wrapper for ERRORS_ALLOW_RETRY error handling.

        It will try the number of times specified by the config option
        "self.cluster_error_retry_attempts" which defaults to 3 unless manually
        configured.

        If it reaches the number of times, the command will raise the exception

        Key argument :target_nodes: can be passed with the following types:
            nodes_flag: PRIMARIES, REPLICAS, ALL_NODES, RANDOM
            ClusterNode
            list<ClusterNode>
            dict<Any, ClusterNode>
        """
        ...
    def close(self) -> None: ...

class ClusterNode:
    host: str
    port: int
    name: str
    server_type: str | None
    redis_connection: Redis[Incomplete] | None
    def __init__(
        self, host: str, port: int, server_type: str | None = None, redis_connection: Redis[Incomplete] | None = None
    ) -> None: ...
    def __eq__(self, obj: object) -> bool: ...
    def __del__(self) -> None: ...

class LoadBalancer:
    """Round-Robin Load Balancing"""
    primary_to_idx: dict[str, int]
    start_index: int
    def __init__(self, start_index: int = 0) -> None: ...
    def get_server_index(self, primary: str, list_size: int) -> int: ...
    def reset(self) -> None: ...

class NodesManager:
    nodes_cache: dict[str, ClusterNode]
    slots_cache: dict[str, list[ClusterNode]]
    startup_nodes: dict[str, ClusterNode]
    default_node: ClusterNode | None
    from_url: bool
    connection_pool_class: type[ConnectionPool]
    connection_kwargs: dict[str, Incomplete]  # TODO: could be a TypedDict
    read_load_balancer: LoadBalancer
    address_remap: Callable[[str, int], tuple[str, int]] | None
    def __init__(
        self,
        startup_nodes: Iterable[ClusterNode],
        from_url: bool = False,
        require_full_coverage: bool = False,
        lock: Lock | None = None,
        dynamic_startup_nodes: bool = True,
        connection_pool_class: type[ConnectionPool] = ...,
        address_remap: Callable[[str, int], tuple[str, int]] | None = None,
        **kwargs,  # TODO: same type as connection_kwargs
    ) -> None: ...
    def get_node(
        self, host: str | None = None, port: int | str | None = None, node_name: str | None = None
    ) -> ClusterNode | None:
        """
        Get the requested node from the cluster's nodes.
        nodes.
        :return: ClusterNode if the node exists, else None
        """
        ...
    def update_moved_exception(self, exception: MovedError) -> None: ...
    def get_node_from_slot(self, slot: str, read_from_replicas: bool = False, server_type: str | None = None) -> ClusterNode:
        """Gets a node that servers this hash slot"""
        ...
    def get_nodes_by_server_type(self, server_type: str) -> list[ClusterNode]:
        """
        Get all nodes with the specified server type
        :param server_type: 'primary' or 'replica'
        :return: list of ClusterNode
        """
        ...
    def populate_startup_nodes(self, nodes: Iterable[ClusterNode]) -> None:
        """Populate all startup nodes and filters out any duplicates"""
        ...
    def check_slots_coverage(self, slots_cache: dict[str, list[ClusterNode]]) -> bool: ...
    def create_redis_connections(self, nodes: Iterable[ClusterNode]) -> None:
        """This function will create a redis connection to all nodes in :nodes:"""
        ...
    def create_redis_node(self, host: str, port: int | str, **kwargs: Any) -> Redis[Incomplete]: ...
    def initialize(self) -> None:
        """
        Initializes the nodes cache, slots cache and redis connections.
        :startup_nodes:
            Responsible for discovering other nodes in the cluster
        """
        ...
    def close(self) -> None: ...
    def reset(self) -> None: ...
    def remap_host_port(self, host: str, port: int) -> tuple[str, int]:
        """
        Remap the host and port returned from the cluster to a different
        internal value.  Useful if the client is not connecting directly
        to the cluster.
        """
        ...

class ClusterPubSub(PubSub):
    """
    Wrapper for PubSub class.

    IMPORTANT: before using ClusterPubSub, read about the known limitations
    with pubsub in Cluster mode and learn how to workaround them:
    https://redis-py-cluster.readthedocs.io/en/stable/pubsub.html
    """
    node: ClusterNode | None
    cluster: RedisCluster[Any]
    def __init__(
        self,
        redis_cluster: RedisCluster[Any],
        node: ClusterNode | None = None,
        host: str | None = None,
        port: int | None = None,
        **kwargs,
    ) -> None:
        """
        When a pubsub instance is created without specifying a node, a single
        node will be transparently chosen for the pubsub connection on the
        first command execution. The node will be determined by:
         1. Hashing the channel name in the request to find its keyslot
         2. Selecting a node that handles the keyslot: If read_from_replicas is
            set to true, a replica can be selected.

        :type redis_cluster: RedisCluster
        :type node: ClusterNode
        :type host: str
        :type port: int
        """
        ...
    def set_pubsub_node(
        self, cluster: RedisCluster[Any], node: ClusterNode | None = None, host: str | None = None, port: int | None = None
    ) -> None:
        """
        The pubsub node will be set according to the passed node, host and port
        When none of the node, host, or port are specified - the node is set
        to None and will be determined by the keyslot of the channel in the
        first command to be executed.
        RedisClusterException will be thrown if the passed node does not exist
        in the cluster.
        If host is passed without port, or vice versa, a DataError will be
        thrown.
        :type cluster: RedisCluster
        :type node: ClusterNode
        :type host: str
        :type port: int
        """
        ...
    def get_pubsub_node(self) -> ClusterNode | None:
        """Get the node that is being used as the pubsub connection"""
        ...
    def execute_command(self, *args, **kwargs) -> None:
        """
        Execute a publish/subscribe command.

        Taken code from redis-py and tweak to make it work within a cluster.
        """
        ...
    def get_redis_connection(self) -> Redis[Any] | None:
        """Get the Redis connection of the pubsub connected node."""
        ...

class ClusterPipeline(RedisCluster[_StrType]):
    """
    Support for Redis pipeline
    in cluster mode
    """
    command_stack: list[Incomplete]
    nodes_manager: Incomplete
    refresh_table_asap: bool
    result_callbacks: Incomplete
    startup_nodes: Incomplete
    read_from_replicas: bool
    command_flags: Incomplete
    cluster_response_callbacks: Incomplete
    cluster_error_retry_attempts: int
    reinitialize_counter: int
    reinitialize_steps: int
    encoder: Encoder
    commands_parser: Incomplete
    def __init__(
        self,
        nodes_manager,
        commands_parser,
        result_callbacks: Incomplete | None = None,
        cluster_response_callbacks: Incomplete | None = None,
        startup_nodes: Incomplete | None = None,
        read_from_replicas: bool = False,
        cluster_error_retry_attempts: int = 3,
        reinitialize_steps: int = 5,
        lock: Lock | None = None,
        **kwargs,
    ) -> None: ...
    def __len__(self) -> int: ...
    def __bool__(self) -> Literal[True]:
        """Pipeline instances should  always evaluate to True on Python 3+"""
        ...
    def execute_command(self, *args, **kwargs):
        """Wrapper function for pipeline_execute_command"""
        ...
    def pipeline_execute_command(self, *args, **options):
        """Appends the executed command to the pipeline's command stack"""
        ...
    def raise_first_error(self, stack) -> None:
        """Raise the first exception on the stack"""
        ...
    def annotate_exception(self, exception, number, command) -> None:
        """Provides extra context to the exception prior to it being handled"""
        ...
    def execute(self, raise_on_error: bool = True):
        """Execute all the commands in the current pipeline"""
        ...
    scripts: set[Any]  # is only set in `reset()`
    watching: bool  # is only set in `reset()`
    explicit_transaction: bool  # is only set in `reset()`
    def reset(self) -> None:
        """Reset back to empty pipeline."""
        ...
    def send_cluster_commands(self, stack, raise_on_error: bool = True, allow_redirections: bool = True):
        """
        Wrapper for CLUSTERDOWN error handling.

        If the cluster reports it is down it is assumed that:
         - connection_pool was disconnected
         - connection_pool was reseted
         - refereh_table_asap set to True

        It will try the number of times specified by
        the config option "self.cluster_error_retry_attempts"
        which defaults to 3 unless manually configured.

        If it reaches the number of times, the command will
        raises ClusterDownException.
        """
        ...
    def eval(self) -> None: ...
    def multi(self) -> None: ...
    def immediate_execute_command(self, *args, **options) -> None: ...
    def load_scripts(self) -> None: ...
    def watch(self, *names) -> None: ...
    def unwatch(self) -> None: ...
    def script_load_for_pipeline(self, *args, **kwargs) -> None: ...
    def delete(self, *names):
        """"Delete a key specified by ``names``\""""
        ...

def block_pipeline_command(name: str) -> Callable[..., NoReturn]:
    """
    Prints error because some pipelined commands should
    be blocked when running in cluster-mode
    """
    ...

class PipelineCommand:
    args: Sequence[EncodableT]
    options: _ParseResponseOptions
    position: int | None
    result: Any | Exception | None
    node: Incomplete | None
    asking: bool
    def __init__(
        self, args: Sequence[EncodableT], options: _ParseResponseOptions | None = None, position: int | None = None
    ) -> None: ...

class _ParseResponseCallback(Protocol):
    def __call__(self, connection: Connection, command: EncodableT, /, **kwargs) -> Any: ...

class NodeCommands:
    parse_response: _ParseResponseCallback
    connection_pool: ConnectionPool
    connection: Connection
    commands: list[PipelineCommand]
    def __init__(
        self, parse_response: _ParseResponseCallback, connection_pool: ConnectionPool, connection: Connection
    ) -> None: ...
    def append(self, c: PipelineCommand) -> None: ...
    def write(self) -> None:
        """Code borrowed from Redis so it can be fixed"""
        ...
    def read(self) -> None: ...
