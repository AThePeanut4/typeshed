"""Graph diameter, radius, eccentricity and other properties."""

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

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
def eccentricity(G: Graph[_Node], v: _Node | None = None, sp=None, weight: str | None = None):
    """
    Returns the eccentricity of nodes in G.

    The eccentricity of a node v is the maximum distance from v to
    all other nodes in G.

    Parameters
    ----------
    G : NetworkX graph
       A graph

    v : node, optional
       Return value of specified node

    sp : dict of dicts, optional
       All pairs shortest path lengths as a dictionary of dictionaries

    weight : string, function, or None (default=None)
        If this is a string, then edge weights will be accessed via the
        edge attribute with this key (that is, the weight of the edge
        joining `u` to `v` will be ``G.edges[u, v][weight]``). If no
        such edge attribute exists, the weight of the edge is assumed to
        be one.

        If this is a function, the weight of an edge is the value
        returned by the function. The function must accept exactly three
        positional arguments: the two endpoints of an edge and the
        dictionary of edge attributes for that edge. The function must
        return a number.

        If this is None, every edge has weight/distance/cost 1.

        Weights stored as floating point values can lead to small round-off
        errors in distances. Use integer weights to avoid this.

        Weights should be positive, since they are distances.

    Returns
    -------
    ecc : dictionary
       A dictionary of eccentricity values keyed by node.

    Examples
    --------
    >>> G = nx.Graph([(1, 2), (1, 3), (1, 4), (3, 4), (3, 5), (4, 5)])
    >>> dict(nx.eccentricity(G))
    {1: 2, 2: 3, 3: 2, 4: 2, 5: 3}

    >>> dict(
    ...     nx.eccentricity(G, v=[1, 5])
    ... )  # This returns the eccentricity of node 1 & 5
    {1: 2, 5: 3}
    """
    ...
@_dispatchable
def diameter(G: Graph[_Node], e=None, usebounds=False, weight: str | None = None):
    """
    Returns the diameter of the graph G.

    The diameter is the maximum eccentricity.

    Parameters
    ----------
    G : NetworkX graph
       A graph

    e : eccentricity dictionary, optional
      A precomputed dictionary of eccentricities.

    weight : string, function, or None
        If this is a string, then edge weights will be accessed via the
        edge attribute with this key (that is, the weight of the edge
        joining `u` to `v` will be ``G.edges[u, v][weight]``). If no
        such edge attribute exists, the weight of the edge is assumed to
        be one.

        If this is a function, the weight of an edge is the value
        returned by the function. The function must accept exactly three
        positional arguments: the two endpoints of an edge and the
        dictionary of edge attributes for that edge. The function must
        return a number.

        If this is None, every edge has weight/distance/cost 1.

        Weights stored as floating point values can lead to small round-off
        errors in distances. Use integer weights to avoid this.

        Weights should be positive, since they are distances.

    Returns
    -------
    d : integer
       Diameter of graph

    Examples
    --------
    >>> G = nx.Graph([(1, 2), (1, 3), (1, 4), (3, 4), (3, 5), (4, 5)])
    >>> nx.diameter(G)
    3

    See Also
    --------
    eccentricity
    """
    ...
@_dispatchable
def harmonic_diameter(G, sp=None) -> float: ...
@_dispatchable
def periphery(G: Graph[_Node], e=None, usebounds=False, weight: str | None = None): ...
@_dispatchable
def radius(G: Graph[_Node], e=None, usebounds=False, weight: str | None = None):
    """
    Returns the radius of the graph G.

    The radius is the minimum eccentricity.

    Parameters
    ----------
    G : NetworkX graph
       A graph

    e : eccentricity dictionary, optional
      A precomputed dictionary of eccentricities.

    weight : string, function, or None
        If this is a string, then edge weights will be accessed via the
        edge attribute with this key (that is, the weight of the edge
        joining `u` to `v` will be ``G.edges[u, v][weight]``). If no
        such edge attribute exists, the weight of the edge is assumed to
        be one.

        If this is a function, the weight of an edge is the value
        returned by the function. The function must accept exactly three
        positional arguments: the two endpoints of an edge and the
        dictionary of edge attributes for that edge. The function must
        return a number.

        If this is None, every edge has weight/distance/cost 1.

        Weights stored as floating point values can lead to small round-off
        errors in distances. Use integer weights to avoid this.

        Weights should be positive, since they are distances.

    Returns
    -------
    r : integer
       Radius of graph

    Examples
    --------
    >>> G = nx.Graph([(1, 2), (1, 3), (1, 4), (3, 4), (3, 5), (4, 5)])
    >>> nx.radius(G)
    2
    """
    ...
