"""
View Classes provide node, edge and degree "views" of a graph.

Views for nodes, edges and degree are provided for all base graph classes.
A view means a read-only object that is quick to create, automatically
updated when the graph changes, and provides basic access like `n in V`,
`for n in V`, `V[n]` and sometimes set operations.

The views are read-only iterable containers that are updated as the
graph is updated. As with dicts, the graph should not be updated
while iterating through the view. Views can be iterated multiple times.

Edge and Node views also allow data attribute lookup.
The resulting attribute dict is writable as `G.edges[3, 4]['color']='red'`
Degree views allow lookup of degree values for single nodes.
Weighted degree is supported with the `weight` argument.

NodeView
========

    `V = G.nodes` (or `V = G.nodes()`) allows `len(V)`, `n in V`, set
    operations e.g. "G.nodes & H.nodes", and `dd = G.nodes[n]`, where
    `dd` is the node data dict. Iteration is over the nodes by default.

NodeDataView
============

    To iterate over (node, data) pairs, use arguments to `G.nodes()`
    to create a DataView e.g. `DV = G.nodes(data='color', default='red')`.
    The DataView iterates as `for n, color in DV` and allows
    `(n, 'red') in DV`. Using `DV = G.nodes(data=True)`, the DataViews
    use the full datadict in writeable form also allowing contain testing as
    `(n, {'color': 'red'}) in VD`. DataViews allow set operations when
    data attributes are hashable.

DegreeView
==========

    `V = G.degree` allows iteration over (node, degree) pairs as well
    as lookup: `deg=V[n]`. There are many flavors of DegreeView
    for In/Out/Directed/Multi. For Directed Graphs, `G.degree`
    counts both in and out going edges. `G.out_degree` and
    `G.in_degree` count only specific directions.
    Weighted degree using edge data attributes is provide via
    `V = G.degree(weight='attr_name')` where any string with the
    attribute name can be used. `weight=None` is the default.
    No set operations are implemented for degrees, use NodeView.

    The argument `nbunch` restricts iteration to nodes in nbunch.
    The DegreeView can still lookup any node even if nbunch is specified.

EdgeView
========

    `V = G.edges` or `V = G.edges()` allows iteration over edges as well as
    `e in V`, set operations and edge data lookup `dd = G.edges[2, 3]`.
    Iteration is over 2-tuples `(u, v)` for Graph/DiGraph. For multigraphs
    edges 3-tuples `(u, v, key)` are the default but 2-tuples can be obtained
    via `V = G.edges(keys=False)`.

    Set operations for directed graphs treat the edges as a set of 2-tuples.
    For undirected graphs, 2-tuples are not a unique representation of edges.
    So long as the set being compared to contains unique representations
    of its edges, the set operations will act as expected. If the other
    set contains both `(0, 1)` and `(1, 0)` however, the result of set
    operations may contain both representations of the same edge.

EdgeDataView
============

    Edge data can be reported using an EdgeDataView typically created
    by calling an EdgeView: `DV = G.edges(data='weight', default=1)`.
    The EdgeDataView allows iteration over edge tuples, membership checking
    but no set operations.

    Iteration depends on `data` and `default` and for multigraph `keys`
    If `data is False` (the default) then iterate over 2-tuples `(u, v)`.
    If `data is True` iterate over 3-tuples `(u, v, datadict)`.
    Otherwise iterate over `(u, v, datadict.get(data, default))`.
    For Multigraphs, if `keys is True`, replace `u, v` with `u, v, key`
    to create 3-tuples and 4-tuples.

    The argument `nbunch` restricts edges to those incident to nodes in nbunch.
"""

from _typeshed import Incomplete, Unused
from abc import ABC
from collections.abc import Iterable, Iterator, Mapping, Set as AbstractSet
from typing import Any, Generic, Literal, TypeVar, overload
from typing_extensions import Self

from networkx.classes.graph import Graph, _Edge, _NBunch, _Node

_D = TypeVar("_D")
_U = TypeVar("_U")

__all__ = [
    "NodeView",
    "NodeDataView",
    "EdgeView",
    "OutEdgeView",
    "InEdgeView",
    "EdgeDataView",
    "OutEdgeDataView",
    "InEdgeDataView",
    "MultiEdgeView",
    "OutMultiEdgeView",
    "InMultiEdgeView",
    "MultiEdgeDataView",
    "OutMultiEdgeDataView",
    "InMultiEdgeDataView",
    "DegreeView",
    "DiDegreeView",
    "InDegreeView",
    "OutDegreeView",
    "MultiDegreeView",
    "DiMultiDegreeView",
    "InMultiDegreeView",
    "OutMultiDegreeView",
]

class NodeView(Mapping[_Node, dict[str, Any]], AbstractSet[_Node]):
    """
    A NodeView class to act as G.nodes for a NetworkX Graph

    Set operations act on the nodes without considering data.
    Iteration is over nodes. Node data can be looked up like a dict.
    Use NodeDataView to iterate over node data or to specify a data
    attribute for lookup. NodeDataView is created by calling the NodeView.

    Parameters
    ----------
    graph : NetworkX graph-like class

    Examples
    --------
    >>> G = nx.path_graph(3)
    >>> NV = G.nodes()
    >>> 2 in NV
    True
    >>> for n in NV:
    ...     print(n)
    0
    1
    2
    >>> assert NV & {1, 2, 3} == {1, 2}

    >>> G.add_node(2, color="blue")
    >>> NV[2]
    {'color': 'blue'}
    >>> G.add_node(8, color="red")
    >>> NDV = G.nodes(data=True)
    >>> (2, NV[2]) in NDV
    True
    >>> for n, dd in NDV:
    ...     print((n, dd.get("color", "aqua")))
    (0, 'aqua')
    (1, 'aqua')
    (2, 'blue')
    (8, 'red')
    >>> NDV[2] == NV[2]
    True

    >>> NVdata = G.nodes(data="color", default="aqua")
    >>> (2, NVdata[2]) in NVdata
    True
    >>> for n, dd in NVdata:
    ...     print((n, dd))
    (0, 'aqua')
    (1, 'aqua')
    (2, 'blue')
    (8, 'red')
    >>> NVdata[2] == NV[2]  # NVdata gets 'color', NV gets datadict
    False
    """
    def __init__(self, graph: Graph[_Node]) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_Node]: ...
    def __getitem__(self, n: _Node) -> dict[str, Any]: ...
    def __contains__(self, n: object) -> bool: ...
    @overload
    def __call__(self, data: Literal[False] = False, default=None) -> Iterator[_Node]: ...
    @overload
    def __call__(self, data: Literal[True] | str, default=None) -> Iterator[tuple[_Node, dict[str, Any]]]: ...
    def data(self, data: bool | str = True, default=None) -> NodeDataView[_Node]:
        """
        Return a read-only view of node data.

        Parameters
        ----------
        data : bool or node data key, default=True
            If ``data=True`` (the default), return a `NodeDataView` object that
            maps each node to *all* of its attributes. `data` may also be an
            arbitrary key, in which case the `NodeDataView` maps each node to
            the value for the keyed attribute. In this case, if a node does
            not have the `data` attribute, the `default` value is used.
        default : object, default=None
            The value used when a node does not have a specific attribute.

        Returns
        -------
        NodeDataView
            The layout of the returned NodeDataView depends on the value of the
            `data` parameter.

        Notes
        -----
        If ``data=False``, returns a `NodeView` object without data.

        See Also
        --------
        NodeDataView

        Examples
        --------
        >>> G = nx.Graph()
        >>> G.add_nodes_from(
        ...     [
        ...         (0, {"color": "red", "weight": 10}),
        ...         (1, {"color": "blue"}),
        ...         (2, {"color": "yellow", "weight": 2}),
        ...     ]
        ... )

        Accessing node data with ``data=True`` (the default) returns a
        NodeDataView mapping each node to all of its attributes:

        >>> G.nodes.data()
        NodeDataView({0: {'color': 'red', 'weight': 10}, 1: {'color': 'blue'}, 2: {'color': 'yellow', 'weight': 2}})

        If `data` represents  a key in the node attribute dict, a NodeDataView mapping
        the nodes to the value for that specific key is returned:

        >>> G.nodes.data("color")
        NodeDataView({0: 'red', 1: 'blue', 2: 'yellow'}, data='color')

        If a specific key is not found in an attribute dict, the value specified
        by `default` is returned:

        >>> G.nodes.data("weight", default=-999)
        NodeDataView({0: 10, 1: -999, 2: 2}, data='weight')

        Note that there is no check that the `data` key is in any of the
        node attribute dictionaries:

        >>> G.nodes.data("height")
        NodeDataView({0: None, 1: None, 2: None}, data='height')
        """
        ...

