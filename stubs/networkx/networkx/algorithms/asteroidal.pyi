"""
Algorithms for asteroidal triples and asteroidal numbers in graphs.

An asteroidal triple in a graph G is a set of three non-adjacent vertices
u, v and w such that there exist a path between any two of them that avoids
closed neighborhood of the third. More formally, v_j, v_k belongs to the same
connected component of G - N[v_i], where N[v_i] denotes the closed neighborhood
of v_i. A graph which does not contain any asteroidal triples is called
an AT-free graph. The class of AT-free graphs is a graph class for which
many NP-complete problems are solvable in polynomial time. Amongst them,
independent set and coloring.
"""

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["is_at_free", "find_asteroidal_triple"]

@_dispatchable
def find_asteroidal_triple(G: Graph[_Node]):
    r"""
    Find an asteroidal triple in the given graph.

    An asteroidal triple is a triple of non-adjacent vertices such that
    there exists a path between any two of them which avoids the closed
    neighborhood of the third. It checks all independent triples of vertices
    and whether they are an asteroidal triple or not. This is done with the
    help of a data structure called a component structure.
    A component structure encodes information about which vertices belongs to
    the same connected component when the closed neighborhood of a given vertex
    is removed from the graph. The algorithm used to check is the trivial
    one, outlined in [1]_, which has a runtime of
    :math:`O(|V||\overline{E} + |V||E|)`, where the second term is the
    creation of the component structure.

    Parameters
    ----------
    G : NetworkX Graph
        The graph to check whether is AT-free or not

    Returns
    -------
    list or None
        An asteroidal triple is returned as a list of nodes. If no asteroidal
        triple exists, i.e. the graph is AT-free, then None is returned.
        The returned value depends on the certificate parameter. The default
        option is a bool which is True if the graph is AT-free, i.e. the
        given graph contains no asteroidal triples, and False otherwise, i.e.
        if the graph contains at least one asteroidal triple.

    Notes
    -----
    The component structure and the algorithm is described in [1]_. The current
    implementation implements the trivial algorithm for simple graphs.

    References
    ----------
    .. [1] Ekkehard Köhler,
       "Recognizing Graphs without asteroidal triples",
       Journal of Discrete Algorithms 2, pages 439-452, 2004.
       https://www.sciencedirect.com/science/article/pii/S157086670400019X
    """
    ...
@_dispatchable
def is_at_free(G: Graph[_Node]) -> bool: ...
