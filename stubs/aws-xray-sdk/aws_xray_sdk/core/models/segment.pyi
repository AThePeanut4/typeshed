from types import TracebackType
from typing import Any

from ..recorder import AWSXRayRecorder
from ..utils.atomic_counter import AtomicCounter
from .entity import Entity
from .subsegment import Subsegment

ORIGIN_TRACE_HEADER_ATTR_KEY: str

class SegmentContextManager:
    """Wrapper for segment and recorder to provide segment context manager."""
    name: str
    segment_kwargs: dict[str, Any]
    recorder: AWSXRayRecorder
    segment: Segment
    def __init__(self, recorder: AWSXRayRecorder, name: str | None = None, **segment_kwargs) -> None: ...
    def __enter__(self): ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...

class Segment(Entity):
    """
    The compute resources running your application logic send data
    about their work as segments. A segment provides the resource's name,
    details about the request, and details about the work done.
    """
    trace_id: str | None
    id: str | None
    in_progress: bool
    sampled: bool
    user: str | None
    ref_counter: AtomicCounter
    parent_id: str | None
    service: dict[str, str]
    def __init__(
        self, name, entityid: str | None = None, traceid: str | None = None, parent_id: str | None = None, sampled: bool = True
    ) -> None:
        """
        Create a segment object.

        :param str name: segment name. If not specified a
            SegmentNameMissingException will be thrown.
        :param str entityid: hexdigits segment id.
        :param str traceid: The trace id of the segment.
        :param str parent_id: The parent id of the segment. It comes
            from id of an upstream segment or subsegment.
        :param bool sampled: If False this segment will not be sent
            to the X-Ray daemon.
        """
        ...
    def add_subsegment(self, subsegment: Subsegment) -> None:
        """
        Add input subsegment as a child subsegment and increment
        reference counter and total subsegments counter.
        """
        ...
    def increment(self) -> None:
        """
        Increment reference counter to track on open subsegments
        and total subsegments counter to track total size of subsegments
        it currently hold.
        """
        ...
    def decrement_ref_counter(self) -> None:
        """Decrement reference counter by 1 when a subsegment is closed."""
        ...
    def ready_to_send(self):
        """
        Return True if the segment doesn't have any open subsegments
        and itself is not in progress.
        """
        ...
    def get_total_subsegments_size(self):
        """Return the number of total subsegments regardless of open or closed."""
        ...
    def decrement_subsegments_size(self):
        """
        Decrement total subsegments by 1. This usually happens when
        a subsegment is streamed out.
        """
        ...
    def remove_subsegment(self, subsegment) -> None:
        """Remove the reference of input subsegment."""
        ...
    def set_user(self, user) -> None:
        """
        set user of a segment. One segment can only have one user.
        User is indexed and can be later queried.
        """
        ...
    def set_service(self, service_info) -> None:
        """
        Add python runtime and version info.
        This method should be only used by the recorder.
        """
        ...
    def set_rule_name(self, rule_name) -> None:
        """
        Add the matched centralized sampling rule name
        if a segment is sampled because of that rule.
        This method should be only used by the recorder.
        """
        ...
    def to_dict(self):
        """
        Convert Segment object to dict with required properties
        that have non-empty values. 
        """
        ...
