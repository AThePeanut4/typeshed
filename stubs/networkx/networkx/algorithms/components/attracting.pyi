"""Attracting components."""

from _typeshed import Incomplete
from collections.abc import Generator

from networkx.classes.digraph import DiGraph
from networkx.classes.graph import _Node
from networkx.classes.multidigraph import MultiDiGraph
from networkx.utils.backends import _dispatchable

__all__ = ["number_attracting_components", "attracting_components", "is_attracting_component"]

@_dispatchable
def attracting_components(G) -> Generator[Incomplete, None, None]:
    """
    Generates the attracting components in `G`.

    An attracting component in a directed graph `G` is a strongly connected
    component with the property that a random walker on the graph will never
    leave the component, once it enters the component.

    The nodes in attracting components can also be thought of as recurrent
    nodes.  If a random walker enters the attractor containing the node, then
    the node will be visited infinitely often.

    To obtain induced subgraphs on each component use:
    ``(G.subgraph(c).copy() for c in attracting_components(G))``

    Parameters
    ----------
    G : DiGraph, MultiDiGraph
        The graph to be analyzed.

    Returns
    -------
    attractors : generator of sets
        A generator of sets of nodes, one for each attracting component of G.

    Raises
    ------
    NetworkXNotImplemented
        If the input graph is undirected.

    See Also
    --------
    number_attracting_components
    is_attracting_component
    """
    ...
@_dispatchable
def number_attracting_components(G) -> int:
    """
    Returns the number of attracting components in `G`.

    Parameters
    ----------
    G : DiGraph, MultiDiGraph
        The graph to be analyzed.

    Returns
    -------
    n : int
        The number of attracting components in G.

    Raises
    ------
    NetworkXNotImplemented
        If the input graph is undirected.

    See Also
    --------
    attracting_components
    is_attracting_component
    """
    ...
@_dispatchable
def is_attracting_component(G: DiGraph[_Node] | MultiDiGraph[_Node]) -> bool:
    """
    Returns True if `G` consists of a single attracting component.

    Parameters
    ----------
    G : DiGraph, MultiDiGraph
        The graph to be analyzed.

    Returns
    -------
    attracting : bool
        True if `G` has a single attracting component. Otherwise, False.

    Raises
    ------
    NetworkXNotImplemented
        If the input graph is undirected.

    See Also
    --------
    attracting_components
    number_attracting_components
    """
    ...
