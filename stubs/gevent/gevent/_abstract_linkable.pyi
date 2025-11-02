"""
Internal use only base class for objects
that can be waited on and then asked to notify (wake up)
waiters.  Examples include locks, events, semaphores.

gevent has the generic concept of "linkable" objects, or the "linkable"
protocol, which is the ``link`` and ``rawlink`` methods. (Actually sending
the notification is up to the implementation of the individual
objects.) `gevent.greenlet.Greenlet` implements this protocol but
does not extend this object (TODO: It probably should.)
"""

from collections.abc import Callable
from typing_extensions import Self

from gevent.hub import Hub

class AbstractLinkable:
    """AbstractLinkable(hub=None)"""
    __slots__ = ("hub", "_links", "_notifier", "_notify_all", "__weakref__")
    @property
    def hub(self) -> Hub | None: ...
    def __init__(self, hub: Hub | None = None) -> None: ...
    def linkcount(self) -> int:
        """AbstractLinkable.linkcount(self)"""
        ...
    def rawlink(self, callback: Callable[[Self], object], /) -> None:
        """
        AbstractLinkable.rawlink(self, callback)

        Register a callback to call when this object is ready.

        *callback* will be called in the :class:`Hub
        <gevent.hub.Hub>`, so it must not use blocking gevent API.
        *callback* will be passed one argument: this instance.
        """
        ...
    def ready(self) -> bool:
        """AbstractLinkable.ready(self) -> bool"""
        ...
    def unlink(self, callback: Callable[[Self], object], /) -> None:
        """
        AbstractLinkable.unlink(self, callback)

        Remove the callback set by :meth:`rawlink`
        """
        ...

__all__ = ["AbstractLinkable"]
