from typing import Any

class TraceId:
    """
    A trace ID tracks the path of a request through your application.
    A trace collects all the segments generated by a single request.
    A trace ID is required for a segment.
    """
    VERSION: str
    DELIMITER: str
    start_time: Any
    def __init__(self) -> None:
        """Generate a random trace id."""
        ...
    def to_id(self):
        """Convert TraceId object to a string."""
        ...
