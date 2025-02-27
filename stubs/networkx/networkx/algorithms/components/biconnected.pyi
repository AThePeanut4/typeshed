"""Biconnected components and articulation points."""

from _typeshed import Incomplete
from collections.abc import Generator

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def is_biconnected(G: Graph[_Node]):
    """
    Returns True if the graph is biconnected, False otherwise.

    A graph is biconnected if, and only if, it cannot be disconnected by
    removing only one node (and all edges incident on that node).  If
    removing a node increases the number of disconnected components
    in the graph, that node is called an articulation point, or cut
    vertex.  A biconnected graph has no articulation points.

    Parameters
    ----------
    G : NetworkX Graph
        An undirected graph.

    Returns
    -------
    biconnected : bool
        True if the graph is biconnected, False otherwise.

    Raises
    ------
    NetworkXNotImplemented
        If the input graph is not undirected.

    Examples
    --------
    >>> G = nx.path_graph(4)
    >>> print(nx.is_biconnected(G))
    False
    >>> G.add_edge(0, 3)
    >>> print(nx.is_biconnected(G))
    True

    See Also
    --------
    biconnected_components
    articulation_points
    biconnected_component_edges
    is_strongly_connected
    is_weakly_connected
    is_connected
    is_semiconnected

    Notes
    -----
    The algorithm to find articulation points and biconnected
    components is implemented using a non-recursive depth-first-search
    (DFS) that keeps track of the highest level that back edges reach
    in the DFS tree.  A node `n` is an articulation point if, and only
    if, there exists a subtree rooted at `n` such that there is no
    back edge from any successor of `n` that links to a predecessor of
    `n` in the DFS tree.  By keeping track of all the edges traversed
    by the DFS we can obtain the biconnected components because all
    edges of a bicomponent will be traversed consecutively between
    articulation points.

    References
    ----------
    .. [1] Hopcroft, J.; Tarjan, R. (1973).
       "Efficient algorithms for graph manipulation".
       Communications of the ACM 16: 372–378. doi:10.1145/362248.362272
    """
    ...
@_dispatchable
def biconnected_component_edges(G: Graph[_Node]) -> Generator[Incomplete, Incomplete, None]:
    """
    Returns a generator of lists of edges, one list for each biconnected
    component of the input graph.

    Biconnected components are maximal subgraphs such that the removal of a
    node (and all edges incident on that node) will not disconnect the
    subgraph.  Note that nodes may be part of more than one biconnected
    component.  Those nodes are articulation points, or cut vertices.
    However, each edge belongs to one, and only one, biconnected component.

    Notice that by convention a dyad is considered a biconnected component.

    Parameters
    ----------
    G : NetworkX Graph
        An undirected graph.

    Returns
    -------
    edges : generator of lists
        Generator of lists of edges, one list for each bicomponent.

    Raises
    ------
    NetworkXNotImplemented
        If the input graph is not undirected.

    Examples
    --------
    >>> G = nx.barbell_graph(4, 2)
    >>> print(nx.is_biconnected(G))
    False
    >>> bicomponents_edges = list(nx.biconnected_component_edges(G))
    >>> len(bicomponents_edges)
    5
    >>> G.add_edge(2, 8)
    >>> print(nx.is_biconnected(G))
    True
    >>> bicomponents_edges = list(nx.biconnected_component_edges(G))
    >>> len(bicomponents_edges)
    1

    See Also
    --------
    is_biconnected,
    biconnected_components,
    articulation_points,

    Notes
    -----
    The algorithm to find articulation points and biconnected
    components is implemented using a non-recursive depth-first-search
    (DFS) that keeps track of the highest level that back edges reach
    in the DFS tree.  A node `n` is an articulation point if, and only
    if, there exists a subtree rooted at `n` such that there is no
    back edge from any successor of `n` that links to a predecessor of
    `n` in the DFS tree.  By keeping track of all the edges traversed
    by the DFS we can obtain the biconnected components because all
    edges of a bicomponent will be traversed consecutively between
    articulation points.

    References
    ----------
    .. [1] Hopcroft, J.; Tarjan, R. (1973).
           "Efficient algorithms for graph manipulation".
           Communications of the ACM 16: 372–378. doi:10.1145/362248.362272
    """
    ...
