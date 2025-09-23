class HaltServer(BaseException):
    reason: str
    exit_status: int

    def __init__(self, reason: str, exit_status: int = 1) -> None: ...

class ConfigError(Exception):
    """Exception raised on config error """
    ...
class AppImportError(Exception):
    """Exception raised when loading an application """
    ...
