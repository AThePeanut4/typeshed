"""
Useful base classes for watchers. The available
watchers will depend on the specific event loop.
"""

from _typeshed import FileDescriptor, StrOrBytesPath
from collections.abc import Callable
from types import TracebackType
from typing import Any, Literal, overload
from typing_extensions import Self, TypeVarTuple, Unpack

from gevent._types import _Loop, _StatResult

_Ts = TypeVarTuple("_Ts")

class AbstractWatcherType(type):
    """
    Base metaclass for watchers.

    To use, you will:

    - subclass the watcher class defined from this type.
    - optionally subclass this type
    """
    def new_handle(cls, obj: object) -> int: ...
    def new(cls, kind: object) -> Any: ...

class watcher(metaclass=AbstractWatcherType):
    loop: _Loop
    def __init__(self, _loop: _Loop, ref: bool = True, priority: int | None = None, args: tuple[object, ...] = ...) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, t: type[BaseException] | None, v: BaseException | None, tb: TracebackType | None) -> None: ...
    @property
    def ref(self) -> bool: ...
    callback: Callable[..., Any]
    args: tuple[Any, ...]
    def start(self, callback: Callable[[Unpack[_Ts]], Any], *args: Unpack[_Ts]) -> None: ...
    def stop(self) -> None: ...
    @property
    def priority(self) -> int | None: ...
    @priority.setter
    def priority(self, value: int | None) -> None: ...
    @property
    def active(self) -> bool: ...
    @property
    def pending(self) -> bool: ...

class IoMixin:
    EVENT_MASK: int
    def __init__(self, loop: _Loop, fd: FileDescriptor, events: int, ref: bool = True, priority: int | None = None) -> None: ...
    @overload
    def start(self, callback: Callable[[int, Unpack[_Ts]], Any], *args: Unpack[_Ts], pass_events: Literal[True]) -> None: ...
    @overload
    def start(self, callback: Callable[[Unpack[_Ts]], Any], *args: Unpack[_Ts]) -> None: ...

class TimerMixin:
    def __init__(
        self, loop: _Loop, after: float = 0.0, repeat: float = 0.0, ref: bool = True, priority: int | None = None
    ) -> None: ...
    @overload
    def start(self, callback: Callable[[Unpack[_Ts]], object], *args: Unpack[_Ts], update: bool) -> None: ...
    @overload
    def start(self, callback: Callable[[Unpack[_Ts]], object], *args: Unpack[_Ts]) -> None: ...
    @overload
    def again(self, callback: Callable[[Unpack[_Ts]], object], *args: Unpack[_Ts], update: bool) -> None: ...
    @overload
    def again(self, callback: Callable[[Unpack[_Ts]], object], *args: Unpack[_Ts]) -> None: ...

class SignalMixin:
    def __init__(self, loop: _Loop, signalnum: int, ref: bool = True, priority: int | None = None) -> None: ...

class IdleMixin: ...
class PrepareMixin: ...
class CheckMixin: ...
class ForkMixin: ...

class AsyncMixin:
    def send(self) -> None: ...
    def send_ignoring_arg(self, _ignored: object) -> None:
        """
        Calling compatibility with ``greenlet.switch(arg)``
        as used by waiters that have ``rawlink``.

        This is an advanced method, not usually needed.
        """
        ...
    @property
    def pending(self) -> bool: ...

class ChildMixin:
    def __init__(self, loop: _Loop, pid: int, trace: int = 0, ref: bool = True) -> None: ...
    @property
    def pid(self) -> int: ...
    @property
    def rpid(self) -> int | None: ...
    @property
    def rstatus(self) -> int: ...

class StatMixin:
    def __init__(
        self, _loop: _Loop, path: StrOrBytesPath, interval: float = 0.0, ref: bool = True, priority: float | None = None
    ) -> None: ...
    @property
    def path(self) -> StrOrBytesPath: ...
    @property
    def attr(self) -> _StatResult | None: ...
    @property
    def prev(self) -> _StatResult | None: ...
    @property
    def interval(self) -> float: ...

__all__: list[str] = []
