from _typeshed import Incomplete
from types import TracebackType
from typing import Any, ClassVar, Protocol
from typing_extensions import Self

from redis.client import Redis

class _Local(Protocol):
    token: str | bytes | None

class Lock:
    """
    A shared, distributed Lock. Using Redis for locking allows the Lock
    to be shared across processes and/or machines.

    It's left to the user to resolve deadlock issues and make sure
    multiple clients play nicely together.
    """
    LUA_EXTEND_SCRIPT: ClassVar[str]
    LUA_REACQUIRE_SCRIPT: ClassVar[str]
    LUA_RELEASE_SCRIPT: ClassVar[str]
    lua_extend: ClassVar[Incomplete | None]
    lua_reacquire: ClassVar[Incomplete | None]
    lua_release: ClassVar[Incomplete | None]
    redis: Redis[Any]
    name: str
    timeout: float | None
    sleep: float
    blocking: bool
    blocking_timeout: float | None
    thread_local: bool
    local: _Local
    def __init__(
        self,
        redis: Redis[Any],
        name: str,
        timeout: float | None = None,
        sleep: float = 0.1,
        blocking: bool = True,
        blocking_timeout: float | None = None,
        thread_local: bool = True,
    ) -> None:
        """
        Create a new Lock instance named ``name`` using the Redis client
        supplied by ``redis``.

        ``timeout`` indicates a maximum life for the lock in seconds.
        By default, it will remain locked until release() is called.
        ``timeout`` can be specified as a float or integer, both representing
        the number of seconds to wait.

        ``sleep`` indicates the amount of time to sleep in seconds per loop
        iteration when the lock is in blocking mode and another client is
        currently holding the lock.

        ``blocking`` indicates whether calling ``acquire`` should block until
        the lock has been acquired or to fail immediately, causing ``acquire``
        to return False and the lock not being acquired. Defaults to True.
        Note this value can be overridden by passing a ``blocking``
        argument to ``acquire``.

        ``blocking_timeout`` indicates the maximum amount of time in seconds to
        spend trying to acquire the lock. A value of ``None`` indicates
        continue trying forever. ``blocking_timeout`` can be specified as a
        float or integer, both representing the number of seconds to wait.

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
    def register_scripts(self) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None
    ) -> bool | None: ...
    def acquire(
        self,
        sleep: float | None = None,
        blocking: bool | None = None,
        blocking_timeout: float | None = None,
        token: str | bytes | None = None,
    ) -> bool:
        """
        Use Redis to hold a shared, distributed lock named ``name``.
        Returns True once the lock is acquired.

        If ``blocking`` is False, always return immediately. If the lock
        was acquired, return True, otherwise return False.

        ``blocking_timeout`` specifies the maximum number of seconds to
        wait trying to acquire the lock.

        ``token`` specifies the token value to be used. If provided, token
        must be a bytes object or a string that can be encoded to a bytes
        object with the default encoding. If a token isn't specified, a UUID
        will be generated.
        """
        ...
    def do_acquire(self, token: str | bytes) -> bool: ...
    def locked(self) -> bool:
        """Returns True if this key is locked by any process, otherwise False."""
        ...
    def owned(self) -> bool:
        """Returns True if this key is locked by this lock, otherwise False."""
        ...
    def release(self) -> None:
        """Releases the already acquired lock"""
        ...
    def do_release(self, expected_token: str | bytes) -> None: ...
    def extend(self, additional_time: float, replace_ttl: bool = False) -> bool:
        """
        Adds more time to an already acquired lock.

        ``additional_time`` can be specified as an integer or a float, both
        representing the number of seconds to add.

        ``replace_ttl`` if False (the default), add `additional_time` to
        the lock's existing ttl. If True, replace the lock's ttl with
        `additional_time`.
        """
        ...
    def do_extend(self, additional_time: float, replace_ttl: bool) -> bool: ...
    def reacquire(self) -> bool:
        """Resets a TTL of an already acquired lock back to a timeout value."""
        ...
    def do_reacquire(self) -> bool: ...
