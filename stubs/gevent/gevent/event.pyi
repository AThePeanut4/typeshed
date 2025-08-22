"""Basic synchronization primitives: Event and AsyncResult"""

from types import TracebackType
from typing import Generic, Literal, Protocol, TypeVar, overload, type_check_only
from typing_extensions import TypeAlias

from gevent._abstract_linkable import AbstractLinkable

_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)
# gevent generally allows the tracebock to be omitted, it can also fail to serialize
# in which case it will be None as well.
_ExcInfo: TypeAlias = tuple[type[BaseException], BaseException, TracebackType | None]
_OptExcInfo: TypeAlias = _ExcInfo | tuple[None, None, None]

@type_check_only
class _ValueSource(Protocol[_T_co]):
    def successful(self) -> bool: ...
    @property
    def value(self) -> _T_co | None: ...
    @property
    def exception(self) -> BaseException | None: ...

class Event(AbstractLinkable):
    __slots__ = ("_flag",)
    def __init__(self) -> None: ...
    def is_set(self) -> bool:
        """
        Event.is_set(self)
        Return true if and only if the internal flag is true.
        """
        ...
    def isSet(self) -> bool:
        """Event.isSet(self)"""
        ...
    def ready(self) -> bool:
        """Event.ready(self) -> bool"""
        ...
    def set(self) -> None:
        """
        Event.set(self)

        Set the internal flag to true.

        All greenlets waiting for it to become true are awakened in
        some order at some time in the future. Greenlets that call
        :meth:`wait` once the flag is true will not block at all
        (until :meth:`clear` is called).
        """
        ...
    def clear(self) -> None:
        """
        Event.clear(self)

        Reset the internal flag to false.

        Subsequently, threads calling :meth:`wait` will block until
        :meth:`set` is called to set the internal flag to true again.
        """
        ...
    @overload
    def wait(self, timeout: None = None) -> Literal[True]:
        """
        Event.wait(self, timeout=None)

        Block until this object is :meth:`ready`.

        If the internal flag is true on entry, return immediately. Otherwise,
        block until another thread (greenlet) calls :meth:`set` to set the flag to true,
        or until the optional *timeout* expires.

        When the *timeout* argument is present and not ``None``, it should be a
        floating point number specifying a timeout for the operation in seconds
        (or fractions thereof).

        :return: This method returns true if and only if the internal flag has been set to
            true, either before the wait call or after the wait starts, so it will
            always return ``True`` except if a timeout is given and the operation
            times out.

        .. versionchanged:: 1.1
            The return value represents the flag during the elapsed wait, not
            just after it elapses. This solves a race condition if one greenlet
            sets and then clears the flag without switching, while other greenlets
            are waiting. When the waiters wake up, this will return True; previously,
            they would still wake up, but the return value would be False. This is most
            noticeable when the *timeout* is present.
        """
        ...
    @overload
    def wait(self, timeout: float) -> bool:
        """
        Event.wait(self, timeout=None)

        Block until this object is :meth:`ready`.

        If the internal flag is true on entry, return immediately. Otherwise,
        block until another thread (greenlet) calls :meth:`set` to set the flag to true,
        or until the optional *timeout* expires.

        When the *timeout* argument is present and not ``None``, it should be a
        floating point number specifying a timeout for the operation in seconds
        (or fractions thereof).

        :return: This method returns true if and only if the internal flag has been set to
            true, either before the wait call or after the wait starts, so it will
            always return ``True`` except if a timeout is given and the operation
            times out.

        .. versionchanged:: 1.1
            The return value represents the flag during the elapsed wait, not
            just after it elapses. This solves a race condition if one greenlet
            sets and then clears the flag without switching, while other greenlets
            are waiting. When the waiters wake up, this will return True; previously,
            they would still wake up, but the return value would be False. This is most
            noticeable when the *timeout* is present.
        """
        ...

