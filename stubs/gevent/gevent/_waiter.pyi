"""Low-level waiting primitives."""

from types import TracebackType
from typing import Generic, TypeVar, final, overload
from typing_extensions import TypeAlias

from gevent.event import _ValueSource
from gevent.hub import Hub
from greenlet import greenlet as greenlet_t

__all__ = ["Waiter"]

_T = TypeVar("_T")
# this is annoying, it's due to them using *throw args, rather than just storing them in standardized form
_ThrowArgs: TypeAlias = (
    tuple[()]
    | tuple[BaseException]
    | tuple[BaseException, None]
    | tuple[BaseException, None, TracebackType | None]
    | tuple[type[BaseException]]
    | tuple[type[BaseException], BaseException | object]
    | tuple[type[BaseException], BaseException | object, TracebackType | None]
)

class Waiter(Generic[_T]):
    __slots__ = ["hub", "greenlet", "value", "_exception"]
    @property
    def hub(self) -> Hub: ...  # readonly in Cython
    @property
    def greenlet(self) -> greenlet_t | None: ...  # readonly in Cython
    @property
    def value(self) -> _T | None: ...  # readonly in Cython
    def __init__(self, hub: Hub | None = None) -> None: ...
    def clear(self) -> None:
        """Waiter.clear(self)"""
        ...
    def ready(self) -> bool:
        """
        Waiter.ready(self)
        Return true if and only if it holds a value or an exception
        """
        ...
    def successful(self) -> bool:
        """
        Waiter.successful(self)
        Return true if and only if it is ready and holds a value
        """
        ...
    @property
    def exc_info(self) -> _ThrowArgs | None:
        """Holds the exception info passed to :meth:`throw` if :meth:`throw` was called. Otherwise ``None``."""
        ...
    def switch(self, value: _T) -> None:
        """
        Waiter.switch(self, value)

        Switch to the greenlet if one's available. Otherwise store the
        *value*.

        .. versionchanged:: 1.3b1
           The *value* is no longer optional.
        """
        ...
    @overload
    def throw(self, typ: type[BaseException], val: BaseException | object = None, tb: TracebackType | None = None, /) -> None:
        """
        Waiter.throw(self, *throw_args)
        Switch to the greenlet with the exception. If there's no greenlet, store the exception.
        """
        ...
    @overload
    def throw(self, typ: BaseException = ..., val: None = None, tb: TracebackType | None = None, /) -> None:
        """
        Waiter.throw(self, *throw_args)
        Switch to the greenlet with the exception. If there's no greenlet, store the exception.
        """
        ...
    def get(self) -> _T:
        """
        Waiter.get(self)
        If a value/an exception is stored, return/raise it. Otherwise until switch() or throw() is called.
        """
        ...
    def __call__(self, source: _ValueSource[_T]) -> None:
        """Call self as a function."""
        ...

@final
class MultipleWaiter(Waiter[_T]):
    __slots__ = ["_values"]
