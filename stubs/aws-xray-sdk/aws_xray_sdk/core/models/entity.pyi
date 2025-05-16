from logging import Logger
from traceback import StackSummary
from typing import Any

log: Logger
ORIGIN_TRACE_HEADER_ATTR_KEY: str

class Entity:
    """
    The parent class for segment/subsegment. It holds common properties
    and methods on segment and subsegment.
    """
    id: Any
    name: Any
    start_time: Any
    parent_id: Any
    sampled: bool
    in_progress: bool
    http: Any
    annotations: Any
    metadata: Any
    aws: Any
    cause: Any
    subsegments: Any
    end_time: Any
    def __init__(self, name, entity_id=None) -> None: ...
    def close(self, end_time=None) -> None: ...
    def add_subsegment(self, subsegment) -> None: ...
    def remove_subsegment(self, subsegment) -> None: ...
    def put_http_meta(self, key, value) -> None: ...
    def put_annotation(self, key, value) -> None: ...
    def put_metadata(self, key, value, namespace: str = "default") -> None: ...
    def set_aws(self, aws_meta) -> None: ...
    throttle: bool
    def add_throttle_flag(self) -> None: ...
    fault: bool
    def add_fault_flag(self) -> None: ...
    error: bool
    def add_error_flag(self) -> None: ...
    def apply_status_code(self, status_code) -> None:
        """
        When a trace entity is generated under the http context,
        the status code will affect this entity's fault/error/throttle flags.
        Flip these flags based on status code.
        """
        ...
    def add_exception(self, exception: Exception, stack: StackSummary, remote: bool = False) -> None:
        """
        Add an exception to trace entities.

        :param Exception exception: the caught exception.
        :param list stack: the output from python built-in
            `traceback.extract_stack()`.
        :param bool remote: If False it means it's a client error
            instead of a downstream service.
        """
        ...
    def save_origin_trace_header(self, trace_header) -> None:
        """
        Temporarily store additional data fields in trace header
        to the entity for later propagation. The data will be
        cleaned up upon serialization.
        """
        ...
    def get_origin_trace_header(self):
        """Retrieve saved trace header data."""
        ...
    def serialize(self):
        """
        Serialize to JSON document that can be accepted by the
        X-Ray backend service. It uses json to perform serialization.
        """
        ...
    def to_dict(self):
        """
        Convert Entity(Segment/Subsegment) object to dict
        with required properties that have non-empty values.
        """
        ...
