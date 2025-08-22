"""
Locking primitives.

These include semaphores with arbitrary bounds (:class:`Semaphore` and
its safer subclass :class:`BoundedSemaphore`) and a semaphore with
infinite bounds (:class:`DummySemaphore`), along with a reentrant lock
(:class:`RLock`) with the same API as :class:`threading.RLock`.
"""

from collections.abc import Callable
from types import TracebackType
from typing import Any, Literal

from gevent._abstract_linkable import AbstractLinkable
from gevent.hub import Hub

__all__ = ["Semaphore", "BoundedSemaphore", "DummySemaphore", "RLock"]

class Semaphore(AbstractLinkable):
    __slots__ = ("counter", "_multithreaded")
    counter: int
    def __init__(self, value: int = 1, hub: Hub | None = None) -> None: ...
    def acquire(self, blocking: bool = True, timeout: float | None = None) -> bool:
        """
        Semaphore.acquire(self, bool blocking=True, timeout=None) -> bool

class BoundedSemaphore(Semaphore):
    __slots__ = ("_initial_value",)

class DummySemaphore:
    """
    DummySemaphore(value=None) -> DummySemaphore

    An object with the same API as :class:`Semaphore`,
    initialized with "infinite" initial value. None of its
    methods ever block.

    This can be used to parameterize on whether or not to actually
    guard access to a potentially limited resource. If the resource is
    actually limited, such as a fixed-size thread pool, use a real
    :class:`Semaphore`, but if the resource is unbounded, use an
    instance of this class. In that way none of the supporting code
    needs to change.

    Similarly, it can be used to parameterize on whether or not to
    enforce mutual exclusion to some underlying object. If the
    underlying object is known to be thread-safe itself mutual
    exclusion is not needed and a ``DummySemaphore`` can be used, but
    if that's not true, use a real ``Semaphore``.
    """
    def __init__(self, value: int | None = None) -> None:
        """
        .. versionchanged:: 1.1rc3
            Accept and ignore a *value* argument for compatibility with Semaphore.
        """
        ...
    def locked(self) -> Literal[False]:
        """A DummySemaphore is never locked so this always returns False."""
        ...
    def ready(self) -> Literal[True]:
        """A DummySemaphore is never locked so this always returns True."""
        ...
    def release(self) -> None:
        """Releasing a dummy semaphore does nothing."""
        ...
    def rawlink(self, callback: Callable[[Any], object]) -> None: ...
    def unlink(self, callback: Callable[[Any], object]) -> None: ...
    def wait(self, timeout: float | None = None) -> Literal[1]:
        """Waiting for a DummySemaphore returns immediately."""
        ...
    def acquire(self, blocking: bool = True, timeout: float | None = None) -> Literal[True]:
        """
        A DummySemaphore can always be acquired immediately so this always
        returns True and ignores its arguments.

        .. versionchanged:: 1.1a1
           Always return *true*.
        """
        ...
    def __enter__(self) -> None: ...
    def __exit__(self, typ: type[BaseException] | None, val: BaseException | None, tb: TracebackType | None) -> None: ...

class RLock:
    __slots__ = ("_block", "_owner", "_count", "__weakref__")
    def __init__(self, hub: Hub | None = None) -> None: ...
    def acquire(self, blocking: bool = True, timeout: float | None = None) -> bool: ...
    def __enter__(self) -> bool: ...
    def release(self) -> None:
        """
        Release the mutex.

        Only the greenlet that originally acquired the mutex can
        release it.
        """
        ...
    def __exit__(self, typ: type[BaseException] | None, val: BaseException | None, tb: TracebackType | None) -> None: ...
    def locked(self) -> bool:
        """
        Return a boolean indicating whether this object is locked right now.

        .. versionadded:: 25.4.1
        """
        ...
