"""
Algorithms for finding optimum branchings and spanning arborescences.

This implementation is based on:

    J. Edmonds, Optimum branchings, J. Res. Natl. Bur. Standards 71B (1967),
    233–240. URL: http://archive.org/details/jresv71Bn4p233
"""

from _typeshed import Incomplete
from collections.abc import Iterator
from dataclasses import dataclass

from networkx.classes.digraph import DiGraph
from networkx.classes.graph import _Node
from networkx.utils.backends import _dispatchable
from numpy.random import RandomState

__all__ = [
    "branching_weight",
    "greedy_branching",
    "maximum_branching",
    "minimum_branching",
    "maximum_spanning_arborescence",
    "minimum_spanning_arborescence",
    "ArborescenceIterator",
]

@_dispatchable
def branching_weight(G: DiGraph[_Node], attr: str = "weight", default: float = 1): ...
@_dispatchable
def greedy_branching(
    G: DiGraph[_Node], attr: str = "weight", default: float = 1, kind: str = "max", seed: int | RandomState | None = None
): ...
@_dispatchable
def maximum_branching(
    G: DiGraph[_Node], attr: str = "weight", default: float = 1, preserve_attrs: bool = False, partition: str | None = None
): ...
@_dispatchable
def minimum_branching(
    G: DiGraph[_Node], attr: str = "weight", default: float = 1, preserve_attrs: bool = False, partition: str | None = None
): ...
@_dispatchable
def maximum_spanning_arborescence(
    G: DiGraph[_Node], attr: str = "weight", default: float = 1, preserve_attrs: bool = False, partition: str | None = None
): ...
@_dispatchable
def minimum_spanning_arborescence(
    G: DiGraph[_Node], attr: str = "weight", default: float = 1, preserve_attrs: bool = False, partition: str | None = None
): ...

class ArborescenceIterator:
    """
    Iterate over all spanning arborescences of a graph in either increasing or
    decreasing cost.

    Notes
    -----
    This iterator uses the partition scheme from [1]_ (included edges,
    excluded edges and open edges). It generates minimum spanning
    arborescences using a modified Edmonds' Algorithm which respects the
    partition of edges. For arborescences with the same weight, ties are
    broken arbitrarily.

    References
    ----------
    .. [1] G.K. Janssens, K. Sörensen, An algorithm to generate all spanning
           trees in order of increasing cost, Pesquisa Operacional, 2005-08,
           Vol. 25 (2), p. 219-229,
           https://www.scielo.br/j/pope/a/XHswBwRwJyrfL88dmMwYNWp/?lang=en
    """
    @dataclass
    class Partition:
        """
        This dataclass represents a partition and stores a dict with the edge
        data and the weight of the minimum spanning arborescence of the
        partition dict.
        """
        mst_weight: float
        partition_dict: dict[Incomplete, Incomplete]

    G: Incomplete
    weight: Incomplete
    minimum: Incomplete
    method: Incomplete
    partition_key: str
    init_partition: Incomplete

    def __init__(self, G, weight: str = "weight", minimum: bool = True, init_partition: Incomplete | None = None) -> None: ...
    partition_queue: Incomplete

    def __iter__(self) -> Iterator[Incomplete]: ...
    def __next__(self): ...
