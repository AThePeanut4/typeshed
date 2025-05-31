"""Functional interface to graph methods and assorted utilities."""

from _typeshed import Incomplete, SupportsItems, SupportsKeysAndGetItem, Unused
from collections.abc import Generator, Hashable, Iterable, Iterator
from typing import Literal, TypeVar, overload

from networkx import _dispatchable
from networkx.algorithms.planarity import PlanarEmbedding
from networkx.classes.digraph import DiGraph
from networkx.classes.graph import Graph, _NBunch, _Node
from networkx.classes.multigraph import MultiGraph

__all__ = [
    "nodes",
    "edges",
    "degree",
    "degree_histogram",
    "neighbors",
    "number_of_nodes",
    "number_of_edges",
    "density",
    "is_directed",
    "freeze",
    "is_frozen",
    "subgraph",
    "induced_subgraph",
    "edge_subgraph",
    "restricted_view",
    "to_directed",
    "to_undirected",
    "add_star",
    "add_path",
    "add_cycle",
    "create_empty_copy",
    "set_node_attributes",
    "get_node_attributes",
    "remove_node_attributes",
    "set_edge_attributes",
    "get_edge_attributes",
    "remove_edge_attributes",
    "all_neighbors",
    "non_neighbors",
    "non_edges",
    "common_neighbors",
    "is_weighted",
    "is_negatively_weighted",
    "is_empty",
    "selfloop_edges",
    "nodes_with_selfloops",
    "number_of_selfloops",
    "path_weight",
    "is_path",
]

_U = TypeVar("_U")

def nodes(G):
    """
    Returns a NodeView over the graph nodes.

    This function wraps the :func:`G.nodes <networkx.Graph.nodes>` property.
    """
    ...
def edges(G, nbunch=None):
    """
    Returns an edge view of edges incident to nodes in nbunch.

    Return all edges if nbunch is unspecified or nbunch=None.

    For digraphs, edges=out_edges

    This function wraps the :func:`G.edges <networkx.Graph.edges>` property.
    """
    ...
def degree(G, nbunch=None, weight=None):
    """
    Returns a degree view of single node or of nbunch of nodes.
    If nbunch is omitted, then return degrees of *all* nodes.

    This function wraps the :func:`G.degree <networkx.Graph.degree>` property.
    """
    ...
def neighbors(G, n):
    """
    Returns an iterator over all neighbors of node n.

    This function wraps the :func:`G.neighbors <networkx.Graph.neighbors>` function.
    """
    ...
def number_of_nodes(G):
    """
    Returns the number of nodes in the graph.

    This function wraps the :func:`G.number_of_nodes <networkx.Graph.number_of_nodes>` function.
    """
    ...
def number_of_edges(G):
    """
    Returns the number of edges in the graph.

    This function wraps the :func:`G.number_of_edges <networkx.Graph.number_of_edges>` function.
    """
    ...
def density(G):
    r"""
    Returns the density of a graph.

    The density for undirected graphs is

    .. math::

       d = \frac{2m}{n(n-1)},

    and for directed graphs is

    .. math::

       d = \frac{m}{n(n-1)},

    where `n` is the number of nodes and `m`  is the number of edges in `G`.

    Notes
    -----
    The density is 0 for a graph without edges and 1 for a complete graph.
    The density of multigraphs can be higher than 1.

    Self loops are counted in the total number of edges so graphs with self
    loops can have density higher than 1.
    """
    ...
def degree_histogram(G):
    """
    Returns a list of the frequency of each degree value.

    Parameters
    ----------
    G : Networkx graph
       A graph

    Returns
    -------
    hist : list
       A list of frequencies of degrees.
       The degree values are the index in the list.

    Notes
    -----
    Note: the bins are width one, hence len(list) can be large
    (Order(number_of_edges))
    """
    ...
@overload
def is_directed(G: PlanarEmbedding[Hashable]) -> Literal[False]:
    """Return True if graph is directed."""
    ...
@overload
def is_directed(G: DiGraph[Hashable]) -> Literal[True]:
    """Return True if graph is directed."""
    ...
@overload
def is_directed(G: Graph[Hashable]) -> Literal[False]:
    """Return True if graph is directed."""
    ...
