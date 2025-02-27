from collections.abc import Generator

from networkx.classes.digraph import DiGraph
from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def strongly_connected_components(G: Graph[_Node]) -> Generator[set[_Node], None, None]:
    """
    Generate nodes in strongly connected components of graph.

    Parameters
    ----------
    G : NetworkX Graph
        A directed graph.

    Returns
    -------
    comp : generator of sets
        A generator of sets of nodes, one for each strongly connected
        component of G.

    Raises
    ------
    NetworkXNotImplemented
        If G is undirected.

    Examples
    --------
    Generate a sorted list of strongly connected components, largest first.

    >>> G = nx.cycle_graph(4, create_using=nx.DiGraph())
    >>> nx.add_cycle(G, [10, 11, 12])
    >>> [
    ...     len(c)
    ...     for c in sorted(nx.strongly_connected_components(G), key=len, reverse=True)
    ... ]
    [4, 3]

    If you only want the largest component, it's more efficient to
    use max instead of sort.

    >>> largest = max(nx.strongly_connected_components(G), key=len)

    See Also
    --------
    connected_components
    weakly_connected_components
    kosaraju_strongly_connected_components

    Notes
    -----
    Uses Tarjan's algorithm[1]_ with Nuutila's modifications[2]_.
    Nonrecursive version of algorithm.

    References
    ----------
    .. [1] Depth-first search and linear graph algorithms, R. Tarjan
       SIAM Journal of Computing 1(2):146-160, (1972).

    .. [2] On finding the strongly connected components in a directed graph.
       E. Nuutila and E. Soisalon-Soinen
       Information Processing Letters 49(1): 9-14, (1994)..
    """
    ...
@_dispatchable
def kosaraju_strongly_connected_components(G: Graph[_Node], source=None) -> Generator[set[_Node], None, None]: ...
@_dispatchable
def number_strongly_connected_components(G: Graph[_Node]) -> int: ...
@_dispatchable
def is_strongly_connected(G: Graph[_Node]) -> bool: ...
@_dispatchable
def condensation(G: DiGraph[_Node], scc=None) -> DiGraph[int]: ...
