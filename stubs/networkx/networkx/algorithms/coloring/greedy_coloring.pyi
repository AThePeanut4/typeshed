from _typeshed import Incomplete, Unused
from collections.abc import Callable, Generator
from typing import Final

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = [
    "greedy_color",
    "strategy_connected_sequential",
    "strategy_connected_sequential_bfs",
    "strategy_connected_sequential_dfs",
    "strategy_independent_set",
    "strategy_largest_first",
    "strategy_random_sequential",
    "strategy_saturation_largest_first",
    "strategy_smallest_last",
]

@_dispatchable
def strategy_largest_first(G: Graph[_Node], colors: Unused): ...
@_dispatchable
def strategy_random_sequential(G: Graph[_Node], colors: Unused, seed=None): ...
@_dispatchable
def strategy_smallest_last(G: Graph[_Node], colors: Unused): ...
@_dispatchable
def strategy_independent_set(G: Graph[_Node], colors: Unused) -> Generator[Incomplete, Incomplete, None]: ...
@_dispatchable
def strategy_connected_sequential_bfs(G: Graph[_Node], colors): ...
@_dispatchable
def strategy_connected_sequential_dfs(G: Graph[_Node], colors): ...
@_dispatchable
def strategy_connected_sequential(
    G: Graph[_Node], colors: Unused, traversal: str = "bfs"
) -> Generator[Incomplete, None, None]: ...
@_dispatchable
def strategy_saturation_largest_first(G: Graph[_Node], colors) -> Generator[Incomplete, None, Incomplete]: ...

STRATEGIES: Final[dict[str, Callable[..., Incomplete]]]

@_dispatchable
def greedy_color(G: Graph[_Node], strategy="largest_first", interchange: bool = False):
    """
    Color a graph using various strategies of greedy graph coloring.

    Attempts to color a graph using as few colors as possible, where no
    neighbors of a node can have same color as the node itself. The
    given strategy determines the order in which nodes are colored.

    The strategies are described in [1]_, and smallest-last is based on
    [2]_.

    Parameters
    ----------
    G : NetworkX graph

    strategy : string or function(G, colors)
       A function (or a string representing a function) that provides
       the coloring strategy, by returning nodes in the ordering they
       should be colored. ``G`` is the graph, and ``colors`` is a
       dictionary of the currently assigned colors, keyed by nodes. The
       function must return an iterable over all the nodes in ``G``.

       If the strategy function is an iterator generator (that is, a
       function with ``yield`` statements), keep in mind that the
       ``colors`` dictionary will be updated after each ``yield``, since
       this function chooses colors greedily.

       If ``strategy`` is a string, it must be one of the following,
       each of which represents one of the built-in strategy functions.

       * ``'largest_first'``
       * ``'random_sequential'``
       * ``'smallest_last'``
       * ``'independent_set'``
       * ``'connected_sequential_bfs'``
       * ``'connected_sequential_dfs'``
       * ``'connected_sequential'`` (alias for the previous strategy)
       * ``'saturation_largest_first'``
       * ``'DSATUR'`` (alias for the previous strategy)

    interchange: bool
       Will use the color interchange algorithm described by [3]_ if set
       to ``True``.

       Note that ``saturation_largest_first`` and ``independent_set``
       do not work with interchange. Furthermore, if you use
       interchange with your own strategy function, you cannot rely
       on the values in the ``colors`` argument.

    Returns
    -------
    A dictionary with keys representing nodes and values representing
    corresponding coloring.

    Examples
    --------
    >>> G = nx.cycle_graph(4)
    >>> d = nx.coloring.greedy_color(G, strategy="largest_first")
    >>> d in [{0: 0, 1: 1, 2: 0, 3: 1}, {0: 1, 1: 0, 2: 1, 3: 0}]
    True

    Raises
    ------
    NetworkXPointlessConcept
        If ``strategy`` is ``saturation_largest_first`` or
        ``independent_set`` and ``interchange`` is ``True``.

    References
    ----------
    .. [1] Adrian Kosowski, and Krzysztof Manuszewski,
       Classical Coloring of Graphs, Graph Colorings, 2-19, 2004.
       ISBN 0-8218-3458-4.
    .. [2] David W. Matula, and Leland L. Beck, "Smallest-last
       ordering and clustering and graph coloring algorithms." *J. ACM* 30,
       3 (July 1983), 417–427. <https://doi.org/10.1145/2402.322385>
    .. [3] Maciej M. Sysło, Narsingh Deo, Janusz S. Kowalik,
       Discrete Optimization Algorithms with Pascal Programs, 415-424, 1983.
       ISBN 0-486-45353-7.
    """
    ...
