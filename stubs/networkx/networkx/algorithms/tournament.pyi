from _typeshed import Incomplete

from networkx.classes.digraph import DiGraph
from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable
from numpy.random import RandomState

__all__ = [
    "hamiltonian_path",
    "is_reachable",
    "is_strongly_connected",
    "is_tournament",
    "random_tournament",
    "score_sequence",
    "tournament_matrix",
]

@_dispatchable
def is_tournament(G: Graph[_Node]) -> bool:
    """
    Returns True if and only if `G` is a tournament.

    A tournament is a directed graph, with neither self-loops nor
    multi-edges, in which there is exactly one directed edge joining
    each pair of distinct nodes.

    Parameters
    ----------
    G : NetworkX graph
        A directed graph representing a tournament.

    Returns
    -------
    bool
        Whether the given graph is a tournament graph.

    Examples
    --------
    >>> G = nx.DiGraph([(0, 1), (1, 2), (2, 0)])
    >>> nx.is_tournament(G)
    True

    Notes
    -----
    Some definitions require a self-loop on each node, but that is not
    the convention used here.
    """
    ...
@_dispatchable
def hamiltonian_path(G: Graph[_Node]) -> list[Incomplete]: ...
@_dispatchable
def random_tournament(n: int, seed: int | RandomState | None = None) -> DiGraph[Incomplete]: ...
@_dispatchable
def tournament_matrix(G: Graph[_Node]):
    r"""
    Returns the tournament matrix for the given tournament graph.

    This function requires SciPy.

    The *tournament matrix* of a tournament graph with edge set *E* is
    the matrix *T* defined by

    .. math::

       T_{i j} =
       \begin{cases}
       +1 & \text{if } (i, j) \in E \\
       -1 & \text{if } (j, i) \in E \\
       0 & \text{if } i == j.
       \end{cases}

    An equivalent definition is `T = A - A^T`, where *A* is the
    adjacency matrix of the graph `G`.

    Parameters
    ----------
    G : NetworkX graph
        A directed graph representing a tournament.

    Returns
    -------
    SciPy sparse array
        The tournament matrix of the tournament graph `G`.

    Raises
    ------
    ImportError
        If SciPy is not available.
    """
    ...
@_dispatchable
def score_sequence(G: Graph[_Node]) -> list[Incomplete]: ...
@_dispatchable
def is_reachable(G: Graph[_Node], s: _Node, t: _Node) -> bool:
    """
    Decides whether there is a path from `s` to `t` in the
    tournament.

    This function is more theoretically efficient than the reachability
    checks than the shortest path algorithms in
    :mod:`networkx.algorithms.shortest_paths`.

    The given graph **must** be a tournament, otherwise this function's
    behavior is undefined.

    Parameters
    ----------
    G : NetworkX graph
        A directed graph representing a tournament.

    s : node
        A node in the graph.

    t : node
        A node in the graph.

    Returns
    -------
    bool
        Whether there is a path from `s` to `t` in `G`.

    Examples
    --------
    >>> G = nx.DiGraph([(1, 0), (1, 3), (1, 2), (2, 3), (2, 0), (3, 0)])
    >>> nx.is_tournament(G)
    True
    >>> nx.tournament.is_reachable(G, 1, 3)
    True
    >>> nx.tournament.is_reachable(G, 3, 2)
    False

    Notes
    -----
    Although this function is more theoretically efficient than the
    generic shortest path functions, a speedup requires the use of
    parallelism. Though it may in the future, the current implementation
    does not use parallelism, thus you may not see much of a speedup.

    This algorithm comes from [1].

    References
    ----------
    .. [1] Tantau, Till.
           "A note on the complexity of the reachability problem for
           tournaments."
           *Electronic Colloquium on Computational Complexity*. 2001.
           <http://eccc.hpi-web.de/report/2001/092/>
    """
    ...
@_dispatchable
def is_strongly_connected(G: Graph[_Node]) -> bool:
    """
    Decides whether the given tournament is strongly connected.

    This function is more theoretically efficient than the
    :func:`~networkx.algorithms.components.is_strongly_connected`
    function.

    The given graph **must** be a tournament, otherwise this function's
    behavior is undefined.

    Parameters
    ----------
    G : NetworkX graph
        A directed graph representing a tournament.

    Returns
    -------
    bool
        Whether the tournament is strongly connected.

    Examples
    --------
    >>> G = nx.DiGraph([(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 0)])
    >>> nx.is_tournament(G)
    True
    >>> nx.tournament.is_strongly_connected(G)
    True
    >>> G.remove_edge(3, 0)
    >>> G.add_edge(0, 3)
    >>> nx.is_tournament(G)
    True
    >>> nx.tournament.is_strongly_connected(G)
    False

    Notes
    -----
    Although this function is more theoretically efficient than the
    generic strong connectivity function, a speedup requires the use of
    parallelism. Though it may in the future, the current implementation
    does not use parallelism, thus you may not see much of a speedup.

    This algorithm comes from [1].

    References
    ----------
    .. [1] Tantau, Till.
           "A note on the complexity of the reachability problem for
           tournaments."
           *Electronic Colloquium on Computational Complexity*. 2001.
           <http://eccc.hpi-web.de/report/2001/092/>
    """
    ...
