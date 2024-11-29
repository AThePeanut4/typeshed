from .noop_traceid import NoOpTraceId as NoOpTraceId
from .segment import Segment as Segment
from .subsegment import Subsegment as Subsegment
from .traceid import TraceId as TraceId

class DummySegment(Segment):
    """
    A dummy segment is created when ``xray_recorder`` decide to not sample
    the segment based on sampling rules.
    Adding data to a dummy segment becomes a no-op except for
    subsegments. This is to reduce the memory footprint of the SDK.
    A dummy segment will not be sent to the X-Ray daemon. Manually creating
    dummy segments is not recommended.
    """
    sampled: bool
    def __init__(self, name: str = "dummy") -> None: ...
    def set_aws(self, aws_meta) -> None:
        """No-op"""
        ...
    def put_http_meta(self, key, value) -> None:
        """No-op"""
        ...
    def put_annotation(self, key, value) -> None:
        """No-op"""
        ...
    def put_metadata(self, key, value, namespace: str = "default") -> None:
        """No-op"""
        ...
    def set_user(self, user) -> None:
        """No-op"""
        ...
    def set_service(self, service_info) -> None:
        """No-op"""
        ...
    def apply_status_code(self, status_code) -> None:
        """No-op"""
        ...
    def add_exception(self, exception, stack, remote: bool = False) -> None:
        """No-op"""
        ...
    def serialize(self) -> None:
        """No-op"""
        ...

class DummySubsegment(Subsegment):
    """
    A dummy subsegment will be created when ``xray_recorder`` tries
    to create a subsegment under a not sampled segment. Adding data
    to a dummy subsegment becomes no-op. Dummy subsegment will not
    be sent to the X-Ray daemon.
    """
    sampled: bool
    def __init__(self, segment, name: str = "dummy") -> None: ...
    def set_aws(self, aws_meta) -> None:
        """No-op"""
        ...
    def put_http_meta(self, key, value) -> None:
        """No-op"""
        ...
    def put_annotation(self, key, value) -> None:
        """No-op"""
        ...
    def put_metadata(self, key, value, namespace: str = "default") -> None:
        """No-op"""
        ...
    def set_sql(self, sql) -> None:
        """No-op"""
        ...
    def apply_status_code(self, status_code) -> None:
        """No-op"""
        ...
    def add_exception(self, exception, stack, remote: bool = False) -> None:
        """No-op"""
        ...
    def serialize(self) -> None:
        """No-op"""
        ...
