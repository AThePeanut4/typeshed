"""Operations on graphs including union, intersection, difference."""

from _typeshed import Incomplete
from collections.abc import Hashable, Iterable
from typing import TypeVar

from networkx.classes.digraph import DiGraph
from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["union", "compose", "disjoint_union", "intersection", "difference", "symmetric_difference", "full_join"]

@_dispatchable
def disjoint_union(G: Graph[_Node], H: Graph[_Node]):
    """
    Combine graphs G and H. The nodes are assumed to be unique (disjoint).

    This algorithm automatically relabels nodes to avoid name collisions.

    Parameters
    ----------
    G,H : graph
       A NetworkX graph

    Returns
    -------
    U : A union graph with the same type as G.

    See Also
    --------
    union
    compose
    :func:`~networkx.Graph.update`

    Notes
    -----
    A new graph is created, of the same class as G.  It is recommended
    that G and H be either both directed or both undirected.

    The nodes of G are relabeled 0 to len(G)-1, and the nodes of H are
    relabeled len(G) to len(G)+len(H)-1.

    Renumbering forces G and H to be disjoint, so no exception is ever raised for a name collision.
    To preserve the check for common nodes, use union().

    Edge and node attributes are propagated from G and H to the union graph.
    Graph attributes are also propagated, but if they are present in both G and H,
    then the value from H is used.

    To combine graphs that have common nodes, consider compose(G, H)
    or the method, Graph.update().

    Examples
    --------
    >>> G = nx.Graph([(0, 1), (0, 2), (1, 2)])
    >>> H = nx.Graph([(0, 3), (1, 2), (2, 3)])
    >>> G.nodes[0]["key1"] = 5
    >>> H.nodes[0]["key2"] = 10
    >>> U = nx.disjoint_union(G, H)
    >>> U.nodes(data=True)
    NodeDataView({0: {'key1': 5}, 1: {}, 2: {}, 3: {'key2': 10}, 4: {}, 5: {}, 6: {}})
    >>> U.edges
    EdgeView([(0, 1), (0, 2), (1, 2), (3, 4), (4, 6), (5, 6)])
    """
    ...
@_dispatchable
def intersection(G: Graph[_Node], H: Graph[_Node]):
    """
    Returns a new graph that contains only the nodes and the edges that exist in
    both G and H.

    Parameters
    ----------
    G,H : graph
       A NetworkX graph. G and H can have different node sets but must be both graphs or both multigraphs.

    Raises
    ------
    NetworkXError
        If one is a MultiGraph and the other one is a graph.

    Returns
    -------
    GH : A new graph with the same type as G.

    Notes
    -----
    Attributes from the graph, nodes, and edges are not copied to the new
    graph.  If you want a new graph of the intersection of G and H
    with the attributes (including edge data) from G use remove_nodes_from()
    as follows

    >>> G = nx.path_graph(3)
    >>> H = nx.path_graph(5)
    >>> R = G.copy()
    >>> R.remove_nodes_from(n for n in G if n not in H)
    >>> R.remove_edges_from(e for e in G.edges if e not in H.edges)

    Examples
    --------
    >>> G = nx.Graph([(0, 1), (0, 2), (1, 2)])
    >>> H = nx.Graph([(0, 3), (1, 2), (2, 3)])
    >>> R = nx.intersection(G, H)
    >>> R.nodes
    NodeView((0, 1, 2))
    >>> R.edges
    EdgeView([(1, 2)])
    """
    ...
@_dispatchable
def difference(G: Graph[_Node], H: Graph[_Node]):
    """
    Returns a new graph that contains the edges that exist in G but not in H.

    The node sets of H and G must be the same.

    Parameters
    ----------
    G,H : graph
       A NetworkX graph. G and H must have the same node sets.

    Returns
    -------
    D : A new graph with the same type as G.

    Notes
    -----
    Attributes from the graph, nodes, and edges are not copied to the new
    graph.  If you want a new graph of the difference of G and H with
    the attributes (including edge data) from G use remove_nodes_from()
    as follows:

    >>> G = nx.path_graph(3)
    >>> H = nx.path_graph(5)
    >>> R = G.copy()
    >>> R.remove_nodes_from(n for n in G if n in H)

    Examples
    --------
    >>> G = nx.Graph([(0, 1), (0, 2), (1, 2), (1, 3)])
    >>> H = nx.Graph([(0, 1), (1, 2), (0, 3)])
    >>> R = nx.difference(G, H)
    >>> R.nodes
    NodeView((0, 1, 2, 3))
    >>> R.edges
    EdgeView([(0, 2), (1, 3)])
    """
    ...
