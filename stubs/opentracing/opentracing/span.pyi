from types import TracebackType
from typing import Any
from typing_extensions import Self

from .tracer import Tracer

class SpanContext:
    r"""
    SpanContext represents :class:`Span` state that must propagate to
    descendant :class:`Span`\ s and across process boundaries.

    SpanContext is logically divided into two pieces: the user-level "Baggage"
    (see :meth:`Span.set_baggage_item` and :meth:`Span.get_baggage_item`) that
    propagates across :class:`Span` boundaries and any
    tracer-implementation-specific fields that are needed to identify or
    otherwise contextualize the associated :class:`Span` (e.g., a ``(trace_id,
    span_id, sampled)`` tuple).
    """
    EMPTY_BAGGAGE: dict[str, str]
    @property
    def baggage(self) -> dict[str, str]:
        """
        Return baggage associated with this :class:`SpanContext`.
        If no baggage has been added to the :class:`Span`, returns an empty
        dict.

        The caller must not modify the returned dictionary.

        See also: :meth:`Span.set_baggage_item()` /
        :meth:`Span.get_baggage_item()`

        :rtype: dict
        :return: baggage associated with this :class:`SpanContext` or ``{}``.
        """
        ...

class Span:
    """
    Span represents a unit of work executed on behalf of a trace. Examples of
    spans include a remote procedure call, or a in-process method call to a
    sub-component. Every span in a trace may have zero or more causal parents,
    and these relationships transitively form a DAG. It is common for spans to
    have at most one parent, and thus most traces are merely tree structures.

    Span implements a context manager API that allows the following usage::

        with tracer.start_span(operation_name='go_fishing') as span:
            call_some_service()

    In the context manager syntax it's not necessary to call
    :meth:`Span.finish()`
    """
    def __init__(self, tracer: Tracer, context: SpanContext) -> None: ...
    @property
    def context(self) -> SpanContext:
        """
        Provides access to the :class:`SpanContext` associated with this
        :class:`Span`.

        The :class:`SpanContext` contains state that propagates from
        :class:`Span` to :class:`Span` in a larger trace.

        :rtype: SpanContext
        :return: the :class:`SpanContext` associated with this :class:`Span`.
        """
        ...
    @property
    def tracer(self) -> Tracer:
        """
        Provides access to the :class:`Tracer` that created this
        :class:`Span`.

        :rtype: Tracer
        :return: the :class:`Tracer` that created this :class:`Span`.
        """
        ...
    def set_operation_name(self, operation_name: str) -> Self:
        """
        Changes the operation name.

        :param operation_name: the new operation name
        :type operation_name: str

        :rtype: Span
        :return: the :class:`Span` itself, for call chaining.
        """
        ...
    def finish(self, finish_time: float | None = None) -> None:
        """
        Indicates that the work represented by this :class:`Span` has completed or
        terminated.

        With the exception of the :attr:`Span.context` property, the semantics
        of all other :class:`Span` methods are undefined after
        :meth:`Span.finish()` has been invoked.

        :param finish_time: an explicit :class:`Span` finish timestamp as a
            unix timestamp per :meth:`time.time()`
        :type finish_time: float
        """
        ...
    def set_tag(self, key: str, value: str | bool | float) -> Self:
        """
        Attaches a key/value pair to the :class:`Span`.

        The value must be a string, a bool, or a numeric type.

        If the user calls set_tag multiple times for the same key,
        the behavior of the :class:`Tracer` is undefined, i.e. it is
        implementation specific whether the :class:`Tracer` will retain the
        first value, or the last value, or pick one randomly, or even keep all
        of them.

        :param key: key or name of the tag. Must be a string.
        :type key: str

        :param value: value of the tag.
        :type value: string or bool or int or float

        :rtype: Span
        :return: the :class:`Span` itself, for call chaining.
        """
        ...
    def log_kv(self, key_values: dict[str, Any], timestamp: float | None = None) -> Self:
        """
        Adds a log record to the :class:`Span`.

        For example::

            span.log_kv({
                "event": "time to first byte",
                "packet.size": packet.size()})

            span.log_kv({"event": "two minutes ago"}, time.time() - 120)

        :param key_values: A dict of string keys and values of any type
        :type key_values: dict

        :param timestamp: A unix timestamp per :meth:`time.time()`; current
            time if ``None``
        :type timestamp: float

        :rtype: Span
        :return: the :class:`Span` itself, for call chaining.
        """
        ...
    def set_baggage_item(self, key: str, value: str) -> Self:
        """
        Stores a Baggage item in the :class:`Span` as a key/value pair.

        Enables powerful distributed context propagation functionality where
        arbitrary application data can be carried along the full path of
        request execution throughout the system.

        Note 1: Baggage is only propagated to the future (recursive) children
        of this :class:`Span`.

        Note 2: Baggage is sent in-band with every subsequent local and remote
        calls, so this feature must be used with care.

        :param key: Baggage item key
        :type key: str

        :param value: Baggage item value
        :type value: str

        :rtype: Span
        :return: itself, for chaining the calls.
        """
        ...
    def get_baggage_item(self, key: str) -> str | None:
        """
        Retrieves value of the baggage item with the given key.

        :param key: key of the baggage item
        :type key: str

        :rtype: str
        :return: value of the baggage item with given key, or ``None``.
        """
        ...
    def __enter__(self) -> Self:
        """
        Invoked when :class:`Span` is used as a context manager.

        :rtype: Span
        :return: the :class:`Span` itself
        """
        ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        """
        Ends context manager and calls finish() on the :class:`Span`.

        If exception has occurred during execution, it is automatically logged
        and added as a tag. :attr:`~operation.ext.tags.ERROR` will also be set
        to `True`.
        """
        ...
    def log_event(self, event: Any, payload=None) -> Self:
        """DEPRECATED"""
        ...
    def log(self, **kwargs: Any) -> Self:
        """DEPRECATED"""
        ...
