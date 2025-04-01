from asyncio import AbstractEventLoop
from collections.abc import Callable
from logging import Logger
from typing_extensions import Self

from ..connection import Parameters
from .base_connection import BaseConnection
from .utils import connection_workflow, io_services_utils, nbio_interface

LOGGER: Logger

class AsyncioConnection(BaseConnection):
    """
    The AsyncioConnection runs on the Asyncio EventLoop.

    
    """
    def __init__(
        self,
        parameters: Parameters | None = None,
        on_open_callback: Callable[[Self], object] | None = None,
        on_open_error_callback: Callable[[Self, BaseException], object] | None = None,
        on_close_callback: Callable[[Self, BaseException], object] | None = None,
        custom_ioloop: AbstractEventLoop | None = None,
        internal_connection_workflow: bool = True,
    ) -> None:
        """
        Create a new instance of the AsyncioConnection class, connecting
        to RabbitMQ automatically

        :param pika.connection.Parameters parameters: Connection parameters
        :param callable on_open_callback: The method to call when the connection
            is open
        :param None | method on_open_error_callback: Called if the connection
            can't be established or connection establishment is interrupted by
            `Connection.close()`: on_open_error_callback(Connection, exception).
        :param None | method on_close_callback: Called when a previously fully
            open connection is closed:
            `on_close_callback(Connection, exception)`, where `exception` is
            either an instance of `exceptions.ConnectionClosed` if closed by
            user or broker or exception of another type that describes the cause
            of connection failure.
        :param None | asyncio.AbstractEventLoop |
            nbio_interface.AbstractIOServices custom_ioloop:
                Defaults to asyncio.get_event_loop().
        :param bool internal_connection_workflow: True for autonomous connection
            establishment which is default; False for externally-managed
            connection workflow via the `create_connection()` factory.
        """
        ...
    @classmethod
    def create_connection(
        cls,
        connection_configs,
        on_done,
        custom_ioloop: AbstractEventLoop | None = None,
        workflow: connection_workflow.AbstractAMQPConnectionWorkflow | None = None,
    ): ...

class _AsyncioIOServicesAdapter(
    io_services_utils.SocketConnectionMixin,
    io_services_utils.StreamingConnectionMixin,
    nbio_interface.AbstractIOServices,
    nbio_interface.AbstractFileDescriptorServices,
):
    def __init__(self, loop: AbstractEventLoop | None = None) -> None: ...
    def get_native_ioloop(self): ...
    def close(self) -> None: ...
    def run(self) -> None: ...
    def stop(self) -> None: ...
    def add_callback_threadsafe(self, callback) -> None: ...
    def call_later(self, delay, callback): ...
    def getaddrinfo(self, host, port, on_done, family: int = 0, socktype: int = 0, proto: int = 0, flags: int = 0): ...
    def set_reader(self, fd, on_readable) -> None: ...
    def remove_reader(self, fd): ...
    def set_writer(self, fd, on_writable) -> None: ...
    def remove_writer(self, fd): ...

class _TimerHandle(nbio_interface.AbstractTimerReference):
    """
    This module's adaptation of `nbio_interface.AbstractTimerReference`.

    
    """
    def __init__(self, handle) -> None:
        """:param asyncio.Handle handle:"""
        ...
    def cancel(self) -> None: ...

class _AsyncioIOReference(nbio_interface.AbstractIOReference):
    """
    This module's adaptation of `nbio_interface.AbstractIOReference`.

    
    """
    def __init__(self, future, on_done) -> None:
        """
        :param asyncio.Future future:
        :param callable on_done: user callback that takes the completion result
            or exception as its only arg. It will not be called if the operation
            was cancelled.
        """
        ...
    def cancel(self):
        """
        Cancel pending operation

        :returns: False if was already done or cancelled; True otherwise
        :rtype: bool
        """
        ...
