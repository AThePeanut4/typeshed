"""
Compute the shortest paths and path lengths between nodes in the graph.

These algorithms work with undirected and directed graphs.
"""

from _typeshed import Incomplete
from collections.abc import Callable, Generator
from typing import overload

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = [
    "shortest_path",
    "all_shortest_paths",
    "single_source_all_shortest_paths",
    "all_pairs_all_shortest_paths",
    "shortest_path_length",
    "average_shortest_path_length",
    "has_path",
]

@_dispatchable
def has_path(G: Graph[_Node], source: _Node, target: _Node) -> bool:
    """
    Returns *True* if *G* has a path from *source* to *target*.

    Parameters
    ----------
    G : NetworkX graph

    source : node
       Starting node for path

    target : node
       Ending node for path
    """
    ...
@overload
def shortest_path(
    G: Graph[_Node],
    source: _Node | None = None,
    target: _Node | None = None,
    weight: str | Callable[..., Incomplete] | None = None,
    method: str | None = "dijkstra",
) -> list[_Node]:
    """
    Compute shortest paths in the graph.

    Parameters
    ----------
    G : NetworkX graph

    source : node, optional
        Starting node for path. If not specified, compute shortest
        paths for each possible starting node.

    target : node, optional
        Ending node for path. If not specified, compute shortest
        paths to all possible nodes.

    weight : None, string or function, optional (default = None)
        If None, every edge has weight/distance/cost 1.
        If a string, use this edge attribute as the edge weight.
        Any edge attribute not present defaults to 1.
        If this is a function, the weight of an edge is the value
        returned by the function. The function must accept exactly
        three positional arguments: the two endpoints of an edge and
        the dictionary of edge attributes for that edge.
        The function must return a number.

    method : string, optional (default = 'dijkstra')
        The algorithm to use to compute the path.
        Supported options: 'dijkstra', 'bellman-ford'.
        Other inputs produce a ValueError.
        If `weight` is None, unweighted graph methods are used, and this
        suggestion is ignored.

    Returns
    -------
    path: list or dictionary or iterator
        All returned paths include both the source and target in the path.

        If the source and target are both specified, return a single list
        of nodes in a shortest path from the source to the target.

        If only the source is specified, return a dictionary keyed by
        targets with a list of nodes in a shortest path from the source
        to one of the targets.

        If only the target is specified, return a dictionary keyed by
        sources with a list of nodes in a shortest path from one of the
        sources to the target.

        If neither the source nor target are specified, return an iterator
        over (source, dictionary) where dictionary is keyed by target to
        list of nodes in a shortest path from the source to the target.

    Raises
    ------
    NodeNotFound
        If `source` is not in `G`.

    ValueError
        If `method` is not among the supported options.

    Examples
    --------
    >>> G = nx.path_graph(5)
    >>> print(nx.shortest_path(G, source=0, target=4))
    [0, 1, 2, 3, 4]
    >>> p = nx.shortest_path(G, source=0)  # target not specified
    >>> p[3]  # shortest path from source=0 to target=3
    [0, 1, 2, 3]
    >>> p = nx.shortest_path(G, target=4)  # source not specified
    >>> p[1]  # shortest path from source=1 to target=4
    [1, 2, 3, 4]
    >>> p = dict(nx.shortest_path(G))  # source, target not specified
    >>> p[2][4]  # shortest path from source=2 to target=4
    [2, 3, 4]

    Notes
    -----
    There may be more than one shortest path between a source and target.
    This returns only one of them.

    See Also
    --------
    all_pairs_shortest_path
    all_pairs_dijkstra_path
    all_pairs_bellman_ford_path
    single_source_shortest_path
    single_source_dijkstra_path
    single_source_bellman_ford_path
    """
    ...
