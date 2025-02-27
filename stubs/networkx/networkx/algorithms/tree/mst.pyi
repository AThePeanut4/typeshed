"""Algorithms for calculating min/max spanning trees/forests."""

from _typeshed import Incomplete
from collections.abc import Iterator
from dataclasses import dataclass
from enum import Enum

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable
from numpy.random import RandomState

class EdgePartition(Enum):
    """
    An enum to store the state of an edge partition. The enum is written to the
    edges of a graph before being pasted to `kruskal_mst_edges`. Options are:

    - EdgePartition.OPEN
    - EdgePartition.INCLUDED
    - EdgePartition.EXCLUDED
    """
    OPEN = 0
    INCLUDED = 1
    EXCLUDED = 2

@_dispatchable
def minimum_spanning_edges(
    G: Graph[_Node],
    algorithm: str = "kruskal",
    weight: str = "weight",
    keys: bool = True,
    data: bool | None = True,
    ignore_nan: bool = False,
): ...
@_dispatchable
def maximum_spanning_edges(
    G: Graph[_Node],
    algorithm: str = "kruskal",
    weight: str = "weight",
    keys: bool = True,
    data: bool | None = True,
    ignore_nan: bool = False,
): ...
@_dispatchable
def minimum_spanning_tree(G: Graph[_Node], weight: str = "weight", algorithm: str = "kruskal", ignore_nan: bool = False): ...
@_dispatchable
def partition_spanning_tree(
    G: Graph[_Node], minimum: bool = True, weight: str = "weight", partition: str = "partition", ignore_nan: bool = False
): ...
@_dispatchable
def maximum_spanning_tree(G: Graph[_Node], weight: str = "weight", algorithm: str = "kruskal", ignore_nan: bool = False): ...
@_dispatchable
def random_spanning_tree(
    G: Graph[_Node], weight: str | None = None, *, multiplicative=True, seed: int | RandomState | None = None
): ...

class SpanningTreeIterator:
    """
    Iterate over all spanning trees of a graph in either increasing or
    decreasing cost.

    Notes
    -----
    This iterator uses the partition scheme from [1]_ (included edges,
    excluded edges and open edges) as well as a modified Kruskal's Algorithm
    to generate minimum spanning trees which respect the partition of edges.
    For spanning trees with the same weight, ties are broken arbitrarily.

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
        data and the weight of the minimum spanning tree of the partition dict.
        """
        mst_weight: float
        partition_dict: dict[Incomplete, Incomplete]

    G: Incomplete
    weight: Incomplete
    minimum: Incomplete
    ignore_nan: Incomplete
    partition_key: str

    def __init__(self, G, weight: str = "weight", minimum: bool = True, ignore_nan: bool = False) -> None: ...
    partition_queue: Incomplete

    def __iter__(self) -> Iterator[Incomplete]: ...
    def __next__(self): ...
