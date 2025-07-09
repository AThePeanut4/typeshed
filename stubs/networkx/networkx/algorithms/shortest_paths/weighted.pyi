"""Shortest path algorithms for weighted graphs."""

from _typeshed import Incomplete, SupportsGetItem
from collections.abc import Callable, Generator
from typing import Any

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = [
    "dijkstra_path",
    "dijkstra_path_length",
    "bidirectional_dijkstra",
    "single_source_dijkstra",
    "single_source_dijkstra_path",
    "single_source_dijkstra_path_length",
    "multi_source_dijkstra",
    "multi_source_dijkstra_path",
    "multi_source_dijkstra_path_length",
    "all_pairs_dijkstra",
    "all_pairs_dijkstra_path",
    "all_pairs_dijkstra_path_length",
    "dijkstra_predecessor_and_distance",
    "bellman_ford_path",
    "bellman_ford_path_length",
    "single_source_bellman_ford",
    "single_source_bellman_ford_path",
    "single_source_bellman_ford_path_length",
    "all_pairs_bellman_ford_path",
    "all_pairs_bellman_ford_path_length",
    "bellman_ford_predecessor_and_distance",
    "negative_edge_cycle",
    "find_negative_cycle",
    "goldberg_radzik",
    "johnson",
]

@_dispatchable
def dijkstra_path(
    G: Graph[_Node],
    source: _Node,
    target: _Node,
    weight: str | Callable[[Any, Any, SupportsGetItem[str, Any]], float | None] | None = "weight",
) -> dict[Incomplete, list[Incomplete]] | list[Incomplete]: ...
@_dispatchable
def dijkstra_path_length(
    G: Graph[_Node],
    source: _Node,
    target: _Node,
    weight: str | Callable[[Any, Any, SupportsGetItem[str, Any]], float | None] | None = "weight",
):
    """
    Returns the shortest weighted path length in G from source to target.

    Uses Dijkstra's Method to compute the shortest weighted path length
    between two nodes in a graph.

    Parameters
    ----------
    G : NetworkX graph

    source : node label
        starting node for path

    target : node label
        ending node for path

    weight : string or function
        If this is a string, then edge weights will be accessed via the
        edge attribute with this key (that is, the weight of the edge
        joining `u` to `v` will be ``G.edges[u, v][weight]``). If no
        such edge attribute exists, the weight of the edge is assumed to
        be one.

        If this is a function, the weight of an edge is the value
        returned by the function. The function must accept exactly three
        positional arguments: the two endpoints of an edge and the
        dictionary of edge attributes for that edge. The function must
        return a number or None to indicate a hidden edge.

    Returns
    -------
    length : number
        Shortest path length.

    Raises
    ------
    NodeNotFound
        If `source` is not in `G`.

    NetworkXNoPath
        If no path exists between source and target.

    Examples
    --------
    >>> G = nx.path_graph(5)
    >>> nx.dijkstra_path_length(G, 0, 4)
    4

    Notes
    -----
    Edge weight attributes must be numerical.
    Distances are calculated as sums of weighted edges traversed.

    The weight function can be used to hide edges by returning None.
    So ``weight = lambda u, v, d: 1 if d['color']=="red" else None``
    will find the shortest red path.

    The function :func:`single_source_dijkstra` computes both
    path and length-of-path if you need both, use that.

    See Also
    --------
    bidirectional_dijkstra
    bellman_ford_path_length
    single_source_dijkstra
    """
    ...