class NodeDataView(AbstractSet[_Node]):
    """
    A DataView class for nodes of a NetworkX Graph

    The main use for this class is to iterate through node-data pairs.
    The data can be the entire data-dictionary for each node, or it
    can be a specific attribute (with default) for each node.
    Set operations are enabled with NodeDataView, but don't work in
    cases where the data is not hashable. Use with caution.
    Typically, set operations on nodes use NodeView, not NodeDataView.
    That is, they use `G.nodes` instead of `G.nodes(data='foo')`.

    Parameters
    ==========
    graph : NetworkX graph-like class
    data : bool or string (default=False)
    default : object (default=None)
    """
    def __init__(self, nodedict: Mapping[str, Incomplete], data: bool | str = False, default=None) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[tuple[_Node, Incomplete]]: ...  # type: ignore[override]
    def __contains__(self, n: object) -> bool: ...
    def __getitem__(self, n: _Node): ...

class DiDegreeView(Generic[_Node]):
    """
    A View class for degree of nodes in a NetworkX Graph

    The functionality is like dict.items() with (node, degree) pairs.
    Additional functionality includes read-only lookup of node degree,
    and calling with optional features nbunch (for only a subset of nodes)
    and weight (use edge weights to compute degree).

    Parameters
    ==========
    graph : NetworkX graph-like class
    nbunch : node, container of nodes, or None meaning all nodes (default=None)
    weight : bool or string (default=None)

    Notes
    -----
    DegreeView can still lookup any node even if nbunch is specified.

    Examples
    --------
    >>> G = nx.path_graph(3)
    >>> DV = G.degree()
    >>> assert DV[2] == 1
    >>> assert sum(deg for n, deg in DV) == 4

    >>> DVweight = G.degree(weight="span")
    >>> G.add_edge(1, 2, span=34)
    >>> DVweight[2]
    34
    >>> DVweight[0]  #  default edge weight is 1
    1
    >>> sum(span for n, span in DVweight)  # sum weighted degrees
    70

    >>> DVnbunch = G.degree(nbunch=(1, 2))
    >>> assert len(list(DVnbunch)) == 2  # iteration over nbunch only
    """
    def __init__(self, G: Graph[_Node], nbunch: _NBunch[_Node] = None, weight: None | bool | str = None) -> None: ...
    def __call__(self, nbunch: _NBunch[_Node] = None, weight: None | bool | str = None) -> int | DiDegreeView[_Node]: ...
    def __getitem__(self, n: _Node) -> float: ...
    def __iter__(self) -> Iterator[tuple[_Node, float]]: ...
    def __len__(self) -> int: ...

class DegreeView(DiDegreeView[_Node]):
    """
    A DegreeView class to act as G.degree for a NetworkX Graph

    Typical usage focuses on iteration over `(node, degree)` pairs.
    The degree is by default the number of edges incident to the node.
    Optional argument `weight` enables weighted degree using the edge
    attribute named in the `weight` argument.  Reporting and iteration
    can also be restricted to a subset of nodes using `nbunch`.

    Additional functionality include node lookup so that `G.degree[n]`
    reported the (possibly weighted) degree of node `n`. Calling the
    view creates a view with different arguments `nbunch` or `weight`.

    Parameters
    ==========
    graph : NetworkX graph-like class
    nbunch : node, container of nodes, or None meaning all nodes (default=None)
    weight : string or None (default=None)

    Notes
    -----
    DegreeView can still lookup any node even if nbunch is specified.

    Examples
    --------
    >>> G = nx.path_graph(3)
    >>> DV = G.degree()
    >>> assert DV[2] == 1
    >>> assert G.degree[2] == 1
    >>> assert sum(deg for n, deg in DV) == 4

    >>> DVweight = G.degree(weight="span")
    >>> G.add_edge(1, 2, span=34)
    >>> DVweight[2]
    34
    >>> DVweight[0]  #  default edge weight is 1
    1
    >>> sum(span for n, span in DVweight)  # sum weighted degrees
    70

    >>> DVnbunch = G.degree(nbunch=(1, 2))
    >>> assert len(list(DVnbunch)) == 2  # iteration over nbunch only
    """
    ...
class OutDegreeView(DiDegreeView[_Node]):
    """A DegreeView class to report out_degree for a DiGraph; See DegreeView"""
    ...
class InDegreeView(DiDegreeView[_Node]):
    """A DegreeView class to report in_degree for a DiGraph; See DegreeView"""
    ...
class MultiDegreeView(DiDegreeView[_Node]):
    """A DegreeView class for undirected multigraphs; See DegreeView"""
    ...
class DiMultiDegreeView(DiDegreeView[_Node]):
    """A DegreeView class for MultiDiGraph; See DegreeView"""
    ...
class InMultiDegreeView(DiDegreeView[_Node]):
    """A DegreeView class for inward degree of MultiDiGraph; See DegreeView"""
    ...
class OutMultiDegreeView(DiDegreeView[_Node]):
    """A DegreeView class for outward degree of MultiDiGraph; See DegreeView"""
    ...
class EdgeViewABC(ABC): ...

class OutEdgeDataView(EdgeViewABC, Generic[_Node, _D]):
    """EdgeDataView for outward edges of DiGraph; See EdgeDataView"""
    def __init__(self, viewer, nbunch: _NBunch[_Node] = None, data: bool = False, *, default=None) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_D]: ...
    def __contains__(self, e: _Edge[_Node]) -> bool: ...