@_dispatchable
def symmetric_difference(G: Graph[_Node], H: Graph[_Node]):
    """
    Returns new graph with edges that exist in either G or H but not both.

    The node sets of H and G must be the same.

    Parameters
    ----------
    G,H : graph
       A NetworkX graph.  G and H must have the same node sets.

    Returns
    -------
    D : A new graph with the same type as G.

    Notes
    -----
    Attributes from the graph, nodes, and edges are not copied to the new
    graph.

    Examples
    --------
    >>> G = nx.Graph([(0, 1), (0, 2), (1, 2), (1, 3)])
    >>> H = nx.Graph([(0, 1), (1, 2), (0, 3)])
    >>> R = nx.symmetric_difference(G, H)
    >>> R.nodes
    NodeView((0, 1, 2, 3))
    >>> R.edges
    EdgeView([(0, 2), (0, 3), (1, 3)])
    """
    ...

_X_co = TypeVar("_X_co", bound=Hashable, covariant=True)
_Y_co = TypeVar("_Y_co", bound=Hashable, covariant=True)

@_dispatchable
def compose(G: Graph[_X_co], H: Graph[_Y_co]) -> DiGraph[_X_co | _Y_co]:
    """
    Compose graph G with H by combining nodes and edges into a single graph.

    The node sets and edges sets do not need to be disjoint.

    Composing preserves the attributes of nodes and edges.
    Attribute values from H take precedent over attribute values from G.

    Parameters
    ----------
    G, H : graph
       A NetworkX graph

    Returns
    -------
    C: A new graph with the same type as G

    See Also
    --------
    :func:`~networkx.Graph.update`
    union
    disjoint_union

    Notes
    -----
    It is recommended that G and H be either both directed or both undirected.

    For MultiGraphs, the edges are identified by incident nodes AND edge-key.
    This can cause surprises (i.e., edge `(1, 2)` may or may not be the same
    in two graphs) if you use MultiGraph without keeping track of edge keys.

    If combining the attributes of common nodes is not desired, consider union(),
    which raises an exception for name collisions.

    Examples
    --------
    >>> G = nx.Graph([(0, 1), (0, 2)])
    >>> H = nx.Graph([(0, 1), (1, 2)])
    >>> R = nx.compose(G, H)
    >>> R.nodes
    NodeView((0, 1, 2))
    >>> R.edges
    EdgeView([(0, 1), (0, 2), (1, 2)])

    By default, the attributes from `H` take precedent over attributes from `G`.
    If you prefer another way of combining attributes, you can update them after the compose operation:

    >>> G = nx.Graph([(0, 1, {"weight": 2.0}), (3, 0, {"weight": 100.0})])
    >>> H = nx.Graph([(0, 1, {"weight": 10.0}), (1, 2, {"weight": -1.0})])
    >>> nx.set_node_attributes(G, {0: "dark", 1: "light", 3: "black"}, name="color")
    >>> nx.set_node_attributes(H, {0: "green", 1: "orange", 2: "yellow"}, name="color")
    >>> GcomposeH = nx.compose(G, H)

    Normally, color attribute values of nodes of GcomposeH come from H. We can workaround this as follows:

    >>> node_data = {
    ...     n: G.nodes[n]["color"] + " " + H.nodes[n]["color"]
    ...     for n in G.nodes & H.nodes
    ... }
    >>> nx.set_node_attributes(GcomposeH, node_data, "color")
    >>> print(GcomposeH.nodes[0]["color"])
    dark green

    >>> print(GcomposeH.nodes[3]["color"])
    black

    Similarly, we can update edge attributes after the compose operation in a way we prefer:

    >>> edge_data = {
    ...     e: G.edges[e]["weight"] * H.edges[e]["weight"] for e in G.edges & H.edges
    ... }
    >>> nx.set_edge_attributes(GcomposeH, edge_data, "weight")
    >>> print(GcomposeH.edges[(0, 1)]["weight"])
    20.0

    >>> print(GcomposeH.edges[(3, 0)]["weight"])
    100.0
    """
    ...
