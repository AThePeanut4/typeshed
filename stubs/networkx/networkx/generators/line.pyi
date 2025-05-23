"""Functions for generating line graphs."""

from networkx.utils.backends import _dispatchable

__all__ = ["line_graph", "inverse_line_graph"]

@_dispatchable
def line_graph(G, create_using=None):
    r"""
    Returns the line graph of the graph or digraph `G`.

    The line graph of a graph `G` has a node for each edge in `G` and an
    edge joining those nodes if the two edges in `G` share a common node. For
    directed graphs, nodes are adjacent exactly when the edges they represent
    form a directed path of length two.

    The nodes of the line graph are 2-tuples of nodes in the original graph (or
    3-tuples for multigraphs, with the key of the edge as the third element).

    For information about self-loops and more discussion, see the **Notes**
    section below.

    Parameters
    ----------
    G : graph
        A NetworkX Graph, DiGraph, MultiGraph, or MultiDigraph.
    create_using : NetworkX graph constructor, optional (default=nx.Graph)
       Graph type to create. If graph instance, then cleared before populated.

    Returns
    -------
    L : graph
        The line graph of G.

    Examples
    --------
    >>> G = nx.star_graph(3)
    >>> L = nx.line_graph(G)
    >>> print(sorted(map(sorted, L.edges())))  # makes a 3-clique, K3
    [[(0, 1), (0, 2)], [(0, 1), (0, 3)], [(0, 2), (0, 3)]]

    Edge attributes from `G` are not copied over as node attributes in `L`, but
    attributes can be copied manually:

    >>> G = nx.path_graph(4)
    >>> G.add_edges_from((u, v, {"tot": u + v}) for u, v in G.edges)
    >>> G.edges(data=True)
    EdgeDataView([(0, 1, {'tot': 1}), (1, 2, {'tot': 3}), (2, 3, {'tot': 5})])
    >>> H = nx.line_graph(G)
    >>> H.add_nodes_from((node, G.edges[node]) for node in H)
    >>> H.nodes(data=True)
    NodeDataView({(0, 1): {'tot': 1}, (2, 3): {'tot': 5}, (1, 2): {'tot': 3}})

    Notes
    -----
    Graph, node, and edge data are not propagated to the new graph. For
    undirected graphs, the nodes in G must be sortable, otherwise the
    constructed line graph may not be correct.

    *Self-loops in undirected graphs*

    For an undirected graph `G` without multiple edges, each edge can be
    written as a set `\{u, v\}`.  Its line graph `L` has the edges of `G` as
    its nodes. If `x` and `y` are two nodes in `L`, then `\{x, y\}` is an edge
    in `L` if and only if the intersection of `x` and `y` is nonempty. Thus,
    the set of all edges is determined by the set of all pairwise intersections
    of edges in `G`.

    Trivially, every edge in G would have a nonzero intersection with itself,
    and so every node in `L` should have a self-loop. This is not so
    interesting, and the original context of line graphs was with simple
    graphs, which had no self-loops or multiple edges. The line graph was also
    meant to be a simple graph and thus, self-loops in `L` are not part of the
    standard definition of a line graph. In a pairwise intersection matrix,
    this is analogous to excluding the diagonal entries from the line graph
    definition.

    Self-loops and multiple edges in `G` add nodes to `L` in a natural way, and
    do not require any fundamental changes to the definition. It might be
    argued that the self-loops we excluded before should now be included.
    However, the self-loops are still "trivial" in some sense and thus, are
    usually excluded.

    *Self-loops in directed graphs*

    For a directed graph `G` without multiple edges, each edge can be written
    as a tuple `(u, v)`. Its line graph `L` has the edges of `G` as its
    nodes. If `x` and `y` are two nodes in `L`, then `(x, y)` is an edge in `L`
    if and only if the tail of `x` matches the head of `y`, for example, if `x
    = (a, b)` and `y = (b, c)` for some vertices `a`, `b`, and `c` in `G`.

    Due to the directed nature of the edges, it is no longer the case that
    every edge in `G` should have a self-loop in `L`. Now, the only time
    self-loops arise is if a node in `G` itself has a self-loop.  So such
    self-loops are no longer "trivial" but instead, represent essential
    features of the topology of `G`. For this reason, the historical
    development of line digraphs is such that self-loops are included. When the
    graph `G` has multiple edges, once again only superficial changes are
    required to the definition.

    References
    ----------
    * Harary, Frank, and Norman, Robert Z., "Some properties of line digraphs",
      Rend. Circ. Mat. Palermo, II. Ser. 9 (1960), 161--168.
    * Hemminger, R. L.; Beineke, L. W. (1978), "Line graphs and line digraphs",
      in Beineke, L. W.; Wilson, R. J., Selected Topics in Graph Theory,
      Academic Press Inc., pp. 271--305.
    """
    ...
@_dispatchable
def inverse_line_graph(G):
    """
    Returns the inverse line graph of graph G.

    If H is a graph, and G is the line graph of H, such that G = L(H).
    Then H is the inverse line graph of G.

    Not all graphs are line graphs and these do not have an inverse line graph.
    In these cases this function raises a NetworkXError.

    Parameters
    ----------
    G : graph
        A NetworkX Graph

    Returns
    -------
    H : graph
        The inverse line graph of G.

    Raises
    ------
    NetworkXNotImplemented
        If G is directed or a multigraph

    NetworkXError
        If G is not a line graph

    Notes
    -----
    This is an implementation of the Roussopoulos algorithm[1]_.

    If G consists of multiple components, then the algorithm doesn't work.
    You should invert every component separately:

    >>> K5 = nx.complete_graph(5)
    >>> P4 = nx.Graph([("a", "b"), ("b", "c"), ("c", "d")])
    >>> G = nx.union(K5, P4)
    >>> root_graphs = []
    >>> for comp in nx.connected_components(G):
    ...     root_graphs.append(nx.inverse_line_graph(G.subgraph(comp)))
    >>> len(root_graphs)
    2

    References
    ----------
    .. [1] Roussopoulos, N.D. , "A max {m, n} algorithm for determining the graph H from
       its line graph G", Information Processing Letters 2, (1973), 108--112, ISSN 0020-0190,
       `DOI link <https://doi.org/10.1016/0020-0190(73)90029-X>`_
    """
    ...