class AsyncResult(AbstractLinkable, Generic[_T]):
    __slots__ = ("_value", "_exc_info", "_imap_task_index")
    def __init__(self) -> None: ...
    @property
    def value(self) -> _T | None:
        """
        Holds the value passed to :meth:`set` if :meth:`set` was called. Otherwise,
        ``None``
        """
        ...
    @property
    def exc_info(self) -> _OptExcInfo | tuple[None, None, None] | tuple[()]:
        """The three-tuple of exception information if :meth:`set_exception` was called."""
        ...
    @property
    def exception(self) -> BaseException | None:
        """
        Holds the exception instance passed to :meth:`set_exception` if :meth:`set_exception` was called.
        Otherwise ``None``.
        """
        ...
    def ready(self) -> bool:
        """
        AsyncResult.ready(self) -> bool
        Return true if and only if it holds a value or an exception
        """
        ...
    def successful(self) -> bool:
        """
        AsyncResult.successful(self) -> bool
        Return true if and only if it is ready and holds a value
        """
        ...
    def set(self, value: _T | None = None) -> None:
        """
        AsyncResult.set(self, value=None)
        Store the value and wake up any waiters.

                All greenlets blocking on :meth:`get` or :meth:`wait` are awakened.
                Subsequent calls to :meth:`wait` and :meth:`get` will not block at all.
        
        """
        ...
    @overload
    def set_exception(self, exception: BaseException, exc_info: None = None) -> None:
        """
        AsyncResult.set_exception(self, exception, exc_info=None)
        Store the exception and wake up any waiters.

                All greenlets blocking on :meth:`get` or :meth:`wait` are awakened.
                Subsequent calls to :meth:`wait` and :meth:`get` will not block at all.

                :keyword tuple exc_info: If given, a standard three-tuple of type, value, :class:`traceback`
                    as returned by :func:`sys.exc_info`. This will be used when the exception
                    is re-raised to propagate the correct traceback.
        
        """
        ...
    @overload
    def set_exception(self, exception: BaseException | None, exc_info: _OptExcInfo) -> None:
        """
        AsyncResult.set_exception(self, exception, exc_info=None)
        Store the exception and wake up any waiters.

                All greenlets blocking on :meth:`get` or :meth:`wait` are awakened.
                Subsequent calls to :meth:`wait` and :meth:`get` will not block at all.

                :keyword tuple exc_info: If given, a standard three-tuple of type, value, :class:`traceback`
                    as returned by :func:`sys.exc_info`. This will be used when the exception
                    is re-raised to propagate the correct traceback.
        
        """
        ...
    # technically get/get_nowait/result should just return _T, but the API is designed in
    # such a way that it is perfectly legal for a ValueSource to have neither its value nor
    # its exception set, while still being marked successful, at which point None would be
    # stored into value, it's also legal to call set without arguments, which has the same
    # effect, this is a little annoying, since it will introduce some additional None checks
    # that may not be necessary, but it's impossible to annotate this situation, so for now
    # we just deal with the possibly redundant None checks...
    def get(self, block: bool = True, timeout: float | None = None) -> _T | None:
        """
        AsyncResult.get(self, block=True, timeout=None)
        Return the stored value or raise the exception.

                If this instance already holds a value or an exception, return  or raise it immediately.
                Otherwise, block until another greenlet calls :meth:`set` or :meth:`set_exception` or
                until the optional timeout occurs.

                When the *timeout* argument is present and not ``None``, it should be a
                floating point number specifying a timeout for the operation in seconds
                (or fractions thereof). If the *timeout* elapses, the *Timeout* exception will
                be raised.

                :keyword bool block: If set to ``False`` and this instance is not ready,
                    immediately raise a :class:`Timeout` exception.
        
        """
        ...
    def get_nowait(self) -> _T | None:
        """
        AsyncResult.get_nowait(self)

        Return the value or raise the exception without blocking.

        If this object is not yet :meth:`ready <ready>`, raise
        :class:`gevent.Timeout` immediately.
        """
        ...
    def wait(self, timeout: float | None = None) -> _T | None:
        """
        AsyncResult.wait(self, timeout=None)
        Block until the instance is ready.

                If this instance already holds a value, it is returned immediately. If this
                instance already holds an exception, ``None`` is returned immediately.

                Otherwise, block until another greenlet calls :meth:`set` or :meth:`set_exception`
                (at which point either the value or ``None`` will be returned, respectively),
                or until the optional timeout expires (at which point ``None`` will also be
                returned).

                When the *timeout* argument is present and not ``None``, it should be a
                floating point number specifying a timeout for the operation in seconds
                (or fractions thereof).

                .. note:: If a timeout is given and expires, ``None`` will be returned
                    (no timeout exception will be raised).

        
        """
        ...
    def __call__(self, source: _ValueSource[_T]) -> None:
        """Call self as a function."""
        ...
    def result(self, timeout: float | None = None) -> _T | None:
        """AsyncResult.result(self, timeout=None)"""
        ...
    set_result = set
    def done(self) -> bool:
        """AsyncResult.done(self) -> bool"""
        ...
    def cancel(self) -> Literal[False]:
        """AsyncResult.cancel(self) -> bool"""
        ...
    def cancelled(self) -> Literal[False]:
        """AsyncResult.cancelled(self) -> bool"""
        ...

__all__ = ["Event", "AsyncResult"]