@_dispatchable
def single_source_dijkstra_path(
    G: Graph[_Node],
    source: _Node,
    cutoff: float | None = None,
    weight: str | Callable[[Any, Any, SupportsGetItem[str, Any]], float | None] | None = "weight",
) -> dict[Incomplete, list[Incomplete]] | list[Incomplete]: ...
@_dispatchable
def single_source_dijkstra_path_length(
    G: Graph[_Node],
    source: _Node,
    cutoff: float | None = None,
    weight: str | Callable[[Any, Any, SupportsGetItem[str, Any]], float | None] | None = "weight",
) -> dict[Incomplete, Incomplete]: ...
@_dispatchable
def single_source_dijkstra(
    G: Graph[_Node],
    source: _Node,
    target: _Node | None = None,
    cutoff: float | None = None,
    weight: str | Callable[[Any, Any, SupportsGetItem[str, Any]], float | None] | None = "weight",
) -> tuple[Incomplete, Incomplete]: ...
@_dispatchable
def multi_source_dijkstra_path(
    G: Graph[_Node],
    sources,
    cutoff: float | None = None,
    weight: str | Callable[[Any, Any, SupportsGetItem[str, Any]], float | None] | None = "weight",
) -> dict[Incomplete, list[Incomplete]] | list[Incomplete]: ...
@_dispatchable
def multi_source_dijkstra_path_length(
    G: Graph[_Node],
    sources,
    cutoff: float | None = None,
    weight: str | Callable[[Any, Any, SupportsGetItem[str, Any]], float | None] | None = "weight",
) -> dict[Incomplete, Incomplete]: ...
@_dispatchable
def multi_source_dijkstra(
    G: Graph[_Node],
    sources,
    target: _Node | None = None,
    cutoff: float | None = None,
    weight: str | Callable[[Any, Any, SupportsGetItem[str, Any]], float | None] | None = "weight",
) -> tuple[Incomplete, Incomplete]: ...
@_dispatchable
def dijkstra_predecessor_and_distance(
    G: Graph[_Node],
    source: _Node,
    cutoff: float | None = None,
    weight: str | Callable[[Any, Any, SupportsGetItem[str, Any]], float | None] | None = "weight",
) -> tuple[dict[Incomplete, list[Incomplete]], dict[Incomplete, Incomplete]]: ...
@_dispatchable
def all_pairs_dijkstra(
    G: Graph[_Node],
    cutoff: float | None = None,
    weight: str | Callable[[Any, Any, SupportsGetItem[str, Any]], float | None] | None = "weight",
) -> Generator[Incomplete, None, None]:
    """
    Find shortest weighted paths and lengths between all nodes.

    Parameters
    ----------
    G : NetworkX graph

    cutoff : integer or float, optional
        Length (sum of edge weights) at which the search is stopped.
        If cutoff is provided, only return paths with summed weight <= cutoff.

    weight : string or function
        If this is a string, then edge weights will be accessed via the
        edge attribute with this key (that is, the weight of the edge
        joining `u` to `v` will be ``G.edge[u][v][weight]``). If no
        such edge attribute exists, the weight of the edge is assumed to
        be one.

        If this is a function, the weight of an edge is the value
        returned by the function. The function must accept exactly three
        positional arguments: the two endpoints of an edge and the
        dictionary of edge attributes for that edge. The function must
        return a number or None to indicate a hidden edge.

    Yields
    ------
    (node, (distance, path)) : (node obj, (dict, dict))
        Each source node has two associated dicts. The first holds distance
        keyed by target and the second holds paths keyed by target.
        (See single_source_dijkstra for the source/target node terminology.)
        If desired you can apply `dict()` to this function to create a dict
        keyed by source node to the two dicts.

    Examples
    --------
    >>> G = nx.path_graph(5)
    >>> len_path = dict(nx.all_pairs_dijkstra(G))
    >>> len_path[3][0][1]
    2
    >>> for node in [0, 1, 2, 3, 4]:
    ...     print(f"3 - {node}: {len_path[3][0][node]}")
    3 - 0: 3
    3 - 1: 2
    3 - 2: 1
    3 - 3: 0
    3 - 4: 1
    >>> len_path[3][1][1]
    [3, 2, 1]
    >>> for n, (dist, path) in nx.all_pairs_dijkstra(G):
    ...     print(path[1])
    [0, 1]
    [1]
    [2, 1]
    [3, 2, 1]
    [4, 3, 2, 1]

    Notes
    -----
    Edge weight attributes must be numerical.
    Distances are calculated as sums of weighted edges traversed.

    The yielded dicts only have keys for reachable nodes.
    """
    ...
