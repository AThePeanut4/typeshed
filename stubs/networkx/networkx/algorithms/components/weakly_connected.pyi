from collections.abc import Generator

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def weakly_connected_components(G: Graph[_Node]) -> Generator[set[_Node], None, None]:
    """
    Generate weakly connected components of G.

    Parameters
    ----------
    G : NetworkX graph
        A directed graph

    Returns
    -------
    comp : generator of sets
        A generator of sets of nodes, one for each weakly connected
        component of G.

    Raises
    ------
    NetworkXNotImplemented
        If G is undirected.

    Examples
    --------
    Generate a sorted list of weakly connected components, largest first.

    >>> G = nx.path_graph(4, create_using=nx.DiGraph())
    >>> nx.add_path(G, [10, 11, 12])
    >>> [
    ...     len(c)
    ...     for c in sorted(nx.weakly_connected_components(G), key=len, reverse=True)
    ... ]
    [4, 3]

    If you only want the largest component, it's more efficient to
    use max instead of sort:

    >>> largest_cc = max(nx.weakly_connected_components(G), key=len)

    See Also
    --------
    connected_components
    strongly_connected_components

    Notes
    -----
    For directed graphs only.
    """
    ...
@_dispatchable
def number_weakly_connected_components(G: Graph[_Node]) -> int: ...
@_dispatchable
def is_weakly_connected(G: Graph[_Node]) -> bool: ...
