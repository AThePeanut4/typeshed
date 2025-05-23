from _typeshed import SupportsItems
from collections import OrderedDict
from collections.abc import Iterable, Mapping
from typing import ClassVar, TypeVar, overload
from typing_extensions import Self

__all__ = ["canonsort_keys", "canonsort_items", "CaselessDict"]

_T = TypeVar("_T")
_VT = TypeVar("_VT")

def canonsort_keys(keys: Iterable[str], canonical_order: Iterable[str] | None = None) -> list[str]:
    """
    Sorts leading keys according to canonical_order.  Keys not specified in
    canonical_order will appear alphabetically at the end.
    """
    ...
def canonsort_items(dict1: Mapping[str, _VT], canonical_order: Iterable[str] | None = None) -> list[tuple[str, _VT]]:
    """Returns a list of items from dict1, sorted by canonical_order."""
    ...

class CaselessDict(OrderedDict[str, _VT]):
    """
    A dictionary that isn't case sensitive, and only uses strings as keys.
    Values retain their case.
    """
    # Inherit complex __init__ from dict.
    def __getitem__(self, key: str | bytes) -> _VT: ...
    def __setitem__(self, key: str | bytes, value: _VT) -> None: ...
    def __delitem__(self, key: str | bytes) -> None: ...
    def __contains__(self, key: str | bytes) -> bool: ...  # type: ignore[override]
    @overload
    def get(self, key: str | bytes, default: None = None) -> _VT: ...
    @overload
    def get(self, key: str | bytes, default: _VT) -> _VT: ...
    @overload
    def get(self, key: str | bytes, default: _T) -> _VT | _T: ...
    @overload
    def setdefault(self: CaselessDict[_T | None], key: str | bytes, value: None = None) -> _T | None: ...
    @overload
    def setdefault(self, key: str | bytes, value: _VT) -> _VT: ...
    @overload  # type: ignore[override]
    def pop(self, key: str | bytes, default: None = None) -> _VT | None: ...
    @overload
    def pop(self, key: str | bytes, default: _VT) -> _VT: ...
    @overload
    def pop(self, key: str | bytes, default: _T) -> _VT | _T: ...
    def popitem(self) -> tuple[str, _VT]: ...  # type: ignore[override]
    def has_key(self, key: str | bytes) -> bool: ...
    def update(self, *args: SupportsItems[str, _VT] | Iterable[tuple[str, _VT]], **kwargs: _VT) -> None: ...  # type: ignore[override]
    def copy(self) -> Self: ...
    def __eq__(self, other: SupportsItems[str, _VT]) -> bool: ...  # type: ignore[override]
    def __ne__(self, other: SupportsItems[str, _VT]) -> bool: ...  # type: ignore[override]
    canonical_order: ClassVar[Iterable[str] | None]
    def sorted_keys(self) -> list[str]:
        """
        Sorts keys according to the canonical_order for the derived class.
        Keys not specified in canonical_order will appear at the end.
        """
        ...
    def sorted_items(self) -> list[tuple[str, _VT]]:
        """
        Sorts items according to the canonical_order for the derived class.
        Items not specified in canonical_order will appear at the end.
        """
        ...