class EdgeDataView(OutEdgeDataView[_Node, _D]):
    """
    A EdgeDataView class for edges of Graph

    This view is primarily used to iterate over the edges reporting
    edges as node-tuples with edge data optionally reported. The
    argument `nbunch` allows restriction to edges incident to nodes
    in that container/singleton. The default (nbunch=None)
    reports all edges. The arguments `data` and `default` control
    what edge data is reported. The default `data is False` reports
    only node-tuples for each edge. If `data is True` the entire edge
    data dict is returned. Otherwise `data` is assumed to hold the name
    of the edge attribute to report with default `default` if  that
    edge attribute is not present.

    Parameters
    ----------
    nbunch : container of nodes, node or None (default None)
    data : False, True or string (default False)
    default : default value (default None)

    Examples
    --------
    >>> G = nx.path_graph(3)
    >>> G.add_edge(1, 2, foo="bar")
    >>> list(G.edges(data="foo", default="biz"))
    [(0, 1, 'biz'), (1, 2, 'bar')]
    >>> assert (0, 1, "biz") in G.edges(data="foo", default="biz")
    """
    ...
class InEdgeDataView(OutEdgeDataView[_Node, _D]):
    """An EdgeDataView class for outward edges of DiGraph; See EdgeDataView"""
    ...

class OutMultiEdgeDataView(OutEdgeDataView[_Node, _D]):
    """An EdgeDataView for outward edges of MultiDiGraph; See EdgeDataView"""
    keys: bool
    def __init__(
        self, viewer, nbunch: _NBunch[_Node] = None, data: bool = False, *, default=None, keys: bool = False
    ) -> None: ...

class MultiEdgeDataView(OutEdgeDataView[_Node, _D]):
    """An EdgeDataView class for edges of MultiGraph; See EdgeDataView"""
    ...
class InMultiEdgeDataView(OutEdgeDataView[_Node, _D]):
    """An EdgeDataView for inward edges of MultiDiGraph; See EdgeDataView"""
    ...

class OutEdgeView(AbstractSet[Incomplete], Mapping[Incomplete, Incomplete], EdgeViewABC, Generic[_Node]):
    """A EdgeView class for outward edges of a DiGraph"""
    def __init__(self, G: Graph[_Node]) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[tuple[_Node, _Node]]: ...
    def __contains__(self, e: _Edge[_Node]) -> bool: ...  # type: ignore[override]
    def __getitem__(self, e: _Edge[_Node]) -> dict[str, Any]: ...
    dataview = OutEdgeDataView
    @overload
    def __call__(self, nbunch: None = None, data: Literal[False] = False, *, default: Unused = None) -> Self: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(
        self, nbunch: _Node | Iterable[_Node], data: Literal[False] = False, *, default: None = None
    ) -> OutEdgeDataView[_Node, tuple[_Node, _Node]]: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node], data: Literal[True], *, default: None = None
    ) -> OutEdgeDataView[_Node, tuple[_Node, _Node, dict[str, Incomplete]]]: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node] = None, *, data: Literal[True], default: None = None
    ) -> OutEdgeDataView[_Node, tuple[_Node, _Node, dict[str, Incomplete]]]: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node], data: str, *, default: _U | None = None
    ) -> OutEdgeDataView[_Node, tuple[_Node, _Node, _U]]: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node] = None, *, data: str, default: _U | None = None
    ) -> OutEdgeDataView[_Node, tuple[_Node, _Node, _U]]: ...
    @overload
    def data(self, data: Literal[False], default: Unused = None, nbunch: None = None) -> Self:
        """
        Return a read-only view of edge data.

        Parameters
        ----------
        data : bool or edge attribute key
            If ``data=True``, then the data view maps each edge to a dictionary
            containing all of its attributes. If `data` is a key in the edge
            dictionary, then the data view maps each edge to its value for
            the keyed attribute. In this case, if the edge doesn't have the
            attribute, the `default` value is returned.
        default : object, default=None
            The value used when an edge does not have a specific attribute
        nbunch : container of nodes, optional (default=None)
            Allows restriction to edges only involving certain nodes. All edges
            are considered by default.

        Returns
        -------
        dataview
            Returns an `EdgeDataView` for undirected Graphs, `OutEdgeDataView`
            for DiGraphs, `MultiEdgeDataView` for MultiGraphs and
            `OutMultiEdgeDataView` for MultiDiGraphs.

        Notes
        -----
        If ``data=False``, returns an `EdgeView` without any edge data.

        See Also
        --------
        EdgeDataView
        OutEdgeDataView
        MultiEdgeDataView
        OutMultiEdgeDataView

        Examples
        --------
        >>> G = nx.Graph()
        >>> G.add_edges_from(
        ...     [
        ...         (0, 1, {"dist": 3, "capacity": 20}),
        ...         (1, 2, {"dist": 4}),
        ...         (2, 0, {"dist": 5}),
        ...     ]
        ... )

        Accessing edge data with ``data=True`` (the default) returns an
        edge data view object listing each edge with all of its attributes:

        >>> G.edges.data()
        EdgeDataView([(0, 1, {'dist': 3, 'capacity': 20}), (0, 2, {'dist': 5}), (1, 2, {'dist': 4})])

        If `data` represents a key in the edge attribute dict, a dataview listing
        each edge with its value for that specific key is returned:

        >>> G.edges.data("dist")
        EdgeDataView([(0, 1, 3), (0, 2, 5), (1, 2, 4)])

        `nbunch` can be used to limit the edges:

        >>> G.edges.data("dist", nbunch=[0])
        EdgeDataView([(0, 1, 3), (0, 2, 5)])

        If a specific key is not found in an edge attribute dict, the value
        specified by `default` is used:

        >>> G.edges.data("capacity")
        EdgeDataView([(0, 1, 20), (0, 2, None), (1, 2, None)])

        Note that there is no check that the `data` key is present in any of
        the edge attribute dictionaries:

        >>> G.edges.data("speed")
        EdgeDataView([(0, 1, None), (0, 2, None), (1, 2, None)])
        """
        ...
    @overload
    def data(
        self, data: Literal[True] = True, default: None = None, nbunch: _NBunch[_Node] = None
    ) -> OutEdgeDataView[_Node, tuple[_Node, _Node, dict[str, Incomplete]]]:
        """
        Return a read-only view of edge data.

        Parameters
        ----------
        data : bool or edge attribute key
            If ``data=True``, then the data view maps each edge to a dictionary
            containing all of its attributes. If `data` is a key in the edge
            dictionary, then the data view maps each edge to its value for
            the keyed attribute. In this case, if the edge doesn't have the
            attribute, the `default` value is returned.
        default : object, default=None
            The value used when an edge does not have a specific attribute
        nbunch : container of nodes, optional (default=None)
            Allows restriction to edges only involving certain nodes. All edges
            are considered by default.

        Returns
        -------
        dataview
            Returns an `EdgeDataView` for undirected Graphs, `OutEdgeDataView`
            for DiGraphs, `MultiEdgeDataView` for MultiGraphs and
            `OutMultiEdgeDataView` for MultiDiGraphs.

        Notes
        -----
        If ``data=False``, returns an `EdgeView` without any edge data.

        See Also
        --------
        EdgeDataView
        OutEdgeDataView
        MultiEdgeDataView
        OutMultiEdgeDataView

        Examples
        --------
        >>> G = nx.Graph()
        >>> G.add_edges_from(
        ...     [
        ...         (0, 1, {"dist": 3, "capacity": 20}),
        ...         (1, 2, {"dist": 4}),
        ...         (2, 0, {"dist": 5}),
        ...     ]
        ... )

        Accessing edge data with ``data=True`` (the default) returns an
        edge data view object listing each edge with all of its attributes:

        >>> G.edges.data()
        EdgeDataView([(0, 1, {'dist': 3, 'capacity': 20}), (0, 2, {'dist': 5}), (1, 2, {'dist': 4})])

        If `data` represents a key in the edge attribute dict, a dataview listing
        each edge with its value for that specific key is returned:

        >>> G.edges.data("dist")
        EdgeDataView([(0, 1, 3), (0, 2, 5), (1, 2, 4)])

        `nbunch` can be used to limit the edges:

        >>> G.edges.data("dist", nbunch=[0])
        EdgeDataView([(0, 1, 3), (0, 2, 5)])

        If a specific key is not found in an edge attribute dict, the value
        specified by `default` is used:

        >>> G.edges.data("capacity")
        EdgeDataView([(0, 1, 20), (0, 2, None), (1, 2, None)])

        Note that there is no check that the `data` key is present in any of
        the edge attribute dictionaries:

        >>> G.edges.data("speed")
        EdgeDataView([(0, 1, None), (0, 2, None), (1, 2, None)])
        """
        ...
    @overload
    def data(
        self, data: str, default: _U | None = None, nbunch: _NBunch[_Node] = None
    ) -> OutEdgeDataView[_Node, tuple[_Node, _Node, _U]]:
        """
        Return a read-only view of edge data.

        Parameters
        ----------
        data : bool or edge attribute key
            If ``data=True``, then the data view maps each edge to a dictionary
            containing all of its attributes. If `data` is a key in the edge
            dictionary, then the data view maps each edge to its value for
            the keyed attribute. In this case, if the edge doesn't have the
            attribute, the `default` value is returned.
        default : object, default=None
            The value used when an edge does not have a specific attribute
        nbunch : container of nodes, optional (default=None)
            Allows restriction to edges only involving certain nodes. All edges
            are considered by default.

        Returns
        -------
        dataview
            Returns an `EdgeDataView` for undirected Graphs, `OutEdgeDataView`
            for DiGraphs, `MultiEdgeDataView` for MultiGraphs and
            `OutMultiEdgeDataView` for MultiDiGraphs.

        Notes
        -----
        If ``data=False``, returns an `EdgeView` without any edge data.

        See Also
        --------
        EdgeDataView
        OutEdgeDataView
        MultiEdgeDataView
        OutMultiEdgeDataView

        Examples
        --------
        >>> G = nx.Graph()
        >>> G.add_edges_from(
        ...     [
        ...         (0, 1, {"dist": 3, "capacity": 20}),
        ...         (1, 2, {"dist": 4}),
        ...         (2, 0, {"dist": 5}),
        ...     ]
        ... )

        Accessing edge data with ``data=True`` (the default) returns an
        edge data view object listing each edge with all of its attributes:

        >>> G.edges.data()
        EdgeDataView([(0, 1, {'dist': 3, 'capacity': 20}), (0, 2, {'dist': 5}), (1, 2, {'dist': 4})])

        If `data` represents a key in the edge attribute dict, a dataview listing
        each edge with its value for that specific key is returned:

        >>> G.edges.data("dist")
        EdgeDataView([(0, 1, 3), (0, 2, 5), (1, 2, 4)])

        `nbunch` can be used to limit the edges:

        >>> G.edges.data("dist", nbunch=[0])
        EdgeDataView([(0, 1, 3), (0, 2, 5)])

        If a specific key is not found in an edge attribute dict, the value
        specified by `default` is used:

        >>> G.edges.data("capacity")
        EdgeDataView([(0, 1, 20), (0, 2, None), (1, 2, None)])

        Note that there is no check that the `data` key is present in any of
        the edge attribute dictionaries:

        >>> G.edges.data("speed")
        EdgeDataView([(0, 1, None), (0, 2, None), (1, 2, None)])
        """
        ...