def freeze(G):
    """
    Modify graph to prevent further change by adding or removing
    nodes or edges.

    Node and edge data can still be modified.

    Parameters
    ----------
    G : graph
      A NetworkX graph

    Examples
    --------
    >>> G = nx.path_graph(4)
    >>> G = nx.freeze(G)
    >>> try:
    ...     G.add_edge(4, 5)
    ... except nx.NetworkXError as err:
    ...     print(str(err))
    Frozen graph can't be modified

    Notes
    -----
    To "unfreeze" a graph you must make a copy by creating a new graph object:

    >>> graph = nx.path_graph(4)
    >>> frozen_graph = nx.freeze(graph)
    >>> unfrozen_graph = nx.Graph(frozen_graph)
    >>> nx.is_frozen(unfrozen_graph)
    False

    See Also
    --------
    is_frozen
    """
    ...
def is_frozen(G: Graph[Incomplete]) -> bool:
    """
    Returns True if graph is frozen.

    Parameters
    ----------
    G : graph
      A NetworkX graph

    See Also
    --------
    freeze
    """
    ...
def add_star(G_to_add_to, nodes_for_star, **attr) -> None:
    """
    Add a star to Graph G_to_add_to.

    The first node in `nodes_for_star` is the middle of the star.
    It is connected to all other nodes.

    Parameters
    ----------
    G_to_add_to : graph
        A NetworkX graph
    nodes_for_star : iterable container
        A container of nodes.
    attr : keyword arguments, optional (default= no attributes)
        Attributes to add to every edge in star.

    See Also
    --------
    add_path, add_cycle

    Examples
    --------
    >>> G = nx.Graph()
    >>> nx.add_star(G, [0, 1, 2, 3])
    >>> nx.add_star(G, [10, 11, 12], weight=2)
    """
    ...
def add_path(G_to_add_to, nodes_for_path, **attr) -> None:
    """
    Add a path to the Graph G_to_add_to.

    Parameters
    ----------
    G_to_add_to : graph
        A NetworkX graph
    nodes_for_path : iterable container
        A container of nodes.  A path will be constructed from
        the nodes (in order) and added to the graph.
    attr : keyword arguments, optional (default= no attributes)
        Attributes to add to every edge in path.

    See Also
    --------
    add_star, add_cycle

    Examples
    --------
    >>> G = nx.Graph()
    >>> nx.add_path(G, [0, 1, 2, 3])
    >>> nx.add_path(G, [10, 11, 12], weight=7)
    """
    ...
def add_cycle(G_to_add_to, nodes_for_cycle, **attr) -> None:
    """
    Add a cycle to the Graph G_to_add_to.

    Parameters
    ----------
    G_to_add_to : graph
        A NetworkX graph
    nodes_for_cycle: iterable container
        A container of nodes.  A cycle will be constructed from
        the nodes (in order) and added to the graph.
    attr : keyword arguments, optional (default= no attributes)
        Attributes to add to every edge in cycle.

    See Also
    --------
    add_path, add_star

    Examples
    --------
    >>> G = nx.Graph()  # or DiGraph, MultiGraph, MultiDiGraph, etc
    >>> nx.add_cycle(G, [0, 1, 2, 3])
    >>> nx.add_cycle(G, [10, 11, 12], weight=7)
    """
    ...
def subgraph(G, nbunch):
    """
    Returns the subgraph induced on nodes in nbunch.

    Parameters
    ----------
    G : graph
       A NetworkX graph

    nbunch : list, iterable
       A container of nodes that will be iterated through once (thus
       it should be an iterator or be iterable).  Each element of the
       container should be a valid node type: any hashable type except
       None.  If nbunch is None, return all edges data in the graph.
       Nodes in nbunch that are not in the graph will be (quietly)
       ignored.

    Notes
    -----
    subgraph(G) calls G.subgraph()
    """
    ...
