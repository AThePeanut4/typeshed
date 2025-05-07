"""
Laplacian matrix of graphs.

All calculations here are done using the out-degree. For Laplacians using
in-degree, use `G.reverse(copy=False)` instead of `G` and take the transpose.

The `laplacian_matrix` function provides an unnormalized matrix,
while `normalized_laplacian_matrix`, `directed_laplacian_matrix`,
and `directed_combinatorial_laplacian_matrix` are all normalized.
"""

from _typeshed import Incomplete
from collections.abc import Collection

from networkx.utils.backends import _dispatchable

@_dispatchable
def laplacian_matrix(G, nodelist: Collection[Incomplete] | None = None, weight: str = "weight"): ...
@_dispatchable
def normalized_laplacian_matrix(G, nodelist: Collection[Incomplete] | None = None, weight: str = "weight"): ...
@_dispatchable
def total_spanning_tree_weight(G, weight: Incomplete | None = None):
    """
    Returns the total weight of all spanning trees of `G`.

    Kirchoff's Tree Matrix Theorem [1]_, [2]_ states that the determinant of any
    cofactor of the Laplacian matrix of a graph is the number of spanning trees
    in the graph. For a weighted Laplacian matrix, it is the sum across all
    spanning trees of the multiplicative weight of each tree. That is, the
    weight of each tree is the product of its edge weights.

    For unweighted graphs, the total weight equals the number of spanning trees in `G`.

    For directed graphs, the total weight follows by summing over all directed
    spanning trees in `G` that start in the `root` node [3]_.

    .. deprecated:: 3.3

       ``total_spanning_tree_weight`` is deprecated and will be removed in v3.5.
       Use ``nx.number_of_spanning_trees(G)`` instead.

    Parameters
    ----------
    G : NetworkX Graph

    weight : string or None, optional (default=None)
        The key for the edge attribute holding the edge weight.
        If None, then each edge has weight 1.

    root : node (only required for directed graphs)
       A node in the directed graph `G`.

    Returns
    -------
    total_weight : float
        Undirected graphs:
            The sum of the total multiplicative weights for all spanning trees in `G`.
        Directed graphs:
            The sum of the total multiplicative weights for all spanning trees of `G`,
            rooted at node `root`.

    Raises
    ------
    NetworkXPointlessConcept
        If `G` does not contain any nodes.

    NetworkXError
        If the graph `G` is not (weakly) connected,
        or if `G` is directed and the root node is not specified or not in G.

    Examples
    --------
    >>> G = nx.complete_graph(5)
    >>> round(nx.total_spanning_tree_weight(G))
    125

    >>> G = nx.Graph()
    >>> G.add_edge(1, 2, weight=2)
    >>> G.add_edge(1, 3, weight=1)
    >>> G.add_edge(2, 3, weight=1)
    >>> round(nx.total_spanning_tree_weight(G, "weight"))
    5

    Notes
    -----
    Self-loops are excluded. Multi-edges are contracted in one edge
    equal to the sum of the weights.

    References
    ----------
    .. [1] Wikipedia
       "Kirchhoff's theorem."
       https://en.wikipedia.org/wiki/Kirchhoff%27s_theorem
    .. [2] Kirchhoff, G. R.
        Über die Auflösung der Gleichungen, auf welche man
        bei der Untersuchung der linearen Vertheilung
        Galvanischer Ströme geführt wird
        Annalen der Physik und Chemie, vol. 72, pp. 497-508, 1847.
    .. [3] Margoliash, J.
        "Matrix-Tree Theorem for Directed Graphs"
        https://www.math.uchicago.edu/~may/VIGRE/VIGRE2010/REUPapers/Margoliash.pdf
    """
    ...
@_dispatchable
def directed_laplacian_matrix(
    G,
    nodelist: Collection[Incomplete] | None = None,
    weight: str = "weight",
    walk_type: Incomplete | None = None,
    alpha: float = 0.95,
): ...
@_dispatchable
def directed_combinatorial_laplacian_matrix(
    G,
    nodelist: Collection[Incomplete] | None = None,
    weight: str = "weight",
    walk_type: Incomplete | None = None,
    alpha: float = 0.95,
): ...
