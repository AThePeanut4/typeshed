from networkx.utils.backends import _dispatchable

__all__ = ["line_graph", "inverse_line_graph"]

@_dispatchable
def line_graph(G, create_using=None): ...
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
