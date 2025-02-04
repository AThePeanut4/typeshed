from typing import Any

class ImportExportError(Exception):
    """A generic exception for all others to extend."""
    ...
class FieldError(ImportExportError):
    """Raised when a field encounters an error."""
    ...
class WidgetError(ImportExportError): ...

class ImportError(ImportExportError):
    error: Exception
    number: int | None
    row: dict[str, Any] | None
    def __init__(self, error: Exception, number: int | None = None, row: dict[str, Any] | None = None) -> None: ...
