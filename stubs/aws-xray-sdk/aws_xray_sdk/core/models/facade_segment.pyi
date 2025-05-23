from typing import Any

from .segment import Segment

MUTATION_UNSUPPORTED_MESSAGE: str

class FacadeSegment(Segment):
    """
    This type of segment should only be used in an AWS Lambda environment.
    It holds the same id, traceid and sampling decision as
    the segment generated by Lambda service but its properties cannot
    be mutated except for its subsegments. If this segment is created
    before Lambda worker finishes initializatioin, all the child
    subsegments will be discarded.
    """
    initializing: Any
    def __init__(self, name, entityid, traceid, sampled) -> None: ...
    def close(self, end_time=None) -> None:
        """Unsupported operation. Will raise an exception."""
        ...
    def put_http_meta(self, key, value) -> None:
        """Unsupported operation. Will raise an exception."""
        ...
    def put_annotation(self, key, value) -> None:
        """Unsupported operation. Will raise an exception."""
        ...
    def put_metadata(self, key, value, namespace: str = "default") -> None:
        """Unsupported operation. Will raise an exception."""
        ...
    def set_aws(self, aws_meta) -> None:
        """Unsupported operation. Will raise an exception."""
        ...
    def set_user(self, user) -> None:
        """Unsupported operation. Will raise an exception."""
        ...
    def add_throttle_flag(self) -> None:
        """Unsupported operation. Will raise an exception."""
        ...
    def add_fault_flag(self) -> None:
        """Unsupported operation. Will raise an exception."""
        ...
    def add_error_flag(self) -> None:
        """Unsupported operation. Will raise an exception."""
        ...
    def add_exception(self, exception, stack, remote: bool = False) -> None:
        """Unsupported operation. Will raise an exception."""
        ...
    def apply_status_code(self, status_code) -> None:
        """Unsupported operation. Will raise an exception."""
        ...
    def serialize(self) -> None:
        """Unsupported operation. Will raise an exception."""
        ...
    def ready_to_send(self):
        """
        Facade segment should never be sent out. This always
        return False.
        """
        ...
    def increment(self) -> None:
        """Increment total subsegments counter by 1."""
        ...
    def decrement_ref_counter(self) -> None:
        """No-op"""
        ...
