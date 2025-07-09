"""
==========================
Bipartite Graph Algorithms
==========================
"""

from _typeshed import Incomplete
from collections.abc import Iterable

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["is_bipartite", "is_bipartite_node_set", "color", "sets", "density", "degrees"]

@_dispatchable
def color(G: Graph[_Node]) -> dict[Incomplete, Incomplete]: ...
@_dispatchable
def is_bipartite(G: Graph[_Node]) -> bool:
    """
    Returns True if graph G is bipartite, False if not.

    Parameters
    ----------
    G : NetworkX graph

    Examples
    --------
    >>> from networkx.algorithms import bipartite
    >>> G = nx.path_graph(4)
    >>> print(bipartite.is_bipartite(G))
    True

    See Also
    --------
    color, is_bipartite_node_set
    """
    ...
@_dispatchable
def is_bipartite_node_set(G: Graph[_Node], nodes: Iterable[Incomplete]) -> bool:
    """
    Returns True if nodes and G/nodes are a bipartition of G.

    Parameters
    ----------
    G : NetworkX graph

    nodes: list or container
      Check if nodes are a one of a bipartite set.

    Examples
    --------
    >>> from networkx.algorithms import bipartite
    >>> G = nx.path_graph(4)
    >>> X = set([1, 3])
    >>> bipartite.is_bipartite_node_set(G, X)
    True

    Notes
    -----
    An exception is raised if the input nodes are not distinct, because in this
    case some bipartite algorithms will yield incorrect results.
    For connected graphs the bipartite sets are unique.  This function handles
    disconnected graphs.
    """
    ...
@_dispatchable
def sets(G: Graph[_Node], top_nodes: Iterable[Incomplete] | None = None) -> tuple[set[Incomplete], set[Incomplete]]: ...
@_dispatchable
def density(B: Graph[_Node], nodes) -> float: ...
@_dispatchable
def degrees(B: Graph[_Node], nodes, weight: str | None = None) -> tuple[Incomplete, Incomplete]: ...
