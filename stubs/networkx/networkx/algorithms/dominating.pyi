from collections.abc import Iterable

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["dominating_set", "is_dominating_set"]

@_dispatchable
def dominating_set(G: Graph[_Node], start_with: _Node | None = None):
    """
    Finds a dominating set for the graph G.

    A *dominating set* for a graph with node set *V* is a subset *D* of
    *V* such that every node not in *D* is adjacent to at least one
    member of *D* [1]_.

    Parameters
    ----------
    G : NetworkX graph

    start_with : node (default=None)
        Node to use as a starting point for the algorithm.

    Returns
    -------
    D : set
        A dominating set for G.

    Notes
    -----
    This function is an implementation of algorithm 7 in [2]_ which
    finds some dominating set, not necessarily the smallest one.

    See also
    --------
    is_dominating_set

    References
    ----------
    .. [1] https://en.wikipedia.org/wiki/Dominating_set

    .. [2] Abdol-Hossein Esfahanian. Connectivity Algorithms.
        http://www.cse.msu.edu/~cse835/Papers/Graph_connectivity_revised.pdf
    """
    ...
@_dispatchable
def is_dominating_set(G: Graph[_Node], nbunch: Iterable[_Node]) -> bool: ...
