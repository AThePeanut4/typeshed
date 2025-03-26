"""passlib.registry - registry for password hash handlers"""

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

def register_crypt_handler_path(name: str, path: str) -> None:
    """
    register location to lazy-load handler when requested.

    custom hashes may be registered via :func:`register_crypt_handler`,
    or they may be registered by this function,
    which will delay actually importing and loading the handler
    until a call to :func:`get_crypt_handler` is made for the specified name.

    :arg name: name of handler
    :arg path: module import path

    the specified module path should contain a password hash handler
    called :samp:`{name}`, or the path may contain a colon,
    specifying the module and module attribute to use.
    for example, the following would cause ``get_handler("myhash")`` to look
    for a class named ``myhash`` within the ``myapp.helpers`` module::

        >>> from passlib.registry import registry_crypt_handler_path
        >>> registry_crypt_handler_path("myhash", "myapp.helpers")

    ...while this form would cause ``get_handler("myhash")`` to look
    for a class name ``MyHash`` within the ``myapp.helpers`` module::

        >>> from passlib.registry import registry_crypt_handler_path
        >>> registry_crypt_handler_path("myhash", "myapp.helpers:MyHash")
    """
    ...
def register_crypt_handler(
    handler: Any, force: bool = False, _attr: str | None = None
) -> None: ...  # expected handler is object with attr handler.name
def get_crypt_handler(name: str, default: Any = ...) -> Any: ...  # returns handler or default
def list_crypt_handlers(loaded_only: bool = False) -> list[str]: ...

__all__ = ["register_crypt_handler_path", "register_crypt_handler", "get_crypt_handler", "list_crypt_handlers"]
