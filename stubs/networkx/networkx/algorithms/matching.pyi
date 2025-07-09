"""Functions for computing and verifying matchings in a graph."""

from _typeshed import Incomplete
from collections.abc import Iterable, Mapping

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = [
    "is_matching",
    "is_maximal_matching",
    "is_perfect_matching",
    "max_weight_matching",
    "min_weight_matching",
    "maximal_matching",
]

@_dispatchable
def maximal_matching(G: Graph[_Node]) -> set[Incomplete]: ...
def matching_dict_to_set(matching: Mapping[Incomplete, Incomplete]) -> set[Incomplete]: ...
@_dispatchable
def is_matching(G: Graph[_Node], matching: dict[Incomplete, Incomplete] | Iterable[Iterable[Incomplete]]) -> bool:
    """
    Return True if ``matching`` is a valid matching of ``G``

    A *matching* in a graph is a set of edges in which no two distinct
    edges share a common endpoint. Each node is incident to at most one
    edge in the matching. The edges are said to be independent.

    Parameters
    ----------
    G : NetworkX graph

    matching : dict or set
        A dictionary or set representing a matching. If a dictionary, it
        must have ``matching[u] == v`` and ``matching[v] == u`` for each
        edge ``(u, v)`` in the matching. If a set, it must have elements
        of the form ``(u, v)``, where ``(u, v)`` is an edge in the
        matching.

    Returns
    -------
    bool
        Whether the given set or dictionary represents a valid matching
        in the graph.

    Raises
    ------
    NetworkXError
        If the proposed matching has an edge to a node not in G.
        Or if the matching is not a collection of 2-tuple edges.

    Examples
    --------
    >>> G = nx.Graph([(1, 2), (1, 3), (2, 3), (2, 4), (3, 5), (4, 5)])
    >>> nx.is_maximal_matching(G, {1: 3, 2: 4})  # using dict to represent matching
    True

    >>> nx.is_matching(G, {(1, 3), (2, 4)})  # using set to represent matching
    True
    """
    ...
@_dispatchable
def is_maximal_matching(G: Graph[_Node], matching: dict[Incomplete, Incomplete] | Iterable[Iterable[Incomplete]]) -> bool:
    """
    Return True if ``matching`` is a maximal matching of ``G``

    A *maximal matching* in a graph is a matching in which adding any
    edge would cause the set to no longer be a valid matching.

    Parameters
    ----------
    G : NetworkX graph

    matching : dict or set
        A dictionary or set representing a matching. If a dictionary, it
        must have ``matching[u] == v`` and ``matching[v] == u`` for each
        edge ``(u, v)`` in the matching. If a set, it must have elements
        of the form ``(u, v)``, where ``(u, v)`` is an edge in the
        matching.

    Returns
    -------
    bool
        Whether the given set or dictionary represents a valid maximal
        matching in the graph.

    Examples
    --------
    >>> G = nx.Graph([(1, 2), (1, 3), (2, 3), (3, 4), (3, 5)])
    >>> nx.is_maximal_matching(G, {(1, 2), (3, 4)})
    True
    """
    ...
@_dispatchable
def is_perfect_matching(G: Graph[_Node], matching: dict[Incomplete, Incomplete] | Iterable[Iterable[Incomplete]]) -> bool:
    """
    Return True if ``matching`` is a perfect matching for ``G``

    A *perfect matching* in a graph is a matching in which exactly one edge
    is incident upon each vertex.

    Parameters
    ----------
    G : NetworkX graph

    matching : dict or set
        A dictionary or set representing a matching. If a dictionary, it
        must have ``matching[u] == v`` and ``matching[v] == u`` for each
        edge ``(u, v)`` in the matching. If a set, it must have elements
        of the form ``(u, v)``, where ``(u, v)`` is an edge in the
        matching.

    Returns
    -------
    bool
        Whether the given set or dictionary represents a valid perfect
        matching in the graph.

    Examples
    --------
    >>> G = nx.Graph([(1, 2), (1, 3), (2, 3), (2, 4), (3, 5), (4, 5), (4, 6)])
    >>> my_match = {1: 2, 3: 5, 4: 6}
    >>> nx.is_perfect_matching(G, my_match)
    True
    """
    ...
@_dispatchable
def min_weight_matching(G: Graph[_Node], weight: str | None = "weight") -> set[Incomplete]: ...
@_dispatchable
def max_weight_matching(
    G: Graph[_Node], maxcardinality: bool | None = False, weight: str | None = "weight"
) -> set[Incomplete]: ...
