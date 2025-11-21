from _typeshed import Incomplete
from typing import NamedTuple

class _Event(NamedTuple):
    when: Incomplete
    callback: Incomplete
    args: Incomplete
    kwargs: Incomplete

class EventLoop:
    current: Incomplete
    idlers: Incomplete
    inactive: int
    queue: Incomplete
    rpcs: Incomplete
    rpc_results: Incomplete
    def __init__(self) -> None: ...
    def clear(self) -> None:
        """Remove all pending events without running any."""
        ...
    def insort_event_right(self, event) -> None:
        """
        Insert event in queue with sorting.

        This function assumes the queue is already sorted by ``event.when`` and
        inserts ``event`` in the queue, maintaining the sort.

        For events with same `event.when`, new events are inserted to the
        right, to keep FIFO order.

        Args:
            event (_Event): The event to insert.
        """
        ...
    def call_soon(self, callback, *args, **kwargs) -> None:
        """
        Schedule a function to be called soon, without a delay.

        Arguments:
            callback (callable): The function to eventually call.
            *args: Positional arguments to be passed to callback.
            **kwargs: Keyword arguments to be passed to callback.
        """
        ...
    def queue_call(self, delay, callback, *args, **kwargs) -> None:
        """
        Schedule a function call at a specific time in the future.

        Arguments:
            delay (float): Time in seconds to delay running the callback.
                Times over a billion seconds are assumed to be absolute
                timestamps rather than delays.
            callback (callable): The function to eventually call.
            *args: Positional arguments to be passed to callback.
            **kwargs: Keyword arguments to be passed to callback.
        """
        ...
    def queue_rpc(self, rpc, callback) -> None:
        """
        Add a gRPC call to the queue.

        Args:
            rpc (:class:`_remote.RemoteCall`): The future for the gRPC
                call.
            callback (Callable[[:class:`_remote.RemoteCall`], None]):
                Callback function to execute when gRPC call has finished.

        gRPC handles its asynchronous calls in a separate processing thread, so
        we add our own callback to `rpc` which adds `rpc` to a synchronized
        queue when it has finished. The event loop consumes the synchronized
        queue and calls `callback` with the finished gRPC future.
        """
        ...
    def add_idle(self, callback, *args, **kwargs) -> None:
        """
        Add an idle callback.

        An idle callback is a low priority task which is executed when
        there aren't other events scheduled for immediate execution.

        An idle callback can return True, False or None. These mean:

        - None: remove the callback (don't reschedule)
        - False: the callback did no work; reschedule later
        - True: the callback did some work; reschedule soon

        If the callback raises an exception, the traceback is logged and
        the callback is removed.

        Arguments:
            callback (callable): The function to eventually call.
            *args: Positional arguments to be passed to callback.
            **kwargs: Keyword arguments to be passed to callback.
        """
        ...
    def run_idle(self):
        """
        Run one of the idle callbacks.

        Returns:
            bool: Indicates if an idle callback was called.
        """
        ...
    def run0(self):
        """
        Run one item (a callback or an RPC wait_any).

        Returns:
            float: A time to sleep if something happened (may be 0);
              None if all queues are empty.
        """
        ...
    def run1(self):
        """
        Run one item (a callback or an RPC wait_any) or sleep.

        Returns:
            bool: True if something happened; False if all queues are empty.
        """
        ...
    def run(self) -> None:
        """Run until there's nothing left to do."""
        ...