@overload
def shortest_path(
    G: Graph[_Node],
    source: _Node | None = None,
    target: _Node | None = None,
    weight: str | Callable[..., Incomplete] | None = None,
    method: str | None = "dijkstra",
) -> dict[_Node, list[_Node]]:
    """
    Compute shortest paths in the graph.

    Parameters
    ----------
    G : NetworkX graph

    source : node, optional
        Starting node for path. If not specified, compute shortest
        paths for each possible starting node.

    target : node, optional
        Ending node for path. If not specified, compute shortest
        paths to all possible nodes.

    weight : None, string or function, optional (default = None)
        If None, every edge has weight/distance/cost 1.
        If a string, use this edge attribute as the edge weight.
        Any edge attribute not present defaults to 1.
        If this is a function, the weight of an edge is the value
        returned by the function. The function must accept exactly
        three positional arguments: the two endpoints of an edge and
        the dictionary of edge attributes for that edge.
        The function must return a number.

    method : string, optional (default = 'dijkstra')
        The algorithm to use to compute the path.
        Supported options: 'dijkstra', 'bellman-ford'.
        Other inputs produce a ValueError.
        If `weight` is None, unweighted graph methods are used, and this
        suggestion is ignored.

    Returns
    -------
    path: list or dictionary or iterator
        All returned paths include both the source and target in the path.

        If the source and target are both specified, return a single list
        of nodes in a shortest path from the source to the target.

        If only the source is specified, return a dictionary keyed by
        targets with a list of nodes in a shortest path from the source
        to one of the targets.

        If only the target is specified, return a dictionary keyed by
        sources with a list of nodes in a shortest path from one of the
        sources to the target.

        If neither the source nor target are specified, return an iterator
        over (source, dictionary) where dictionary is keyed by target to
        list of nodes in a shortest path from the source to the target.

    Raises
    ------
    NodeNotFound
        If `source` is not in `G`.

    ValueError
        If `method` is not among the supported options.

    Examples
    --------
    >>> G = nx.path_graph(5)
    >>> print(nx.shortest_path(G, source=0, target=4))
    [0, 1, 2, 3, 4]
    >>> p = nx.shortest_path(G, source=0)  # target not specified
    >>> p[3]  # shortest path from source=0 to target=3
    [0, 1, 2, 3]
    >>> p = nx.shortest_path(G, target=4)  # source not specified
    >>> p[1]  # shortest path from source=1 to target=4
    [1, 2, 3, 4]
    >>> p = dict(nx.shortest_path(G))  # source, target not specified
    >>> p[2][4]  # shortest path from source=2 to target=4
    [2, 3, 4]

    Notes
    -----
    There may be more than one shortest path between a source and target.
    This returns only one of them.

    See Also
    --------
    all_pairs_shortest_path
    all_pairs_dijkstra_path
    all_pairs_bellman_ford_path
    single_source_shortest_path
    single_source_dijkstra_path
    single_source_bellman_ford_path
    """
    ...
@overload
def shortest_path(
    G: Graph[_Node],
    source: _Node | None = None,
    target: _Node | None = None,
    weight: str | Callable[..., Incomplete] | None = None,
    method: str | None = "dijkstra",
) -> dict[_Node, list[_Node]]:
    """
    Compute shortest paths in the graph.

    Parameters
    ----------
    G : NetworkX graph

    source : node, optional
        Starting node for path. If not specified, compute shortest
        paths for each possible starting node.

    target : node, optional
        Ending node for path. If not specified, compute shortest
        paths to all possible nodes.

    weight : None, string or function, optional (default = None)
        If None, every edge has weight/distance/cost 1.
        If a string, use this edge attribute as the edge weight.
        Any edge attribute not present defaults to 1.
        If this is a function, the weight of an edge is the value
        returned by the function. The function must accept exactly
        three positional arguments: the two endpoints of an edge and
        the dictionary of edge attributes for that edge.
        The function must return a number.

    method : string, optional (default = 'dijkstra')
        The algorithm to use to compute the path.
        Supported options: 'dijkstra', 'bellman-ford'.
        Other inputs produce a ValueError.
        If `weight` is None, unweighted graph methods are used, and this
        suggestion is ignored.

    Returns
    -------
    path: list or dictionary or iterator
        All returned paths include both the source and target in the path.

        If the source and target are both specified, return a single list
        of nodes in a shortest path from the source to the target.

        If only the source is specified, return a dictionary keyed by
        targets with a list of nodes in a shortest path from the source
        to one of the targets.

        If only the target is specified, return a dictionary keyed by
        sources with a list of nodes in a shortest path from one of the
        sources to the target.

        If neither the source nor target are specified, return an iterator
        over (source, dictionary) where dictionary is keyed by target to
        list of nodes in a shortest path from the source to the target.

    Raises
    ------
    NodeNotFound
        If `source` is not in `G`.

    ValueError
        If `method` is not among the supported options.

    Examples
    --------
    >>> G = nx.path_graph(5)
    >>> print(nx.shortest_path(G, source=0, target=4))
    [0, 1, 2, 3, 4]
    >>> p = nx.shortest_path(G, source=0)  # target not specified
    >>> p[3]  # shortest path from source=0 to target=3
    [0, 1, 2, 3]
    >>> p = nx.shortest_path(G, target=4)  # source not specified
    >>> p[1]  # shortest path from source=1 to target=4
    [1, 2, 3, 4]
    >>> p = dict(nx.shortest_path(G))  # source, target not specified
    >>> p[2][4]  # shortest path from source=2 to target=4
    [2, 3, 4]

    Notes
    -----
    There may be more than one shortest path between a source and target.
    This returns only one of them.

    See Also
    --------
    all_pairs_shortest_path
    all_pairs_dijkstra_path
    all_pairs_bellman_ford_path
    single_source_shortest_path
    single_source_dijkstra_path
    single_source_bellman_ford_path
    """
    ...
