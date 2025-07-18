from typing import ClassVar

class NoOpTraceId:
    """
    A trace ID tracks the path of a request through your application.
    A trace collects all the segments generated by a single request.
    A trace ID is required for a segment.
    """
    VERSION: ClassVar[str]
    DELIMITER: ClassVar[str]
    start_time: str
    def __init__(self) -> None:
        """Generate a no-op trace id."""
        ...
    def to_id(self) -> str:
        """Convert TraceId object to a string."""
        ...
