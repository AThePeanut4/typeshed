from _typeshed import Incomplete

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["load_centrality", "edge_load_centrality"]

@_dispatchable
def newman_betweenness_centrality(
    G: Graph[_Node], v=None, cutoff: bool | None = None, normalized: bool | None = True, weight: str | None = None
) -> float | dict[Incomplete, float]: ...

load_centrality = newman_betweenness_centrality

@_dispatchable
def edge_load_centrality(G: Graph[_Node], cutoff: bool | None = False):
    """
    Compute edge load.

    WARNING: This concept of edge load has not been analysed
    or discussed outside of NetworkX that we know of.
    It is based loosely on load_centrality in the sense that
    it counts the number of shortest paths which cross each edge.
    This function is for demonstration and testing purposes.

    Parameters
    ----------
    G : graph
        A networkx graph

    cutoff : bool, optional (default=False)
        If specified, only consider paths of length <= cutoff.

    Returns
    -------
    A dict keyed by edge 2-tuple to the number of shortest paths
    which use that edge. Where more than one path is shortest
    the count is divided equally among paths.
    """
    ...
