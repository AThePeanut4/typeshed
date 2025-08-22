"""Internal module, support for the linkable protocol for "event" like objects."""

from collections.abc import Callable
from typing_extensions import Self

from gevent.hub import Hub

class AbstractLinkable:
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
