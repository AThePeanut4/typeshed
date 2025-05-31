from collections.abc import Callable
from typing_extensions import TypeAlias

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

_WeightFunction: TypeAlias = Callable[..., int]

__all__ = [
    "eccentricity",
    "diameter",
    "harmonic_diameter",
    "radius",
    "periphery",
    "center",
    "barycenter",
    "resistance_distance",
    "kemeny_constant",
    "effective_graph_resistance",
]

@_dispatchable
def eccentricity(G: Graph[_Node], v: _Node | None = None, sp=None, weight: str | _WeightFunction | None = None): ...
@_dispatchable
def diameter(G: Graph[_Node], e=None, usebounds: bool = False, weight: str | _WeightFunction | None = None): ...
@_dispatchable
def harmonic_diameter(G, sp=None, *, weight: str | _WeightFunction | None = None) -> float: ...
@_dispatchable
def periphery(G: Graph[_Node], e=None, usebounds: bool = False, weight: str | _WeightFunction | None = None): ...
@_dispatchable
def radius(G: Graph[_Node], e=None, usebounds: bool = False, weight: str | _WeightFunction | None = None): ...
@_dispatchable
def center(G: Graph[_Node], e=None, usebounds: bool = False, weight: str | _WeightFunction | None = None): ...
@_dispatchable
def barycenter(G, weight: str | _WeightFunction | None = None, attr=None, sp=None): ...
@_dispatchable
def resistance_distance(G: Graph[_Node], nodeA=None, nodeB=None, weight: str | None = None, invert_weight: bool = True):
    """
    Returns the resistance distance between pairs of nodes in graph G.

    The resistance distance between two nodes of a graph is akin to treating
    the graph as a grid of resistors with a resistance equal to the provided
    weight [1]_, [2]_.

    If weight is not provided, then a weight of 1 is used for all edges.

    If two nodes are the same, the resistance distance is zero.

    Parameters
    ----------
    G : NetworkX graph
       A graph

    nodeA : node or None, optional (default=None)
      A node within graph G.
      If None, compute resistance distance using all nodes as source nodes.

    nodeB : node or None, optional (default=None)
      A node within graph G.
      If None, compute resistance distance using all nodes as target nodes.

    weight : string or None, optional (default=None)
       The edge data key used to compute the resistance distance.
       If None, then each edge has weight 1.

    invert_weight : boolean (default=True)
        Proper calculation of resistance distance requires building the
        Laplacian matrix with the reciprocal of the weight. Not required
        if the weight is already inverted. Weight cannot be zero.

    Returns
    -------
    rd : dict or float
       If `nodeA` and `nodeB` are given, resistance distance between `nodeA`
       and `nodeB`. If `nodeA` or `nodeB` is unspecified (the default), a
       dictionary of nodes with resistance distances as the value.

    Raises
    ------
    NetworkXNotImplemented
        If `G` is a directed graph.

    NetworkXError
        If `G` is not connected, or contains no nodes,
        or `nodeA` is not in `G` or `nodeB` is not in `G`.

    Examples
    --------
    >>> G = nx.Graph([(1, 2), (1, 3), (1, 4), (3, 4), (3, 5), (4, 5)])
    >>> round(nx.resistance_distance(G, 1, 3), 10)
    0.625

    Notes
    -----
    The implementation is based on Theorem A in [2]_. Self-loops are ignored.
    Multi-edges are contracted in one edge with weight equal to the harmonic sum of the weights.

    References
    ----------
    .. [1] Wikipedia
       "Resistance distance."
       https://en.wikipedia.org/wiki/Resistance_distance
    .. [2] D. J. Klein and M. Randic.
        Resistance distance.
        J. of Math. Chem. 12:81-95, 1993.
    """
    ...
@_dispatchable
def effective_graph_resistance(G, weight: str | None = None, invert_weight: bool = True) -> float: ...
@_dispatchable
def kemeny_constant(G, *, weight: str | None = None) -> float: ...
