from logging import Logger

from pika.adapters.base_connection import BaseConnection
from pika.adapters.utils.nbio_interface import AbstractIOReference
from pika.adapters.utils.selector_ioloop_adapter import AbstractSelectorIOLoop, SelectorIOServicesAdapter

LOGGER: Logger

class GeventConnection(BaseConnection):
    """
    Implementation of pika's ``BaseConnection``.

    An async selector-based connection which integrates with Gevent.
    """
    def __init__(
        self,
        parameters=None,
        on_open_callback=None,
        on_open_error_callback=None,
        on_close_callback=None,
        custom_ioloop=None,
        internal_connection_workflow: bool = True,
    ) -> None: ...
    @classmethod
    def create_connection(cls, connection_configs, on_done, custom_ioloop=None, workflow=None): ...

class _TSafeCallbackQueue:
    """
    Dispatch callbacks from any thread to be executed in the main thread
    efficiently with IO events.
    """
    def __init__(self) -> None:
        """:param _GeventSelectorIOLoop loop: IO loop to add callbacks to."""
        ...
    @property
    def fd(self):
        """The file-descriptor to register for READ events in the IO loop."""
        ...
    def add_callback_threadsafe(self, callback) -> None:
        """
        Add an item to the queue from any thread. The configured handler
        will be invoked with the item in the main thread.

        :param item: Object to add to the queue.
        """
        ...
    def run_next_callback(self) -> None:
        """
        Invoke the next callback from the queue.

        MUST run in the main thread. If no callback was added to the queue,
        this will block the IO loop.

        Performs a blocking READ on the pipe so must only be called when the
        pipe is ready for reading.
        """
        ...

class _GeventSelectorIOLoop(AbstractSelectorIOLoop):
    """
    Implementation of `AbstractSelectorIOLoop` using the Gevent event loop.

    Required by implementations of `SelectorIOServicesAdapter`.
    """
    READ: int
    WRITE: int
    ERROR: int
    def __init__(self, gevent_hub=None) -> None: ...
    def close(self) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def add_callback(self, callback) -> None: ...
    def call_later(self, delay, callback): ...
    def remove_timeout(self, timeout_handle) -> None: ...
    def add_handler(self, fd, handler, events) -> None: ...
    def update_handler(self, fd, events) -> None: ...
    def remove_handler(self, fd) -> None: ...

class _GeventSelectorIOServicesAdapter(SelectorIOServicesAdapter):
    def getaddrinfo(self, host, port, on_done, family: int = 0, socktype: int = 0, proto: int = 0, flags: int = 0): ...

class _GeventIOLoopIOHandle(AbstractIOReference):
    """
    Implement `AbstractIOReference`.

    Only used to wrap the _GeventAddressResolver.
    """
    def __init__(self, subject) -> None:
        """:param subject: subject of the reference containing a `cancel()` method"""
        ...
    def cancel(self):
        """
        Cancel pending operation

        :returns: False if was already done or cancelled; True otherwise
        :rtype: bool
        """
        ...

class _GeventAddressResolver:
    __slots__ = ("_loop", "_on_done", "_greenlet", "_ga_host", "_ga_port", "_ga_family", "_ga_socktype", "_ga_proto", "_ga_flags")
    def __init__(self, native_loop, host, port, family, socktype, proto, flags, on_done) -> None: ...
    def start(self) -> None: ...
    def cancel(self): ...
