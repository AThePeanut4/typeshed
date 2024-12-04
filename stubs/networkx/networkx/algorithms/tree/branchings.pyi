"""
Algorithms for finding optimum branchings and spanning arborescences.

This implementation is based on:

    J. Edmonds, Optimum branchings, J. Res. Natl. Bur. Standards 71B (1967),
    233–240. URL: http://archive.org/details/jresv71Bn4p233
"""

from _typeshed import Incomplete
from collections.abc import Iterator
from dataclasses import dataclass

from networkx.utils.backends import _dispatchable

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
def branching_weight(G, attr: str = "weight", default: float = 1):
    """
    Returns the total weight of a branching.

    You must access this function through the networkx.algorithms.tree module.

    Parameters
    ----------
    G : DiGraph
        The directed graph.
    attr : str
        The attribute to use as weights. If None, then each edge will be
        treated equally with a weight of 1.
    default : float
        When `attr` is not None, then if an edge does not have that attribute,
        `default` specifies what value it should take.

    Returns
    -------
    weight: int or float
        The total weight of the branching.

    Examples
    --------
    >>> G = nx.DiGraph()
    >>> G.add_weighted_edges_from([(0, 1, 2), (1, 2, 4), (2, 3, 3), (3, 4, 2)])
    >>> nx.tree.branching_weight(G)
    11
    """
    ...
@_dispatchable
def greedy_branching(G, attr: str = "weight", default: float = 1, kind: str = "max", seed: Incomplete | None = None):
    """
    Returns a branching obtained through a greedy algorithm.

    This algorithm is wrong, and cannot give a proper optimal branching.
    However, we include it for pedagogical reasons, as it can be helpful to
    see what its outputs are.

    The output is a branching, and possibly, a spanning arborescence. However,
    it is not guaranteed to be optimal in either case.

    Parameters
    ----------
    G : DiGraph
        The directed graph to scan.
    attr : str
        The attribute to use as weights. If None, then each edge will be
        treated equally with a weight of 1.
    default : float
        When `attr` is not None, then if an edge does not have that attribute,
        `default` specifies what value it should take.
    kind : str
        The type of optimum to search for: 'min' or 'max' greedy branching.
    seed : integer, random_state, or None (default)
        Indicator of random number generation state.
        See :ref:`Randomness<randomness>`.

    Returns
    -------
    B : directed graph
        The greedily obtained branching.
    """
    ...
@_dispatchable
def maximum_branching(
    G, attr: str = "weight", default: float = 1, preserve_attrs: bool = False, partition: Incomplete | None = None
):
    """
    Returns a maximum branching from G.

    Parameters
    ----------
    G : (multi)digraph-like
        The graph to be searched.
    attr : str
        The edge attribute used to in determining optimality.
    default : float
        The value of the edge attribute used if an edge does not have
        the attribute `attr`.
    preserve_attrs : bool
        If True, preserve the other attributes of the original graph (that are not
        passed to `attr`)
    partition : str
        The key for the edge attribute containing the partition
        data on the graph. Edges can be included, excluded or open using the
        `EdgePartition` enum.

    Returns
    -------
    B : (multi)digraph-like
        A maximum branching.
    """
    ...
@_dispatchable
def minimum_branching(
    G, attr: str = "weight", default: float = 1, preserve_attrs: bool = False, partition: Incomplete | None = None
):
    """
    Returns a minimum branching from G.

    Parameters
    ----------
    G : (multi)digraph-like
        The graph to be searched.
    attr : str
        The edge attribute used to in determining optimality.
    default : float
        The value of the edge attribute used if an edge does not have
        the attribute `attr`.
    preserve_attrs : bool
        If True, preserve the other attributes of the original graph (that are not
        passed to `attr`)
    partition : str
        The key for the edge attribute containing the partition
        data on the graph. Edges can be included, excluded or open using the
        `EdgePartition` enum.

    Returns
    -------
    B : (multi)digraph-like
        A minimum branching.

    See Also
    --------
        minimal_branching
    """
    ...
@_dispatchable
def maximum_spanning_arborescence(
    G, attr: str = "weight", default: float = 1, preserve_attrs: bool = False, partition: Incomplete | None = None
):
    """
    Returns a maximum spanning arborescence from G.

    Parameters
    ----------
    G : (multi)digraph-like
        The graph to be searched.
    attr : str
        The edge attribute used to in determining optimality.
    default : float
        The value of the edge attribute used if an edge does not have
        the attribute `attr`.
    preserve_attrs : bool
        If True, preserve the other attributes of the original graph (that are not
        passed to `attr`)
    partition : str
        The key for the edge attribute containing the partition
        data on the graph. Edges can be included, excluded or open using the
        `EdgePartition` enum.

    Returns
    -------
    B : (multi)digraph-like
        A maximum spanning arborescence.

    Raises
    ------
    NetworkXException
        If the graph does not contain a maximum spanning arborescence.
    """
    ...
@_dispatchable
def minimum_spanning_arborescence(
    G, attr: str = "weight", default: float = 1, preserve_attrs: bool = False, partition: Incomplete | None = None
):
    """
    Returns a minimum spanning arborescence from G.

    Parameters
    ----------
    G : (multi)digraph-like
        The graph to be searched.
    attr : str
        The edge attribute used to in determining optimality.
    default : float
        The value of the edge attribute used if an edge does not have
        the attribute `attr`.
    preserve_attrs : bool
        If True, preserve the other attributes of the original graph (that are not
        passed to `attr`)
    partition : str
        The key for the edge attribute containing the partition
        data on the graph. Edges can be included, excluded or open using the
        `EdgePartition` enum.

    Returns
    -------
    B : (multi)digraph-like
        A minimum spanning arborescence.

    Raises
    ------
    NetworkXException
        If the graph does not contain a minimum spanning arborescence.
    """
    ...

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
    def __init__(self, G, weight: str = "weight", minimum: bool = True, init_partition: Incomplete | None = None) -> None:
        """
        Initialize the iterator

        Parameters
        ----------
        G : nx.DiGraph
            The directed graph which we need to iterate trees over

        weight : String, default = "weight"
            The edge attribute used to store the weight of the edge

        minimum : bool, default = True
            Return the trees in increasing order while true and decreasing order
            while false.

        init_partition : tuple, default = None
            In the case that certain edges have to be included or excluded from
            the arborescences, `init_partition` should be in the form
            `(included_edges, excluded_edges)` where each edges is a
            `(u, v)`-tuple inside an iterable such as a list or set.
        """
        ...
    partition_queue: Incomplete
    def __iter__(self) -> Iterator[Incomplete]:
        """
        Returns
        -------
        ArborescenceIterator
            The iterator object for this graph
        """
        ...
    def __next__(self):
        """
        Returns
        -------
        (multi)Graph
            The spanning tree of next greatest weight, which ties broken
            arbitrarily.
        """
        ...
