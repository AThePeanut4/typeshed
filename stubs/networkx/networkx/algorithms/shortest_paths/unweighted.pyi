"""Shortest path algorithms for unweighted graphs."""

from _typeshed import Incomplete
from collections.abc import Generator

from networkx.utils.backends import _dispatchable

@_dispatchable
def single_source_shortest_path_length(G, source, cutoff: Incomplete | None = None):
    """
    Compute the shortest path lengths from source to all reachable nodes.

    Parameters
    ----------
    G : NetworkX graph

    source : node
       Starting node for path

    cutoff : integer, optional
        Depth to stop the search. Only paths of length <= cutoff are returned.

    Returns
    -------
    lengths : dict
        Dict keyed by node to shortest path length to source.

    Examples
    --------
    >>> G = nx.path_graph(5)
    >>> length = nx.single_source_shortest_path_length(G, 0)
    >>> length[4]
    4
    >>> for node in length:
    ...     print(f"{node}: {length[node]}")
    0: 0
    1: 1
    2: 2
    3: 3
    4: 4

    See Also
    --------
    shortest_path_length
    """
    ...
@_dispatchable
def single_target_shortest_path_length(G, target, cutoff: Incomplete | None = None):
    """
    Compute the shortest path lengths to target from all reachable nodes.

    Parameters
    ----------
    G : NetworkX graph

    target : node
       Target node for path

    cutoff : integer, optional
        Depth to stop the search. Only paths of length <= cutoff are returned.

    Returns
    -------
    lengths : iterator
        (source, shortest path length) iterator

    Examples
    --------
    >>> G = nx.path_graph(5, create_using=nx.DiGraph())
    >>> length = dict(nx.single_target_shortest_path_length(G, 4))
    >>> length[0]
    4
    >>> for node in range(5):
    ...     print(f"{node}: {length[node]}")
    0: 4
    1: 3
    2: 2
    3: 1
    4: 0

    See Also
    --------
    single_source_shortest_path_length, shortest_path_length
    """
    ...
@_dispatchable
def all_pairs_shortest_path_length(G, cutoff: Incomplete | None = None) -> Generator[Incomplete, None, None]:
    """
    Computes the shortest path lengths between all nodes in `G`.

    Parameters
    ----------
    G : NetworkX graph

    cutoff : integer, optional
        Depth at which to stop the search. Only paths of length at most
        `cutoff` are returned.

    Returns
    -------
    lengths : iterator
        (source, dictionary) iterator with dictionary keyed by target and
        shortest path length as the key value.

    Notes
    -----
    The iterator returned only has reachable node pairs.

    Examples
    --------
    >>> G = nx.path_graph(5)
    >>> length = dict(nx.all_pairs_shortest_path_length(G))
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
    """
    ...
@_dispatchable
def bidirectional_shortest_path(G, source, target):
    """
    Returns a list of nodes in a shortest path between source and target.

    Parameters
    ----------
    G : NetworkX graph

    source : node label
       starting node for path

    target : node label
       ending node for path

    Returns
    -------
    path: list
       List of nodes in a path from source to target.

    Raises
    ------
    NetworkXNoPath
       If no path exists between source and target.

    Examples
    --------
    >>> G = nx.Graph()
    >>> nx.add_path(G, [0, 1, 2, 3, 0, 4, 5, 6, 7, 4])
    >>> nx.bidirectional_shortest_path(G, 2, 6)
    [2, 1, 0, 4, 5, 6]

    See Also
    --------
    shortest_path

    Notes
    -----
    This algorithm is used by shortest_path(G, source, target).
    """
    ...
