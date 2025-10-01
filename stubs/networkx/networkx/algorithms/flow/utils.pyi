"""Utility classes and functions for network flow algorithms."""

from _typeshed import Incomplete
from typing import NoReturn, overload
from typing_extensions import deprecated

from networkx.classes.graph import Graph, _Node
from networkx.classes.multigraph import MultiGraph
from networkx.utils.backends import _dispatchable

__all__ = ["CurrentEdge", "Level", "GlobalRelabelThreshold", "build_residual_network", "detect_unboundedness", "build_flow_dict"]

class CurrentEdge:
    """
    Mechanism for iterating over out-edges incident to a node in a circular
    manner. StopIteration exception is raised when wraparound occurs.
    """
    __slots__ = ("_edges", "_it", "_curr")
    def __init__(self, edges) -> None: ...
    def get(self): ...
    def move_to_next(self) -> None: ...

class Level:
    """Active and inactive nodes in a level."""
    __slots__ = ("active", "inactive")
    active: Incomplete
    inactive: Incomplete

    def __init__(self) -> None: ...

class GlobalRelabelThreshold:
    """
    Measurement of work before the global relabeling heuristic should be
    applied.
    """
    def __init__(self, n, m, freq) -> None: ...
    def add_work(self, work) -> None: ...
    def is_reached(self) -> bool: ...
    def clear_work(self) -> None: ...

@overload
@deprecated("MultiGraph and MultiDiGraph not supported (yet).")
def build_residual_network(G: MultiGraph[_Node], capacity, *, backend: str | None = None, **backend_kwargs) -> NoReturn: ...
@overload
def build_residual_network(G: Graph[_Node], capacity, *, backend: str | None = None, **backend_kwargs): ...
@_dispatchable
def detect_unboundedness(R, s, t) -> None:
    """Detect an infinite-capacity s-t path in R."""
    ...
@_dispatchable
def build_flow_dict(G: Graph[_Node], R): ...