def induced_subgraph(G: Graph[_Node], nbunch: _NBunch[_Node]) -> Graph[_Node]:
    """
    Returns a SubGraph view of `G` showing only nodes in nbunch.

    The induced subgraph of a graph on a set of nodes N is the
    graph with nodes N and edges from G which have both ends in N.

    Parameters
    ----------
    G : NetworkX Graph
    nbunch : node, container of nodes or None (for all nodes)

    Returns
    -------
    subgraph : SubGraph View
        A read-only view of the subgraph in `G` induced by the nodes.
        Changes to the graph `G` will be reflected in the view.

    Notes
    -----
    To create a mutable subgraph with its own copies of nodes
    edges and attributes use `subgraph.copy()` or `Graph(subgraph)`

    For an inplace reduction of a graph to a subgraph you can remove nodes:
    `G.remove_nodes_from(n in G if n not in set(nbunch))`

    If you are going to compute subgraphs of your subgraphs you could
    end up with a chain of views that can be very slow once the chain
    has about 15 views in it. If they are all induced subgraphs, you
    can short-cut the chain by making them all subgraphs of the original
    graph. The graph class method `G.subgraph` does this when `G` is
    a subgraph. In contrast, this function allows you to choose to build
    chains or not, as you wish. The returned subgraph is a view on `G`.

    Examples
    --------
    >>> G = nx.path_graph(4)  # or DiGraph, MultiGraph, MultiDiGraph, etc
    >>> H = nx.induced_subgraph(G, [0, 1, 3])
    >>> list(H.edges)
    [(0, 1)]
    >>> list(H.nodes)
    [0, 1, 3]
    """
    ...
def edge_subgraph(G, edges):
    """
    Returns a view of the subgraph induced by the specified edges.

    The induced subgraph contains each edge in `edges` and each
    node incident to any of those edges.

    Parameters
    ----------
    G : NetworkX Graph
    edges : iterable
        An iterable of edges. Edges not present in `G` are ignored.

    Returns
    -------
    subgraph : SubGraph View
        A read-only edge-induced subgraph of `G`.
        Changes to `G` are reflected in the view.

    Notes
    -----
    To create a mutable subgraph with its own copies of nodes
    edges and attributes use `subgraph.copy()` or `Graph(subgraph)`

    If you create a subgraph of a subgraph recursively you can end up
    with a chain of subgraphs that becomes very slow with about 15
    nested subgraph views. Luckily the edge_subgraph filter nests
    nicely so you can use the original graph as G in this function
    to avoid chains. We do not rule out chains programmatically so
    that odd cases like an `edge_subgraph` of a `restricted_view`
    can be created.

    Examples
    --------
    >>> G = nx.path_graph(5)
    >>> H = G.edge_subgraph([(0, 1), (3, 4)])
    >>> list(H.nodes)
    [0, 1, 3, 4]
    >>> list(H.edges)
    [(0, 1), (3, 4)]
    """
    ...
def restricted_view(G, nodes, edges):
    """
    Returns a view of `G` with hidden nodes and edges.

    The resulting subgraph filters out node `nodes` and edges `edges`.
    Filtered out nodes also filter out any of their edges.

    Parameters
    ----------
    G : NetworkX Graph
    nodes : iterable
        An iterable of nodes. Nodes not present in `G` are ignored.
    edges : iterable
        An iterable of edges. Edges not present in `G` are ignored.

    Returns
    -------
    subgraph : SubGraph View
        A read-only restricted view of `G` filtering out nodes and edges.
        Changes to `G` are reflected in the view.

    Notes
    -----
    To create a mutable subgraph with its own copies of nodes
    edges and attributes use `subgraph.copy()` or `Graph(subgraph)`

    If you create a subgraph of a subgraph recursively you may end up
    with a chain of subgraph views. Such chains can get quite slow
    for lengths near 15. To avoid long chains, try to make your subgraph
    based on the original graph.  We do not rule out chains programmatically
    so that odd cases like an `edge_subgraph` of a `restricted_view`
    can be created.

    Examples
    --------
    >>> G = nx.path_graph(5)
    >>> H = nx.restricted_view(G, [0], [(1, 2), (3, 4)])
    >>> list(H.nodes)
    [1, 2, 3, 4]
    >>> list(H.edges)
    [(2, 3)]
    """
    ...
def to_directed(graph):
    """
    Returns a directed view of the graph `graph`.

    Identical to graph.to_directed(as_view=True)
    Note that graph.to_directed defaults to `as_view=False`
    while this function always provides a view.
    """
    ...
def to_undirected(graph):
    """
    Returns an undirected view of the graph `graph`.

    Identical to graph.to_undirected(as_view=True)
    Note that graph.to_undirected defaults to `as_view=False`
    while this function always provides a view.
    """
    ...
