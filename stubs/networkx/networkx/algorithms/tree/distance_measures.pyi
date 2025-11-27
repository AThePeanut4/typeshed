"""Algorithms for computing distance measures on trees."""

from _typeshed import Incomplete

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["center", "centroid"]

def center(G: Graph[_Node]) -> list[Incomplete]:
    """
    Returns the center of an undirected tree graph.

    The center of a tree consists of nodes that minimize the maximum eccentricity.
    That is, these nodes minimize the maximum distance to all other nodes.
    This implementation currently only works for unweighted edges.

    If the input graph is not a tree, results are not guaranteed to be correct and while
    some non-trees will raise an ``nx.NotATree`` exception, not all non-trees will be discovered.
    Thus, this function should not be used if caller is unsure whether the input graph
    is a tree. Use ``nx.is_tree(G)`` to check.

    Parameters
    ----------
    G : NetworkX graph
        A tree graph (undirected, acyclic graph).

    Returns
    -------
    center : list
        A list of nodes forming the center of the tree. This can be one or two nodes.

    Raises
    ------
    NetworkXNotImplemented
        If the input graph is directed.

    NotATree
        If the algorithm detects the input graph is not a tree. There is no guarantee
        this error will always raise if a non-tree is passed.

    Notes
    -----
    This algorithm iteratively removes leaves (nodes with degree 1) from the tree until
    there are only 1 or 2 nodes left. The remaining nodes form the center of the tree.

    This algorithm's time complexity is ``O(N)`` where ``N`` is the number of nodes in the tree.

    Examples
    --------
    >>> G = nx.Graph([(1, 2), (1, 3), (2, 4), (2, 5)])
    >>> nx.tree.center(G)
    [1, 2]

    >>> G = nx.path_graph(5)
    >>> nx.tree.center(G)
    [2]
    """
    ...
@_dispatchable
def centroid(G: Graph[_Node]) -> list[Incomplete]:
    """
    Return the centroid of an unweighted tree.

    The centroid of a tree is the set of nodes such that removing any
    one of them would split the tree into a forest of subtrees, each
    with at most ``N / 2`` nodes, where ``N`` is the number of nodes
    in the original tree. This set may contain two nodes if removing
    an edge between them results in two trees of size exactly ``N /
    2``.

    Parameters
    ----------
    G : NetworkX graph
       A tree.

    Returns
    -------
    c : list
       List of nodes in centroid of the tree. This could be one or two nodes.

    Raises
    ------
    NotATree
        If the input graph is not a tree.
    NotImplementedException
        If the input graph is directed.
    NetworkXPointlessConcept
        If `G` has no nodes or edges.

    Notes
    -----
    This algorithm's time complexity is ``O(N)`` where ``N`` is the
    number of nodes in the tree.

    In unweighted trees the centroid coincides with the barycenter,
    the node or nodes that minimize the sum of distances to all other
    nodes. However, this concept is different from that of the graph
    center, which is the set of nodes minimizing the maximum distance
    to all other nodes.

    Examples
    --------
    >>> G = nx.path_graph(4)
    >>> nx.tree.centroid(G)
    [1, 2]

    A star-shaped tree with one long branch illustrates the difference
    between the centroid and the center. The center lies near the
    middle of the long branch, minimizing maximum distance. The
    centroid, however, limits the size of any resulting subtree to at
    most half the total nodes, forcing it to remain near the hub when
    enough short branches are present.

    >>> G = nx.star_graph(6)
    >>> nx.add_path(G, [6, 7, 8, 9, 10])
    >>> nx.tree.centroid(G), nx.tree.center(G)
    ([0], [7])

    See Also
    --------
    :func:`~networkx.algorithms.distance_measures.barycenter`
    :func:`~networkx.algorithms.distance_measures.center`
    center : tree center
    """
    ...