@_dispatchable
def biconnected_components(G: Graph[_Node]) -> Generator[Incomplete, None, None]:
    """
    Returns a generator of sets of nodes, one set for each biconnected
    component of the graph

    Biconnected components are maximal subgraphs such that the removal of a
    node (and all edges incident on that node) will not disconnect the
    subgraph. Note that nodes may be part of more than one biconnected
    component.  Those nodes are articulation points, or cut vertices.  The
    removal of articulation points will increase the number of connected
    components of the graph.

    Notice that by convention a dyad is considered a biconnected component.

    Parameters
    ----------
    G : NetworkX Graph
        An undirected graph.

    Returns
    -------
    nodes : generator
        Generator of sets of nodes, one set for each biconnected component.

    Raises
    ------
    NetworkXNotImplemented
        If the input graph is not undirected.

    Examples
    --------
    >>> G = nx.lollipop_graph(5, 1)
    >>> print(nx.is_biconnected(G))
    False
    >>> bicomponents = list(nx.biconnected_components(G))
    >>> len(bicomponents)
    2
    >>> G.add_edge(0, 5)
    >>> print(nx.is_biconnected(G))
    True
    >>> bicomponents = list(nx.biconnected_components(G))
    >>> len(bicomponents)
    1

    You can generate a sorted list of biconnected components, largest
    first, using sort.

    >>> G.remove_edge(0, 5)
    >>> [len(c) for c in sorted(nx.biconnected_components(G), key=len, reverse=True)]
    [5, 2]

    If you only want the largest connected component, it's more
    efficient to use max instead of sort.

    >>> Gc = max(nx.biconnected_components(G), key=len)

    To create the components as subgraphs use:
    ``(G.subgraph(c).copy() for c in biconnected_components(G))``

    See Also
    --------
    is_biconnected
    articulation_points
    biconnected_component_edges
    k_components : this function is a special case where k=2
    bridge_components : similar to this function, but is defined using
        2-edge-connectivity instead of 2-node-connectivity.

    Notes
    -----
    The algorithm to find articulation points and biconnected
    components is implemented using a non-recursive depth-first-search
    (DFS) that keeps track of the highest level that back edges reach
    in the DFS tree.  A node `n` is an articulation point if, and only
    if, there exists a subtree rooted at `n` such that there is no
    back edge from any successor of `n` that links to a predecessor of
    `n` in the DFS tree.  By keeping track of all the edges traversed
    by the DFS we can obtain the biconnected components because all
    edges of a bicomponent will be traversed consecutively between
    articulation points.

    References
    ----------
    .. [1] Hopcroft, J.; Tarjan, R. (1973).
           "Efficient algorithms for graph manipulation".
           Communications of the ACM 16: 372–378. doi:10.1145/362248.362272
    """
    ...
@_dispatchable
def articulation_points(G: Graph[_Node]) -> Generator[Incomplete, None, None]:
    """
    Yield the articulation points, or cut vertices, of a graph.

    An articulation point or cut vertex is any node whose removal (along with
    all its incident edges) increases the number of connected components of
    a graph.  An undirected connected graph without articulation points is
    biconnected. Articulation points belong to more than one biconnected
    component of a graph.

    Notice that by convention a dyad is considered a biconnected component.

    Parameters
    ----------
    G : NetworkX Graph
        An undirected graph.

    Yields
    ------
    node
        An articulation point in the graph.

    Raises
    ------
    NetworkXNotImplemented
        If the input graph is not undirected.

    Examples
    --------

    >>> G = nx.barbell_graph(4, 2)
    >>> print(nx.is_biconnected(G))
    False
    >>> len(list(nx.articulation_points(G)))
    4
    >>> G.add_edge(2, 8)
    >>> print(nx.is_biconnected(G))
    True
    >>> len(list(nx.articulation_points(G)))
    0

    See Also
    --------
    is_biconnected
    biconnected_components
    biconnected_component_edges

    Notes
    -----
    The algorithm to find articulation points and biconnected
    components is implemented using a non-recursive depth-first-search
    (DFS) that keeps track of the highest level that back edges reach
    in the DFS tree.  A node `n` is an articulation point if, and only
    if, there exists a subtree rooted at `n` such that there is no
    back edge from any successor of `n` that links to a predecessor of
    `n` in the DFS tree.  By keeping track of all the edges traversed
    by the DFS we can obtain the biconnected components because all
    edges of a bicomponent will be traversed consecutively between
    articulation points.

    References
    ----------
    .. [1] Hopcroft, J.; Tarjan, R. (1973).
           "Efficient algorithms for graph manipulation".
           Communications of the ACM 16: 372–378. doi:10.1145/362248.362272
    """
    ...
