class UWSGIParseException(Exception):
    """Base exception for uWSGI protocol parsing errors."""
    ...

class InvalidUWSGIHeader(UWSGIParseException):
    """Raised when the uWSGI header is malformed."""
    msg: str
    code: int

    def __init__(self, msg: str = "") -> None: ...

class UnsupportedModifier(UWSGIParseException):
    """Raised when modifier1 is not 0 (WSGI request)."""
    modifier: int
    code: int

    def __init__(self, modifier: int) -> None: ...

class ForbiddenUWSGIRequest(UWSGIParseException):
    """Raised when source IP is not in the allow list."""
    host: str
    code: int

    def __init__(self, host: str) -> None: ...
