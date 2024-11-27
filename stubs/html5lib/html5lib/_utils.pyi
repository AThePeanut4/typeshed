from _typeshed import Incomplete
from collections.abc import Mapping
from typing import Any

supports_lone_surrogates: bool

class MethodDispatcher(dict[Any, Any]):
    """
    Dict with 2 special properties:

    On initiation, keys that are lists, sets or tuples are converted to
    multiple keys so accessing any one of the items in the original
    list-like object returns the matching value

    md = MethodDispatcher({("foo", "bar"):"baz"})
    md["foo"] == "baz"

    A default value which can be set through the default attribute.
    """
    default: Any
    def __init__(self, items=()) -> None: ...
    def __getitem__(self, key): ...
    def __get__(self, instance, owner: Incomplete | None = None): ...

class BoundMethodDispatcher(Mapping[Any, Any]):
    """Wraps a MethodDispatcher, binding its return values to `instance`"""
    instance: Any
    dispatcher: Any
    def __init__(self, instance, dispatcher) -> None: ...
    def __getitem__(self, key): ...
    def get(self, key, default): ...  # type: ignore[override]
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def __contains__(self, key): ...

def isSurrogatePair(data): ...
def surrogatePairToCodepoint(data): ...
def moduleFactoryFactory(factory): ...