@_dispatchable
def all_pairs_dijkstra_path_length(
    G: Graph[_Node],
    cutoff: float | None = None,
    weight: str | Callable[[Any, Any, SupportsGetItem[str, Any]], float | None] | None = "weight",
) -> Generator[Incomplete, None, None]:
    """
    Compute shortest path lengths between all nodes in a weighted graph.

    Parameters
    ----------
    G : NetworkX graph

    cutoff : integer or float, optional
        Length (sum of edge weights) at which the search is stopped.
        If cutoff is provided, only return paths with summed weight <= cutoff.

    weight : string or function
        If this is a string, then edge weights will be accessed via the
        edge attribute with this key (that is, the weight of the edge
        joining `u` to `v` will be ``G.edges[u, v][weight]``). If no
        such edge attribute exists, the weight of the edge is assumed to
        be one.

        If this is a function, the weight of an edge is the value
        returned by the function. The function must accept exactly three
        positional arguments: the two endpoints of an edge and the
        dictionary of edge attributes for that edge. The function must
        return a number or None to indicate a hidden edge.

    Returns
    -------
    distance : iterator
        (source, dictionary) iterator with dictionary keyed by target and
        shortest path length as the key value.

    Examples
    --------
    >>> G = nx.path_graph(5)
    >>> length = dict(nx.all_pairs_dijkstra_path_length(G))
    >>> for node in [0, 1, 2, 3, 4]:
    ...     print(f"1 - {node}: {length[1][node]}")
    1 - 0: 1
    1 - 1: 0
    1 - 2: 1
    1 - 3: 2
    1 - 4: 3
    >>> length[3][2]
    1
    >>> length[2][2]
    0

    Notes
    -----
    Edge weight attributes must be numerical.
    Distances are calculated as sums of weighted edges traversed.

    The dictionary returned only has keys for reachable node pairs.
    """
    ...
@_dispatchable
def all_pairs_dijkstra_path(
    G: Graph[_Node],
    cutoff: float | None = None,
    weight: str | Callable[[Any, Any, SupportsGetItem[str, Any]], float | None] | None = "weight",
) -> Generator[tuple[Incomplete, Incomplete], None, None]: ...
@_dispatchable
def bellman_ford_predecessor_and_distance(
    G: Graph[_Node],
    source: _Node,
    target: _Node | None = None,
    weight: str | Callable[[Any, Any, SupportsGetItem[str, Any]], float | None] | None = "weight",
    heuristic: bool = False,
) -> tuple[Incomplete, Incomplete]: ...
@_dispatchable
def bellman_ford_path(
    G: Graph[_Node],
    source: _Node,
    target: _Node,
    weight: str | Callable[[Any, Any, SupportsGetItem[str, Any]], float | None] | None = "weight",
) -> list[Incomplete] | dict[Incomplete, list[Incomplete]]: ...
@_dispatchable
def bellman_ford_path_length(
    G: Graph[_Node],
    source: _Node,
    target: _Node,
    weight: str | Callable[[Any, Any, SupportsGetItem[str, Any]], float | None] | None = "weight",
):
    """
    Returns the shortest path length from source to target
    in a weighted graph.

    Parameters
    ----------
    G : NetworkX graph

    source : node label
        starting node for path

    target : node label
        ending node for path

    weight : string or function (default="weight")
        If this is a string, then edge weights will be accessed via the
        edge attribute with this key (that is, the weight of the edge
        joining `u` to `v` will be ``G.edges[u, v][weight]``). If no
        such edge attribute exists, the weight of the edge is assumed to
        be one.

        If this is a function, the weight of an edge is the value
        returned by the function. The function must accept exactly three
        positional arguments: the two endpoints of an edge and the
        dictionary of edge attributes for that edge. The function must
        return a number.

    Returns
    -------
    length : number
        Shortest path length.

    Raises
    ------
    NodeNotFound
        If `source` is not in `G`.

    NetworkXNoPath
        If no path exists between source and target.

    Examples
    --------
    >>> G = nx.path_graph(5)
    >>> nx.bellman_ford_path_length(G, 0, 4)
    4

    Notes
    -----
    Edge weight attributes must be numerical.
    Distances are calculated as sums of weighted edges traversed.

    See Also
    --------
    dijkstra_path_length, bellman_ford_path
    """
    ...