@_dispatchable
def shortest_path_length(
    G: Graph[_Node],
    source: _Node | None = None,
    target: _Node | None = None,
    weight: str | Callable[..., Incomplete] | None = None,
    method: str | None = "dijkstra",
):
    """
    Compute shortest path lengths in the graph.

    Parameters
    ----------
    G : NetworkX graph

    source : node, optional
        Starting node for path.
        If not specified, compute shortest path lengths using all nodes as
        source nodes.

    target : node, optional
        Ending node for path.
        If not specified, compute shortest path lengths using all nodes as
        target nodes.

    weight : None, string or function, optional (default = None)
        If None, every edge has weight/distance/cost 1.
        If a string, use this edge attribute as the edge weight.
        Any edge attribute not present defaults to 1.
        If this is a function, the weight of an edge is the value
        returned by the function. The function must accept exactly
        three positional arguments: the two endpoints of an edge and
        the dictionary of edge attributes for that edge.
        The function must return a number.

    method : string, optional (default = 'dijkstra')
        The algorithm to use to compute the path length.
        Supported options: 'dijkstra', 'bellman-ford'.
        Other inputs produce a ValueError.
        If `weight` is None, unweighted graph methods are used, and this
        suggestion is ignored.

    Returns
    -------
    length: number or iterator
        If the source and target are both specified, return the length of
        the shortest path from the source to the target.

        If only the source is specified, return a dict keyed by target
        to the shortest path length from the source to that target.

        If only the target is specified, return a dict keyed by source
        to the shortest path length from that source to the target.

        If neither the source nor target are specified, return an iterator
        over (source, dictionary) where dictionary is keyed by target to
        shortest path length from source to that target.

    Raises
    ------
    NodeNotFound
        If `source` is not in `G`.

    NetworkXNoPath
        If no path exists between source and target.

    ValueError
        If `method` is not among the supported options.

    Examples
    --------
    >>> G = nx.path_graph(5)
    >>> nx.shortest_path_length(G, source=0, target=4)
    4
    >>> p = nx.shortest_path_length(G, source=0)  # target not specified
    >>> p[4]
    4
    >>> p = nx.shortest_path_length(G, target=4)  # source not specified
    >>> p[0]
    4
    >>> p = dict(nx.shortest_path_length(G))  # source,target not specified
    >>> p[0][4]
    4

    Notes
    -----
    The length of the path is always 1 less than the number of nodes involved
    in the path since the length measures the number of edges followed.

    For digraphs this returns the shortest directed path length. To find path
    lengths in the reverse direction use G.reverse(copy=False) first to flip
    the edge orientation.

    See Also
    --------
    all_pairs_shortest_path_length
    all_pairs_dijkstra_path_length
    all_pairs_bellman_ford_path_length
    single_source_shortest_path_length
    single_source_dijkstra_path_length
    single_source_bellman_ford_path_length
    """
    ...
