"""A Future class similar to the one in PEP 3148."""

from _asyncio import Future as Future
from concurrent.futures._base import Future as _ConcurrentFuture
from typing import Any, TypeVar
from typing_extensions import TypeIs

from .events import AbstractEventLoop

__all__ = ("Future", "wrap_future", "isfuture")

_T = TypeVar("_T")

# asyncio defines 'isfuture()' in base_futures.py and re-imports it in futures.py
# but it leads to circular import error in pytype tool.
# That's why the import order is reversed.
def isfuture(obj: object) -> TypeIs[Future[Any]]:
    """
    Check for a Future.

    This returns True when obj is a Future instance or is advertising
    itself as duck-type compatible by setting _asyncio_future_blocking.
    See comment in Future for more details.
    """
    ...
def wrap_future(future: _ConcurrentFuture[_T] | Future[_T], *, loop: AbstractEventLoop | None = None) -> Future[_T]:
    """Wrap concurrent.futures.Future object."""
    ...