def create_empty_copy(G, with_data: bool = True):
    """
    Returns a copy of the graph G with all of the edges removed.

    Parameters
    ----------
    G : graph
       A NetworkX graph

    with_data :  bool (default=True)
       Propagate Graph and Nodes data to the new graph.

    See Also
    --------
    empty_graph
    """
    ...

# incomplete: Can "Any scalar value" be enforced?
@overload
def set_node_attributes(
    G: Graph[Hashable],
    values: SupportsItems[_Node, Unused],
    name: str,
    *,
    backend=None,  # @_dispatchable adds these arguments, but we can't use this decorator with @overload
    **backend_kwargs,
) -> None: ...
@overload
def set_node_attributes(
    G: Graph[_Node],
    values: SupportsItems[_Node, SupportsKeysAndGetItem[Incomplete, Incomplete] | Iterable[tuple[Incomplete, Incomplete]]],
    name: None = None,
    *,
    backend=None,
    **backend_kwargs,
) -> None: ...
@_dispatchable
def get_node_attributes(G: Graph[_Node], name: str, default=None) -> dict[_Node, Incomplete]: ...
@_dispatchable
def remove_node_attributes(G, *attr_names, nbunch=None) -> None: ...
@overload
def set_edge_attributes(
    G: Graph[_Node],
    values: SupportsItems[tuple[_Node, _Node], Incomplete],
    name: str,
    *,
    backend=None,  # @_dispatchable adds these arguments, but we can't use this decorator with @overload
    **backend_kwargs,
) -> None: ...
@overload
def set_edge_attributes(
    G: MultiGraph[_Node], values: dict[tuple[_Node, _Node, Incomplete], Incomplete], name: str, *, backend=None, **backend_kwargs
) -> None: ...
@overload
def set_edge_attributes(G: Graph[Hashable], values, name: None = None, *, backend=None, **backend_kwargs) -> None: ...
@_dispatchable
def get_edge_attributes(G: Graph[_Node], name: str, default=None) -> dict[tuple[_Node, _Node], Incomplete]: ...
@_dispatchable
def remove_edge_attributes(G, *attr_names, ebunch=None) -> None: ...
def all_neighbors(graph: Graph[_Node], node: _Node) -> Iterator[_Node]: ...
def non_neighbors(graph: Graph[_Node], node: _Node) -> Generator[_Node, None, None]: ...
def non_edges(graph: Graph[_Node]) -> Generator[tuple[_Node, _Node], None, None]: ...
def common_neighbors(G: Graph[_Node], u: _Node, v: _Node) -> Generator[_Node, None, None]: ...
@_dispatchable
def is_weighted(G: Graph[_Node], edge: tuple[_Node, _Node] | None = None, weight: str = "weight") -> bool: ...
@_dispatchable
def is_negatively_weighted(G: Graph[_Node], edge: tuple[_Node, _Node] | None = None, weight: str = "weight") -> bool: ...
@_dispatchable
def is_empty(G: Graph[Hashable]) -> bool: ...
def nodes_with_selfloops(G: Graph[_Node]) -> Generator[_Node, None, None]: ...
@overload
def selfloop_edges(
    G: Graph[_Node], data: Literal[False] = False, keys: Literal[False] = False, default=None
) -> Generator[tuple[_Node, _Node], None, None]:
    """
    Returns an iterator over selfloop edges.

    A selfloop edge has the same node at both ends.

    Parameters
    ----------
    G : graph
        A NetworkX graph.
    data : string or bool, optional (default=False)
        Return selfloop edges as two tuples (u, v) (data=False)
        or three-tuples (u, v, datadict) (data=True)
        or three-tuples (u, v, datavalue) (data='attrname')
    keys : bool, optional (default=False)
        If True, return edge keys with each edge.
    default : value, optional (default=None)
        Value used for edges that don't have the requested attribute.
        Only relevant if data is not True or False.

    Returns
    -------
    edgeiter : iterator over edge tuples
        An iterator over all selfloop edges.

    See Also
    --------
    nodes_with_selfloops, number_of_selfloops

    Examples
    --------
    >>> G = nx.MultiGraph()  # or Graph, DiGraph, MultiDiGraph, etc
    >>> ekey = G.add_edge(1, 1)
    >>> ekey = G.add_edge(1, 2)
    >>> list(nx.selfloop_edges(G))
    [(1, 1)]
    >>> list(nx.selfloop_edges(G, data=True))
    [(1, 1, {})]
    >>> list(nx.selfloop_edges(G, keys=True))
    [(1, 1, 0)]
    >>> list(nx.selfloop_edges(G, keys=True, data=True))
    [(1, 1, 0, {})]
    """
    ...