@_dispatchable
def average_shortest_path_length(
    G: Graph[_Node], weight: str | Callable[..., Incomplete] | None = None, method: str | None = None
):
    r"""
    Returns the average shortest path length.

    The average shortest path length is

    .. math::

       a =\sum_{\substack{s,t \in V \\ s\neq t}} \frac{d(s, t)}{n(n-1)}

    where `V` is the set of nodes in `G`,
    `d(s, t)` is the shortest path from `s` to `t`,
    and `n` is the number of nodes in `G`.

    .. versionchanged:: 3.0
       An exception is raised for directed graphs that are not strongly
       connected.

    Parameters
    ----------
    G : NetworkX graph

    weight : None, string or function, optional (default = None)
        If None, every edge has weight/distance/cost 1.
        If a string, use this edge attribute as the edge weight.
        Any edge attribute not present defaults to 1.
        If this is a function, the weight of an edge is the value
        returned by the function. The function must accept exactly
        three positional arguments: the two endpoints of an edge and
        the dictionary of edge attributes for that edge.
        The function must return a number.

    method : string, optional (default = 'unweighted' or 'dijkstra')
        The algorithm to use to compute the path lengths.
        Supported options are 'unweighted', 'dijkstra', 'bellman-ford',
        'floyd-warshall' and 'floyd-warshall-numpy'.
        Other method values produce a ValueError.
        The default method is 'unweighted' if `weight` is None,
        otherwise the default method is 'dijkstra'.

    Raises
    ------
    NetworkXPointlessConcept
        If `G` is the null graph (that is, the graph on zero nodes).

    NetworkXError
        If `G` is not connected (or not strongly connected, in the case
        of a directed graph).

    ValueError
        If `method` is not among the supported options.

    Examples
    --------
    >>> G = nx.path_graph(5)
    >>> nx.average_shortest_path_length(G)
    2.0

    For disconnected graphs, you can compute the average shortest path
    length for each component

    >>> G = nx.Graph([(1, 2), (3, 4)])
    >>> for C in (G.subgraph(c).copy() for c in nx.connected_components(G)):
    ...     print(nx.average_shortest_path_length(C))
    1.0
    1.0
    """
    ...
@_dispatchable
def all_shortest_paths(
    G: Graph[_Node],
    source: _Node,
    target: _Node,
    weight: str | Callable[..., Incomplete] | None = None,
    method: str | None = "dijkstra",
) -> Generator[list[_Node], None, None]:
    """
    Compute all shortest simple paths in the graph.

    Parameters
    ----------
    G : NetworkX graph

    source : node
       Starting node for path.

    target : node
       Ending node for path.

    weight : None, string or function, optional (default = None)
        If None, every edge has weight/distance/cost 1.
        If a string, use this edge attribute as the edge weight.
        Any edge attribute not present defaults to 1.
        If this is a function, the weight of an edge is the value
        returned by the function. The function must accept exactly
        three positional arguments: the two endpoints of an edge and
        the dictionary of edge attributes for that edge.
        The function must return a number.

    method : string, optional (default = 'dijkstra')
       The algorithm to use to compute the path lengths.
       Supported options: 'dijkstra', 'bellman-ford'.
       Other inputs produce a ValueError.
       If `weight` is None, unweighted graph methods are used, and this
       suggestion is ignored.

    Returns
    -------
    paths : generator of lists
        A generator of all paths between source and target.

    Raises
    ------
    ValueError
        If `method` is not among the supported options.

    NetworkXNoPath
        If `target` cannot be reached from `source`.

    Examples
    --------
    >>> G = nx.Graph()
    >>> nx.add_path(G, [0, 1, 2])
    >>> nx.add_path(G, [0, 10, 2])
    >>> print([p for p in nx.all_shortest_paths(G, source=0, target=2)])
    [[0, 1, 2], [0, 10, 2]]

    Notes
    -----
    There may be many shortest paths between the source and target.  If G
    contains zero-weight cycles, this function will not produce all shortest
    paths because doing so would produce infinitely many paths of unbounded
    length -- instead, we only produce the shortest simple paths.

    See Also
    --------
    shortest_path
    single_source_shortest_path
    all_pairs_shortest_path
    """
    ...
