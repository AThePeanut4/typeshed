from typing import Any
from typing_extensions import Self

from ..span import Span
from ..tracer import Tracer
from .context import SpanContext
from .tracer import MockTracer

class MockSpan(Span):
    """
    MockSpan is a thread-safe implementation of opentracing.Span.
    
    """
    operation_name: str | None
    start_time: Any
    parent_id: int | None
    tags: dict[str, Any]
    finish_time: float
    finished: bool
    logs: list[LogData]
    def __init__(
        self,
        tracer: Tracer,
        operation_name: str | None = None,
        context: SpanContext | None = None,
        parent_id: int | None = None,
        tags: dict[str, Any] | None = None,
        start_time: float | None = None,
    ) -> None: ...
    @property
    def tracer(self) -> MockTracer:
        """
        Provides access to the :class:`Tracer` that created this
        :class:`Span`.

        :rtype: Tracer
        :return: the :class:`Tracer` that created this :class:`Span`.
        """
        ...
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
    def set_operation_name(self, operation_name: str) -> Self: ...
    def set_tag(self, key: str, value: str | bool | float) -> Self: ...
    def log_kv(self, key_values: dict[str, Any], timestamp: float | None = None) -> Self: ...
    def set_baggage_item(self, key: str, value: str) -> Self: ...

class LogData:
    key_values: dict[str, Any]
    timestamp: float | None
    def __init__(self, key_values: dict[str, Any], timestamp: float | None = None) -> None: ...
