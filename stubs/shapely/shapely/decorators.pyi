from collections.abc import Callable, Container
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

def multithreading_enabled(func: _F) -> _F: ...
def deprecate_positional(should_be_kwargs: Container[str], category: type[Warning] = ...) -> Callable[..., object]: ...