@_dispatchable
def single_source_shortest_path(G, source, cutoff: Incomplete | None = None):
    """
    Compute shortest path between source
    and all other nodes reachable from source.

    Parameters
    ----------
    G : NetworkX graph

    source : node label
       Starting node for path

    cutoff : integer, optional
        Depth to stop the search. Only paths of length <= cutoff are returned.

    Returns
    -------
    paths : dictionary
        Dictionary, keyed by target, of shortest paths.

    Examples
    --------
    >>> G = nx.path_graph(5)
    >>> path = nx.single_source_shortest_path(G, 0)
    >>> path[4]
    [0, 1, 2, 3, 4]

    Notes
    -----
    The shortest path is not necessarily unique. So there can be multiple
    paths between the source and each target node, all of which have the
    same 'shortest' length. For each target node, this function returns
    only one of those paths.

    See Also
    --------
    shortest_path
    """
    ...
@_dispatchable
def single_target_shortest_path(G, target, cutoff: Incomplete | None = None):
    """
    Compute shortest path to target from all nodes that reach target.

    Parameters
    ----------
    G : NetworkX graph

    target : node label
       Target node for path

    cutoff : integer, optional
        Depth to stop the search. Only paths of length <= cutoff are returned.

    Returns
    -------
    paths : dictionary
        Dictionary, keyed by target, of shortest paths.

    Examples
    --------
    >>> G = nx.path_graph(5, create_using=nx.DiGraph())
    >>> path = nx.single_target_shortest_path(G, 4)
    >>> path[0]
    [0, 1, 2, 3, 4]

    Notes
    -----
    The shortest path is not necessarily unique. So there can be multiple
    paths between the source and each target node, all of which have the
    same 'shortest' length. For each target node, this function returns
    only one of those paths.

    See Also
    --------
    shortest_path, single_source_shortest_path
    """
    ...
@_dispatchable
def all_pairs_shortest_path(G, cutoff: Incomplete | None = None) -> Generator[Incomplete, None, None]:
    """
    Compute shortest paths between all nodes.

    Parameters
    ----------
    G : NetworkX graph

    cutoff : integer, optional
        Depth at which to stop the search. Only paths of length at most
        `cutoff` are returned.

    Returns
    -------
    paths : iterator
        Dictionary, keyed by source and target, of shortest paths.

    Examples
    --------
    >>> G = nx.path_graph(5)
    >>> path = dict(nx.all_pairs_shortest_path(G))
    >>> print(path[0][4])
    [0, 1, 2, 3, 4]

    Notes
    -----
    There may be multiple shortest paths with the same length between
    two nodes. For each pair, this function returns only one of those paths.

    See Also
    --------
    floyd_warshall
    all_pairs_all_shortest_paths
    """
    ...
@_dispatchable
def predecessor(
    G, source, target: Incomplete | None = None, cutoff: Incomplete | None = None, return_seen: Incomplete | None = None
):
    """
    Returns dict of predecessors for the path from source to all nodes in G.

    Parameters
    ----------
    G : NetworkX graph

    source : node label
       Starting node for path

    target : node label, optional
       Ending node for path. If provided only predecessors between
       source and target are returned

    cutoff : integer, optional
        Depth to stop the search. Only paths of length <= cutoff are returned.

    return_seen : bool, optional (default=None)
        Whether to return a dictionary, keyed by node, of the level (number of
        hops) to reach the node (as seen during breadth-first-search).

    Returns
    -------
    pred : dictionary
        Dictionary, keyed by node, of predecessors in the shortest path.


    (pred, seen): tuple of dictionaries
        If `return_seen` argument is set to `True`, then a tuple of dictionaries
        is returned. The first element is the dictionary, keyed by node, of
        predecessors in the shortest path. The second element is the dictionary,
        keyed by node, of the level (number of hops) to reach the node (as seen
        during breadth-first-search).

    Examples
    --------
    >>> G = nx.path_graph(4)
    >>> list(G)
    [0, 1, 2, 3]
    >>> nx.predecessor(G, 0)
    {0: [], 1: [0], 2: [1], 3: [2]}
    >>> nx.predecessor(G, 0, return_seen=True)
    ({0: [], 1: [0], 2: [1], 3: [2]}, {0: 0, 1: 1, 2: 2, 3: 3})
    """
    ...
