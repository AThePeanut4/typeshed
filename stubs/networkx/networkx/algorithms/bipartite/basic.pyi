"""
==========================
Bipartite Graph Algorithms
==========================
"""

from _typeshed import Incomplete
from collections.abc import Iterable

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["is_bipartite", "is_bipartite_node_set", "color", "sets", "density", "degrees"]

@_dispatchable
def color(G: Graph[_Node]) -> dict[Incomplete, Incomplete]:
    """
    Returns a two-coloring of the graph.

    Raises an exception if the graph is not bipartite.

    Parameters
    ----------
    G : NetworkX graph

    Returns
    -------
    color : dictionary
        A dictionary keyed by node with a 1 or 0 as data for each node color.

    Raises
    ------
    NetworkXError
        If the graph is not two-colorable.

    Examples
    --------
    >>> from networkx.algorithms import bipartite
    >>> G = nx.path_graph(4)
    >>> c = bipartite.color(G)
    >>> print(c)
    {0: 1, 1: 0, 2: 1, 3: 0}

    You can use this to set a node attribute indicating the bipartite set:

    >>> nx.set_node_attributes(G, c, "bipartite")
    >>> print(G.nodes[0]["bipartite"])
    1
    >>> print(G.nodes[1]["bipartite"])
    0
    """
    ...
@_dispatchable
def is_bipartite(G: Graph[_Node]) -> bool:
    """
    Returns True if graph G is bipartite, False if not.

    Parameters
    ----------
    G : NetworkX graph

    Examples
    --------
    >>> from networkx.algorithms import bipartite
    >>> G = nx.path_graph(4)
    >>> print(bipartite.is_bipartite(G))
    True

    See Also
    --------
    color, is_bipartite_node_set
    """
    ...
@_dispatchable
def is_bipartite_node_set(G: Graph[_Node], nodes: Iterable[Incomplete]) -> bool:
    """
    Returns True if nodes and G/nodes are a bipartition of G.

    Parameters
    ----------
    G : NetworkX graph

    nodes: list or container
      Check if nodes are a one of a bipartite set.

    Examples
    --------
    >>> from networkx.algorithms import bipartite
    >>> G = nx.path_graph(4)
    >>> X = set([1, 3])
    >>> bipartite.is_bipartite_node_set(G, X)
    True

    Notes
    -----
    An exception is raised if the input nodes are not distinct, because in this
    case some bipartite algorithms will yield incorrect results.
    For connected graphs the bipartite sets are unique.  This function handles
    disconnected graphs.
    """
    ...
@_dispatchable
def sets(G: Graph[_Node], top_nodes: Iterable[Incomplete] | None = None) -> tuple[set[Incomplete], set[Incomplete]]:
    """
    Returns bipartite node sets of graph G.

    Raises an exception if the graph is not bipartite or if the input
    graph is disconnected and thus more than one valid solution exists.
    See :mod:`bipartite documentation <networkx.algorithms.bipartite>`
    for further details on how bipartite graphs are handled in NetworkX.

    Parameters
    ----------
    G : NetworkX graph

    top_nodes : container, optional
      Container with all nodes in one bipartite node set. If not supplied
      it will be computed. But if more than one solution exists an exception
      will be raised.

    Returns
    -------
    X : set
      Nodes from one side of the bipartite graph.
    Y : set
      Nodes from the other side.

    Raises
    ------
    AmbiguousSolution
      Raised if the input bipartite graph is disconnected and no container
      with all nodes in one bipartite set is provided. When determining
      the nodes in each bipartite set more than one valid solution is
      possible if the input graph is disconnected.
    NetworkXError
      Raised if the input graph is not bipartite.

    Examples
    --------
    >>> from networkx.algorithms import bipartite
    >>> G = nx.path_graph(4)
    >>> X, Y = bipartite.sets(G)
    >>> list(X)
    [0, 2]
    >>> list(Y)
    [1, 3]

    See Also
    --------
    color
    """
    ...
@_dispatchable
def density(B: Graph[_Node], nodes) -> float:
    """
    Returns density of bipartite graph B.

    Parameters
    ----------
    B : NetworkX graph

    nodes: list or container
      Nodes in one node set of the bipartite graph.

    Returns
    -------
    d : float
       The bipartite density

    Examples
    --------
    >>> from networkx.algorithms import bipartite
    >>> G = nx.complete_bipartite_graph(3, 2)
    >>> X = set([0, 1, 2])
    >>> bipartite.density(G, X)
    1.0
    >>> Y = set([3, 4])
    >>> bipartite.density(G, Y)
    1.0

    Notes
    -----
    The container of nodes passed as argument must contain all nodes
    in one of the two bipartite node sets to avoid ambiguity in the
    case of disconnected graphs.
    See :mod:`bipartite documentation <networkx.algorithms.bipartite>`
    for further details on how bipartite graphs are handled in NetworkX.

    See Also
    --------
    color
    """
    ...
@_dispatchable
def degrees(B: Graph[_Node], nodes, weight: str | None = None) -> tuple[Incomplete, Incomplete]:
    """
    Returns the degrees of the two node sets in the bipartite graph B.

    Parameters
    ----------
    B : NetworkX graph

    nodes: list or container
      Nodes in one node set of the bipartite graph.

    weight : string or None, optional (default=None)
       The edge attribute that holds the numerical value used as a weight.
       If None, then each edge has weight 1.
       The degree is the sum of the edge weights adjacent to the node.

    Returns
    -------
    (degX,degY) : tuple of dictionaries
       The degrees of the two bipartite sets as dictionaries keyed by node.

    Examples
    --------
    >>> from networkx.algorithms import bipartite
    >>> G = nx.complete_bipartite_graph(3, 2)
    >>> Y = set([3, 4])
    >>> degX, degY = bipartite.degrees(G, Y)
    >>> dict(degX)
    {0: 2, 1: 2, 2: 2}

    Notes
    -----
    The container of nodes passed as argument must contain all nodes
    in one of the two bipartite node sets to avoid ambiguity in the
    case of disconnected graphs.
    See :mod:`bipartite documentation <networkx.algorithms.bipartite>`
    for further details on how bipartite graphs are handled in NetworkX.

    See Also
    --------
    color, density
    """
    ...
