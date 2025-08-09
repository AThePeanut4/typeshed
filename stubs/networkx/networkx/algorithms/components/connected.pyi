from collections.abc import Generator

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["number_connected_components", "connected_components", "is_connected", "node_connected_component"]

@_dispatchable
def connected_components(G: Graph[_Node]) -> Generator[set[_Node]]: ...
@_dispatchable
def number_connected_components(G: Graph[_Node]) -> int: ...
@_dispatchable
def is_connected(G: Graph[_Node]) -> bool:
    """
    Returns True if the graph is connected, False otherwise.

    Parameters
    ----------
    G : NetworkX Graph
       An undirected graph.

    Returns
    -------
    connected : bool
      True if the graph is connected, false otherwise.

    Raises
    ------
    NetworkXNotImplemented
        If G is directed.

    Examples
    --------
    >>> G = nx.path_graph(4)
    >>> print(nx.is_connected(G))
    True

    See Also
    --------
    is_strongly_connected
    is_weakly_connected
    is_semiconnected
    is_biconnected
    connected_components

    Notes
    -----
    For undirected graphs only.
    """
    ...
@_dispatchable
def node_connected_component(G: Graph[_Node], n: _Node) -> set[_Node]: ...