@overload
def selfloop_edges(
    G: Graph[_Node], data: Literal[True], keys: Literal[False] = False, default=None
) -> Generator[tuple[_Node, _Node, dict[str, Incomplete]], None, None]:
    """
    Returns an iterator over selfloop edges.

    A selfloop edge has the same node at both ends.

    Parameters
    ----------
    G : graph
        A NetworkX graph.
    data : string or bool, optional (default=False)
        Return selfloop edges as two tuples (u, v) (data=False)
        or three-tuples (u, v, datadict) (data=True)
        or three-tuples (u, v, datavalue) (data='attrname')
    keys : bool, optional (default=False)
        If True, return edge keys with each edge.
    default : value, optional (default=None)
        Value used for edges that don't have the requested attribute.
        Only relevant if data is not True or False.

    Returns
    -------
    edgeiter : iterator over edge tuples
        An iterator over all selfloop edges.

    See Also
    --------
    nodes_with_selfloops, number_of_selfloops

    Examples
    --------
    >>> G = nx.MultiGraph()  # or Graph, DiGraph, MultiDiGraph, etc
    >>> ekey = G.add_edge(1, 1)
    >>> ekey = G.add_edge(1, 2)
    >>> list(nx.selfloop_edges(G))
    [(1, 1)]
    >>> list(nx.selfloop_edges(G, data=True))
    [(1, 1, {})]
    >>> list(nx.selfloop_edges(G, keys=True))
    [(1, 1, 0)]
    >>> list(nx.selfloop_edges(G, keys=True, data=True))
    [(1, 1, 0, {})]
    """
    ...
@overload
def selfloop_edges(
    G: Graph[_Node], data: str, keys: Literal[False] = False, default: _U | None = None
) -> Generator[tuple[_Node, _Node, _U], None, None]:
    """
    Returns an iterator over selfloop edges.

    A selfloop edge has the same node at both ends.

    Parameters
    ----------
    G : graph
        A NetworkX graph.
    data : string or bool, optional (default=False)
        Return selfloop edges as two tuples (u, v) (data=False)
        or three-tuples (u, v, datadict) (data=True)
        or three-tuples (u, v, datavalue) (data='attrname')
    keys : bool, optional (default=False)
        If True, return edge keys with each edge.
    default : value, optional (default=None)
        Value used for edges that don't have the requested attribute.
        Only relevant if data is not True or False.

    Returns
    -------
    edgeiter : iterator over edge tuples
        An iterator over all selfloop edges.

    See Also
    --------
    nodes_with_selfloops, number_of_selfloops

    Examples
    --------
    >>> G = nx.MultiGraph()  # or Graph, DiGraph, MultiDiGraph, etc
    >>> ekey = G.add_edge(1, 1)
    >>> ekey = G.add_edge(1, 2)
    >>> list(nx.selfloop_edges(G))
    [(1, 1)]
    >>> list(nx.selfloop_edges(G, data=True))
    [(1, 1, {})]
    >>> list(nx.selfloop_edges(G, keys=True))
    [(1, 1, 0)]
    >>> list(nx.selfloop_edges(G, keys=True, data=True))
    [(1, 1, 0, {})]
    """
    ...
@overload
def selfloop_edges(
    G: Graph[_Node], data: Literal[False], keys: Literal[True], default=None
) -> Generator[tuple[_Node, _Node, int], None, None]:
    """
    Returns an iterator over selfloop edges.

    A selfloop edge has the same node at both ends.

    Parameters
    ----------
    G : graph
        A NetworkX graph.
    data : string or bool, optional (default=False)
        Return selfloop edges as two tuples (u, v) (data=False)
        or three-tuples (u, v, datadict) (data=True)
        or three-tuples (u, v, datavalue) (data='attrname')
    keys : bool, optional (default=False)
        If True, return edge keys with each edge.
    default : value, optional (default=None)
        Value used for edges that don't have the requested attribute.
        Only relevant if data is not True or False.

    Returns
    -------
    edgeiter : iterator over edge tuples
        An iterator over all selfloop edges.

    See Also
    --------
    nodes_with_selfloops, number_of_selfloops

    Examples
    --------
    >>> G = nx.MultiGraph()  # or Graph, DiGraph, MultiDiGraph, etc
    >>> ekey = G.add_edge(1, 1)
    >>> ekey = G.add_edge(1, 2)
    >>> list(nx.selfloop_edges(G))
    [(1, 1)]
    >>> list(nx.selfloop_edges(G, data=True))
    [(1, 1, {})]
    >>> list(nx.selfloop_edges(G, keys=True))
    [(1, 1, 0)]
    >>> list(nx.selfloop_edges(G, keys=True, data=True))
    [(1, 1, 0, {})]
    """
    ...
