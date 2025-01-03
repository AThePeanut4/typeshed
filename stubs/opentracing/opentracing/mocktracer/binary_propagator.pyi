from typing import Any

from .context import SpanContext
from .propagator import Propagator

class BinaryPropagator(Propagator):
    """A MockTracer Propagator for Format.BINARY."""
    def inject(self, span_context: SpanContext, carrier: dict[Any, Any]) -> None: ...
    def extract(self, carrier: dict[Any, Any]) -> SpanContext: ...
