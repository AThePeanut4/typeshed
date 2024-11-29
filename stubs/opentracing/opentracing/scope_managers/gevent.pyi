from ..scope import Scope
from ..scope_manager import ScopeManager
from ..span import Span

class GeventScopeManager(ScopeManager):
    """
    :class:`~opentracing.ScopeManager` implementation for **gevent**
    that stores the :class:`~opentracing.Scope` in the current greenlet
    (:func:`gevent.getcurrent()`).

    Automatic :class:`~opentracing.Span` propagation from parent greenlets to
    their children is not provided, which needs to be
    done manually:

    .. code-block:: python

        def child_greenlet(span):
            # activate the parent Span, but do not finish it upon
            # deactivation. That will be done by the parent greenlet.
            with tracer.scope_manager.activate(span, finish_on_close=False):
                with tracer.start_active_span('child') as scope:
                    ...

        def parent_greenlet():
            with tracer.start_active_span('parent') as scope:
                ...
                gevent.spawn(child_greenlet, span).join()
                ...
    """
    def activate(self, span: Span, finish_on_close: bool) -> Scope:
        """
        Make a :class:`~opentracing.Span` instance active.

        :param span: the :class:`~opentracing.Span` that should become active.
        :param finish_on_close: whether *span* should automatically be
            finished when :meth:`Scope.close()` is called.

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
