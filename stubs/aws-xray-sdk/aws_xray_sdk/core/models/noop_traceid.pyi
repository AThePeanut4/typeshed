class NoOpTraceId:
    """
    A trace ID tracks the path of a request through your application.
    A trace collects all the segments generated by a single request.
    A trace ID is required for a segment.
    """
    VERSION: str
    DELIMITER: str
    start_time: str
    def __init__(self) -> None:
        """Generate a no-op trace id."""
        ...
    def to_id(self):
        """Convert TraceId object to a string."""
        ...
