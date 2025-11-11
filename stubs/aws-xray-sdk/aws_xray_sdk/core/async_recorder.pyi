from _typeshed import Incomplete
from collections.abc import Awaitable, Callable, Iterable, Mapping
from types import TracebackType
from typing import TypeVar

from .models.dummy_entities import DummySegment, DummySubsegment
from .models.segment import Segment, SegmentContextManager
from .models.subsegment import Subsegment, SubsegmentContextManager
from .recorder import AWSXRayRecorder

_T = TypeVar("_T")

class AsyncSegmentContextManager(SegmentContextManager):
    async def __aenter__(self) -> DummySegment | Segment: ...
    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...

class AsyncSubsegmentContextManager(SubsegmentContextManager):
    async def __call__(
        self, wrapped: Callable[..., Awaitable[_T]], instance, args: Iterable[Incomplete], kwargs: Mapping[str, Incomplete]
    ) -> _T: ...
    async def __aenter__(self) -> DummySubsegment | Subsegment | None: ...
    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...

class AsyncAWSXRayRecorder(AWSXRayRecorder):
    def capture_async(self, name: str | None = None) -> AsyncSubsegmentContextManager:
        """
        A decorator that records enclosed function in a subsegment.
        It only works with asynchronous functions.

        params str name: The name of the subsegment. If not specified
        the function name will be used.
        """
        ...
    def in_segment_async(
        self, name: str | None = None, *, traceid: str | None = None, parent_id: str | None = None, sampling: bool | None = None
    ) -> AsyncSegmentContextManager:
        """
        Return a segment async context manager.

        :param str name: the name of the segment
        :param dict segment_kwargs: remaining arguments passed directly to `begin_segment`
        """
        ...
    def in_subsegment_async(self, name: str | None = None, *, namespace: str = "local") -> AsyncSubsegmentContextManager:
        """
        Return a subsegment async context manager.

        :param str name: the name of the segment
        :param dict segment_kwargs: remaining arguments passed directly to `begin_segment`
        """
        ...
    async def record_subsegment_async(
        self,
        wrapped: Callable[..., Awaitable[_T]],
        instance,
        args: Iterable[Incomplete],
        kwargs: Mapping[str, Incomplete],
        name: str,
        namespace: str,
        meta_processor: Callable[..., object] | None,
    ) -> _T: ...