class EdgeView(OutEdgeView[_Node]):
    """
    A EdgeView class for edges of a Graph

    This densely packed View allows iteration over edges, data lookup
    like a dict and set operations on edges represented by node-tuples.
    In addition, edge data can be controlled by calling this object
    possibly creating an EdgeDataView. Typically edges are iterated over
    and reported as `(u, v)` node tuples or `(u, v, key)` node/key tuples
    for multigraphs. Those edge representations can also be using to
    lookup the data dict for any edge. Set operations also are available
    where those tuples are the elements of the set.
    Calling this object with optional arguments `data`, `default` and `keys`
    controls the form of the tuple (see EdgeDataView). Optional argument
    `nbunch` allows restriction to edges only involving certain nodes.

    If `data is False` (the default) then iterate over 2-tuples `(u, v)`.
    If `data is True` iterate over 3-tuples `(u, v, datadict)`.
    Otherwise iterate over `(u, v, datadict.get(data, default))`.
    For Multigraphs, if `keys is True`, replace `u, v` with `u, v, key` above.

    Parameters
    ==========
    graph : NetworkX graph-like class
    nbunch : (default= all nodes in graph) only report edges with these nodes
    keys : (only for MultiGraph. default=False) report edge key in tuple
    data : bool or string (default=False) see above
    default : object (default=None)

    Examples
    ========
    >>> G = nx.path_graph(4)
    >>> EV = G.edges()
    >>> (2, 3) in EV
    True
    >>> for u, v in EV:
    ...     print((u, v))
    (0, 1)
    (1, 2)
    (2, 3)
    >>> assert EV & {(1, 2), (3, 4)} == {(1, 2)}

    >>> EVdata = G.edges(data="color", default="aqua")
    >>> G.add_edge(2, 3, color="blue")
    >>> assert (2, 3, "blue") in EVdata
    >>> for u, v, c in EVdata:
    ...     print(f"({u}, {v}) has color: {c}")
    (0, 1) has color: aqua
    (1, 2) has color: aqua
    (2, 3) has color: blue

    >>> EVnbunch = G.edges(nbunch=2)
    >>> assert (2, 3) in EVnbunch
    >>> assert (0, 1) not in EVnbunch
    >>> for u, v in EVnbunch:
    ...     assert u == 2 or v == 2

    >>> MG = nx.path_graph(4, create_using=nx.MultiGraph)
    >>> EVmulti = MG.edges(keys=True)
    >>> (2, 3, 0) in EVmulti
    True
    >>> (2, 3) in EVmulti  # 2-tuples work even when keys is True
    True
    >>> key = MG.add_edge(2, 3)
    >>> for u, v, k in EVmulti:
    ...     print((u, v, k))
    (0, 1, 0)
    (1, 2, 0)
    (2, 3, 0)
    (2, 3, 1)
    """
    dataview = EdgeDataView
    # Have to override parent's overloads with the proper return type based on dataview
    @overload
    def __call__(self, nbunch: None = None, data: Literal[False] = False, *, default: Unused = None) -> Self: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(
        self, nbunch: _Node | Iterable[_Node], data: Literal[False] = False, *, default: None = None
    ) -> EdgeDataView[_Node, tuple[_Node, _Node]]: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node], data: Literal[True], *, default: None = None
    ) -> EdgeDataView[_Node, tuple[_Node, _Node, dict[str, Incomplete]]]: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node] = None, *, data: Literal[True], default: None = None
    ) -> EdgeDataView[_Node, tuple[_Node, _Node, dict[str, Incomplete]]]: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node], data: str, *, default: _U | None = None
    ) -> EdgeDataView[_Node, tuple[_Node, _Node, _U]]: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node] = None, *, data: str, default: _U | None = None
    ) -> EdgeDataView[_Node, tuple[_Node, _Node, _U]]: ...
    @overload
    def data(self, data: Literal[False], default: Unused = None, nbunch: None = None) -> Self:
        """
        Return a read-only view of edge data.

        Parameters
        ----------
        data : bool or edge attribute key
            If ``data=True``, then the data view maps each edge to a dictionary
            containing all of its attributes. If `data` is a key in the edge
            dictionary, then the data view maps each edge to its value for
            the keyed attribute. In this case, if the edge doesn't have the
            attribute, the `default` value is returned.
        default : object, default=None
            The value used when an edge does not have a specific attribute
        nbunch : container of nodes, optional (default=None)
            Allows restriction to edges only involving certain nodes. All edges
            are considered by default.

        Returns
        -------
        dataview
            Returns an `EdgeDataView` for undirected Graphs, `OutEdgeDataView`
            for DiGraphs, `MultiEdgeDataView` for MultiGraphs and
            `OutMultiEdgeDataView` for MultiDiGraphs.

        Notes
        -----
        If ``data=False``, returns an `EdgeView` without any edge data.

        See Also
        --------
        EdgeDataView
        OutEdgeDataView
        MultiEdgeDataView
        OutMultiEdgeDataView

        Examples
        --------
        >>> G = nx.Graph()
        >>> G.add_edges_from(
        ...     [
        ...         (0, 1, {"dist": 3, "capacity": 20}),
        ...         (1, 2, {"dist": 4}),
        ...         (2, 0, {"dist": 5}),
        ...     ]
        ... )

        Accessing edge data with ``data=True`` (the default) returns an
        edge data view object listing each edge with all of its attributes:

        >>> G.edges.data()
        EdgeDataView([(0, 1, {'dist': 3, 'capacity': 20}), (0, 2, {'dist': 5}), (1, 2, {'dist': 4})])

        If `data` represents a key in the edge attribute dict, a dataview listing
        each edge with its value for that specific key is returned:

        >>> G.edges.data("dist")
        EdgeDataView([(0, 1, 3), (0, 2, 5), (1, 2, 4)])

        `nbunch` can be used to limit the edges:

        >>> G.edges.data("dist", nbunch=[0])
        EdgeDataView([(0, 1, 3), (0, 2, 5)])

        If a specific key is not found in an edge attribute dict, the value
        specified by `default` is used:

        >>> G.edges.data("capacity")
        EdgeDataView([(0, 1, 20), (0, 2, None), (1, 2, None)])

        Note that there is no check that the `data` key is present in any of
        the edge attribute dictionaries:

        >>> G.edges.data("speed")
        EdgeDataView([(0, 1, None), (0, 2, None), (1, 2, None)])
        """
        ...
    @overload
    def data(
        self, data: Literal[True] = True, default: None = None, nbunch: _NBunch[_Node] = None
    ) -> EdgeDataView[_Node, tuple[_Node, _Node, dict[str, Incomplete]]]:
        """
        Return a read-only view of edge data.

        Parameters
        ----------
        data : bool or edge attribute key
            If ``data=True``, then the data view maps each edge to a dictionary
            containing all of its attributes. If `data` is a key in the edge
            dictionary, then the data view maps each edge to its value for
            the keyed attribute. In this case, if the edge doesn't have the
            attribute, the `default` value is returned.
        default : object, default=None
            The value used when an edge does not have a specific attribute
        nbunch : container of nodes, optional (default=None)
            Allows restriction to edges only involving certain nodes. All edges
            are considered by default.

        Returns
        -------
        dataview
            Returns an `EdgeDataView` for undirected Graphs, `OutEdgeDataView`
            for DiGraphs, `MultiEdgeDataView` for MultiGraphs and
            `OutMultiEdgeDataView` for MultiDiGraphs.

        Notes
        -----
        If ``data=False``, returns an `EdgeView` without any edge data.

        See Also
        --------
        EdgeDataView
        OutEdgeDataView
        MultiEdgeDataView
        OutMultiEdgeDataView

        Examples
        --------
        >>> G = nx.Graph()
        >>> G.add_edges_from(
        ...     [
        ...         (0, 1, {"dist": 3, "capacity": 20}),
        ...         (1, 2, {"dist": 4}),
        ...         (2, 0, {"dist": 5}),
        ...     ]
        ... )

        Accessing edge data with ``data=True`` (the default) returns an
        edge data view object listing each edge with all of its attributes:

        >>> G.edges.data()
        EdgeDataView([(0, 1, {'dist': 3, 'capacity': 20}), (0, 2, {'dist': 5}), (1, 2, {'dist': 4})])

        If `data` represents a key in the edge attribute dict, a dataview listing
        each edge with its value for that specific key is returned:

        >>> G.edges.data("dist")
        EdgeDataView([(0, 1, 3), (0, 2, 5), (1, 2, 4)])

        `nbunch` can be used to limit the edges:

        >>> G.edges.data("dist", nbunch=[0])
        EdgeDataView([(0, 1, 3), (0, 2, 5)])

        If a specific key is not found in an edge attribute dict, the value
        specified by `default` is used:

        >>> G.edges.data("capacity")
        EdgeDataView([(0, 1, 20), (0, 2, None), (1, 2, None)])

        Note that there is no check that the `data` key is present in any of
        the edge attribute dictionaries:

        >>> G.edges.data("speed")
        EdgeDataView([(0, 1, None), (0, 2, None), (1, 2, None)])
        """
        ...
    @overload
    def data(
        self, data: str, default: _U | None = None, nbunch: _NBunch[_Node] = None
    ) -> EdgeDataView[_Node, tuple[_Node, _Node, _U]]:
        """
        Return a read-only view of edge data.

        Parameters
        ----------
        data : bool or edge attribute key
            If ``data=True``, then the data view maps each edge to a dictionary
            containing all of its attributes. If `data` is a key in the edge
            dictionary, then the data view maps each edge to its value for
            the keyed attribute. In this case, if the edge doesn't have the
            attribute, the `default` value is returned.
        default : object, default=None
            The value used when an edge does not have a specific attribute
        nbunch : container of nodes, optional (default=None)
            Allows restriction to edges only involving certain nodes. All edges
            are considered by default.

        Returns
        -------
        dataview
            Returns an `EdgeDataView` for undirected Graphs, `OutEdgeDataView`
            for DiGraphs, `MultiEdgeDataView` for MultiGraphs and
            `OutMultiEdgeDataView` for MultiDiGraphs.

        Notes
        -----
        If ``data=False``, returns an `EdgeView` without any edge data.

        See Also
        --------
        EdgeDataView
        OutEdgeDataView
        MultiEdgeDataView
        OutMultiEdgeDataView

        Examples
        --------
        >>> G = nx.Graph()
        >>> G.add_edges_from(
        ...     [
        ...         (0, 1, {"dist": 3, "capacity": 20}),
        ...         (1, 2, {"dist": 4}),
        ...         (2, 0, {"dist": 5}),
        ...     ]
        ... )

        Accessing edge data with ``data=True`` (the default) returns an
        edge data view object listing each edge with all of its attributes:

        >>> G.edges.data()
        EdgeDataView([(0, 1, {'dist': 3, 'capacity': 20}), (0, 2, {'dist': 5}), (1, 2, {'dist': 4})])

        If `data` represents a key in the edge attribute dict, a dataview listing
        each edge with its value for that specific key is returned:

        >>> G.edges.data("dist")
        EdgeDataView([(0, 1, 3), (0, 2, 5), (1, 2, 4)])

        `nbunch` can be used to limit the edges:

        >>> G.edges.data("dist", nbunch=[0])
        EdgeDataView([(0, 1, 3), (0, 2, 5)])

        If a specific key is not found in an edge attribute dict, the value
        specified by `default` is used:

        >>> G.edges.data("capacity")
        EdgeDataView([(0, 1, 20), (0, 2, None), (1, 2, None)])

        Note that there is no check that the `data` key is present in any of
        the edge attribute dictionaries:

        >>> G.edges.data("speed")
        EdgeDataView([(0, 1, None), (0, 2, None), (1, 2, None)])
        """
        ...

