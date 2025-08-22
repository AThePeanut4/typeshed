"""
Views of core data structures such as nested Mappings (e.g. dict-of-dicts).
These ``Views`` often restrict element access, with either the entire view or
layers of nested mappings being read-only.
"""

from collections.abc import Callable, Iterator, Mapping
from typing import TypeVar
from typing_extensions import Self

_T = TypeVar("_T")
_U = TypeVar("_U")
_V = TypeVar("_V")

__all__ = [
    "AtlasView",
    "AdjacencyView",
    "MultiAdjacencyView",
    "UnionAtlas",
    "UnionAdjacency",
    "UnionMultiInner",
    "UnionMultiAdjacency",
    "FilterAtlas",
    "FilterAdjacency",
    "FilterMultiInner",
    "FilterMultiAdjacency",
]

class AtlasView(Mapping[_T, dict[_U, _V]]):
    __slots__ = ("_atlas",)
    def __getstate__(self) -> dict[str, Mapping[_T, dict[_U, _V]]]: ...
    def __setstate__(self, state: dict[str, Mapping[_T, dict[_U, _V]]]) -> None: ...
    def __init__(self, d: Mapping[_T, dict[_U, _V]]) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __getitem__(self, key: _T) -> dict[_U, _V]: ...
    def copy(self) -> dict[_T, dict[_U, _V]]: ...

class AdjacencyView(AtlasView[_T, _U, _V]):
    __slots__ = ()

class MultiAdjacencyView(AdjacencyView[_T, _U, _V]):
    __slots__ = ()

class UnionAtlas(Mapping[_T, dict[_U, _V]]):
    __slots__ = ("_succ", "_pred")
    def __init__(self, succ: AtlasView[_T, _U, _V], pred: AtlasView[_T, _U, _V]) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __getitem__(self, key: _T) -> dict[_U, _V]: ...
    def copy(self) -> Self: ...

class UnionAdjacency(Mapping[_T, dict[_U, _V]]):
    __slots__ = ("_succ", "_pred")
    def __init__(self, succ: AdjacencyView[_T, _U, _V], pred: AdjacencyView[_T, _U, _V]) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __getitem__(self, key: _T) -> dict[_U, _V]: ...
    def copy(self) -> Self: ...

class UnionMultiInner(UnionAtlas[_T, _U, _V]):
    __slots__ = ()

class UnionMultiAdjacency(UnionAdjacency[_T, _U, _V]):
    __slots__ = ()

class FilterAtlas(Mapping[_T, _U]):
    """
    A read-only Mapping of Mappings with filtering criteria for nodes.

    It is a view into a dict-of-dict data structure, and it selects only
    nodes that meet the criteria defined by ``NODE_OK``.

    See Also
    ========
    FilterAdjacency
    FilterMultiInner
    FilterMultiAdjacency
    """
    NODE_OK: Callable[[_T], bool]
    def __init__(self, d: Mapping[_T, _U], NODE_OK: Callable[[_T], bool]) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __getitem__(self, key: _T) -> _U: ...

class FilterAdjacency(Mapping[_T, Mapping[_U, _V]]):
    """
    A read-only Mapping of Mappings with filtering criteria for nodes and edges.

    It is a view into a dict-of-dict-of-dict data structure, and it selects nodes
    and edges that satisfy specific criteria defined by ``NODE_OK`` and ``EDGE_OK``,
    respectively.

    See Also
    ========
    FilterAtlas
    FilterMultiInner
    FilterMultiAdjacency
    """
    NODE_OK: Callable[[_T], bool]
    EDGE_OK: Callable[[_T, _T], bool]
    def __init__(
        self, d: Mapping[_T, Mapping[_U, _V]], NODE_OK: Callable[[_T], bool], EDGE_OK: Callable[[_T, _T], bool]
    ) -> None: ...
    def __len__(self): ...
    def __iter__(self): ...
    def __getitem__(self, node: _T) -> FilterAtlas[_U, _V]: ...

class FilterMultiInner(FilterAdjacency[_T, _U, _V]):
    """
    A read-only Mapping of Mappings with filtering criteria for nodes and edges.

    It is a view into a dict-of-dict-of-dict-of-dict data structure, and it selects nodes
    and edges that meet specific criteria defined by ``NODE_OK`` and ``EDGE_OK``.

    See Also
    ========
    FilterAtlas
    FilterAdjacency
    FilterMultiAdjacency
    """
    ...
class FilterMultiAdjacency(FilterAdjacency[_T, _U, _V]):
    """
    A read-only Mapping of Mappings with filtering criteria
    for nodes and edges.

    It is a view into a dict-of-dict-of-dict-of-dict data structure,
    and it selects nodes and edges that satisfy specific criteria
    defined by ``NODE_OK`` and ``EDGE_OK``, respectively.

    See Also
    ========
    FilterAtlas
    FilterAdjacency
    FilterMultiInner
    """
    ...
