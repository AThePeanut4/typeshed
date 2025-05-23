from collections.abc import Hashable, Mapping
from typing import Literal, TypeVar, overload

from networkx.classes.digraph import DiGraph
from networkx.classes.graph import Graph
from networkx.classes.multidigraph import MultiDiGraph
from networkx.classes.multigraph import MultiGraph
from networkx.utils.backends import _dispatchable

_X = TypeVar("_X", bound=Hashable)
_Y = TypeVar("_Y", bound=Hashable)

__all__ = ["convert_node_labels_to_integers", "relabel_nodes"]

@overload
def relabel_nodes(G: MultiDiGraph[_X], mapping: Mapping[_X, _Y], copy: bool = True) -> MultiDiGraph[_X | _Y]:
    """
    Relabel the nodes of the graph G according to a given mapping.

    The original node ordering may not be preserved if `copy` is `False` and the
    mapping includes overlap between old and new labels.

    Parameters
    ----------
    G : graph
       A NetworkX graph

    mapping : dictionary
       A dictionary with the old labels as keys and new labels as values.
       A partial mapping is allowed. Mapping 2 nodes to a single node is allowed.
       Any non-node keys in the mapping are ignored.

    copy : bool (optional, default=True)
       If True return a copy, or if False relabel the nodes in place.

    Examples
    --------
    To create a new graph with nodes relabeled according to a given
    dictionary:

    >>> G = nx.path_graph(3)
    >>> sorted(G)
    [0, 1, 2]
    >>> mapping = {0: "a", 1: "b", 2: "c"}
    >>> H = nx.relabel_nodes(G, mapping)
    >>> sorted(H)
    ['a', 'b', 'c']

    Nodes can be relabeled with any hashable object, including numbers
    and strings:

    >>> import string
    >>> G = nx.path_graph(26)  # nodes are integers 0 through 25
    >>> sorted(G)[:3]
    [0, 1, 2]
    >>> mapping = dict(zip(G, string.ascii_lowercase))
    >>> G = nx.relabel_nodes(G, mapping)  # nodes are characters a through z
    >>> sorted(G)[:3]
    ['a', 'b', 'c']
    >>> mapping = dict(zip(G, range(1, 27)))
    >>> G = nx.relabel_nodes(G, mapping)  # nodes are integers 1 through 26
    >>> sorted(G)[:3]
    [1, 2, 3]

    To perform a partial in-place relabeling, provide a dictionary
    mapping only a subset of the nodes, and set the `copy` keyword
    argument to False:

    >>> G = nx.path_graph(3)  # nodes 0-1-2
    >>> mapping = {0: "a", 1: "b"}  # 0->'a' and 1->'b'
    >>> G = nx.relabel_nodes(G, mapping, copy=False)
    >>> sorted(G, key=str)
    [2, 'a', 'b']

    A mapping can also be given as a function:

    >>> G = nx.path_graph(3)
    >>> H = nx.relabel_nodes(G, lambda x: x**2)
    >>> list(H)
    [0, 1, 4]

    In a multigraph, relabeling two or more nodes to the same new node
    will retain all edges, but may change the edge keys in the process:

    >>> G = nx.MultiGraph()
    >>> G.add_edge(0, 1, value="a")  # returns the key for this edge
    0
    >>> G.add_edge(0, 2, value="b")
    0
    >>> G.add_edge(0, 3, value="c")
    0
    >>> mapping = {1: 4, 2: 4, 3: 4}
    >>> H = nx.relabel_nodes(G, mapping, copy=True)
    >>> print(H[0])
    {4: {0: {'value': 'a'}, 1: {'value': 'b'}, 2: {'value': 'c'}}}

    This works for in-place relabeling too:

    >>> G = nx.relabel_nodes(G, mapping, copy=False)
    >>> print(G[0])
    {4: {0: {'value': 'a'}, 1: {'value': 'b'}, 2: {'value': 'c'}}}

    Notes
    -----
    Only the nodes specified in the mapping will be relabeled.
    Any non-node keys in the mapping are ignored.

    The keyword setting copy=False modifies the graph in place.
    Relabel_nodes avoids naming collisions by building a
    directed graph from ``mapping`` which specifies the order of
    relabelings. Naming collisions, such as a->b, b->c, are ordered
    such that "b" gets renamed to "c" before "a" gets renamed "b".
    In cases of circular mappings (e.g. a->b, b->a), modifying the
    graph is not possible in-place and an exception is raised.
    In that case, use copy=True.

    If a relabel operation on a multigraph would cause two or more
    edges to have the same source, target and key, the second edge must
    be assigned a new key to retain all edges. The new key is set
    to the lowest non-negative integer not already used as a key
    for edges between these two nodes. Note that this means non-numeric
    keys may be replaced by numeric keys.

    See Also
    --------
    convert_node_labels_to_integers
    """
    ...