class InEdgeView(OutEdgeView[_Node]):
    """A EdgeView class for inward edges of a DiGraph"""
    dataview = InEdgeDataView
    # Have to override parent's overloads with the proper return type based on dataview
    @overload
    def __call__(self, nbunch: None = None, data: Literal[False] = False, *, default: Unused = None) -> Self: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(
        self, nbunch: _Node | Iterable[_Node], data: Literal[False] = False, *, default: None = None
    ) -> InEdgeDataView[_Node, tuple[_Node, _Node]]: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node], data: Literal[True], *, default: None = None
    ) -> InEdgeDataView[_Node, tuple[_Node, _Node, dict[str, Incomplete]]]: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node] = None, *, data: Literal[True], default: None = None
    ) -> InEdgeDataView[_Node, tuple[_Node, _Node, dict[str, Incomplete]]]: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node], data: str, *, default: _U | None = None
    ) -> InEdgeDataView[_Node, tuple[_Node, _Node, _U]]: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node] = None, *, data: str, default: _U | None = None
    ) -> InEdgeDataView[_Node, tuple[_Node, _Node, _U]]: ...
    @overload
    def data(self, data: Literal[False], default: Unused = None, nbunch: None = None) -> Self:
        """
        Return a read-only view of edge data.

        Parameters
        ----------
        data : bool or edge attribute key
            If ``data=True``, then the data view maps each edge to a dictionary
            containing all of its attributes. If `data` is a key in the edge
            dictionary, then the data view maps each edge to its value for
            the keyed attribute. In this case, if the edge doesn't have the
            attribute, the `default` value is returned.
        default : object, default=None
            The value used when an edge does not have a specific attribute
        nbunch : container of nodes, optional (default=None)
            Allows restriction to edges only involving certain nodes. All edges
            are considered by default.

        Returns
        -------
        dataview
            Returns an `EdgeDataView` for undirected Graphs, `OutEdgeDataView`
            for DiGraphs, `MultiEdgeDataView` for MultiGraphs and
            `OutMultiEdgeDataView` for MultiDiGraphs.

        Notes
        -----
        If ``data=False``, returns an `EdgeView` without any edge data.

        See Also
        --------
        EdgeDataView
        OutEdgeDataView
        MultiEdgeDataView
        OutMultiEdgeDataView

        Examples
        --------
        >>> G = nx.Graph()
        >>> G.add_edges_from(
        ...     [
        ...         (0, 1, {"dist": 3, "capacity": 20}),
        ...         (1, 2, {"dist": 4}),
        ...         (2, 0, {"dist": 5}),
        ...     ]
        ... )

        Accessing edge data with ``data=True`` (the default) returns an
        edge data view object listing each edge with all of its attributes:

        >>> G.edges.data()
        EdgeDataView([(0, 1, {'dist': 3, 'capacity': 20}), (0, 2, {'dist': 5}), (1, 2, {'dist': 4})])

        If `data` represents a key in the edge attribute dict, a dataview listing
        each edge with its value for that specific key is returned:

        >>> G.edges.data("dist")
        EdgeDataView([(0, 1, 3), (0, 2, 5), (1, 2, 4)])

        `nbunch` can be used to limit the edges:

        >>> G.edges.data("dist", nbunch=[0])
        EdgeDataView([(0, 1, 3), (0, 2, 5)])

        If a specific key is not found in an edge attribute dict, the value
        specified by `default` is used:

        >>> G.edges.data("capacity")
        EdgeDataView([(0, 1, 20), (0, 2, None), (1, 2, None)])

        Note that there is no check that the `data` key is present in any of
        the edge attribute dictionaries:

        >>> G.edges.data("speed")
        EdgeDataView([(0, 1, None), (0, 2, None), (1, 2, None)])
        """
        ...
    @overload
    def data(
        self, data: Literal[True] = True, default: None = None, nbunch: _NBunch[_Node] = None
    ) -> InEdgeDataView[_Node, tuple[_Node, _Node, dict[str, Incomplete]]]:
        """
        Return a read-only view of edge data.

        Parameters
        ----------
        data : bool or edge attribute key
            If ``data=True``, then the data view maps each edge to a dictionary
            containing all of its attributes. If `data` is a key in the edge
            dictionary, then the data view maps each edge to its value for
            the keyed attribute. In this case, if the edge doesn't have the
            attribute, the `default` value is returned.
        default : object, default=None
            The value used when an edge does not have a specific attribute
        nbunch : container of nodes, optional (default=None)
            Allows restriction to edges only involving certain nodes. All edges
            are considered by default.

        Returns
        -------
        dataview
            Returns an `EdgeDataView` for undirected Graphs, `OutEdgeDataView`
            for DiGraphs, `MultiEdgeDataView` for MultiGraphs and
            `OutMultiEdgeDataView` for MultiDiGraphs.

        Notes
        -----
        If ``data=False``, returns an `EdgeView` without any edge data.

        See Also
        --------
        EdgeDataView
        OutEdgeDataView
        MultiEdgeDataView
        OutMultiEdgeDataView

        Examples
        --------
        >>> G = nx.Graph()
        >>> G.add_edges_from(
        ...     [
        ...         (0, 1, {"dist": 3, "capacity": 20}),
        ...         (1, 2, {"dist": 4}),
        ...         (2, 0, {"dist": 5}),
        ...     ]
        ... )

        Accessing edge data with ``data=True`` (the default) returns an
        edge data view object listing each edge with all of its attributes:

        >>> G.edges.data()
        EdgeDataView([(0, 1, {'dist': 3, 'capacity': 20}), (0, 2, {'dist': 5}), (1, 2, {'dist': 4})])

        If `data` represents a key in the edge attribute dict, a dataview listing
        each edge with its value for that specific key is returned:

        >>> G.edges.data("dist")
        EdgeDataView([(0, 1, 3), (0, 2, 5), (1, 2, 4)])

        `nbunch` can be used to limit the edges:

        >>> G.edges.data("dist", nbunch=[0])
        EdgeDataView([(0, 1, 3), (0, 2, 5)])

        If a specific key is not found in an edge attribute dict, the value
        specified by `default` is used:

        >>> G.edges.data("capacity")
        EdgeDataView([(0, 1, 20), (0, 2, None), (1, 2, None)])

        Note that there is no check that the `data` key is present in any of
        the edge attribute dictionaries:

        >>> G.edges.data("speed")
        EdgeDataView([(0, 1, None), (0, 2, None), (1, 2, None)])
        """
        ...
    @overload
    def data(
        self, data: str, default: _U | None = None, nbunch: _NBunch[_Node] = None
    ) -> InEdgeDataView[_Node, tuple[_Node, _Node, _U]]:
        """
        Return a read-only view of edge data.

        Parameters
        ----------
        data : bool or edge attribute key
            If ``data=True``, then the data view maps each edge to a dictionary
            containing all of its attributes. If `data` is a key in the edge
            dictionary, then the data view maps each edge to its value for
            the keyed attribute. In this case, if the edge doesn't have the
            attribute, the `default` value is returned.
        default : object, default=None
            The value used when an edge does not have a specific attribute
        nbunch : container of nodes, optional (default=None)
            Allows restriction to edges only involving certain nodes. All edges
            are considered by default.

        Returns
        -------
        dataview
            Returns an `EdgeDataView` for undirected Graphs, `OutEdgeDataView`
            for DiGraphs, `MultiEdgeDataView` for MultiGraphs and
            `OutMultiEdgeDataView` for MultiDiGraphs.

        Notes
        -----
        If ``data=False``, returns an `EdgeView` without any edge data.

        See Also
        --------
        EdgeDataView
        OutEdgeDataView
        MultiEdgeDataView
        OutMultiEdgeDataView

        Examples
        --------
        >>> G = nx.Graph()
        >>> G.add_edges_from(
        ...     [
        ...         (0, 1, {"dist": 3, "capacity": 20}),
        ...         (1, 2, {"dist": 4}),
        ...         (2, 0, {"dist": 5}),
        ...     ]
        ... )

        Accessing edge data with ``data=True`` (the default) returns an
        edge data view object listing each edge with all of its attributes:

        >>> G.edges.data()
        EdgeDataView([(0, 1, {'dist': 3, 'capacity': 20}), (0, 2, {'dist': 5}), (1, 2, {'dist': 4})])

        If `data` represents a key in the edge attribute dict, a dataview listing
        each edge with its value for that specific key is returned:

        >>> G.edges.data("dist")
        EdgeDataView([(0, 1, 3), (0, 2, 5), (1, 2, 4)])

        `nbunch` can be used to limit the edges:

        >>> G.edges.data("dist", nbunch=[0])
        EdgeDataView([(0, 1, 3), (0, 2, 5)])

        If a specific key is not found in an edge attribute dict, the value
        specified by `default` is used:

        >>> G.edges.data("capacity")
        EdgeDataView([(0, 1, 20), (0, 2, None), (1, 2, None)])

        Note that there is no check that the `data` key is present in any of
        the edge attribute dictionaries:

        >>> G.edges.data("speed")
        EdgeDataView([(0, 1, None), (0, 2, None), (1, 2, None)])
        """
        ...

