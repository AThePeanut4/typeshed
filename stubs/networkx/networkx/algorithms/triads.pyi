"""Functions for analyzing triads of a graph."""

from _typeshed import Incomplete
from collections import defaultdict
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
def triadic_census(G: DiGraph[_Node], nodelist: Collection[_Node] | None = None) -> dict[str, int]: ...
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
def all_triads(G: DiGraph[_Node]) -> Generator[Incomplete, None, None]:
    """
    A generator of all possible triads in G.

    Parameters
    ----------
    G : digraph
       A NetworkX DiGraph

    Returns
    -------
    all_triads : generator of DiGraphs
       Generator of triads (order-3 DiGraphs)

    Examples
    --------
    >>> G = nx.DiGraph([(1, 2), (2, 3), (3, 1), (3, 4), (4, 1), (4, 2)])
    >>> for triad in nx.all_triads(G):
    ...     print(triad.edges)
    [(1, 2), (2, 3), (3, 1)]
    [(1, 2), (4, 1), (4, 2)]
    [(3, 1), (3, 4), (4, 1)]
    [(2, 3), (3, 4), (4, 2)]
    """
    ...
@_dispatchable
def triads_by_type(G: DiGraph[_Node]) -> defaultdict[Incomplete, list[Incomplete]]: ...
@_dispatchable
def triad_type(G: DiGraph[_Node]) -> str | None: ...