@_dispatchable
def center(G: Graph[_Node], e=None, usebounds=False, weight: str | None = None):
    """
    Returns the center of the graph G.

    The center is the set of nodes with eccentricity equal to radius.

    Parameters
    ----------
    G : NetworkX graph
       A graph

    e : eccentricity dictionary, optional
      A precomputed dictionary of eccentricities.

    weight : string, function, or None
        If this is a string, then edge weights will be accessed via the
        edge attribute with this key (that is, the weight of the edge
        joining `u` to `v` will be ``G.edges[u, v][weight]``). If no
        such edge attribute exists, the weight of the edge is assumed to
        be one.

        If this is a function, the weight of an edge is the value
        returned by the function. The function must accept exactly three
        positional arguments: the two endpoints of an edge and the
        dictionary of edge attributes for that edge. The function must
        return a number.

        If this is None, every edge has weight/distance/cost 1.

        Weights stored as floating point values can lead to small round-off
        errors in distances. Use integer weights to avoid this.

        Weights should be positive, since they are distances.

    Returns
    -------
    c : list
       List of nodes in center

    Examples
    --------
    >>> G = nx.Graph([(1, 2), (1, 3), (1, 4), (3, 4), (3, 5), (4, 5)])
    >>> list(nx.center(G))
    [1, 3, 4]

    See Also
    --------
    barycenter
    periphery
    """
    ...
@_dispatchable
def barycenter(G, weight: str | None = None, attr=None, sp=None):
    r"""
    Calculate barycenter of a connected graph, optionally with edge weights.

    The :dfn:`barycenter` a
    :func:`connected <networkx.algorithms.components.is_connected>` graph
    :math:`G` is the subgraph induced by the set of its nodes :math:`v`
    minimizing the objective function

    .. math::

        \sum_{u \in V(G)} d_G(u, v),

    where :math:`d_G` is the (possibly weighted) :func:`path length
    <networkx.algorithms.shortest_paths.generic.shortest_path_length>`.
    The barycenter is also called the :dfn:`median`. See [West01]_, p. 78.

    Parameters
    ----------
    G : :class:`networkx.Graph`
        The connected graph :math:`G`.
    weight : :class:`str`, optional
        Passed through to
        :func:`~networkx.algorithms.shortest_paths.generic.shortest_path_length`.
    attr : :class:`str`, optional
        If given, write the value of the objective function to each node's
        `attr` attribute. Otherwise do not store the value.
    sp : dict of dicts, optional
       All pairs shortest path lengths as a dictionary of dictionaries

    Returns
    -------
    list
        Nodes of `G` that induce the barycenter of `G`.

    Raises
    ------
    NetworkXNoPath
        If `G` is disconnected. `G` may appear disconnected to
        :func:`barycenter` if `sp` is given but is missing shortest path
        lengths for any pairs.
    ValueError
        If `sp` and `weight` are both given.

    Examples
    --------
    >>> G = nx.Graph([(1, 2), (1, 3), (1, 4), (3, 4), (3, 5), (4, 5)])
    >>> nx.barycenter(G)
    [1, 3, 4]

    See Also
    --------
    center
    periphery
    """
    ...
@_dispatchable
def resistance_distance(G: Graph[_Node], nodeA=None, nodeB=None, weight: str | None = None, invert_weight: bool = True): ...
@_dispatchable
def effective_graph_resistance(G, weight=None, invert_weight=True) -> float: ...
@_dispatchable
def kemeny_constant(G, *, weight=None) -> float: ...