class OutMultiEdgeView(OutEdgeView[_Node]):
    """A EdgeView class for outward edges of a MultiDiGraph"""
    def __iter__(self) -> Iterator[tuple[_Node, _Node, Incomplete]]: ...  # type: ignore[override]
    def __getitem__(self, e: tuple[_Node, _Node, Incomplete]) -> dict[str, Any]: ...  # type: ignore[override]
    dataview = OutMultiEdgeDataView
    @overload  # type: ignore[override]  # Has an additional `keys` keyword argument
    def __call__(  # type: ignore[overload-overlap]
        self, nbunch: None = None, data: Literal[False] = False, *, default: Unused = None, keys: Literal[True]
    ) -> Self: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node] = None, data: Literal[False] = False, *, default: None = None, keys: Literal[False] = False
    ) -> OutMultiEdgeDataView[_Node, tuple[_Node, _Node]]: ...
    @overload
    def __call__(
        self, nbunch: _Node | Iterable[_Node], data: Literal[False] = False, *, default: None = None, keys: Literal[True]
    ) -> OutMultiEdgeDataView[_Node, tuple[_Node, _Node, Incomplete]]: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node] = None, *, data: Literal[True], default: None = None, keys: Literal[True]
    ) -> OutMultiEdgeDataView[_Node, tuple[_Node, _Node, Incomplete, dict[str, Incomplete]]]: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node], data: Literal[True], *, default: None = None, keys: Literal[True]
    ) -> OutMultiEdgeDataView[_Node, tuple[_Node, _Node, Incomplete, dict[str, Incomplete]]]: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node] = None, *, data: Literal[True], default: None = None, keys: Literal[False] = False
    ) -> OutMultiEdgeDataView[_Node, tuple[_Node, _Node, dict[str, Incomplete]]]: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node], data: str, *, default: _U | None = None, keys: Literal[False] = False
    ) -> OutMultiEdgeDataView[_Node, tuple[_Node, _Node, _U]]: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node] = None, *, data: str, default: _U | None = None, keys: Literal[True]
    ) -> OutMultiEdgeDataView[_Node, tuple[_Node, _Node, Incomplete, _U]]: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node] = None, *, data: str, default: _U | None = None, keys: Literal[False] = False
    ) -> OutMultiEdgeDataView[_Node, tuple[_Node, _Node, _U]]: ...
    @overload  # type: ignore[override]
    def data(self, data: Literal[False], default: Unused = None, nbunch: None = None, *, keys: Literal[True]) -> Self: ...
    @overload
    def data(
        self, data: Literal[False], default: None = None, nbunch: _NBunch[_Node] = None, keys: Literal[False] = False
    ) -> OutMultiEdgeDataView[_Node, tuple[_Node, _Node]]: ...
    @overload
    def data(
        self, data: Literal[True] = True, default: None = None, nbunch: _NBunch[_Node] = None, keys: Literal[False] = False
    ) -> OutMultiEdgeDataView[_Node, tuple[_Node, _Node, dict[str, Incomplete]]]: ...
    @overload
    def data(
        self, data: Literal[True] = True, default: None = None, nbunch: _NBunch[_Node] = None, *, keys: Literal[True]
    ) -> OutMultiEdgeDataView[_Node, tuple[_Node, _Node, Incomplete, dict[str, Incomplete]]]: ...
    @overload
    def data(
        self, data: str, default: _U | None = None, nbunch: _NBunch[_Node] = None, keys: Literal[False] = False
    ) -> OutMultiEdgeDataView[_Node, tuple[_Node, _Node, _U]]: ...
    @overload
    def data(
        self, data: str, default: _U | None = None, nbunch: _NBunch[_Node] = None, *, keys: Literal[True]
    ) -> OutMultiEdgeDataView[_Node, tuple[_Node, _Node, Incomplete, _U]]: ...

