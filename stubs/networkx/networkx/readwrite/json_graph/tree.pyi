from networkx.classes.digraph import DiGraph
from networkx.classes.graph import _Node
from networkx.utils.backends import _dispatchable

__all__ = ["tree_data", "tree_graph"]

def tree_data(G: DiGraph[_Node], root, ident: str = "id", children: str = "children"): ...
@_dispatchable
def tree_graph(data, ident: str = "id", children: str = "children"):
    """
    Returns graph from tree data format.

    Parameters
    ----------
    data : dict
        Tree formatted graph data

    ident : string
        Attribute name for storing NetworkX-internal graph data. `ident` must
        have a different value than `children`. The default is 'id'.

    children : string
        Attribute name for storing NetworkX-internal graph data. `children`
        must have a different value than `ident`. The default is 'children'.

    Returns
    -------
    G : NetworkX DiGraph

    Examples
    --------
    >>> from networkx.readwrite import json_graph
    >>> G = nx.DiGraph([(1, 2)])
    >>> data = json_graph.tree_data(G, root=1)
    >>> H = json_graph.tree_graph(data)

    See Also
    --------
    tree_data, node_link_data, adjacency_data
    """
    ...
