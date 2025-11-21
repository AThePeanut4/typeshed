from _typeshed import Incomplete

class Future:
    info: Incomplete
    def __init__(self, info: str = ...) -> None: ...
    def done(self): ...
    def running(self): ...
    def wait(self) -> None: ...
    def check_success(self) -> None: ...
    def set_result(self, result) -> None: ...
    def set_exception(self, exception) -> None: ...
    def result(self): ...
    get_result: Incomplete
    def exception(self): ...
    get_exception: Incomplete
    def get_traceback(self): ...
    def add_done_callback(self, callback) -> None: ...
    def cancel(self) -> None: ...
    def cancelled(self): ...
    @staticmethod
    def wait_any(futures):
        """Calls :func:`wait_any`."""
        ...
    @staticmethod
    def wait_all(futures):
        """Calls :func:`wait_all`."""
        ...

class _TaskletFuture(Future):
    generator: Incomplete
    context: Incomplete
    waiting_on: Incomplete
    def __init__(self, generator, context, info: str = ...) -> None: ...
    def cancel(self) -> None:
        """Overrides :meth:`Future.cancel`."""
        ...

class _MultiFuture(Future):
    """
    A future which depends on multiple other futures.

    This future will be done when either all dependencies have results or when
    one dependency has raised an exception.

    Args:
        dependencies (typing.Sequence[tasklets.Future]): A sequence of the
            futures this future depends on.
    """
    def __init__(self, dependencies) -> None: ...
    def cancel(self) -> None:
        """Overrides :meth:`Future.cancel`."""
        ...

def tasklet(wrapped):
    """
    A decorator to turn a function or method into a tasklet.

    Calling a tasklet will return a :class:`~Future` instance which can be used
    to get the eventual return value of the tasklet.

    For more information on tasklets and cooperative multitasking, see the main
    documentation.

    Args:
        wrapped (Callable): The wrapped function.
    """
    ...
def wait_any(futures):
    """
    Wait for any of several futures to finish.

    Args:
        futures (typing.Sequence[Future]): The futures to wait on.

    Returns:
        Future: The first future to be found to have finished.
    """
    ...
def wait_all(futures) -> None:
    """
    Wait for all of several futures to finish.

    Args:
        futures (typing.Sequence[Future]): The futures to wait on.
    """
    ...

class Return(Exception):
    """
    Return from a tasklet in Python 2.

    In Python 2, generators may not return a value. In order to return a value
    from a tasklet, then, it is necessary to raise an instance of this
    exception with the return value::

        from google.cloud import ndb

        @ndb.tasklet
        def get_some_stuff():
            future1 = get_something_async()
            future2 = get_something_else_async()
            thing1, thing2 = yield future1, future2
            result = compute_result(thing1, thing2)
            raise ndb.Return(result)

    In Python 3, you can simply return the result::

        @ndb.tasklet
        def get_some_stuff():
            future1 = get_something_async()
            future2 = get_something_else_async()
            thing1, thing2 = yield future1, future2
            result = compute_result(thing1, thing2)
            return result

    Note that Python 2 is no longer supported by the newest versions of Cloud NDB.
    """
    ...

def sleep(seconds):
    """
    Sleep some amount of time in a tasklet.
    Example:
        ..code-block:: python
            yield tasklets.sleep(0.5)  # Sleep for half a second.
    Arguments:
        seconds (float): Amount of time, in seconds, to sleep.
    Returns:
        Future: Future will be complete after ``seconds`` have elapsed.
    """
    ...
def add_flow_exception(*args, **kwargs) -> None: ...
def make_context(*args, **kwargs) -> None: ...
def make_default_context(*args, **kwargs) -> None: ...

class QueueFuture:
    def __init__(self, *args, **kwargs) -> None: ...

class ReducingFuture:
    def __init__(self, *args, **kwargs) -> None: ...

class SerialQueueFuture:
    def __init__(self, *args, **kwargs) -> None: ...

def set_context(*args, **kwargs) -> None: ...
def synctasklet(wrapped):
    """
    A decorator to run a tasklet as a function when called.

    Use this to wrap a request handler function that will be called by some
    web application framework (e.g. a Django view function or a
    webapp.RequestHandler.get method).

    Args:
        wrapped (Callable): The wrapped function.
    """
    ...
def toplevel(wrapped):
    """
    A synctasklet decorator that flushes any pending work.

    Use of this decorator is largely unnecessary, as you should be using
    :meth:`~google.cloud.ndb.client.Client.context` which also flushes pending
    work when exiting the context.

    Args:
        wrapped (Callable): The wrapped function."
    """
    ...
