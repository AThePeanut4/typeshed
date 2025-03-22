from typing import Any

class _PasslibRegistryProxy:
    """
    proxy module passlib.hash

    this module is in fact an object which lazy-loads
    the requested password hash algorithm from wherever it has been stored.
    it acts as a thin wrapper around :func:`passlib.registry.get_crypt_handler`.
    """
    __name__: str
    __package__: str | None
    def __getattr__(self, attr: str) -> Any: ...  # returns handler that is a value from object.__dict__
    def __setattr__(self, attr: str, value) -> None: ...
    def __dir__(self) -> list[str]: ...

def register_crypt_handler_path(name: str, path: str) -> None: ...
def register_crypt_handler(
    handler: Any, force: bool = False, _attr: str | None = None
) -> None: ...  # expected handler is object with attr handler.name
def get_crypt_handler(name: str, default: Any = ...) -> Any: ...  # returns handler or default
def list_crypt_handlers(loaded_only: bool = False) -> list[str]: ...
