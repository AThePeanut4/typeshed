"""Shortest path algorithms for unweighted graphs."""

from _typeshed import Incomplete
from collections.abc import Generator

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = [
    "bidirectional_shortest_path",
    "single_source_shortest_path",
    "single_source_shortest_path_length",
    "single_target_shortest_path",
    "single_target_shortest_path_length",
    "all_pairs_shortest_path",
    "all_pairs_shortest_path_length",
    "predecessor",
]

@_dispatchable
def single_source_shortest_path_length(G: Graph[_Node], source: _Node, cutoff: int | None = None) -> dict[Incomplete, int]: ...
@_dispatchable
def single_target_shortest_path_length(G: Graph[_Node], target: _Node, cutoff: int | None = None):
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
    lengths : dictionary
        Dictionary, keyed by source, of shortest path lengths.

    Examples
    --------
    >>> G = nx.path_graph(5, create_using=nx.DiGraph())
    >>> length = nx.single_target_shortest_path_length(G, 4)
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
def all_pairs_shortest_path_length(G: Graph[_Node], cutoff: int | None = None) -> Generator[Incomplete, None, None]:
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
def bidirectional_shortest_path(G: Graph[_Node], source: _Node, target: _Node) -> list[Incomplete]: ...
@_dispatchable
def single_source_shortest_path(
    G: Graph[_Node], source: _Node, cutoff: int | None = None
) -> dict[Incomplete, list[Incomplete]]: ...
@_dispatchable
def single_target_shortest_path(
    G: Graph[_Node], target: _Node, cutoff: int | None = None
) -> dict[Incomplete, list[Incomplete]]: ...
@_dispatchable
def all_pairs_shortest_path(
    G: Graph[_Node], cutoff: int | None = None
) -> Generator[tuple[Incomplete, dict[Incomplete, list[Incomplete]]]]: ...
@_dispatchable
def predecessor(
    G: Graph[_Node], source: _Node, target: _Node | None = None, cutoff: int | None = None, return_seen: bool | None = None
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
