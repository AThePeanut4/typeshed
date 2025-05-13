"""Base class for MultiGraph."""

from _typeshed import Incomplete
from functools import cached_property
from typing import ClassVar
from typing_extensions import TypeAlias

from networkx.classes.coreviews import MultiAdjacencyView
from networkx.classes.graph import Graph, _MapFactory, _Node
from networkx.classes.multidigraph import MultiDiGraph
from networkx.classes.reportviews import OutMultiEdgeView

_MultiEdge: TypeAlias = tuple[_Node, _Node, int]  # noqa: Y047

__all__ = ["MultiGraph"]

class MultiGraph(Graph[_Node]):
    edge_key_dict_factory: ClassVar[_MapFactory]
    def __init__(self, incoming_graph_data: Incomplete | None = None, multigraph_input: bool | None = None, **attr) -> None: ...
    @cached_property
    def adj(self) -> MultiAdjacencyView[_Node, _Node, dict[str, Incomplete]]:
        """
        Graph adjacency object holding the neighbors of each node.

        This object is a read-only dict-like structure with node keys
        and neighbor-dict values.  The neighbor-dict is keyed by neighbor
        to the edgekey-data-dict.  So `G.adj[3][2][0]['color'] = 'blue'` sets
        the color of the edge `(3, 2, 0)` to `"blue"`.

        Iterating over G.adj behaves like a dict. Useful idioms include
        `for nbr, edgesdict in G.adj[n].items():`.

        The neighbor information is also provided by subscripting the graph.

        Examples
        --------
        >>> e = [(1, 2), (1, 2), (1, 3), (3, 4)]  # list of edges
        >>> G = nx.MultiGraph(e)
        >>> G.edges[1, 2, 0]["weight"] = 3
        >>> result = set()
        >>> for edgekey, data in G[1][2].items():
        ...     result.add(data.get("weight", 1))
        >>> result
        {1, 3}

        For directed graphs, `G.adj` holds outgoing (successor) info.
        """
        ...
    def new_edge_key(self, u: _Node, v: _Node) -> int:
        """
        Returns an unused key for edges between nodes `u` and `v`.

        The nodes `u` and `v` do not need to be already in the graph.

        Notes
        -----
        In the standard MultiGraph class the new key is the number of existing
        edges between `u` and `v` (increased if necessary to ensure unused).
        The first edge will have key 0, then 1, etc. If an edge is removed
        further new_edge_keys may not be in this order.

        Parameters
        ----------
        u, v : nodes

        Returns
        -------
        key : int
        """
        ...
    def add_edge(self, u_for_edge, v_for_edge, key: Incomplete | None = None, **attr):
        """
        Add an edge between u and v.

        The nodes u and v will be automatically added if they are
        not already in the graph.

        Edge attributes can be specified with keywords or by directly
        accessing the edge's attribute dictionary. See examples below.

        Parameters
        ----------
        u_for_edge, v_for_edge : nodes
            Nodes can be, for example, strings or numbers.
            Nodes must be hashable (and not None) Python objects.
        key : hashable identifier, optional (default=lowest unused integer)
            Used to distinguish multiedges between a pair of nodes.
        attr : keyword arguments, optional
            Edge data (or labels or objects) can be assigned using
            keyword arguments.

        Returns
        -------
        The edge key assigned to the edge.

        See Also
        --------
        add_edges_from : add a collection of edges

        Notes
        -----
        To replace/update edge data, use the optional key argument
        to identify a unique edge.  Otherwise a new edge will be created.

        NetworkX algorithms designed for weighted graphs cannot use
        multigraphs directly because it is not clear how to handle
        multiedge weights.  Convert to Graph using edge attribute
        'weight' to enable weighted graph algorithms.

        Default keys are generated using the method `new_edge_key()`.
        This method can be overridden by subclassing the base class and
        providing a custom `new_edge_key()` method.

        Examples
        --------
        The following each add an additional edge e=(1, 2) to graph G:

        >>> G = nx.MultiGraph()
        >>> e = (1, 2)
        >>> ekey = G.add_edge(1, 2)  # explicit two-node form
        >>> G.add_edge(*e)  # single edge as tuple of two nodes
        1
        >>> G.add_edges_from([(1, 2)])  # add edges from iterable container
        [2]

        Associate data to edges using keywords:

        >>> ekey = G.add_edge(1, 2, weight=3)
        >>> ekey = G.add_edge(1, 2, key=0, weight=4)  # update data for key=0
        >>> ekey = G.add_edge(1, 3, weight=7, capacity=15, length=342.7)

        For non-string attribute keys, use subscript notation.

        >>> ekey = G.add_edge(1, 2)
        >>> G[1][2][0].update({0: 5})
        >>> G.edges[1, 2, 0].update({0: 5})
        """
        ...
    def remove_edge(self, u, v, key: Incomplete | None = None):
        """
        Remove an edge between u and v.

        Parameters
        ----------
        u, v : nodes
            Remove an edge between nodes u and v.
        key : hashable identifier, optional (default=None)
            Used to distinguish multiple edges between a pair of nodes.
            If None, remove a single edge between u and v. If there are
            multiple edges, removes the last edge added in terms of
            insertion order.

        Raises
        ------
        NetworkXError
            If there is not an edge between u and v, or
            if there is no edge with the specified key.

        See Also
        --------
        remove_edges_from : remove a collection of edges

        Examples
        --------
        >>> G = nx.MultiGraph()
        >>> nx.add_path(G, [0, 1, 2, 3])
        >>> G.remove_edge(0, 1)
        >>> e = (1, 2)
        >>> G.remove_edge(*e)  # unpacks e from an edge tuple

        For multiple edges

        >>> G = nx.MultiGraph()  # or MultiDiGraph, etc
        >>> G.add_edges_from([(1, 2), (1, 2), (1, 2)])  # key_list returned
        [0, 1, 2]

        When ``key=None`` (the default), edges are removed in the opposite
        order that they were added:

        >>> G.remove_edge(1, 2)
        >>> G.edges(keys=True)
        MultiEdgeView([(1, 2, 0), (1, 2, 1)])
        >>> G.remove_edge(2, 1)  # edges are not directed
        >>> G.edges(keys=True)
        MultiEdgeView([(1, 2, 0)])

        For edges with keys

        >>> G = nx.MultiGraph()
        >>> G.add_edge(1, 2, key="first")
        'first'
        >>> G.add_edge(1, 2, key="second")
        'second'
        >>> G.remove_edge(1, 2, key="first")
        >>> G.edges(keys=True)
        MultiEdgeView([(1, 2, 'second')])
        """
        ...
    def has_edge(self, u, v, key: Incomplete | None = None):
        """
        Returns True if the graph has an edge between nodes u and v.

        This is the same as `v in G[u] or key in G[u][v]`
        without KeyError exceptions.

        Parameters
        ----------
        u, v : nodes
            Nodes can be, for example, strings or numbers.

        key : hashable identifier, optional (default=None)
            If specified return True only if the edge with
            key is found.

        Returns
        -------
        edge_ind : bool
            True if edge is in the graph, False otherwise.

        Examples
        --------
        Can be called either using two nodes u, v, an edge tuple (u, v),
        or an edge tuple (u, v, key).

        >>> G = nx.MultiGraph()  # or MultiDiGraph
        >>> nx.add_path(G, [0, 1, 2, 3])
        >>> G.has_edge(0, 1)  # using two nodes
        True
        >>> e = (0, 1)
        >>> G.has_edge(*e)  #  e is a 2-tuple (u, v)
        True
        >>> G.add_edge(0, 1, key="a")
        'a'
        >>> G.has_edge(0, 1, key="a")  # specify key
        True
        >>> G.has_edge(1, 0, key="a")  # edges aren't directed
        True
        >>> e = (0, 1, "a")
        >>> G.has_edge(*e)  # e is a 3-tuple (u, v, 'a')
        True

        The following syntax are equivalent:

        >>> G.has_edge(0, 1)
        True
        >>> 1 in G[0]  # though this gives :exc:`KeyError` if 0 not in G
        True
        >>> 0 in G[1]  # other order; also gives :exc:`KeyError` if 0 not in G
        True
        """
        ...
    def get_edge_data(  # type: ignore[override]  # Has an additional `key` keyword argument
        self, u, v, key: Incomplete | None = None, default: Incomplete | None = None
    ):
        """
        Returns the attribute dictionary associated with edge (u, v,
        key).

        If a key is not provided, returns a dictionary mapping edge keys
        to attribute dictionaries for each edge between u and v.

        This is identical to `G[u][v][key]` except the default is returned
        instead of an exception is the edge doesn't exist.

        Parameters
        ----------
        u, v : nodes

        default :  any Python object (default=None)
            Value to return if the specific edge (u, v, key) is not
            found, OR if there are no edges between u and v and no key
            is specified.

        key : hashable identifier, optional (default=None)
            Return data only for the edge with specified key, as an
            attribute dictionary (rather than a dictionary mapping keys
            to attribute dictionaries).

        Returns
        -------
        edge_dict : dictionary
            The edge attribute dictionary, OR a dictionary mapping edge
            keys to attribute dictionaries for each of those edges if no
            specific key is provided (even if there's only one edge
            between u and v).

        Examples
        --------
        >>> G = nx.MultiGraph()  # or MultiDiGraph
        >>> key = G.add_edge(0, 1, key="a", weight=7)
        >>> G[0][1]["a"]  # key='a'
        {'weight': 7}
        >>> G.edges[0, 1, "a"]  # key='a'
        {'weight': 7}

        Warning: we protect the graph data structure by making
        `G.edges` and `G[1][2]` read-only dict-like structures.
        However, you can assign values to attributes in e.g.
        `G.edges[1, 2, 'a']` or `G[1][2]['a']` using an additional
        bracket as shown next. You need to specify all edge info
        to assign to the edge data associated with an edge.

        >>> G[0][1]["a"]["weight"] = 10
        >>> G.edges[0, 1, "a"]["weight"] = 10
        >>> G[0][1]["a"]["weight"]
        10
        >>> G.edges[1, 0, "a"]["weight"]
        10

        >>> G = nx.MultiGraph()  # or MultiDiGraph
        >>> nx.add_path(G, [0, 1, 2, 3])
        >>> G.edges[0, 1, 0]["weight"] = 5
        >>> G.get_edge_data(0, 1)
        {0: {'weight': 5}}
        >>> e = (0, 1)
        >>> G.get_edge_data(*e)  # tuple form
        {0: {'weight': 5}}
        >>> G.get_edge_data(3, 0)  # edge not in graph, returns None
        >>> G.get_edge_data(3, 0, default=0)  # edge not in graph, return default
        0
        >>> G.get_edge_data(1, 0, 0)  # specific key gives back
        {'weight': 5}
        """
        ...
    def copy(self, as_view: bool = False) -> MultiGraph[_Node]:
        """
        Returns a copy of the graph.

        The copy method by default returns an independent shallow copy
        of the graph and attributes. That is, if an attribute is a
        container, that container is shared by the original an the copy.
        Use Python's `copy.deepcopy` for new containers.

        If `as_view` is True then a view is returned instead of a copy.

        Notes
        -----
        All copies reproduce the graph structure, but data attributes
        may be handled in different ways. There are four types of copies
        of a graph that people might want.

        Deepcopy -- A "deepcopy" copies the graph structure as well as
        all data attributes and any objects they might contain.
        The entire graph object is new so that changes in the copy
        do not affect the original object. (see Python's copy.deepcopy)

        Data Reference (Shallow) -- For a shallow copy the graph structure
        is copied but the edge, node and graph attribute dicts are
        references to those in the original graph. This saves
        time and memory but could cause confusion if you change an attribute
        in one graph and it changes the attribute in the other.
        NetworkX does not provide this level of shallow copy.

        Independent Shallow -- This copy creates new independent attribute
        dicts and then does a shallow copy of the attributes. That is, any
        attributes that are containers are shared between the new graph
        and the original. This is exactly what `dict.copy()` provides.
        You can obtain this style copy using:

            >>> G = nx.path_graph(5)
            >>> H = G.copy()
            >>> H = G.copy(as_view=False)
            >>> H = nx.Graph(G)
            >>> H = G.__class__(G)

        Fresh Data -- For fresh data, the graph structure is copied while
        new empty data attribute dicts are created. The resulting graph
        is independent of the original and it has no edge, node or graph
        attributes. Fresh copies are not enabled. Instead use:

            >>> H = G.__class__()
            >>> H.add_nodes_from(G)
            >>> H.add_edges_from(G.edges)

        View -- Inspired by dict-views, graph-views act like read-only
        versions of the original graph, providing a copy of the original
        structure without requiring any memory for copying the information.

        See the Python copy module for more information on shallow
        and deep copies, https://docs.python.org/3/library/copy.html.

        Parameters
        ----------
        as_view : bool, optional (default=False)
            If True, the returned graph-view provides a read-only view
            of the original graph without actually copying any data.

        Returns
        -------
        G : Graph
            A copy of the graph.

        See Also
        --------
        to_directed: return a directed copy of the graph.

        Examples
        --------
        >>> G = nx.path_graph(4)  # or DiGraph, MultiGraph, MultiDiGraph, etc
        >>> H = G.copy()
        """
        ...
    def to_directed(self, as_view: bool = False) -> MultiDiGraph[_Node]:
        """
        Returns a directed representation of the graph.

        Returns
        -------
        G : MultiDiGraph
            A directed graph with the same name, same nodes, and with
            each edge (u, v, k, data) replaced by two directed edges
            (u, v, k, data) and (v, u, k, data).

        Notes
        -----
        This returns a "deepcopy" of the edge, node, and
        graph attributes which attempts to completely copy
        all of the data and references.

        This is in contrast to the similar D=MultiDiGraph(G) which
        returns a shallow copy of the data.

        See the Python copy module for more information on shallow
        and deep copies, https://docs.python.org/3/library/copy.html.

        Warning: If you have subclassed MultiGraph to use dict-like objects
        in the data structure, those changes do not transfer to the
        MultiDiGraph created by this method.

        Examples
        --------
        >>> G = nx.MultiGraph()
        >>> G.add_edge(0, 1)
        0
        >>> G.add_edge(0, 1)
        1
        >>> H = G.to_directed()
        >>> list(H.edges)
        [(0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1)]

        If already directed, return a (deep) copy

        >>> G = nx.MultiDiGraph()
        >>> G.add_edge(0, 1)
        0
        >>> H = G.to_directed()
        >>> list(H.edges)
        [(0, 1, 0)]
        """
        ...
    def to_undirected(self, as_view: bool = False) -> MultiGraph[_Node]:
        """
        Returns an undirected copy of the graph.

        Returns
        -------
        G : Graph/MultiGraph
            A deepcopy of the graph.

        See Also
        --------
        copy, add_edge, add_edges_from

        Notes
        -----
        This returns a "deepcopy" of the edge, node, and
        graph attributes which attempts to completely copy
        all of the data and references.

        This is in contrast to the similar `G = nx.MultiGraph(D)`
        which returns a shallow copy of the data.

        See the Python copy module for more information on shallow
        and deep copies, https://docs.python.org/3/library/copy.html.

        Warning: If you have subclassed MultiGraph to use dict-like
        objects in the data structure, those changes do not transfer
        to the MultiGraph created by this method.

        Examples
        --------
        >>> G = nx.MultiGraph([(0, 1), (0, 1), (1, 2)])
        >>> H = G.to_directed()
        >>> list(H.edges)
        [(0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 2, 0), (2, 1, 0)]
        >>> G2 = H.to_undirected()
        >>> list(G2.edges)
        [(0, 1, 0), (0, 1, 1), (1, 2, 0)]
        """
        ...
    def number_of_edges(self, u: _Node | None = None, v: _Node | None = None) -> int:
        """
        Returns the number of edges between two nodes.

        Parameters
        ----------
        u, v : nodes, optional (Default=all edges)
            If u and v are specified, return the number of edges between
            u and v. Otherwise return the total number of all edges.

        Returns
        -------
        nedges : int
            The number of edges in the graph.  If nodes `u` and `v` are
            specified return the number of edges between those nodes. If
            the graph is directed, this only returns the number of edges
            from `u` to `v`.

        See Also
        --------
        size

        Examples
        --------
        For undirected multigraphs, this method counts the total number
        of edges in the graph::

            >>> G = nx.MultiGraph()
            >>> G.add_edges_from([(0, 1), (0, 1), (1, 2)])
            [0, 1, 0]
            >>> G.number_of_edges()
            3

        If you specify two nodes, this counts the total number of edges
        joining the two nodes::

            >>> G.number_of_edges(0, 1)
            2

        For directed multigraphs, this method can count the total number
        of directed edges from `u` to `v`::

            >>> G = nx.MultiDiGraph()
            >>> G.add_edges_from([(0, 1), (0, 1), (1, 0)])
            [0, 1, 0]
            >>> G.number_of_edges(0, 1)
            2
            >>> G.number_of_edges(1, 0)
            1
        """
        ...
    @cached_property
    def edges(self) -> OutMultiEdgeView[_Node]:
        """
        Returns an iterator over the edges.

        edges(self, nbunch=None, data=False, keys=False, default=None)

        The MultiEdgeView provides set-like operations on the edge-tuples
        as well as edge attribute lookup. When called, it also provides
        an EdgeDataView object which allows control of access to edge
        attributes (but does not provide set-like operations).
        Hence, ``G.edges[u, v, k]['color']`` provides the value of the color
        attribute for the edge from ``u`` to ``v`` with key ``k`` while
        ``for (u, v, k, c) in G.edges(data='color', keys=True, default="red"):``
        iterates through all the edges yielding the color attribute with
        default `'red'` if no color attribute exists.

        Edges are returned as tuples with optional data and keys
        in the order (node, neighbor, key, data). If ``keys=True`` is not
        provided, the tuples will just be (node, neighbor, data), but
        multiple tuples with the same node and neighbor will be generated
        when multiple edges exist between two nodes.

        Parameters
        ----------
        nbunch : single node, container, or all nodes (default= all nodes)
            The view will only report edges from these nodes.
        data : string or bool, optional (default=False)
            The edge attribute returned in 3-tuple (u, v, ddict[data]).
            If True, return edge attribute dict in 3-tuple (u, v, ddict).
            If False, return 2-tuple (u, v).
        keys : bool, optional (default=False)
            If True, return edge keys with each edge, creating (u, v, k)
            tuples or (u, v, k, d) tuples if data is also requested.
        default : value, optional (default=None)
            Value used for edges that don't have the requested attribute.
            Only relevant if data is not True or False.

        Returns
        -------
        edges : MultiEdgeView
            A view of edge attributes, usually it iterates over (u, v)
            (u, v, k) or (u, v, k, d) tuples of edges, but can also be
            used for attribute lookup as ``edges[u, v, k]['foo']``.

        Notes
        -----
        Nodes in nbunch that are not in the graph will be (quietly) ignored.
        For directed graphs this returns the out-edges.

        Examples
        --------
        >>> G = nx.MultiGraph()
        >>> nx.add_path(G, [0, 1, 2])
        >>> key = G.add_edge(2, 3, weight=5)
        >>> key2 = G.add_edge(2, 1, weight=2)  # multi-edge
        >>> [e for e in G.edges()]
        [(0, 1), (1, 2), (1, 2), (2, 3)]
        >>> G.edges.data()  # default data is {} (empty dict)
        MultiEdgeDataView([(0, 1, {}), (1, 2, {}), (1, 2, {'weight': 2}), (2, 3, {'weight': 5})])
        >>> G.edges.data("weight", default=1)
        MultiEdgeDataView([(0, 1, 1), (1, 2, 1), (1, 2, 2), (2, 3, 5)])
        >>> G.edges(keys=True)  # default keys are integers
        MultiEdgeView([(0, 1, 0), (1, 2, 0), (1, 2, 1), (2, 3, 0)])
        >>> G.edges.data(keys=True)
        MultiEdgeDataView([(0, 1, 0, {}), (1, 2, 0, {}), (1, 2, 1, {'weight': 2}), (2, 3, 0, {'weight': 5})])
        >>> G.edges.data("weight", default=1, keys=True)
        MultiEdgeDataView([(0, 1, 0, 1), (1, 2, 0, 1), (1, 2, 1, 2), (2, 3, 0, 5)])
        >>> G.edges([0, 3])  # Note ordering of tuples from listed sources
        MultiEdgeDataView([(0, 1), (3, 2)])
        >>> G.edges([0, 3, 2, 1])  # Note ordering of tuples
        MultiEdgeDataView([(0, 1), (3, 2), (2, 1), (2, 1)])
        >>> G.edges(0)
        MultiEdgeDataView([(0, 1)])
        """
        ...
