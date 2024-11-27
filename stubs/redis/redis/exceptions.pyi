"""Core exceptions raised by the Redis client"""

class RedisError(Exception): ...
class AuthenticationError(RedisError): ...
class ConnectionError(RedisError): ...
class TimeoutError(RedisError): ...
class AuthorizationError(ConnectionError): ...
class BusyLoadingError(ConnectionError): ...
class InvalidResponse(RedisError): ...
class ResponseError(RedisError): ...
class DataError(RedisError): ...
class PubSubError(RedisError): ...
class WatchError(RedisError): ...
class NoScriptError(ResponseError): ...
class ExecAbortError(ResponseError): ...
class ReadOnlyError(ResponseError): ...
class NoPermissionError(ResponseError): ...
class ModuleError(ResponseError): ...
class LockError(RedisError, ValueError):
    """Errors acquiring or releasing a lock"""
    ...
class LockNotOwnedError(LockError):
    """Error trying to extend or release a lock that is (no longer) owned"""
    ...
class ChildDeadlockedError(Exception):
    """Error indicating that a child process is deadlocked after a fork()"""
    ...
class AuthenticationWrongNumberOfArgsError(ResponseError):
    """
    An error to indicate that the wrong number of args
    were sent to the AUTH command
    """
    ...
class RedisClusterException(Exception):
    """Base exception for the RedisCluster client"""
    ...
class ClusterError(RedisError):
    """
    Cluster errors occurred multiple times, resulting in an exhaustion of the
    command execution TTL
    """
    ...

class ClusterDownError(ClusterError, ResponseError):
    """
    Error indicated CLUSTERDOWN error received from cluster.
    By default Redis Cluster nodes stop accepting queries if they detect there
    is at least a hash slot uncovered (no available node is serving it).
    This way if the cluster is partially down (for example a range of hash
    slots are no longer covered) the entire cluster eventually becomes
    unavailable. It automatically returns available as soon as all the slots
    are covered again.
    """
    args: tuple[str]
    message: str
    def __init__(self, resp: str) -> None: ...

class AskError(ResponseError):
    """
    Error indicated ASK error received from cluster.
    When a slot is set as MIGRATING, the node will accept all queries that
    pertain to this hash slot, but only if the key in question exists,
    otherwise the query is forwarded using a -ASK redirection to the node that
    is target of the migration.

    src node: MIGRATING to dst node
        get > ASK error
        ask dst node > ASKING command
    dst node: IMPORTING from src node
        asking command only affects next command
        any op will be allowed after asking command
    """
    args: tuple[str]
    message: str
    slot_id: int
    node_addr: tuple[str, int]
    host: str
    port: int
    def __init__(self, resp: str) -> None:
        """should only redirect to master node"""
        ...

class TryAgainError(ResponseError):
    """
    Error indicated TRYAGAIN error received from cluster.
    Operations on keys that don't exist or are - during resharding - split
    between the source and destination nodes, will generate a -TRYAGAIN error.
    """
    ...
class ClusterCrossSlotError(ResponseError):
    """
    Error indicated CROSSSLOT error received from cluster.
    A CROSSSLOT error is generated when keys in a request don't hash to the
    same slot.
    """
    ...
class MovedError(AskError):
    """
    Error indicated MOVED error received from cluster.
    A request sent to a node that doesn't serve this key will be replayed with
    a MOVED error that points to the correct node.
    """
    ...
class MasterDownError(ClusterDownError):
    """
    Error indicated MASTERDOWN error received from cluster.
    Link with MASTER is down and replica-serve-stale-data is set to 'no'.
    """
    ...
class SlotNotCoveredError(RedisClusterException):
    """
    This error only happens in the case where the connection pool will try to
    fetch what node that is covered by a given slot.

    If this error is raised the client should drop the current node layout and
    attempt to reconnect and refresh the node layout again
    """
    ...