@overload
def relabel_nodes(G: DiGraph[_X], mapping: Mapping[_X, _Y], copy: bool = True) -> DiGraph[_X | _Y]:
    """
    Relabel the nodes of the graph G according to a given mapping.

    The original node ordering may not be preserved if `copy` is `False` and the
    mapping includes overlap between old and new labels.

    Parameters
    ----------
    G : graph
       A NetworkX graph

    mapping : dictionary
       A dictionary with the old labels as keys and new labels as values.
       A partial mapping is allowed. Mapping 2 nodes to a single node is allowed.
       Any non-node keys in the mapping are ignored.

    copy : bool (optional, default=True)
       If True return a copy, or if False relabel the nodes in place.

    Examples
    --------
    To create a new graph with nodes relabeled according to a given
    dictionary:

    >>> G = nx.path_graph(3)
    >>> sorted(G)
    [0, 1, 2]
    >>> mapping = {0: "a", 1: "b", 2: "c"}
    >>> H = nx.relabel_nodes(G, mapping)
    >>> sorted(H)
    ['a', 'b', 'c']

    Nodes can be relabeled with any hashable object, including numbers
    and strings:

    >>> import string
    >>> G = nx.path_graph(26)  # nodes are integers 0 through 25
    >>> sorted(G)[:3]
    [0, 1, 2]
    >>> mapping = dict(zip(G, string.ascii_lowercase))
    >>> G = nx.relabel_nodes(G, mapping)  # nodes are characters a through z
    >>> sorted(G)[:3]
    ['a', 'b', 'c']
    >>> mapping = dict(zip(G, range(1, 27)))
    >>> G = nx.relabel_nodes(G, mapping)  # nodes are integers 1 through 26
    >>> sorted(G)[:3]
    [1, 2, 3]

    To perform a partial in-place relabeling, provide a dictionary
    mapping only a subset of the nodes, and set the `copy` keyword
    argument to False:

    >>> G = nx.path_graph(3)  # nodes 0-1-2
    >>> mapping = {0: "a", 1: "b"}  # 0->'a' and 1->'b'
    >>> G = nx.relabel_nodes(G, mapping, copy=False)
    >>> sorted(G, key=str)
    [2, 'a', 'b']

    A mapping can also be given as a function:

    >>> G = nx.path_graph(3)
    >>> H = nx.relabel_nodes(G, lambda x: x**2)
    >>> list(H)
    [0, 1, 4]

    In a multigraph, relabeling two or more nodes to the same new node
    will retain all edges, but may change the edge keys in the process:

    >>> G = nx.MultiGraph()
    >>> G.add_edge(0, 1, value="a")  # returns the key for this edge
    0
    >>> G.add_edge(0, 2, value="b")
    0
    >>> G.add_edge(0, 3, value="c")
    0
    >>> mapping = {1: 4, 2: 4, 3: 4}
    >>> H = nx.relabel_nodes(G, mapping, copy=True)
    >>> print(H[0])
    {4: {0: {'value': 'a'}, 1: {'value': 'b'}, 2: {'value': 'c'}}}

    This works for in-place relabeling too:

    >>> G = nx.relabel_nodes(G, mapping, copy=False)
    >>> print(G[0])
    {4: {0: {'value': 'a'}, 1: {'value': 'b'}, 2: {'value': 'c'}}}

    Notes
    -----
    Only the nodes specified in the mapping will be relabeled.
    Any non-node keys in the mapping are ignored.

    The keyword setting copy=False modifies the graph in place.
    Relabel_nodes avoids naming collisions by building a
    directed graph from ``mapping`` which specifies the order of
    relabelings. Naming collisions, such as a->b, b->c, are ordered
    such that "b" gets renamed to "c" before "a" gets renamed "b".
    In cases of circular mappings (e.g. a->b, b->a), modifying the
    graph is not possible in-place and an exception is raised.
    In that case, use copy=True.

    If a relabel operation on a multigraph would cause two or more
    edges to have the same source, target and key, the second edge must
    be assigned a new key to retain all edges. The new key is set
    to the lowest non-negative integer not already used as a key
    for edges between these two nodes. Note that this means non-numeric
    keys may be replaced by numeric keys.

    See Also
    --------
    convert_node_labels_to_integers
    """
    ...
