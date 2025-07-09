"""Floyd-Warshall algorithm for shortest paths."""

from _typeshed import Incomplete, SupportsGetItem
from collections import defaultdict
from collections.abc import Collection

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["floyd_warshall", "floyd_warshall_predecessor_and_distance", "reconstruct_path", "floyd_warshall_numpy"]

@_dispatchable
def floyd_warshall_numpy(G: Graph[_Node], nodelist: Collection[_Node] | None = None, weight: str | None = "weight"):
    """
    Find all-pairs shortest path lengths using Floyd's algorithm.

    This algorithm for finding shortest paths takes advantage of
    matrix representations of a graph and works well for dense
    graphs where all-pairs shortest path lengths are desired.
    The results are returned as a NumPy array, distance[i, j],
    where i and j are the indexes of two nodes in nodelist.
    The entry distance[i, j] is the distance along a shortest
    path from i to j. If no path exists the distance is Inf.

    Parameters
    ----------
    G : NetworkX graph

    nodelist : list, optional (default=G.nodes)
       The rows and columns are ordered by the nodes in nodelist.
       If nodelist is None then the ordering is produced by G.nodes.
       Nodelist should include all nodes in G.

    weight: string, optional (default='weight')
       Edge data key corresponding to the edge weight.

    Returns
    -------
    distance : 2D numpy.ndarray
        A numpy array of shortest path distances between nodes.
        If there is no path between two nodes the value is Inf.

    Examples
    --------
    >>> G = nx.DiGraph()
    >>> G.add_weighted_edges_from(
    ...     [(0, 1, 5), (1, 2, 2), (2, 3, -3), (1, 3, 10), (3, 2, 8)]
    ... )
    >>> nx.floyd_warshall_numpy(G)
    array([[ 0.,  5.,  7.,  4.],
           [inf,  0.,  2., -1.],
           [inf, inf,  0., -3.],
           [inf, inf,  8.,  0.]])

    Notes
    -----
    Floyd's algorithm is appropriate for finding shortest paths in
    dense graphs or graphs with negative weights when Dijkstra's
    algorithm fails. This algorithm can still fail if there are negative
    cycles. It has running time $O(n^3)$ with running space of $O(n^2)$.

    Raises
    ------
    NetworkXError
        If nodelist is not a list of the nodes in G.
    """
    ...
@_dispatchable
def floyd_warshall_predecessor_and_distance(
    G: Graph[_Node], weight: str | None = "weight"
) -> tuple[dict[Incomplete, dict[Incomplete, Incomplete]], dict[Incomplete, dict[Incomplete, float]]]: ...
@_dispatchable
def reconstruct_path(source: _Node, target: _Node, predecessors: SupportsGetItem[Incomplete, Incomplete]) -> list[Incomplete]: ...
@_dispatchable
def floyd_warshall(G: Graph[_Node], weight: str | None = "weight") -> dict[Incomplete, defaultdict[Incomplete, float]]: ...