@overload
def selfloop_edges(
    G: Graph[_Node], data: Literal[False] = False, *, keys: Literal[True], default=None
) -> Generator[tuple[_Node, _Node, int], None, None]:
    """
    Returns an iterator over selfloop edges.

    A selfloop edge has the same node at both ends.

    Parameters
    ----------
    G : graph
        A NetworkX graph.
    data : string or bool, optional (default=False)
        Return selfloop edges as two tuples (u, v) (data=False)
        or three-tuples (u, v, datadict) (data=True)
        or three-tuples (u, v, datavalue) (data='attrname')
    keys : bool, optional (default=False)
        If True, return edge keys with each edge.
    default : value, optional (default=None)
        Value used for edges that don't have the requested attribute.
        Only relevant if data is not True or False.

    Returns
    -------
    edgeiter : iterator over edge tuples
        An iterator over all selfloop edges.

    See Also
    --------
    nodes_with_selfloops, number_of_selfloops

    Examples
    --------
    >>> G = nx.MultiGraph()  # or Graph, DiGraph, MultiDiGraph, etc
    >>> ekey = G.add_edge(1, 1)
    >>> ekey = G.add_edge(1, 2)
    >>> list(nx.selfloop_edges(G))
    [(1, 1)]
    >>> list(nx.selfloop_edges(G, data=True))
    [(1, 1, {})]
    >>> list(nx.selfloop_edges(G, keys=True))
    [(1, 1, 0)]
    >>> list(nx.selfloop_edges(G, keys=True, data=True))
    [(1, 1, 0, {})]
    """
    ...
@overload
def selfloop_edges(
    G: Graph[_Node], data: Literal[True], keys: Literal[True], default=None
) -> Generator[tuple[_Node, _Node, int, dict[str, Incomplete]], None, None]:
    """
    Returns an iterator over selfloop edges.

    A selfloop edge has the same node at both ends.

    Parameters
    ----------
    G : graph
        A NetworkX graph.
    data : string or bool, optional (default=False)
        Return selfloop edges as two tuples (u, v) (data=False)
        or three-tuples (u, v, datadict) (data=True)
        or three-tuples (u, v, datavalue) (data='attrname')
    keys : bool, optional (default=False)
        If True, return edge keys with each edge.
    default : value, optional (default=None)
        Value used for edges that don't have the requested attribute.
        Only relevant if data is not True or False.

    Returns
    -------
    edgeiter : iterator over edge tuples
        An iterator over all selfloop edges.

    See Also
    --------
    nodes_with_selfloops, number_of_selfloops

    Examples
    --------
    >>> G = nx.MultiGraph()  # or Graph, DiGraph, MultiDiGraph, etc
    >>> ekey = G.add_edge(1, 1)
    >>> ekey = G.add_edge(1, 2)
    >>> list(nx.selfloop_edges(G))
    [(1, 1)]
    >>> list(nx.selfloop_edges(G, data=True))
    [(1, 1, {})]
    >>> list(nx.selfloop_edges(G, keys=True))
    [(1, 1, 0)]
    >>> list(nx.selfloop_edges(G, keys=True, data=True))
    [(1, 1, 0, {})]
    """
    ...
@overload
def selfloop_edges(
    G: Graph[_Node], data: str, keys: Literal[True], default: _U | None = None
) -> Generator[tuple[_Node, _Node, int, _U], None, None]: ...
@_dispatchable
def number_of_selfloops(G: Graph[Hashable]) -> int: ...
def is_path(G: Graph[_Node], path: Iterable[Incomplete]) -> bool: ...
def path_weight(G, path, weight) -> int: ...