@overload
def relabel_nodes(G: MultiGraph[_X], mapping: Mapping[_X, _Y], copy: bool = True) -> MultiGraph[_X | _Y]:
    """
    Relabel the nodes of the graph G according to a given mapping.

    The original node ordering may not be preserved if `copy` is `False` and the
    mapping includes overlap between old and new labels.

    Parameters
    ----------
    G : graph
       A NetworkX graph

    mapping : dictionary
       A dictionary with the old labels as keys and new labels as values.
       A partial mapping is allowed. Mapping 2 nodes to a single node is allowed.
       Any non-node keys in the mapping are ignored.

    copy : bool (optional, default=True)
       If True return a copy, or if False relabel the nodes in place.

    Examples
    --------
    To create a new graph with nodes relabeled according to a given
    dictionary:

    >>> G = nx.path_graph(3)
    >>> sorted(G)
    [0, 1, 2]
    >>> mapping = {0: "a", 1: "b", 2: "c"}
    >>> H = nx.relabel_nodes(G, mapping)
    >>> sorted(H)
    ['a', 'b', 'c']

    Nodes can be relabeled with any hashable object, including numbers
    and strings:

    >>> import string
    >>> G = nx.path_graph(26)  # nodes are integers 0 through 25
    >>> sorted(G)[:3]
    [0, 1, 2]
    >>> mapping = dict(zip(G, string.ascii_lowercase))
    >>> G = nx.relabel_nodes(G, mapping)  # nodes are characters a through z
    >>> sorted(G)[:3]
    ['a', 'b', 'c']
    >>> mapping = dict(zip(G, range(1, 27)))
    >>> G = nx.relabel_nodes(G, mapping)  # nodes are integers 1 through 26
    >>> sorted(G)[:3]
    [1, 2, 3]

    To perform a partial in-place relabeling, provide a dictionary
    mapping only a subset of the nodes, and set the `copy` keyword
    argument to False:

    >>> G = nx.path_graph(3)  # nodes 0-1-2
    >>> mapping = {0: "a", 1: "b"}  # 0->'a' and 1->'b'
    >>> G = nx.relabel_nodes(G, mapping, copy=False)
    >>> sorted(G, key=str)
    [2, 'a', 'b']

    A mapping can also be given as a function:

    >>> G = nx.path_graph(3)
    >>> H = nx.relabel_nodes(G, lambda x: x**2)
    >>> list(H)
    [0, 1, 4]

    In a multigraph, relabeling two or more nodes to the same new node
    will retain all edges, but may change the edge keys in the process:

    >>> G = nx.MultiGraph()
    >>> G.add_edge(0, 1, value="a")  # returns the key for this edge
    0
    >>> G.add_edge(0, 2, value="b")
    0
    >>> G.add_edge(0, 3, value="c")
    0
    >>> mapping = {1: 4, 2: 4, 3: 4}
    >>> H = nx.relabel_nodes(G, mapping, copy=True)
    >>> print(H[0])
    {4: {0: {'value': 'a'}, 1: {'value': 'b'}, 2: {'value': 'c'}}}

    This works for in-place relabeling too:

    >>> G = nx.relabel_nodes(G, mapping, copy=False)
    >>> print(G[0])
    {4: {0: {'value': 'a'}, 1: {'value': 'b'}, 2: {'value': 'c'}}}

    Notes
    -----
    Only the nodes specified in the mapping will be relabeled.
    Any non-node keys in the mapping are ignored.

    The keyword setting copy=False modifies the graph in place.
    Relabel_nodes avoids naming collisions by building a
    directed graph from ``mapping`` which specifies the order of
    relabelings. Naming collisions, such as a->b, b->c, are ordered
    such that "b" gets renamed to "c" before "a" gets renamed "b".
    In cases of circular mappings (e.g. a->b, b->a), modifying the
    graph is not possible in-place and an exception is raised.
    In that case, use copy=True.

    If a relabel operation on a multigraph would cause two or more
    edges to have the same source, target and key, the second edge must
    be assigned a new key to retain all edges. The new key is set
    to the lowest non-negative integer not already used as a key
    for edges between these two nodes. Note that this means non-numeric
    keys may be replaced by numeric keys.

    See Also
    --------
    convert_node_labels_to_integers
    """
    ...
