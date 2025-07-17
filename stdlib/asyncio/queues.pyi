import sys
from _typeshed import SupportsRichComparisonT
from asyncio.events import AbstractEventLoop
from types import GenericAlias
from typing import Any, Generic, TypeVar

if sys.version_info >= (3, 10):
    from .mixins import _LoopBoundMixin
else:
    _LoopBoundMixin = object

class QueueEmpty(Exception):
    """Raised when Queue.get_nowait() is called on an empty Queue."""
    ...
class QueueFull(Exception):
    """Raised when the Queue.put_nowait() method is called on a full Queue."""
    ...

# Keep asyncio.__all__ updated with any changes to __all__ here
if sys.version_info >= (3, 13):
    __all__ = ("Queue", "PriorityQueue", "LifoQueue", "QueueFull", "QueueEmpty", "QueueShutDown")

else:
    __all__ = ("Queue", "PriorityQueue", "LifoQueue", "QueueFull", "QueueEmpty")

_T = TypeVar("_T")

if sys.version_info >= (3, 13):
    class QueueShutDown(Exception):
        """Raised when putting on to or getting from a shut-down Queue."""
        ...

# If Generic[_T] is last and _LoopBoundMixin is object, pyright is unhappy.
# We can remove the noqa pragma when dropping 3.9 support.
class Queue(Generic[_T], _LoopBoundMixin):  # noqa: Y059
    """
    A queue, useful for coordinating producer and consumer coroutines.

    If maxsize is less than or equal to zero, the queue size is infinite. If it
    is an integer greater than 0, then "await put()" will block when the
    queue reaches maxsize, until an item is removed by get().

    Unlike the standard library Queue, you can reliably know this Queue's size
    with qsize(), since your single-threaded asyncio application won't be
    interrupted between calling qsize() and doing an operation on the Queue.
    """
    if sys.version_info >= (3, 10):
        def __init__(self, maxsize: int = 0) -> None: ...
    else:
        def __init__(self, maxsize: int = 0, *, loop: AbstractEventLoop | None = None) -> None: ...

    def _init(self, maxsize: int) -> None: ...
    def _get(self) -> _T: ...
    def _put(self, item: _T) -> None: ...
    def _format(self) -> str: ...
    def qsize(self) -> int:
        """Number of items in the queue."""
        ...
    @property
    def maxsize(self) -> int:
        """Number of items allowed in the queue."""
        ...
    def empty(self) -> bool:
        """Return True if the queue is empty, False otherwise."""
        ...
    def full(self) -> bool:
        """
        Return True if there are maxsize items in the queue.

class PriorityQueue(Queue[SupportsRichComparisonT]): ...
class LifoQueue(Queue[_T]): ...
