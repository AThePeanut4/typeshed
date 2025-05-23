from _typeshed import Incomplete
from collections.abc import Iterable

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["from_graph6_bytes", "read_graph6", "to_graph6_bytes", "write_graph6"]

@_dispatchable
def from_graph6_bytes(bytes_in):
    """
    Read a simple undirected graph in graph6 format from bytes.

    Parameters
    ----------
    bytes_in : bytes
       Data in graph6 format, without a trailing newline.

    Returns
    -------
    G : Graph

    Raises
    ------
    NetworkXError
        If bytes_in is unable to be parsed in graph6 format

    ValueError
        If any character ``c`` in bytes_in does not satisfy
        ``63 <= ord(c) < 127``.

    Examples
    --------
    >>> G = nx.from_graph6_bytes(b"A_")
    >>> sorted(G.edges())
    [(0, 1)]

    See Also
    --------
    read_graph6, write_graph6

    References
    ----------
    .. [1] Graph6 specification
           <http://users.cecs.anu.edu.au/~bdm/data/formats.html>
    """
    ...
def to_graph6_bytes(G, nodes=None, header: bool = True):
    r"""
    Convert a simple undirected graph to bytes in graph6 format.

    Parameters
    ----------
    G : Graph (undirected)

    nodes: list or iterable
       Nodes are labeled 0...n-1 in the order provided.  If None the ordering
       given by ``G.nodes()`` is used.

    header: bool
       If True add '>>graph6<<' bytes to head of data.

    Raises
    ------
    NetworkXNotImplemented
        If the graph is directed or is a multigraph.

    ValueError
        If the graph has at least ``2 ** 36`` nodes; the graph6 format
        is only defined for graphs of order less than ``2 ** 36``.

    Examples
    --------
    >>> nx.to_graph6_bytes(nx.path_graph(2))
    b'>>graph6<<A_\n'

    See Also
    --------
    from_graph6_bytes, read_graph6, write_graph6_bytes

    Notes
    -----
    The returned bytes end with a newline character.

    The format does not support edge or node labels, parallel edges or
    self loops. If self loops are present they are silently ignored.

    References
    ----------
    .. [1] Graph6 specification
           <http://users.cecs.anu.edu.au/~bdm/data/formats.html>
    """
    ...
@_dispatchable
def read_graph6(path): ...
def write_graph6(G, path, nodes=None, header: bool = True): ...
def write_graph6_file(G: Graph[_Node], f, nodes: Iterable[Incomplete] | None = None, header: bool = True): ...
def data_to_n(data): ...
def n_to_data(n): ...
