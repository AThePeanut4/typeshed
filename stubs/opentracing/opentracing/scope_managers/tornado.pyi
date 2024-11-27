from typing import Any

from ..scope import Scope
from ..scope_managers import ThreadLocalScopeManager
from ..span import Span

class TornadoScopeManager(ThreadLocalScopeManager):
    """
    :class:`~opentracing.ScopeManager` implementation for **Tornado**
    that stores the :class:`~opentracing.Scope` using a custom
    :class:`StackContext`, falling back to thread-local storage if
    none was found.

    Using it under :func:`tracer_stack_context()` will
    also automatically propagate the active :class:`~opentracing.Span`
    from parent coroutines to their children:

    .. code-block:: python

        @tornado.gen.coroutine
        def child_coroutine():
            # No need to pass 'parent' and activate it here,
            # as it is automatically propagated.
            with tracer.start_active_span('child') as scope:
                ...

        @tornado.gen.coroutine
        def parent_coroutine():
            with tracer.start_active_span('parent') as scope:
                ...
                yield child_coroutine()
                ...

        with tracer_stack_context():
            loop.add_callback(parent_coroutine)


    .. note::
        The current version does not support :class:`~opentracing.Span`
        activation in children coroutines when the parent yields over
        **multiple** of them, as the context is effectively shared by all,
        and the active :class:`~opentracing.Span` state is messed up:

        .. code-block:: python

            @tornado.gen.coroutine
            def coroutine(input):
                # No span should be activated here.
                # The parent Span will remain active, though.
                with tracer.start_span('child', child_of=tracer.active_span):
                    ...

            @tornado.gen.coroutine
            def handle_request_wrapper():
                res1 = coroutine('A')
                res2 = coroutine('B')

                yield [res1, res2]
    """
    def activate(self, span: Span, finish_on_close: bool) -> Scope:
        """
        Make a :class:`~opentracing.Span` instance active.

        :param span: the :class:`~opentracing.Span` that should become active.
        :param finish_on_close: whether *span* should automatically be
            finished when :meth:`Scope.close()` is called.

        If no :func:`tracer_stack_context()` is detected, thread-local
        storage will be used to store the :class:`~opentracing.Scope`.
        Observe that in this case the active :class:`~opentracing.Span`
        will not be automatically propagated to the child corotuines.

        :return: a :class:`~opentracing.Scope` instance to control the end
            of the active period for the :class:`~opentracing.Span`.
            It is a programming error to neglect to call :meth:`Scope.close()`
            on the returned instance.
        """
        ...
    @property
    def active(self) -> Scope:
        """
        Return the currently active :class:`~opentracing.Scope` which
        can be used to access the currently active
        :attr:`Scope.span`.

        :return: the :class:`~opentracing.Scope` that is active,
            or ``None`` if not available.
        """
        ...

class ThreadSafeStackContext:
    """
    Thread safe version of Tornado's StackContext (up to 4.3)
    Copy of implementation by caspersj@, until tornado-extras is open-sourced.
    Tornado's StackContext works as follows:
    - When entering a context, create an instance of StackContext and
      add add this instance to the current "context stack"
    - If execution transfers to another thread (using the wraps helper
      method),  copy the current "context stack" and apply that in the new
      thread when execution starts
    - A context stack can be entered/exited by traversing the stack and
      calling enter/exit on all elements. This is how the `wraps` helper
      method enters/exits in new threads.
    - StackContext has an internal pointer to a context factory (i.e.
      RequestContext), and an internal stack of applied contexts (instances
      of RequestContext) for each instance of StackContext. RequestContext
      instances are entered/exited from the stack as the StackContext
      is entered/exited
    - However, the enter/exit logic and maintenance of this stack of
      RequestContext instances is not thread safe.
    ```
    def __init__(self, context_factory):
        self.context_factory = context_factory
        self.contexts = []
        self.active = True
    def enter(self):
        context = self.context_factory()
        self.contexts.append(context)
        context.__enter__()
    def exit(self, type, value, traceback):
        context = self.contexts.pop()
        context.__exit__(type, value, traceback)
    ```
    Unexpected semantics of Tornado's default StackContext implementation:
    - There exist a race on `self.contexts`, where thread A enters a
      context, thread B enters a context, and thread A exits its context.
      In this case, the exit by thread A pops the instance created by
      thread B and calls exit on this instance.
    - There exists a race between `enter` and `exit` where thread A
      executes the two first statements of enter (create instance and
      add to contexts) and thread B executes exit, calling exit on an
      instance that has been initialized but not yet exited (and
      subsequently this instance will then be entered).
    The ThreadSafeStackContext changes the internal contexts stack to be
    thread local, fixing both of the above issues.
    """
    contexts: Any
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

def tracer_stack_context() -> ThreadSafeStackContext:
    """
    Create a custom Tornado's :class:`StackContext` that allows
    :class:`TornadoScopeManager` to store the active
    :class:`~opentracing.Span` in the thread-local request context.

    Suppose you have a method ``handle_request(request)`` in the
    http server. Instead of calling it directly, use a wrapper:

    .. code-block:: python

        from opentracing.scope_managers.tornado import tracer_stack_context

        @tornado.gen.coroutine
        def handle_request_wrapper(request, actual_handler, *args, **kwargs)

            request_wrapper = TornadoRequestWrapper(request=request)
            span = http_server.before_request(request=request_wrapper)

            with tracer_stack_context():
                with tracer.scope_manager.activate(span, True):
                    return actual_handler(*args, **kwargs)

    :return:
        Return a custom :class:`StackContext` that allows
        :class:`TornadoScopeManager` to activate and propagate
        :class:`~opentracing.Span` instances.
    """
    ...