@_dispatchable
def single_source_bellman_ford_path(
    G: Graph[_Node], source: _Node, weight: str | Callable[[Any, Any, SupportsGetItem[str, Any]], float | None] | None = "weight"
) -> list[Incomplete] | dict[Incomplete, list[Incomplete]]: ...
@_dispatchable
def single_source_bellman_ford_path_length(
    G: Graph[_Node], source: _Node, weight: str | Callable[[Any, Any, SupportsGetItem[str, Any]], float | None] | None = "weight"
) -> dict[Incomplete, int]: ...
@_dispatchable
def single_source_bellman_ford(
    G: Graph[_Node],
    source: _Node,
    target: _Node | None = None,
    weight: str | Callable[[Any, Any, SupportsGetItem[str, Any]], float | None] | None = "weight",
):
    """
    Compute shortest paths and lengths in a weighted graph G.

    Uses Bellman-Ford algorithm for shortest paths.

    Parameters
    ----------
    G : NetworkX graph

    source : node label
        Starting node for path

    target : node label, optional
        Ending node for path

    weight : string or function
        If this is a string, then edge weights will be accessed via the
        edge attribute with this key (that is, the weight of the edge
        joining `u` to `v` will be ``G.edges[u, v][weight]``). If no
        such edge attribute exists, the weight of the edge is assumed to
        be one.

        If this is a function, the weight of an edge is the value
        returned by the function. The function must accept exactly three
        positional arguments: the two endpoints of an edge and the
        dictionary of edge attributes for that edge. The function must
        return a number.

    Returns
    -------
    distance, path : pair of dictionaries, or numeric and list
        If target is None, returns a tuple of two dictionaries keyed by node.
        The first dictionary stores distance from one of the source nodes.
        The second stores the path from one of the sources to that node.
        If target is not None, returns a tuple of (distance, path) where
        distance is the distance from source to target and path is a list
        representing the path from source to target.

    Raises
    ------
    NodeNotFound
        If `source` is not in `G`.

    Examples
    --------
    >>> G = nx.path_graph(5)
    >>> length, path = nx.single_source_bellman_ford(G, 0)
    >>> length[4]
    4
    >>> for node in [0, 1, 2, 3, 4]:
    ...     print(f"{node}: {length[node]}")
    0: 0
    1: 1
    2: 2
    3: 3
    4: 4
    >>> path[4]
    [0, 1, 2, 3, 4]
    >>> length, path = nx.single_source_bellman_ford(G, 0, 1)
    >>> length
    1
    >>> path
    [0, 1]

    Notes
    -----
    Edge weight attributes must be numerical.
    Distances are calculated as sums of weighted edges traversed.

    See Also
    --------
    single_source_dijkstra
    single_source_bellman_ford_path
    single_source_bellman_ford_path_length
    """
    ...
