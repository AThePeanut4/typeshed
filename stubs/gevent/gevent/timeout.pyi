"""
Timeouts.

Many functions in :mod:`gevent` have a *timeout* argument that allows
limiting the time the function will block. When that is not available,
the :class:`Timeout` class and :func:`with_timeout` function in this
module add timeouts to arbitrary code.

.. warning::

    Timeouts can only work when the greenlet switches to the hub.
    If a blocking function is called or an intense calculation is ongoing during
    which no switches occur, :class:`Timeout` is powerless.
"""

from collections.abc import Callable
from types import TracebackType
from typing import Any, Literal, Protocol, TypeVar, overload
from typing_extensions import ParamSpec, Self

from gevent._types import _TimerWatcher

_T = TypeVar("_T")
_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")
_TimeoutT = TypeVar("_TimeoutT", bound=Timeout)
_P = ParamSpec("_P")

class _HasSeconds(Protocol):
    @property
    def seconds(self) -> float | int: ...

class Timeout(BaseException):
    """
    Timeout(seconds=None, exception=None, ref=True, priority=-1)

    Raise *exception* in the current greenlet after *seconds*
    have elapsed::

        timeout = Timeout(seconds, exception)
        timeout.start()
        try:
            ...  # exception will be raised here, after *seconds* passed since start() call
        finally:
            timeout.close()

    .. warning::

        You must **always** call `close` on a ``Timeout`` object you have created,
        whether or not the code that the timeout was protecting finishes
        executing before the timeout elapses (whether or not the
        ``Timeout`` exception is raised)  This ``try/finally``
        construct or a ``with`` statement is a good pattern. (If
        the timeout object will be started again, use `cancel` instead
        of `close`; this is rare. You must still `close` it when you are
        done.)

    When *exception* is omitted or ``None``, the ``Timeout`` instance
    itself is raised::

        >>> import gevent
        >>> gevent.Timeout(0.1).start()
        >>> gevent.sleep(0.2)  #doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
         ...
        Timeout: 0.1 seconds

    If the *seconds* argument is not given or is ``None`` (e.g.,
    ``Timeout()``), then the timeout will never expire and never raise
    *exception*. This is convenient for creating functions which take
    an optional timeout parameter of their own. (Note that this is **not**
    the same thing as a *seconds* value of ``0``.)

    ::

       def function(args, timeout=None):
          "A function with an optional timeout."
          timer = Timeout(timeout)
          with timer:
             ...

    .. caution::

        A *seconds* value less than ``0.0`` (e.g., ``-1``) is poorly defined. In the future,
        support for negative values is likely to do the same thing as a value
        of ``None`` or ``0``

    A *seconds* value of ``0`` requests that the event loop spin and poll for I/O;
    it will immediately expire as soon as control returns to the event loop.

    .. rubric:: Use As A Context Manager

    To simplify starting and canceling timeouts, the ``with``
    statement can be used::

        with gevent.Timeout(seconds, exception) as timeout:
            pass  # ... code block ...

    This is equivalent to the try/finally block above with one
    additional feature: if *exception* is the literal ``False``, the
    timeout is still raised, but the context manager suppresses it, so
    the code outside the with-block won't see it.

    This is handy for adding a timeout to the functions that don't
    support a *timeout* parameter themselves::

        data = None
        with gevent.Timeout(5, False):
            data = mysock.makefile().readline()
        if data is None:
            ...  # 5 seconds passed without reading a line
        else:
            ...  # a line was read within 5 seconds

    .. caution::

        If ``readline()`` above catches and doesn't re-raise
        :exc:`BaseException` (for example, with a bare ``except:``), then
        your timeout will fail to function and control won't be returned
        to you when you expect.

    .. rubric:: Catching Timeouts

    When catching timeouts, keep in mind that the one you catch may
    not be the one you have set (a calling function may have set its
    own timeout); if you are going to silence a timeout, always check that
    it's the instance you need::

        timeout = Timeout(1)
        timeout.start()
        try:
            ...
        except Timeout as t:
            if t is not timeout:
                raise # not my timeout
        finally:
            timeout.close()


    .. versionchanged:: 1.1b2

        If *seconds* is not given or is ``None``, no longer allocate a
        native timer object that will never be started.

    .. versionchanged:: 1.1

        Add warning about negative *seconds* values.

    .. versionchanged:: 1.3a1

        Timeout objects now have a :meth:`close`
        method that *must* be called when the timeout will no longer be
        used to properly clean up native resources.
        The ``with`` statement does this automatically.

    .. versionchanged:: 24.10.1

          Timeout values can be compared to be less than an integer value,
          or to be less than other timeouts, e.g., ``Timeout(0) < 1`` is true.
          Timeouts are not absolutely ordered and support no other comparisons; this
          is purely for convenience and may be removed or altered in the future.
    """
    seconds: float | None
    exception: type[BaseException] | BaseException | None
    timer: _TimerWatcher
    def __init__(
        self,
        seconds: float | None = None,
        exception: type[BaseException] | BaseException | None = None,
        ref: bool = True,
        priority: int = -1,
    ) -> None: ...
    def start(self) -> None:
        """Schedule the timeout."""
        ...
    @overload
    @classmethod
    def start_new(
        cls, timeout: None | float = None, exception: type[BaseException] | BaseException | None = None, ref: bool = True
    ) -> Self:
        """
        Create a started :class:`Timeout`.

        This is a shortcut, the exact action depends on *timeout*'s type:

        * If *timeout* is a :class:`Timeout`, then call its :meth:`start` method
          if it's not already begun.
        * Otherwise, create a new :class:`Timeout` instance, passing (*timeout*, *exception*) as
          arguments, then call its :meth:`start` method.

        Returns the :class:`Timeout` instance.
        """
        ...
    @overload
    @classmethod
    def start_new(cls, timeout: _TimeoutT) -> _TimeoutT:
        """
        Create a started :class:`Timeout`.

        This is a shortcut, the exact action depends on *timeout*'s type:

        * If *timeout* is a :class:`Timeout`, then call its :meth:`start` method
          if it's not already begun.
        * Otherwise, create a new :class:`Timeout` instance, passing (*timeout*, *exception*) as
          arguments, then call its :meth:`start` method.

        Returns the :class:`Timeout` instance.
        """
        ...
    @property
    def pending(self) -> bool:
        """True if the timeout is scheduled to be raised."""
        ...
    def cancel(self) -> None:
        """
        If the timeout is pending, cancel it. Otherwise, do nothing.

        The timeout object can be :meth:`started <start>` again. If
        you will not start the timeout again, you should use
        :meth:`close` instead.
        """
        ...
    def close(self) -> None:
        """
        Close the timeout and free resources. The timer cannot be started again
        after this method has been used.
        """
        ...
    def __enter__(self) -> Self:
        """Start and return the timer. If the timer is already started, just return it."""
        ...
    def __exit__(
        self, typ: type[BaseException] | None, value: BaseException | None, tb: TracebackType | None
    ) -> Literal[True] | None:
        """
        Stop the timer.

        .. versionchanged:: 1.3a1
           The underlying native timer is also stopped. This object cannot be
           used again.
        """
        ...
    def __lt__(self, other: _HasSeconds | float) -> bool:
        """
        For convenience, timeouts can be compared to integers (numbers)
        based on their seconds value.
        """
        ...

# when timeout_value is provided we unfortunately get no type checking on *args, **kwargs, because
# ParamSpec does not allow mixing in additional keyword arguments
@overload
def with_timeout(
    seconds: float | None, function: Callable[..., _T1], *args: Any, timeout_value: _T2, **kwds: Any
) -> _T1 | _T2:
    """
    Wrap a call to *function* with a timeout; if the called
    function fails to return before the timeout, cancel it and return a
    flag value, provided by *timeout_value* keyword argument.

    If timeout expires but *timeout_value* is not provided, raise :class:`Timeout`.

    Keyword argument *timeout_value* is not passed to *function*.
    """
    ...
@overload
def with_timeout(seconds: float | None, function: Callable[_P, _T], *args: _P.args, **kwds: _P.kwargs) -> _T:
    """
    Wrap a call to *function* with a timeout; if the called
    function fails to return before the timeout, cancel it and return a
    flag value, provided by *timeout_value* keyword argument.

    If timeout expires but *timeout_value* is not provided, raise :class:`Timeout`.

    Keyword argument *timeout_value* is not passed to *function*.
    """
    ...

__all__ = ["Timeout", "with_timeout"]
