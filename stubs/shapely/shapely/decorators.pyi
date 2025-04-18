"""Decorators for Shapely functions."""

from collections.abc import Callable, Iterable
from typing import TypeVar

_F = TypeVar("_F", bound=Callable[..., object])

class requires_geos:
    """Decorator to require a minimum GEOS version."""
    version: tuple[int, int, int]
    def __init__(self, version: str) -> None:
        """Create a decorator that requires a minimum GEOS version."""
        ...
    def __call__(self, func: _F) -> _F:
        """Return the wrapped function."""
        ...

def multithreading_enabled(func: _F) -> _F:
    """
    Enable multithreading.

    To do this, the writable flags of object type ndarrays are set to False.

    NB: multithreading also requires the GIL to be released, which is done in
    the C extension (ufuncs.c).
    """
    ...
def deprecate_positional(should_be_kwargs: Iterable[str], category: type[Warning] = ...) -> Callable[..., object]:
    """Show warning if positional arguments are used that should be keyword."""
    ...