@overload
def relabel_nodes(G: Graph[_X], mapping: Mapping[_X, _Y], copy: bool = True) -> Graph[_X | _Y]:
    """
    Relabel the nodes of the graph G according to a given mapping.

    The original node ordering may not be preserved if `copy` is `False` and the
    mapping includes overlap between old and new labels.

    Parameters
    ----------
    G : graph
       A NetworkX graph

    mapping : dictionary
       A dictionary with the old labels as keys and new labels as values.
       A partial mapping is allowed. Mapping 2 nodes to a single node is allowed.
       Any non-node keys in the mapping are ignored.

    copy : bool (optional, default=True)
       If True return a copy, or if False relabel the nodes in place.

    Examples
    --------
    To create a new graph with nodes relabeled according to a given
    dictionary:

    >>> G = nx.path_graph(3)
    >>> sorted(G)
    [0, 1, 2]
    >>> mapping = {0: "a", 1: "b", 2: "c"}
    >>> H = nx.relabel_nodes(G, mapping)
    >>> sorted(H)
    ['a', 'b', 'c']

    Nodes can be relabeled with any hashable object, including numbers
    and strings:

    >>> import string
    >>> G = nx.path_graph(26)  # nodes are integers 0 through 25
    >>> sorted(G)[:3]
    [0, 1, 2]
    >>> mapping = dict(zip(G, string.ascii_lowercase))
    >>> G = nx.relabel_nodes(G, mapping)  # nodes are characters a through z
    >>> sorted(G)[:3]
    ['a', 'b', 'c']
    >>> mapping = dict(zip(G, range(1, 27)))
    >>> G = nx.relabel_nodes(G, mapping)  # nodes are integers 1 through 26
    >>> sorted(G)[:3]
    [1, 2, 3]

    To perform a partial in-place relabeling, provide a dictionary
    mapping only a subset of the nodes, and set the `copy` keyword
    argument to False:

    >>> G = nx.path_graph(3)  # nodes 0-1-2
    >>> mapping = {0: "a", 1: "b"}  # 0->'a' and 1->'b'
    >>> G = nx.relabel_nodes(G, mapping, copy=False)
    >>> sorted(G, key=str)
    [2, 'a', 'b']

    A mapping can also be given as a function:

    >>> G = nx.path_graph(3)
    >>> H = nx.relabel_nodes(G, lambda x: x**2)
    >>> list(H)
    [0, 1, 4]

    In a multigraph, relabeling two or more nodes to the same new node
    will retain all edges, but may change the edge keys in the process:

    >>> G = nx.MultiGraph()
    >>> G.add_edge(0, 1, value="a")  # returns the key for this edge
    0
    >>> G.add_edge(0, 2, value="b")
    0
    >>> G.add_edge(0, 3, value="c")
    0
    >>> mapping = {1: 4, 2: 4, 3: 4}
    >>> H = nx.relabel_nodes(G, mapping, copy=True)
    >>> print(H[0])
    {4: {0: {'value': 'a'}, 1: {'value': 'b'}, 2: {'value': 'c'}}}

    This works for in-place relabeling too:

    >>> G = nx.relabel_nodes(G, mapping, copy=False)
    >>> print(G[0])
    {4: {0: {'value': 'a'}, 1: {'value': 'b'}, 2: {'value': 'c'}}}

    Notes
    -----
    Only the nodes specified in the mapping will be relabeled.
    Any non-node keys in the mapping are ignored.

    The keyword setting copy=False modifies the graph in place.
    Relabel_nodes avoids naming collisions by building a
    directed graph from ``mapping`` which specifies the order of
    relabelings. Naming collisions, such as a->b, b->c, are ordered
    such that "b" gets renamed to "c" before "a" gets renamed "b".
    In cases of circular mappings (e.g. a->b, b->a), modifying the
    graph is not possible in-place and an exception is raised.
    In that case, use copy=True.

    If a relabel operation on a multigraph would cause two or more
    edges to have the same source, target and key, the second edge must
    be assigned a new key to retain all edges. The new key is set
    to the lowest non-negative integer not already used as a key
    for edges between these two nodes. Note that this means non-numeric
    keys may be replaced by numeric keys.

    See Also
    --------
    convert_node_labels_to_integers
    """
    ...
@_dispatchable
def convert_node_labels_to_integers(
    G: Graph[Hashable],
    first_label: int = 0,
    ordering: Literal["default", "sorted", "increasing degree", "decreasing degree"] = "default",
    label_attribute=None,
) -> Graph[int]:
    """
    Returns a copy of the graph G with the nodes relabeled using
    consecutive integers.

    Parameters
    ----------
    G : graph
       A NetworkX graph

    first_label : int, optional (default=0)
       An integer specifying the starting offset in numbering nodes.
       The new integer labels are numbered first_label, ..., n-1+first_label.

    ordering : string
       "default" : inherit node ordering from G.nodes()
       "sorted"  : inherit node ordering from sorted(G.nodes())
       "increasing degree" : nodes are sorted by increasing degree
       "decreasing degree" : nodes are sorted by decreasing degree

    label_attribute : string, optional (default=None)
       Name of node attribute to store old label.  If None no attribute
       is created.

    Notes
    -----
    Node and edge attribute data are copied to the new (relabeled) graph.

    There is no guarantee that the relabeling of nodes to integers will
    give the same two integers for two (even identical graphs).
    Use the `ordering` argument to try to preserve the order.

    See Also
    --------
    relabel_nodes
    """
    ...
