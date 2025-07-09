from _typeshed import Incomplete

from networkx.utils.backends import _dispatchable

from ..classes.graph import Graph

__all__ = ["write_dot", "read_dot", "graphviz_layout", "pydot_layout", "to_pydot", "from_pydot"]

def write_dot(G, path) -> None:
    """
    Write NetworkX graph G to Graphviz dot format on path.

    Parameters
    ----------
    G : NetworkX graph

    path : string or file
       Filename or file handle for data output.
       Filenames ending in .gz or .bz2 will be compressed.
    """
    ...
@_dispatchable
def read_dot(path) -> Graph[Incomplete]: ...
@_dispatchable
def from_pydot(P):
    """
    Returns a NetworkX graph from a Pydot graph.

    Parameters
    ----------
    P : Pydot graph
      A graph created with Pydot

    Returns
    -------
    G : NetworkX multigraph
        A MultiGraph or MultiDiGraph.

    Examples
    --------
    >>> K5 = nx.complete_graph(5)
    >>> A = nx.nx_pydot.to_pydot(K5)
    >>> G = nx.nx_pydot.from_pydot(A)  # return MultiGraph

    # make a Graph instead of MultiGraph
    >>> G = nx.Graph(nx.nx_pydot.from_pydot(A))
    """
    ...
def to_pydot(N):
    """
    Returns a pydot graph from a NetworkX graph N.

    Parameters
    ----------
    N : NetworkX graph
      A graph created with NetworkX

    Examples
    --------
    >>> K5 = nx.complete_graph(5)
    >>> P = nx.nx_pydot.to_pydot(K5)

    Notes
    -----
    """
    ...
def graphviz_layout(G, prog: str = "neato", root=None):
    """
    Create node positions using Pydot and Graphviz.

    Returns a dictionary of positions keyed by node.

    Parameters
    ----------
    G : NetworkX Graph
        The graph for which the layout is computed.
    prog : string (default: 'neato')
        The name of the GraphViz program to use for layout.
        Options depend on GraphViz version but may include:
        'dot', 'twopi', 'fdp', 'sfdp', 'circo'
    root : Node from G or None (default: None)
        The node of G from which to start some layout algorithms.

    Returns
    -------
      Dictionary of (x, y) positions keyed by node.

    Examples
    --------
    >>> G = nx.complete_graph(4)
    >>> pos = nx.nx_pydot.graphviz_layout(G)
    >>> pos = nx.nx_pydot.graphviz_layout(G, prog="dot")

    Notes
    -----
    This is a wrapper for pydot_layout.
    """
    ...
def pydot_layout(G, prog: str = "neato", root=None):
    """
    Create node positions using :mod:`pydot` and Graphviz.

    Parameters
    ----------
    G : Graph
        NetworkX graph to be laid out.
    prog : string  (default: 'neato')
        Name of the GraphViz command to use for layout.
        Options depend on GraphViz version but may include:
        'dot', 'twopi', 'fdp', 'sfdp', 'circo'
    root : Node from G or None (default: None)
        The node of G from which to start some layout algorithms.

    Returns
    -------
    dict
        Dictionary of positions keyed by node.

    Examples
    --------
    >>> G = nx.complete_graph(4)
    >>> pos = nx.nx_pydot.pydot_layout(G)
    >>> pos = nx.nx_pydot.pydot_layout(G, prog="dot")

    Notes
    -----
    If you use complex node objects, they may have the same string
    representation and GraphViz could treat them as the same node.
    The layout may assign both nodes a single location. See Issue #1568
    If this occurs in your case, consider relabeling the nodes just
    for the layout computation using something similar to::

        H = nx.convert_node_labels_to_integers(G, label_attribute="node_label")
        H_layout = nx.nx_pydot.pydot_layout(H, prog="dot")
        G_layout = {H.nodes[n]["node_label"]: p for n, p in H_layout.items()}
    """
    ...
