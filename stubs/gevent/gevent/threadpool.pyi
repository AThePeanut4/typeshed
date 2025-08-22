import concurrent.futures
from collections.abc import Callable
from typing import Any, Generic, TypeVar
from typing_extensions import ParamSpec, TypeAlias

from gevent._threading import Queue
from gevent._types import _AsyncWatcher, _Watcher
from gevent.event import AsyncResult, _OptExcInfo, _ValueSource
from gevent.greenlet import Greenlet
from gevent.hub import Hub
from gevent.pool import GroupMappingMixin

_T = TypeVar("_T")
_P = ParamSpec("_P")
_TaskItem: TypeAlias = tuple[Callable[..., Any], tuple[Any, ...], dict[str, Any], ThreadResult[Any]]
_Receiver: TypeAlias = Callable[[_ValueSource[_T]], object]

class ThreadPool(GroupMappingMixin):
    __slots__ = (
        "hub",
        "_maxsize",
        "manager",
        "pid",
        "fork_watcher",
        "_available_worker_threads_greenlet_sem",
        "_worker_greenlets",
        "task_queue",
        "_idle_task_timeout",
    )
    hub: Hub
    pid: int
    manager: Greenlet[..., Any] | None
    task_queue: Queue[_TaskItem]
    fork_watcher: _Watcher
    def __init__(self, maxsize: int, hub: Hub | None = None, idle_task_timeout: int = -1) -> None: ...
    @property
    def maxsize(self) -> int:
        """
        The maximum allowed number of worker threads.

        This is also (approximately) a limit on the number of tasks that
        can be queued without blocking the waiting greenlet. If this many
        tasks are already running, then the next greenlet that submits a task
        will block waiting for a task to finish.
        """
        ...
    @maxsize.setter
    def maxsize(self, value: int) -> None:
        """
        The maximum allowed number of worker threads.

        This is also (approximately) a limit on the number of tasks that
        can be queued without blocking the waiting greenlet. If this many
        tasks are already running, then the next greenlet that submits a task
        will block waiting for a task to finish.
        """
        ...
    @property
    def size(self) -> int:
        """
        The number of running pooled worker threads.

        Setting this attribute will add or remove running
        worker threads, up to `maxsize`.

        Initially there are no pooled running worker threads, and
        threads are created on demand to satisfy concurrent
        requests up to `maxsize` threads.
        """
        ...
    @size.setter
    def size(self, value: int) -> None:
        """
        The number of running pooled worker threads.

        Setting this attribute will add or remove running
        worker threads, up to `maxsize`.

        Initially there are no pooled running worker threads, and
        threads are created on demand to satisfy concurrent
        requests up to `maxsize` threads.
        """
        ...
    def __len__(self) -> int: ...
    def join(self) -> None:
        """Waits until all outstanding tasks have been completed."""
        ...
    def kill(self) -> None: ...
    def adjust(self) -> None: ...
    def spawn(self, func: Callable[_P, _T], *args: _P.args, **kwargs: _P.kwargs) -> AsyncResult[_T]:
        """
        Add a new task to the threadpool that will run ``func(*args,
        **kwargs)``.

        Waits until a slot is available. Creates a new native thread
        if necessary.

        This must only be called from the native thread that owns this
        object's hub. This is because creating the necessary data
        structures to communicate back to this thread isn't thread
        safe, so the hub must not be running something else. Also,
        ensuring the pool size stays correct only works within a
        single thread.

        :return: A :class:`gevent.event.AsyncResult`.
        :raises InvalidThreadUseError: If called from a different thread.

        .. versionchanged:: 1.5
           Document the thread-safety requirements.
        """
        ...

class ThreadResult(Generic[_T]):
    __slots__ = ("exc_info", "async_watcher", "_call_when_ready", "value", "context", "hub", "receiver")
    receiver: _Receiver[_T]
    hub: Hub
    context: object | None
    value: _T | None
    exc_info: _OptExcInfo | tuple[()]
    async_watcher: _AsyncWatcher
    def __init__(self, receiver: _Receiver[_T], hub: Hub, call_when_ready: Callable[[], object]) -> None: ...
    @property
    def exception(self) -> BaseException | None: ...
    def destroy_in_main_thread(self) -> None:
        """This must only be called from the thread running the hub."""
        ...
    def set(self, value: _T) -> None: ...
    def handle_error(self, context: object, exc_info: _OptExcInfo) -> None: ...
    def successful(self) -> bool: ...

class ThreadPoolExecutor(concurrent.futures.ThreadPoolExecutor):
    """
    A version of :class:`concurrent.futures.ThreadPoolExecutor` that
    always uses native threads, even when threading is monkey-patched.

    The ``Future`` objects returned from this object can be used
    with gevent waiting primitives like :func:`gevent.wait`.

    .. caution:: If threading is *not* monkey-patched, then the ``Future``
       objects returned by this object are not guaranteed to work with
       :func:`~concurrent.futures.as_completed` and :func:`~concurrent.futures.wait`.
       The individual blocking methods like :meth:`~concurrent.futures.Future.result`
       and :meth:`~concurrent.futures.Future.exception` will always work.

    .. versionadded:: 1.2a1
       This is a provisional API.
    """
    kill = concurrent.futures.ThreadPoolExecutor.shutdown

__all__ = ["ThreadPool", "ThreadResult", "ThreadPoolExecutor"]
