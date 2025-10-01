from typing import Any

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["adjacency_data", "adjacency_graph"]

# Any: Complex type union
def adjacency_data(G: Graph[_Node], attrs={"id": "id", "key": "key"}) -> dict[str, Any]: ...
@_dispatchable
def adjacency_graph(data, directed: bool = False, multigraph: bool = True, attrs={"id": "id", "key": "key"}):
    """
    Returns graph from adjacency data format.

    Parameters
    ----------
    data : dict
        Adjacency list formatted graph data

    directed : bool
        If True, and direction not specified in data, return a directed graph.

    multigraph : bool
        If True, and multigraph not specified in data, return a multigraph.

    attrs : dict
        A dictionary that contains two keys 'id' and 'key'. The corresponding
        values provide the attribute names for storing NetworkX-internal graph
        data. The values should be unique. Default value:
        :samp:`dict(id='id', key='key')`.

    Returns
    -------
    G : NetworkX graph
       A NetworkX graph object

    Examples
    --------
    >>> from networkx.readwrite import json_graph
    >>> G = nx.Graph([(1, 2)])
    >>> data = json_graph.adjacency_data(G)
    >>> H = json_graph.adjacency_graph(data)

    Notes
    -----
    The default value of attrs will be changed in a future release of NetworkX.

    See Also
    --------
    adjacency_graph, node_link_data, tree_data
    """
    ...
