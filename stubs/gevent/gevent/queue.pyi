"""
Synchronized queues.

The :mod:`gevent.queue` module implements multi-producer, multi-consumer queues
that work across greenlets, with the API similar to the classes found in the
standard :mod:`Queue` and :class:`multiprocessing <multiprocessing.Queue>` modules.

The classes in this module implement the iterator protocol. Iterating
over a queue means repeatedly calling :meth:`get <Queue.get>` until
:meth:`get <Queue.get>` returns ``StopIteration`` (specifically that
class, not an instance or subclass).

    >>> import gevent.queue
    >>> queue = gevent.queue.Queue()
    >>> queue.put(1)
    >>> queue.put(2)
    >>> queue.put(StopIteration)
    >>> for item in queue:
    ...    print(item)
    1
    2

.. versionchanged:: 1.0
       ``Queue(0)`` now means queue of infinite size, not a channel. A :exc:`DeprecationWarning`
       will be issued with this argument.
"""

import sys
import types
from collections import deque
from collections.abc import Iterable

# technically it is using _PySimpleQueue, which has the same interface as SimpleQueue
from queue import Empty as Empty, Full as Full
from typing import Any, Generic, Literal, TypeVar, final, overload
from typing_extensions import Self

from gevent._waiter import Waiter
from gevent.hub import Hub

__all__ = ["Queue", "PriorityQueue", "LifoQueue", "SimpleQueue", "JoinableQueue", "Channel", "Empty", "Full", "ShutDown"]

if sys.version_info >= (3, 13):
    from queue import ShutDown as ShutDown
else:
    class ShutDown(Exception):
        """gevent extension for Python versions less than 3.13"""
        ...

_T = TypeVar("_T")

class SimpleQueue(Generic[_T]):
    @property
    def hub(self) -> Hub: ...  # readonly in Cython
    @property
    def queue(self) -> deque[_T]: ...  # readonly in Cython
    maxsize: int | None
    is_shutdown: bool

    @classmethod
    def __class_getitem__(cls, item: Any, /) -> types.GenericAlias: ...
    @overload
    def __init__(self, maxsize: int | None = None) -> None: ...
    @overload
    def __init__(self, maxsize: int | None, items: Iterable[_T]) -> None: ...
    @overload
    def __init__(self, maxsize: int | None = None, *, items: Iterable[_T]) -> None: ...
    def copy(self) -> Self: ...
    def empty(self) -> bool: ...
    def full(self) -> bool: ...
    def get(self, block: bool = True, timeout: float | None = None) -> _T: ...
    def get_nowait(self) -> _T: ...
    def peek(self, block: bool = True, timeout: float | None = None) -> _T: ...
    def peek_nowait(self) -> _T: ...
    def put(self, item: _T, block: bool = True, timeout: float | None = None) -> None: ...
    def put_nowait(self, item: _T) -> None: ...
    def qsize(self) -> int: ...
    def __bool__(self) -> bool: ...
    def __iter__(self) -> Self: ...
    def __len__(self) -> int: ...
    def __next__(self) -> _T: ...
    next = __next__

class Queue(SimpleQueue[_T]):
    @property
    def unfinished_tasks(self) -> int: ...  # readonly in Cython
    @overload
    def __init__(self, maxsize: int | None = None, *, unfinished_tasks: int | None = None) -> None: ...
    @overload
    def __init__(self, maxsize: int | None, items: Iterable[_T], unfinished_tasks: int | None = None) -> None: ...
    @overload
    def __init__(self, maxsize: int | None = None, *, items: Iterable[_T], unfinished_tasks: int | None = None) -> None: ...
    def join(self, timeout: float | None = None) -> bool: ...
    def task_done(self) -> None: ...
    def shutdown(self, immediate: bool = False) -> None: ...

JoinableQueue = Queue

@final
class UnboundQueue(Queue[_T]):
    """UnboundQueue(maxsize=None, items=())"""
    @overload
    def __init__(self, maxsize: None = None) -> None: ...
    @overload
    def __init__(self, maxsize: None, items: Iterable[_T]) -> None: ...
    @overload
    def __init__(self, maxsize: None = None, *, items: Iterable[_T]) -> None: ...

class PriorityQueue(Queue[_T]):
    """
    A subclass of :class:`Queue` that retrieves entries in priority order (lowest first).

    Entries are typically tuples of the form: ``(priority number, data)``.

    .. versionchanged:: 1.2a1
       Any *items* given to the constructor will now be passed through
       :func:`heapq.heapify` to ensure the invariants of this class hold.
       Previously it was just assumed that they were already a heap.
    """
    ...
class LifoQueue(Queue[_T]):
    """
    A subclass of :class:`JoinableQueue` that retrieves most recently added entries first.

    .. versionchanged:: 24.10.1
       Now extends :class:`JoinableQueue` instead of just :class:`Queue`.
    """
    ...

class Channel(Generic[_T]):
    """Channel(maxsize=1)"""
    @property
    def getters(self) -> deque[Waiter[Any]]: ...  # readonly in Cython
    @property
    def putters(self) -> deque[tuple[_T, Waiter[Any]]]: ...  # readonly in Cython
    @property
    def hub(self) -> Hub: ...  # readonly in Cython
    def __init__(self, maxsize: Literal[1] = 1) -> None: ...
    @classmethod
    def __class_getitem__(cls, item: Any, /) -> types.GenericAlias: ...
    @property
    def balance(self) -> int: ...
    def qsize(self) -> Literal[0]:
        """Channel.qsize(self)"""
        ...
    def empty(self) -> Literal[True]:
        """Channel.empty(self)"""
        ...
    def full(self) -> Literal[True]:
        """Channel.full(self)"""
        ...
    def put(self, item: _T, block: bool = True, timeout: float | None = None) -> None:
        """Channel.put(self, item, block=True, timeout=None)"""
        ...
    def put_nowait(self, item: _T) -> None:
        """Channel.put_nowait(self, item)"""
        ...
    def get(self, block: bool = True, timeout: float | None = None) -> _T:
        """Channel.get(self, block=True, timeout=None)"""
        ...
    def get_nowait(self) -> _T:
        """Channel.get_nowait(self)"""
        ...
    def __iter__(self) -> Self:
        """Implement iter(self)."""
        ...
    def __next__(self) -> _T: ...
    next = __next__
