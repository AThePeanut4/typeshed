from typing import Any

class SlumberBaseException(Exception):
    """All Slumber exceptions inherit from this exception."""
    ...

class SlumberHttpBaseException(SlumberBaseException):
    """All Slumber HTTP Exceptions inherit from this exception."""
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class HttpClientError(SlumberHttpBaseException):
    """Called when the server tells us there was a client error (4xx)."""
    ...
class HttpNotFoundError(HttpClientError):
    """Called when the server sends a 404 error."""
    ...
class HttpServerError(SlumberHttpBaseException):
    """Called when the server tells us there was a server error (5xx)."""
    ...
class SerializerNoAvailable(SlumberBaseException):
    """There are no available Serializers."""
    ...
class SerializerNotAvailable(SlumberBaseException):
    """The chosen Serializer is not available."""
    ...
class ImproperlyConfigured(SlumberBaseException):
    """Slumber is somehow improperly configured."""
    ...