@_dispatchable
def single_source_all_shortest_paths(
    G, source, weight=None, method="dijkstra"
) -> Generator[tuple[Incomplete, list[list[Incomplete]]]]:
    """
    Compute all shortest simple paths from the given source in the graph.

    Parameters
    ----------
    G : NetworkX graph

    source : node
       Starting node for path.

    weight : None, string or function, optional (default = None)
        If None, every edge has weight/distance/cost 1.
        If a string, use this edge attribute as the edge weight.
        Any edge attribute not present defaults to 1.
        If this is a function, the weight of an edge is the value
        returned by the function. The function must accept exactly
        three positional arguments: the two endpoints of an edge and
        the dictionary of edge attributes for that edge.
        The function must return a number.

    method : string, optional (default = 'dijkstra')
       The algorithm to use to compute the path lengths.
       Supported options: 'dijkstra', 'bellman-ford'.
       Other inputs produce a ValueError.
       If `weight` is None, unweighted graph methods are used, and this
       suggestion is ignored.

    Returns
    -------
    paths : generator of dictionary
        A generator of all paths between source and all nodes in the graph.

    Raises
    ------
    ValueError
        If `method` is not among the supported options.

    Examples
    --------
    >>> G = nx.Graph()
    >>> nx.add_path(G, [0, 1, 2, 3, 0])
    >>> dict(nx.single_source_all_shortest_paths(G, source=0))
    {0: [[0]], 1: [[0, 1]], 3: [[0, 3]], 2: [[0, 1, 2], [0, 3, 2]]}

    Notes
    -----
    There may be many shortest paths between the source and target.  If G
    contains zero-weight cycles, this function will not produce all shortest
    paths because doing so would produce infinitely many paths of unbounded
    length -- instead, we only produce the shortest simple paths.

    See Also
    --------
    shortest_path
    all_shortest_paths
    single_source_shortest_path
    all_pairs_shortest_path
    all_pairs_all_shortest_paths
    """
    ...
@_dispatchable
def all_pairs_all_shortest_paths(
    G, weight=None, method="dijkstra"
) -> Generator[tuple[Incomplete, dict[Incomplete, Incomplete]]]:
    """
    Compute all shortest paths between all nodes.

    Parameters
    ----------
    G : NetworkX graph

    weight : None, string or function, optional (default = None)
        If None, every edge has weight/distance/cost 1.
        If a string, use this edge attribute as the edge weight.
        Any edge attribute not present defaults to 1.
        If this is a function, the weight of an edge is the value
        returned by the function. The function must accept exactly
        three positional arguments: the two endpoints of an edge and
        the dictionary of edge attributes for that edge.
        The function must return a number.

    method : string, optional (default = 'dijkstra')
       The algorithm to use to compute the path lengths.
       Supported options: 'dijkstra', 'bellman-ford'.
       Other inputs produce a ValueError.
       If `weight` is None, unweighted graph methods are used, and this
       suggestion is ignored.

    Returns
    -------
    paths : generator of dictionary
        Dictionary of arrays, keyed by source and target, of all shortest paths.

    Raises
    ------
    ValueError
        If `method` is not among the supported options.

    Examples
    --------
    >>> G = nx.cycle_graph(4)
    >>> dict(nx.all_pairs_all_shortest_paths(G))[0][2]
    [[0, 1, 2], [0, 3, 2]]
    >>> dict(nx.all_pairs_all_shortest_paths(G))[0][3]
    [[0, 3]]

    Notes
    -----
    There may be multiple shortest paths with equal lengths. Unlike
    all_pairs_shortest_path, this method returns all shortest paths.

    See Also
    --------
    all_pairs_shortest_path
    single_source_all_shortest_paths
    """
    ...