class MultiEdgeView(OutMultiEdgeView[_Node]):
    """A EdgeView class for edges of a MultiGraph"""
    dataview = MultiEdgeDataView  # type: ignore[assignment]
    # Have to override parent's overloads with the proper return type based on dataview
    @overload  # type: ignore[override]  # Has an additional `keys` keyword argument
    def __call__(  # type: ignore[overload-overlap]
        self, nbunch: None = None, data: Literal[False] = False, *, default: Unused = None, keys: Literal[True]
    ) -> Self: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node] = None, data: Literal[False] = False, *, default: None = None, keys: Literal[False] = False
    ) -> MultiEdgeDataView[_Node, tuple[_Node, _Node]]: ...
    @overload
    def __call__(
        self, nbunch: _Node | Iterable[_Node], data: Literal[False] = False, *, default: None = None, keys: Literal[True]
    ) -> MultiEdgeDataView[_Node, tuple[_Node, _Node, Incomplete]]: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node] = None, *, data: Literal[True], default: None = None, keys: Literal[True]
    ) -> MultiEdgeDataView[_Node, tuple[_Node, _Node, Incomplete, dict[str, Incomplete]]]: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node], data: Literal[True], *, default: None = None, keys: Literal[True]
    ) -> MultiEdgeDataView[_Node, tuple[_Node, _Node, Incomplete, dict[str, Incomplete]]]: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node] = None, *, data: Literal[True], default: None = None, keys: Literal[False] = False
    ) -> MultiEdgeDataView[_Node, tuple[_Node, _Node, dict[str, Incomplete]]]: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node], data: str, *, default: _U | None = None, keys: Literal[False] = False
    ) -> MultiEdgeDataView[_Node, tuple[_Node, _Node, _U]]: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node] = None, *, data: str, default: _U | None = None, keys: Literal[True]
    ) -> MultiEdgeDataView[_Node, tuple[_Node, _Node, Incomplete, _U]]: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node] = None, *, data: str, default: _U | None = None, keys: Literal[False] = False
    ) -> MultiEdgeDataView[_Node, tuple[_Node, _Node, _U]]: ...
    @overload  # type: ignore[override]
    def data(self, data: Literal[False], default: Unused = None, nbunch: None = None, *, keys: Literal[True]) -> Self: ...
    @overload
    def data(
        self, data: Literal[False], default: None = None, nbunch: _NBunch[_Node] = None, keys: Literal[False] = False
    ) -> MultiEdgeDataView[_Node, tuple[_Node, _Node]]: ...
    @overload
    def data(
        self, data: Literal[True] = True, default: None = None, nbunch: _NBunch[_Node] = None, keys: Literal[False] = False
    ) -> MultiEdgeDataView[_Node, tuple[_Node, _Node, dict[str, Incomplete]]]: ...
    @overload
    def data(
        self, data: Literal[True] = True, default: None = None, nbunch: _NBunch[_Node] = None, *, keys: Literal[True]
    ) -> MultiEdgeDataView[_Node, tuple[_Node, _Node, Incomplete, dict[str, Incomplete]]]: ...
    @overload
    def data(
        self, data: str, default: _U | None = None, nbunch: _NBunch[_Node] = None, keys: Literal[False] = False
    ) -> MultiEdgeDataView[_Node, tuple[_Node, _Node, _U]]: ...
    @overload
    def data(
        self, data: str, default: _U | None = None, nbunch: _NBunch[_Node] = None, *, keys: Literal[True]
    ) -> MultiEdgeDataView[_Node, tuple[_Node, _Node, Incomplete, _U]]: ...

