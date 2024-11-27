from typing import Any
from typing_extensions import Self

log: Any
ROOT: str
PARENT: str
SAMPLE: str
SELF: str
HEADER_DELIMITER: str

class TraceHeader:
    """
    The sampling decision and trace ID are added to HTTP requests in
    tracing headers named ``X-Amzn-Trace-Id``. The first X-Ray-integrated
    service that the request hits adds a tracing header, which is read
    by the X-Ray SDK and included in the response. Learn more about
    `Tracing Header <http://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html#xray-concepts-tracingheader>`_.
    """
    def __init__(
        self, root: str | None = None, parent: str | None = None, sampled: bool | None = None, data: dict[str, Any] | None = None
    ) -> None:
        """
        :param str root: trace id
        :param str parent: parent id
        :param int sampled: 0 means not sampled, 1 means sampled
        :param dict data: arbitrary data fields
        """
        ...
    @classmethod
    def from_header_str(cls, header) -> Self:
        """
        Create a TraceHeader object from a tracing header string
        extracted from a http request headers.
        """
        ...
    def to_header_str(self):
        """
        Convert to a tracing header string that can be injected to
        outgoing http request headers.
        """
        ...
    @property
    def root(self):
        """Return trace id of the header"""
        ...
    @property
    def parent(self):
        """Return the parent segment id in the header"""
        ...
    @property
    def sampled(self):
        """
        Return the sampling decision in the header.
        It's 0 or 1 or '?'.
        """
        ...
    @property
    def data(self):
        """Return the arbitrary fields in the trace header."""
        ...
