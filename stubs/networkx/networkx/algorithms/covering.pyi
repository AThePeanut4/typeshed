"""Functions related to graph covers."""

from _typeshed import Incomplete
from collections.abc import Callable, Iterable

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["min_edge_cover", "is_edge_cover"]

@_dispatchable
def min_edge_cover(G: Graph[_Node], matching_algorithm: Callable[..., Incomplete] | None = None) -> set[Incomplete]:
    """
    Returns the min cardinality edge cover of the graph as a set of edges.

    A smallest edge cover can be found in polynomial time by finding
    a maximum matching and extending it greedily so that all nodes
    are covered. This function follows that process. A maximum matching
    algorithm can be specified for the first step of the algorithm.
    The resulting set may return a set with one 2-tuple for each edge,
    (the usual case) or with both 2-tuples `(u, v)` and `(v, u)` for
    each edge. The latter is only done when a bipartite matching algorithm
    is specified as `matching_algorithm`.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    matching_algorithm : function
        A function that returns a maximum cardinality matching for `G`.
        The function must take one input, the graph `G`, and return
        either a set of edges (with only one direction for the pair of nodes)
        or a dictionary mapping each node to its mate. If not specified,
        :func:`~networkx.algorithms.matching.max_weight_matching` is used.
        Common bipartite matching functions include
        :func:`~networkx.algorithms.bipartite.matching.hopcroft_karp_matching`
        or
        :func:`~networkx.algorithms.bipartite.matching.eppstein_matching`.

    Returns
    -------
    min_cover : set

        A set of the edges in a minimum edge cover in the form of tuples.
        It contains only one of the equivalent 2-tuples `(u, v)` and `(v, u)`
        for each edge. If a bipartite method is used to compute the matching,
        the returned set contains both the 2-tuples `(u, v)` and `(v, u)`
        for each edge of a minimum edge cover.

    Examples
    --------
    >>> G = nx.Graph([(0, 1), (0, 2), (0, 3), (1, 2), (1, 3)])
    >>> sorted(nx.min_edge_cover(G))
    [(2, 1), (3, 0)]

    Notes
    -----
    An edge cover of a graph is a set of edges such that every node of
    the graph is incident to at least one edge of the set.
    The minimum edge cover is an edge covering of smallest cardinality.

    Due to its implementation, the worst-case running time of this algorithm
    is bounded by the worst-case running time of the function
    ``matching_algorithm``.

    Minimum edge cover for `G` can also be found using
    :func:`~networkx.algorithms.bipartite.covering.min_edge_covering` which is
    simply this function with a default matching algorithm of
    :func:`~networkx.algorithms.bipartite.matching.hopcroft_karp_matching`
    """
    ...
@_dispatchable
def is_edge_cover(G: Graph[_Node], cover: Iterable[Iterable[Incomplete]]) -> bool:
    """
    Decides whether a set of edges is a valid edge cover of the graph.

    Given a set of edges, whether it is an edge covering can
    be decided if we just check whether all nodes of the graph
    has an edge from the set, incident on it.

    Parameters
    ----------
    G : NetworkX graph
        An undirected bipartite graph.

    cover : set
        Set of edges to be checked.

    Returns
    -------
    bool
        Whether the set of edges is a valid edge cover of the graph.

    Examples
    --------
    >>> G = nx.Graph([(0, 1), (0, 2), (0, 3), (1, 2), (1, 3)])
    >>> cover = {(2, 1), (3, 0)}
    >>> nx.is_edge_cover(G, cover)
    True

    Notes
    -----
    An edge cover of a graph is a set of edges such that every node of
    the graph is incident to at least one edge of the set.
    """
    ...
