"""Function for computing the moral graph of a directed graph."""

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["moral_graph"]

@_dispatchable
def moral_graph(G: Graph[_Node]):
    """
    Return the Moral Graph

    Returns the moralized graph of a given directed graph.

    Parameters
    ----------
    G : NetworkX graph
        Directed graph

    Returns
    -------
    H : NetworkX graph
        The undirected moralized graph of G

    Raises
    ------
    NetworkXNotImplemented
        If `G` is undirected.

    Examples
    --------
    >>> G = nx.DiGraph([(1, 2), (2, 3), (2, 5), (3, 4), (4, 3)])
    >>> G_moral = nx.moral_graph(G)
    >>> G_moral.edges()
    EdgeView([(1, 2), (2, 3), (2, 5), (2, 4), (3, 4)])

    Notes
    -----
    A moral graph is an undirected graph H = (V, E) generated from a
    directed Graph, where if a node has more than one parent node, edges
    between these parent nodes are inserted and all directed edges become
    undirected.

    https://en.wikipedia.org/wiki/Moral_graph

    References
    ----------
    .. [1] Wray L. Buntine. 1995. Chain graphs for learning.
           In Proceedings of the Eleventh conference on Uncertainty
           in artificial intelligence (UAI'95)
    """
    ...
