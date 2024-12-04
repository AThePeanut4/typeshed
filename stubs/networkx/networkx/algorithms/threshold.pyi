"""Threshold Graphs - Creation, manipulation and identification."""

from _typeshed import Incomplete

from networkx.utils.backends import _dispatchable

@_dispatchable
def is_threshold_graph(G):
    """
    Returns `True` if `G` is a threshold graph.

    Parameters
    ----------
    G : NetworkX graph instance
        An instance of `Graph`, `DiGraph`, `MultiGraph` or `MultiDiGraph`

    Returns
    -------
    bool
        `True` if `G` is a threshold graph, `False` otherwise.

    Examples
    --------
    >>> from networkx.algorithms.threshold import is_threshold_graph
    >>> G = nx.path_graph(3)
    >>> is_threshold_graph(G)
    True
    >>> G = nx.barbell_graph(3, 3)
    >>> is_threshold_graph(G)
    False

    References
    ----------
    .. [1] Threshold graphs: https://en.wikipedia.org/wiki/Threshold_graph
    """
    ...
@_dispatchable
def find_threshold_graph(G, create_using: Incomplete | None = None):
    """
    Returns a threshold subgraph that is close to largest in `G`.

    The threshold graph will contain the largest degree node in G.

    Parameters
    ----------
    G : NetworkX graph instance
        An instance of `Graph`, or `MultiDiGraph`
    create_using : NetworkX graph class or `None` (default), optional
        Type of graph to use when constructing the threshold graph.
        If `None`, infer the appropriate graph type from the input.

    Returns
    -------
    graph :
        A graph instance representing the threshold graph

    Examples
    --------
    >>> from networkx.algorithms.threshold import find_threshold_graph
    >>> G = nx.barbell_graph(3, 3)
    >>> T = find_threshold_graph(G)
    >>> T.nodes  # may vary
    NodeView((7, 8, 5, 6))

    References
    ----------
    .. [1] Threshold graphs: https://en.wikipedia.org/wiki/Threshold_graph
    """
    ...
