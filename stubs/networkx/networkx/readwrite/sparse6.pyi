from _typeshed import Incomplete

from networkx.utils.backends import _dispatchable

from ..classes.graph import Graph

__all__ = ["from_sparse6_bytes", "read_sparse6", "to_sparse6_bytes", "write_sparse6"]

@_dispatchable
def from_sparse6_bytes(string) -> Graph[Incomplete]: ...
def to_sparse6_bytes(G, nodes=None, header: bool = True): ...
@_dispatchable
def read_sparse6(path):
    r"""
    Read an undirected graph in sparse6 format from path.

    Parameters
    ----------
    path : file or string
       Filename or file handle to read.
       Filenames ending in .gz or .bz2 will be decompressed.

    Returns
    -------
    G : Graph/Multigraph or list of Graphs/MultiGraphs
       If the file contains multiple lines then a list of graphs is returned

    Raises
    ------
    NetworkXError
        If the string is unable to be parsed in sparse6 format

    Examples
    --------
    You can read a sparse6 file by giving the path to the file::

        >>> import tempfile
        >>> with tempfile.NamedTemporaryFile(delete=False) as f:
        ...     _ = f.write(b">>sparse6<<:An\n")
        ...     _ = f.seek(0)
        ...     G = nx.read_sparse6(f.name)
        >>> list(G.edges())
        [(0, 1)]

    You can also read a sparse6 file by giving an open file-like object::

        >>> import tempfile
        >>> with tempfile.NamedTemporaryFile() as f:
        ...     _ = f.write(b">>sparse6<<:An\n")
        ...     _ = f.seek(0)
        ...     G = nx.read_sparse6(f)
        >>> list(G.edges())
        [(0, 1)]

    See Also
    --------
    read_sparse6, from_sparse6_bytes

    References
    ----------
    .. [1] Sparse6 specification
           <https://users.cecs.anu.edu.au/~bdm/data/formats.html>
    """
    ...
def write_sparse6(G, path, nodes=None, header: bool = True) -> None:
    r"""
    Write graph G to given path in sparse6 format.

    Parameters
    ----------
    G : Graph (undirected)

    path : file or string
       File or filename to write.
       Filenames ending in .gz or .bz2 will be compressed.

    nodes: list or iterable
       Nodes are labeled 0...n-1 in the order provided.  If None the ordering
       given by G.nodes() is used.

    header: bool
       If True add '>>sparse6<<' string to head of data

    Raises
    ------
    NetworkXError
        If the graph is directed

    Examples
    --------
    You can write a sparse6 file by giving the path to the file::

        >>> import tempfile
        >>> with tempfile.NamedTemporaryFile(delete=False) as f:
        ...     nx.write_sparse6(nx.path_graph(2), f.name)
        ...     print(f.read())
        b'>>sparse6<<:An\n'

    You can also write a sparse6 file by giving an open file-like object::

        >>> with tempfile.NamedTemporaryFile() as f:
        ...     nx.write_sparse6(nx.path_graph(2), f)
        ...     _ = f.seek(0)
        ...     print(f.read())
        b'>>sparse6<<:An\n'

    See Also
    --------
    read_sparse6, from_sparse6_bytes

    Notes
    -----
    The format does not support edge or node labels.

    References
    ----------
    .. [1] Sparse6 specification
           <https://users.cecs.anu.edu.au/~bdm/data/formats.html>
    """
    ...
