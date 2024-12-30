"""Waiting for I/O completion."""

import sys
from _typeshed import FileDescriptorLike
from collections.abc import Iterable
from select import error as error
from typing import Any

def select(
    rlist: Iterable[Any], wlist: Iterable[Any], xlist: Iterable[Any], timeout: float | None = None
) -> tuple[list[Any], list[Any], list[Any]]:
    """
    An implementation of :obj:`select.select` that blocks only the current greenlet.

    .. caution:: *xlist* is ignored.

    .. versionchanged:: 1.2a1
       Raise a :exc:`ValueError` if timeout is negative. This matches Python 3's
       behaviour (Python 2 would raise a ``select.error``). Previously gevent had
       undefined behaviour.
    .. versionchanged:: 1.2a1
       Raise an exception if any of the file descriptors are invalid.
    """
    ...

if sys.platform != "win32":
    __all__ = ["error", "poll", "select"]
else:
    __all__ = ["error", "select"]

class poll:
    def register(self, fd: FileDescriptorLike, eventmask: int = ...) -> None: ...
    def modify(self, fd: FileDescriptorLike, eventmask: int) -> None: ...
    def poll(self, timeout: float | None = None) -> list[tuple[int, int]]: ...
    def unregister(self, fd: FileDescriptorLike) -> None: ...
