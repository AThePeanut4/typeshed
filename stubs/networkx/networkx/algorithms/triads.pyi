"""Functions for analyzing triads of a graph."""

from _typeshed import Incomplete
from collections.abc import Collection, Generator
from typing import Final

from networkx.classes.digraph import DiGraph
from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["triadic_census", "is_triad", "all_triads", "triads_by_type", "triad_type"]

TRICODES: Final[tuple[int, ...]]
TRIAD_NAMES: Final[tuple[str, ...]]
TRICODE_TO_NAME: Final[dict[int, str]]

@_dispatchable
def triadic_census(G: DiGraph[_Node], nodelist: Collection[_Node] | None = None):
    """
    Determines the triadic census of a directed graph.

    The triadic census is a count of how many of the 16 possible types of
    triads are present in a directed graph. If a list of nodes is passed, then
    only those triads are taken into account which have elements of nodelist in them.

    Parameters
    ----------
    G : digraph
       A NetworkX DiGraph
    nodelist : list
        List of nodes for which you want to calculate triadic census

    Returns
    -------
    census : dict
       Dictionary with triad type as keys and number of occurrences as values.

    Examples
    --------
    >>> G = nx.DiGraph([(1, 2), (2, 3), (3, 1), (3, 4), (4, 1), (4, 2)])
    >>> triadic_census = nx.triadic_census(G)
    >>> for key, value in triadic_census.items():
    ...     print(f"{key}: {value}")
    003: 0
    012: 0
    102: 0
    021D: 0
    021U: 0
    021C: 0
    111D: 0
    111U: 0
    030T: 2
    030C: 2
    201: 0
    120D: 0
    120U: 0
    120C: 0
    210: 0
    300: 0

    Notes
    -----
    This algorithm has complexity $O(m)$ where $m$ is the number of edges in
    the graph.

    For undirected graphs, the triadic census can be computed by first converting
    the graph into a directed graph using the ``G.to_directed()`` method.
    After this conversion, only the triad types 003, 102, 201 and 300 will be
    present in the undirected scenario.

    Raises
    ------
    ValueError
        If `nodelist` contains duplicate nodes or nodes not in `G`.
        If you want to ignore this you can preprocess with `set(nodelist) & G.nodes`

    See also
    --------
    triad_graph

    References
    ----------
    .. [1] Vladimir Batagelj and Andrej Mrvar, A subquadratic triad census
        algorithm for large sparse networks with small maximum degree,
        University of Ljubljana,
        http://vlado.fmf.uni-lj.si/pub/networks/doc/triads/triads.pdf
    """
    ...
@_dispatchable
def is_triad(G: Graph[_Node]) -> bool:
    """
    Returns True if the graph G is a triad, else False.

    Parameters
    ----------
    G : graph
       A NetworkX Graph

    Returns
    -------
    istriad : boolean
       Whether G is a valid triad

    Examples
    --------
    >>> G = nx.DiGraph([(1, 2), (2, 3), (3, 1)])
    >>> nx.is_triad(G)
    True
    >>> G.add_edge(0, 1)
    >>> nx.is_triad(G)
    False
    """
    ...
@_dispatchable
def all_triads(G: DiGraph[_Node]) -> Generator[Incomplete, None, None]: ...
@_dispatchable
def triads_by_type(G: DiGraph[_Node]):
    """
    Returns a list of all triads for each triad type in a directed graph.
    There are exactly 16 different types of triads possible. Suppose 1, 2, 3 are three
    nodes, they will be classified as a particular triad type if their connections
    are as follows:

    - 003: 1, 2, 3
    - 012: 1 -> 2, 3
    - 102: 1 <-> 2, 3
    - 021D: 1 <- 2 -> 3
    - 021U: 1 -> 2 <- 3
    - 021C: 1 -> 2 -> 3
    - 111D: 1 <-> 2 <- 3
    - 111U: 1 <-> 2 -> 3
    - 030T: 1 -> 2 -> 3, 1 -> 3
    - 030C: 1 <- 2 <- 3, 1 -> 3
    - 201: 1 <-> 2 <-> 3
    - 120D: 1 <- 2 -> 3, 1 <-> 3
    - 120U: 1 -> 2 <- 3, 1 <-> 3
    - 120C: 1 -> 2 -> 3, 1 <-> 3
    - 210: 1 -> 2 <-> 3, 1 <-> 3
    - 300: 1 <-> 2 <-> 3, 1 <-> 3

    Refer to the :doc:`example gallery </auto_examples/graph/plot_triad_types>`
    for visual examples of the triad types.

    Parameters
    ----------
    G : digraph
       A NetworkX DiGraph

    Returns
    -------
    tri_by_type : dict
       Dictionary with triad types as keys and lists of triads as values.

    Examples
    --------
    >>> G = nx.DiGraph([(1, 2), (1, 3), (2, 3), (3, 1), (5, 6), (5, 4), (6, 7)])
    >>> dict = nx.triads_by_type(G)
    >>> dict["120C"][0].edges()
    OutEdgeView([(1, 2), (1, 3), (2, 3), (3, 1)])
    >>> dict["012"][0].edges()
    OutEdgeView([(1, 2)])

    References
    ----------
    .. [1] Snijders, T. (2012). "Transitivity and triads." University of
        Oxford.
        https://web.archive.org/web/20170830032057/http://www.stats.ox.ac.uk/~snijders/Trans_Triads_ha.pdf
    """
    ...
@_dispatchable
def triad_type(G: DiGraph[_Node]): ...