@_dispatchable
def all_pairs_bellman_ford_path_length(
    G: Graph[_Node], weight: str | Callable[[Any, Any, SupportsGetItem[str, Any]], float | None] | None = "weight"
) -> Generator[Incomplete, None, None]:
    """
    Compute shortest path lengths between all nodes in a weighted graph.

    Parameters
    ----------
    G : NetworkX graph

    weight : string or function (default="weight")
        If this is a string, then edge weights will be accessed via the
        edge attribute with this key (that is, the weight of the edge
        joining `u` to `v` will be ``G.edges[u, v][weight]``). If no
        such edge attribute exists, the weight of the edge is assumed to
        be one.

        If this is a function, the weight of an edge is the value
        returned by the function. The function must accept exactly three
        positional arguments: the two endpoints of an edge and the
        dictionary of edge attributes for that edge. The function must
        return a number.

    Returns
    -------
    distance : iterator
        (source, dictionary) iterator with dictionary keyed by target and
        shortest path length as the key value.

    Examples
    --------
    >>> G = nx.path_graph(5)
    >>> length = dict(nx.all_pairs_bellman_ford_path_length(G))
    >>> for node in [0, 1, 2, 3, 4]:
    ...     print(f"1 - {node}: {length[1][node]}")
    1 - 0: 1
    1 - 1: 0
    1 - 2: 1
    1 - 3: 2
    1 - 4: 3
    >>> length[3][2]
    1
    >>> length[2][2]
    0

    Notes
    -----
    Edge weight attributes must be numerical.
    Distances are calculated as sums of weighted edges traversed.

    The dictionary returned only has keys for reachable node pairs.
    """
    ...
@_dispatchable
def all_pairs_bellman_ford_path(
    G: Graph[_Node], weight: str | Callable[[Any, Any, SupportsGetItem[str, Any]], float | None] | None = "weight"
) -> Generator[tuple[Incomplete, Incomplete], None, None]: ...
@_dispatchable
def goldberg_radzik(
    G: Graph[_Node], source: _Node, weight: str | Callable[[Any, Any, SupportsGetItem[str, Any]], float | None] | None = "weight"
) -> tuple[dict[Incomplete, None], dict[Incomplete, int | float]]: ...
@_dispatchable
def negative_edge_cycle(
    G: Graph[_Node],
    weight: str | Callable[[Any, Any, SupportsGetItem[str, Any]], float | None] | None = "weight",
    heuristic: bool = True,
):
    """
    Returns True if there exists a negative edge cycle anywhere in G.

    Parameters
    ----------
    G : NetworkX graph

    weight : string or function
        If this is a string, then edge weights will be accessed via the
        edge attribute with this key (that is, the weight of the edge
        joining `u` to `v` will be ``G.edges[u, v][weight]``). If no
        such edge attribute exists, the weight of the edge is assumed to
        be one.

        If this is a function, the weight of an edge is the value
        returned by the function. The function must accept exactly three
        positional arguments: the two endpoints of an edge and the
        dictionary of edge attributes for that edge. The function must
        return a number.

    heuristic : bool
        Determines whether to use a heuristic to early detect negative
        cycles at a negligible cost. In case of graphs with a negative cycle,
        the performance of detection increases by at least an order of magnitude.

    Returns
    -------
    negative_cycle : bool
        True if a negative edge cycle exists, otherwise False.

    Examples
    --------
    >>> G = nx.cycle_graph(5, create_using=nx.DiGraph())
    >>> print(nx.negative_edge_cycle(G))
    False
    >>> G[1][2]["weight"] = -7
    >>> print(nx.negative_edge_cycle(G))
    True

    Notes
    -----
    Edge weight attributes must be numerical.
    Distances are calculated as sums of weighted edges traversed.

    This algorithm uses bellman_ford_predecessor_and_distance() but finds
    negative cycles on any component by first adding a new node connected to
    every node, and starting bellman_ford_predecessor_and_distance on that
    node.  It then removes that extra node.
    """
    ...
