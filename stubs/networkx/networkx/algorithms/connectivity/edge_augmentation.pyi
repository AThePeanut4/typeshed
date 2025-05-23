from _typeshed import Incomplete, SupportsGetItem
from collections.abc import Generator
from typing import NamedTuple

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["k_edge_augmentation", "is_k_edge_connected", "is_locally_k_edge_connected"]

@_dispatchable
def is_k_edge_connected(G: Graph[_Node], k: int) -> bool:
    """
    Tests to see if a graph is k-edge-connected.

    Is it impossible to disconnect the graph by removing fewer than k edges?
    If so, then G is k-edge-connected.

    Parameters
    ----------
    G : NetworkX graph
       An undirected graph.

    k : integer
        edge connectivity to test for

    Returns
    -------
    boolean
        True if G is k-edge-connected.

    See Also
    --------
    :func:`is_locally_k_edge_connected`

    Examples
    --------
    >>> G = nx.barbell_graph(10, 0)
    >>> nx.is_k_edge_connected(G, k=1)
    True
    >>> nx.is_k_edge_connected(G, k=2)
    False
    """
    ...
@_dispatchable
def is_locally_k_edge_connected(G: Graph[_Node], s: _Node, t: _Node, k: int) -> bool:
    """
    Tests to see if an edge in a graph is locally k-edge-connected.

    Is it impossible to disconnect s and t by removing fewer than k edges?
    If so, then s and t are locally k-edge-connected in G.

    Parameters
    ----------
    G : NetworkX graph
       An undirected graph.

    s : node
        Source node

    t : node
        Target node

    k : integer
        local edge connectivity for nodes s and t

    Returns
    -------
    boolean
        True if s and t are locally k-edge-connected in G.

    See Also
    --------
    :func:`is_k_edge_connected`

    Examples
    --------
    >>> from networkx.algorithms.connectivity import is_locally_k_edge_connected
    >>> G = nx.barbell_graph(10, 0)
    >>> is_locally_k_edge_connected(G, 5, 15, k=1)
    True
    >>> is_locally_k_edge_connected(G, 5, 15, k=2)
    False
    >>> is_locally_k_edge_connected(G, 1, 5, k=2)
    True
    """
    ...
@_dispatchable
def k_edge_augmentation(
    G: Graph[_Node],
    k: int,
    avail: set[tuple[int, int]] | set[tuple[int, int, float]] | SupportsGetItem[tuple[int, int], float] | None = None,
    weight: str | None = None,
    partial: bool = False,
) -> Generator[tuple[_Node, _Node], None, None]: ...
@_dispatchable
def partial_k_edge_augmentation(G: Graph[_Node], k, avail, weight: str | None = None): ...
@_dispatchable
def one_edge_augmentation(G: Graph[_Node], avail=None, weight: str | None = None, partial: bool = False): ...
@_dispatchable
def bridge_augmentation(G: Graph[_Node], avail=None, weight: str | None = None): ...

class MetaEdge(NamedTuple):
    meta_uv: Incomplete
    uv: Incomplete
    w: Incomplete

@_dispatchable
def unconstrained_one_edge_augmentation(G: Graph[_Node]): ...
@_dispatchable
def weighted_one_edge_augmentation(G: Graph[_Node], avail, weight: str | None = None, partial: bool = False): ...
@_dispatchable
def unconstrained_bridge_augmentation(G: Graph[_Node]): ...
@_dispatchable
def weighted_bridge_augmentation(G: Graph[_Node], avail, weight: str | None = None): ...
@_dispatchable
def collapse(G: Graph[_Node], grouped_nodes): ...
@_dispatchable
def complement_edges(G: Graph[_Node]): ...
@_dispatchable
def greedy_k_edge_augmentation(G: Graph[_Node], k, avail=None, weight: str | None = None, seed=None): ...