@_dispatchable
def full_join(G, H, rename=(None, None)):
    """
    Returns the full join of graphs G and H.

    Full join is the union of G and H in which all edges between
    G and H are added.
    The node sets of G and H must be disjoint,
    otherwise an exception is raised.

    Parameters
    ----------
    G, H : graph
       A NetworkX graph

    rename : tuple , default=(None, None)
       Node names of G and H can be changed by specifying the tuple
       rename=('G-','H-') (for example).  Node "u" in G is then renamed
       "G-u" and "v" in H is renamed "H-v".

    Returns
    -------
    U : The full join graph with the same type as G.

    Notes
    -----
    It is recommended that G and H be either both directed or both undirected.

    If G is directed, then edges from G to H are added as well as from H to G.

    Note that full_join() does not produce parallel edges for MultiGraphs.

    The full join operation of graphs G and H is the same as getting
    their complement, performing a disjoint union, and finally getting
    the complement of the resulting graph.

    Graph, edge, and node attributes are propagated from G and H
    to the union graph.  If a graph attribute is present in both
    G and H the value from H is used.

    Examples
    --------
    >>> from pprint import pprint
    >>> G = nx.Graph([(0, 1), (0, 2)])
    >>> H = nx.Graph([(3, 4)])
    >>> R = nx.full_join(G, H, rename=("G", "H"))
    >>> R.nodes
    NodeView(('G0', 'G1', 'G2', 'H3', 'H4'))
    >>> edgelist = list(R.edges)
    >>> pprint(edgelist)
    [('G0', 'G1'),
     ('G0', 'G2'),
     ('G0', 'H3'),
     ('G0', 'H4'),
     ('G1', 'H3'),
     ('G1', 'H4'),
     ('G2', 'H3'),
     ('G2', 'H4'),
     ('H3', 'H4')]

    See Also
    --------
    union
    disjoint_union
    """
    ...
@_dispatchable
def union(G: Graph[_X_co], H: Graph[_Y_co], rename: Iterable[Incomplete] | None = ()) -> DiGraph[_X_co | _Y_co]:
    """
    Combine graphs G and H. The names of nodes must be unique.

    A name collision between the graphs will raise an exception.

    A renaming facility is provided to avoid name collisions.


    Parameters
    ----------
    G, H : graph
       A NetworkX graph

    rename : iterable , optional
       Node names of G and H can be changed by specifying the tuple
       rename=('G-','H-') (for example).  Node "u" in G is then renamed
       "G-u" and "v" in H is renamed "H-v".

    Returns
    -------
    U : A union graph with the same type as G.

    See Also
    --------
    compose
    :func:`~networkx.Graph.update`
    disjoint_union

    Notes
    -----
    To combine graphs that have common nodes, consider compose(G, H)
    or the method, Graph.update().

    disjoint_union() is similar to union() except that it avoids name clashes
    by relabeling the nodes with sequential integers.

    Edge and node attributes are propagated from G and H to the union graph.
    Graph attributes are also propagated, but if they are present in both G and H,
    then the value from H is used.

    Examples
    --------
    >>> from pprint import pprint
    >>> G = nx.Graph([(0, 1), (0, 2), (1, 2)])
    >>> H = nx.Graph([(0, 1), (0, 3), (1, 3), (1, 2)])
    >>> U = nx.union(G, H, rename=("G", "H"))
    >>> U.nodes
    NodeView(('G0', 'G1', 'G2', 'H0', 'H1', 'H3', 'H2'))
    >>> edgelist = list(U.edges)
    >>> pprint(edgelist)
    [('G0', 'G1'),
     ('G0', 'G2'),
     ('G1', 'G2'),
     ('H0', 'H1'),
     ('H0', 'H3'),
     ('H1', 'H3'),
     ('H1', 'H2')]
    """
    ...