class InMultiEdgeView(OutMultiEdgeView[_Node]):
    """A EdgeView class for inward edges of a MultiDiGraph"""
    dataview = InMultiEdgeDataView  # type: ignore[assignment]
    # Have to override parent's overloads with the proper return type based on dataview
    @overload  # type: ignore[override]
    def __call__(  # type: ignore[overload-overlap]
        self, nbunch: None = None, data: Literal[False] = False, *, default: Unused = None, keys: Literal[True]
    ) -> Self: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node] = None, data: Literal[False] = False, *, default: None = None, keys: Literal[False] = False
    ) -> InMultiEdgeDataView[_Node, tuple[_Node, _Node]]: ...
    @overload
    def __call__(
        self, nbunch: _Node | Iterable[_Node], data: Literal[False] = False, *, default: None = None, keys: Literal[True]
    ) -> InMultiEdgeDataView[_Node, tuple[_Node, _Node, Incomplete]]: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node] = None, *, data: Literal[True], default: None = None, keys: Literal[True]
    ) -> InMultiEdgeDataView[_Node, tuple[_Node, _Node, Incomplete, dict[str, Incomplete]]]: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node], data: Literal[True], *, default: None = None, keys: Literal[True]
    ) -> InMultiEdgeDataView[_Node, tuple[_Node, _Node, Incomplete, dict[str, Incomplete]]]: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node] = None, *, data: Literal[True], default: None = None, keys: Literal[False] = False
    ) -> InMultiEdgeDataView[_Node, tuple[_Node, _Node, dict[str, Incomplete]]]: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node], data: str, *, default: _U | None = None, keys: Literal[False] = False
    ) -> InMultiEdgeDataView[_Node, tuple[_Node, _Node, _U]]: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node] = None, *, data: str, default: _U | None = None, keys: Literal[True]
    ) -> InMultiEdgeDataView[_Node, tuple[_Node, _Node, Incomplete, _U]]: ...
    @overload
    def __call__(
        self, nbunch: _NBunch[_Node] = None, *, data: str, default: _U | None = None, keys: Literal[False] = False
    ) -> InMultiEdgeDataView[_Node, tuple[_Node, _Node, _U]]: ...
    @overload  # type: ignore[override]
    def data(self, data: Literal[False], default: Unused = None, nbunch: None = None, *, keys: Literal[True]) -> Self: ...
    @overload
    def data(
        self, data: Literal[False], default: None = None, nbunch: _NBunch[_Node] = None, keys: Literal[False] = False
    ) -> InMultiEdgeDataView[_Node, tuple[_Node, _Node]]: ...
    @overload
    def data(
        self, data: Literal[True] = True, default: None = None, nbunch: _NBunch[_Node] = None, keys: Literal[False] = False
    ) -> InMultiEdgeDataView[_Node, tuple[_Node, _Node, dict[str, Incomplete]]]: ...
    @overload
    def data(
        self, data: Literal[True] = True, default: None = None, nbunch: _NBunch[_Node] = None, *, keys: Literal[True]
    ) -> InMultiEdgeDataView[_Node, tuple[_Node, _Node, Incomplete, dict[str, Incomplete]]]: ...
    @overload
    def data(
        self, data: str, default: _U | None = None, nbunch: _NBunch[_Node] = None, keys: Literal[False] = False
    ) -> InMultiEdgeDataView[_Node, tuple[_Node, _Node, _U]]: ...
    @overload
    def data(
        self, data: str, default: _U | None = None, nbunch: _NBunch[_Node] = None, *, keys: Literal[True]
    ) -> InMultiEdgeDataView[_Node, tuple[_Node, _Node, Incomplete, _U]]: ...