@_dispatchable
def find_negative_cycle(
    G: Graph[_Node], source: _Node, weight: str | Callable[[Any, Any, SupportsGetItem[str, Any]], float | None] | None = "weight"
):
    """
    Returns a cycle with negative total weight if it exists.

    Bellman-Ford is used to find shortest_paths. That algorithm
    stops if there exists a negative cycle. This algorithm
    picks up from there and returns the found negative cycle.

    The cycle consists of a list of nodes in the cycle order. The last
    node equals the first to make it a cycle.
    You can look up the edge weights in the original graph. In the case
    of multigraphs the relevant edge is the minimal weight edge between
    the nodes in the 2-tuple.

    If the graph has no negative cycle, a NetworkXError is raised.

    Parameters
    ----------
    G : NetworkX graph

    source: node label
        The search for the negative cycle will start from this node.

    weight : string or function
        If this is a string, then edge weights will be accessed via the
        edge attribute with this key (that is, the weight of the edge
        joining `u` to `v` will be ``G.edges[u, v][weight]``). If no
        such edge attribute exists, the weight of the edge is assumed to
        be one.

        If this is a function, the weight of an edge is the value
        returned by the function. The function must accept exactly three
        positional arguments: the two endpoints of an edge and the
        dictionary of edge attributes for that edge. The function must
        return a number.

    Examples
    --------
    >>> G = nx.DiGraph()
    >>> G.add_weighted_edges_from(
    ...     [(0, 1, 2), (1, 2, 2), (2, 0, 1), (1, 4, 2), (4, 0, -5)]
    ... )
    >>> nx.find_negative_cycle(G, 0)
    [4, 0, 1, 4]

    Returns
    -------
    cycle : list
        A list of nodes in the order of the cycle found. The last node
        equals the first to indicate a cycle.

    Raises
    ------
    NetworkXError
        If no negative cycle is found.
    """
    ...
@_dispatchable
def bidirectional_dijkstra(
    G: Graph[_Node],
    source: _Node,
    target: _Node,
    weight: str | Callable[[Any, Any, SupportsGetItem[str, Any]], float | None] | None = "weight",
):
    r"""
    Dijkstra's algorithm for shortest paths using bidirectional search.

    Parameters
    ----------
    G : NetworkX graph

    source : node
        Starting node.

    target : node
        Ending node.

    weight : string or function
        If this is a string, then edge weights will be accessed via the
        edge attribute with this key (that is, the weight of the edge
        joining `u` to `v` will be ``G.edges[u, v][weight]``). If no
        such edge attribute exists, the weight of the edge is assumed to
        be one.

        If this is a function, the weight of an edge is the value
        returned by the function. The function must accept exactly three
        positional arguments: the two endpoints of an edge and the
        dictionary of edge attributes for that edge. The function must
        return a number or None to indicate a hidden edge.

    Returns
    -------
    length, path : number and list
        length is the distance from source to target.
        path is a list of nodes on a path from source to target.

    Raises
    ------
    NodeNotFound
        If `source` or `target` is not in `G`.

    NetworkXNoPath
        If no path exists between source and target.

    Examples
    --------
    >>> G = nx.path_graph(5)
    >>> length, path = nx.bidirectional_dijkstra(G, 0, 4)
    >>> print(length)
    4
    >>> print(path)
    [0, 1, 2, 3, 4]

    Notes
    -----
    Edge weight attributes must be numerical.
    Distances are calculated as sums of weighted edges traversed.

    The weight function can be used to hide edges by returning None.
    So ``weight = lambda u, v, d: 1 if d['color']=="red" else None``
    will find the shortest red path.

    In practice  bidirectional Dijkstra is much more than twice as fast as
    ordinary Dijkstra.

    Ordinary Dijkstra expands nodes in a sphere-like manner from the
    source. The radius of this sphere will eventually be the length
    of the shortest path. Bidirectional Dijkstra will expand nodes
    from both the source and the target, making two spheres of half
    this radius. Volume of the first sphere is `\pi*r*r` while the
    others are `2*\pi*r/2*r/2`, making up half the volume.

    This algorithm is not guaranteed to work if edge weights
    are negative or are floating point numbers
    (overflows and roundoff errors can cause problems).

    See Also
    --------
    shortest_path
    shortest_path_length
    """
    ...
@_dispatchable
def johnson(
    G: Graph[_Node], weight: str | Callable[[Any, Any, SupportsGetItem[str, Any]], float | None] | None = "weight"
) -> dict[Any, dict[Any, list[Any]]]: ...
