from typing import overload
from typing_extensions import deprecated

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["node_link_data", "node_link_graph"]

@overload
@deprecated(
    """\
The `link` argument is deprecated and will be removed in version `3.6`.
Use the `edges` keyword instead."""
)
def node_link_data(
    G: Graph[_Node],
    *,
    source: str = "source",
    target: str = "target",
    name: str = "id",
    key: str = "key",
    edges: str | None = None,
    nodes: str = "nodes",
    link: str | None = None,
): ...
@overload
def node_link_data(
    G: Graph[_Node],
    *,
    source: str = "source",
    target: str = "target",
    name: str = "id",
    key: str = "key",
    edges: str | None = None,
    nodes: str = "nodes",
): ...
@_dispatchable
def node_link_graph(
    data,
    directed: bool = False,
    multigraph: bool = True,
    attrs=None,
    *,
    source: str = "source",
    target: str = "target",
    name: str = "id",
    key: str = "key",
    edges: str | None = None,
    nodes: str = "nodes",
    link: str | None = None,
):
    """
    Returns graph from node-link data format.

    Useful for de-serialization from JSON.

    Parameters
    ----------
    data : dict
        node-link formatted graph data

    directed : bool
        If True, and direction not specified in data, return a directed graph.

    multigraph : bool
        If True, and multigraph not specified in data, return a multigraph.

    source : string
        A string that provides the 'source' attribute name for storing NetworkX-internal graph data.
    target : string
        A string that provides the 'target' attribute name for storing NetworkX-internal graph data.
    name : string
        A string that provides the 'name' attribute name for storing NetworkX-internal graph data.
    key : string
        A string that provides the 'key' attribute name for storing NetworkX-internal graph data.
    edges : string
        A string that provides the 'edges' attribute name for storing NetworkX-internal graph data.
    nodes : string
        A string that provides the 'nodes' attribute name for storing NetworkX-internal graph data.
    link : string
        .. deprecated:: 3.4

           The `link` argument is deprecated and will be removed in version `3.6`.
           Use the `edges` keyword instead.

        A string that provides the 'edges' attribute name for storing NetworkX-internal graph data.

    Returns
    -------
    G : NetworkX graph
        A NetworkX graph object

    Examples
    --------

    Create data in node-link format by converting a graph.

    >>> from pprint import pprint
    >>> G = nx.Graph([("A", "B")])
    >>> data = nx.node_link_data(G, edges="edges")
    >>> pprint(data)
    {'directed': False,
     'edges': [{'source': 'A', 'target': 'B'}],
     'graph': {},
     'multigraph': False,
     'nodes': [{'id': 'A'}, {'id': 'B'}]}

    Revert data in node-link format to a graph.

    >>> H = nx.node_link_graph(data, edges="edges")
    >>> print(H.edges)
    [('A', 'B')]

    To serialize and deserialize a graph with JSON,

    >>> import json
    >>> d = json.dumps(nx.node_link_data(G, edges="edges"))
    >>> H = nx.node_link_graph(json.loads(d), edges="edges")
    >>> print(G.edges, H.edges)
    [('A', 'B')] [('A', 'B')]


    Notes
    -----
    Attribute 'key' is only used for multigraphs.

    To use `node_link_data` in conjunction with `node_link_graph`,
    the keyword names for the attributes must match.

    See Also
    --------
    node_link_data, adjacency_data, tree_data
    """
    ...
