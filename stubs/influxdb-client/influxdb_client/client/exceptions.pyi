"""Exceptions utils for InfluxDB."""

from _typeshed import Incomplete

from urllib3 import HTTPResponse

from .._sync.rest import RESTResponse

logger: Incomplete

class InfluxDBError(Exception):
    """Raised when a server error occurs."""
    response: Incomplete
    message: Incomplete
    retry_after: Incomplete
    def __init__(self, response: HTTPResponse | RESTResponse | None = None, message: str | None = None) -> None:
        """Initialize the InfluxDBError handler."""
        ...
