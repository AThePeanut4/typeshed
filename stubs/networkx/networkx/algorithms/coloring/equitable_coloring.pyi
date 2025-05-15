"""Equitable coloring of graphs with bounded degree."""

from _typeshed import Incomplete, SupportsGetItem
from collections.abc import Mapping
from typing import SupportsIndex

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["equitable_color"]

@_dispatchable
def is_coloring(G: Graph[_Node], coloring: SupportsGetItem[Incomplete, Incomplete]) -> bool:
    """Determine if the coloring is a valid coloring for the graph G."""
    ...
@_dispatchable
def is_equitable(G: Graph[_Node], coloring: Mapping[Incomplete, Incomplete], num_colors: SupportsIndex | None = None) -> bool:
    """Determines if the coloring is valid and equitable for the graph G."""
    ...
@_dispatchable
def equitable_color(G: Graph[_Node], num_colors):
    """
    Provides an equitable coloring for nodes of `G`.

    Attempts to color a graph using `num_colors` colors, where no neighbors of
    a node can have same color as the node itself and the number of nodes with
    each color differ by at most 1. `num_colors` must be greater than the
    maximum degree of `G`. The algorithm is described in [1]_ and has
    complexity O(num_colors * n**2).

    Parameters
    ----------
    G : networkX graph
       The nodes of this graph will be colored.

    num_colors : number of colors to use
       This number must be at least one more than the maximum degree of nodes
       in the graph.

    Returns
    -------
    A dictionary with keys representing nodes and values representing
    corresponding coloring.

    Examples
    --------
    >>> G = nx.cycle_graph(4)
    >>> nx.coloring.equitable_color(G, num_colors=3)  # doctest: +SKIP
    {0: 2, 1: 1, 2: 2, 3: 0}

    Raises
    ------
    NetworkXAlgorithmError
        If `num_colors` is not at least the maximum degree of the graph `G`

    References
    ----------
    .. [1] Kierstead, H. A., Kostochka, A. V., Mydlarz, M., & Szemerédi, E.
        (2010). A fast algorithm for equitable coloring. Combinatorica, 30(2),
        217-224.
    """
    ...
