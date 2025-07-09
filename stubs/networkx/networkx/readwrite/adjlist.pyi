from collections.abc import Generator

from networkx.utils.backends import _dispatchable

__all__ = ["generate_adjlist", "write_adjlist", "parse_adjlist", "read_adjlist"]

def generate_adjlist(G, delimiter: str = " ") -> Generator[str, None, None]: ...
def write_adjlist(G, path, comments: str = "#", delimiter: str = " ", encoding: str = "utf-8") -> None: ...
@_dispatchable
def parse_adjlist(lines, comments: str = "#", delimiter=None, create_using=None, nodetype=None):
    """
    Parse lines of a graph adjacency list representation.

    Parameters
    ----------
    lines : list or iterator of strings
        Input data in adjlist format

    create_using : NetworkX graph constructor, optional (default=nx.Graph)
       Graph type to create. If graph instance, then cleared before populated.

    nodetype : Python type, optional
       Convert nodes to this type.

    comments : string, optional
       Marker for comment lines

    delimiter : string, optional
       Separator for node labels.  The default is whitespace.

    Returns
    -------
    G: NetworkX graph
        The graph corresponding to the lines in adjacency list format.

    Examples
    --------
    >>> lines = ["1 2 5", "2 3 4", "3 5", "4", "5"]
    >>> G = nx.parse_adjlist(lines, nodetype=int)
    >>> nodes = [1, 2, 3, 4, 5]
    >>> all(node in G for node in nodes)
    True
    >>> edges = [(1, 2), (1, 5), (2, 3), (2, 4), (3, 5)]
    >>> all((u, v) in G.edges() or (v, u) in G.edges() for (u, v) in edges)
    True

    See Also
    --------
    read_adjlist
    """
    ...
@_dispatchable
def read_adjlist(path, comments: str = "#", delimiter=None, create_using=None, nodetype=None, encoding: str = "utf-8"):
    """
    Read graph in adjacency list format from path.

    Parameters
    ----------
    path : string or file
       Filename or file handle to read.
       Filenames ending in .gz or .bz2 will be decompressed.

    create_using : NetworkX graph constructor, optional (default=nx.Graph)
       Graph type to create. If graph instance, then cleared before populated.

    nodetype : Python type, optional
       Convert nodes to this type.

    comments : string, optional
       Marker for comment lines

    delimiter : string, optional
       Separator for node labels.  The default is whitespace.

    Returns
    -------
    G: NetworkX graph
        The graph corresponding to the lines in adjacency list format.

    Examples
    --------
    >>> G = nx.path_graph(4)
    >>> nx.write_adjlist(G, "test.adjlist")
    >>> G = nx.read_adjlist("test.adjlist")

    The path can be a filehandle or a string with the name of the file. If a
    filehandle is provided, it has to be opened in 'rb' mode.

    >>> fh = open("test.adjlist", "rb")
    >>> G = nx.read_adjlist(fh)

    Filenames ending in .gz or .bz2 will be compressed.

    >>> nx.write_adjlist(G, "test.adjlist.gz")
    >>> G = nx.read_adjlist("test.adjlist.gz")

    The optional nodetype is a function to convert node strings to nodetype.

    For example

    >>> G = nx.read_adjlist("test.adjlist", nodetype=int)

    will attempt to convert all nodes to integer type.

    Since nodes must be hashable, the function nodetype must return hashable
    types (e.g. int, float, str, frozenset - or tuples of those, etc.)

    The optional create_using parameter indicates the type of NetworkX graph
    created.  The default is `nx.Graph`, an undirected graph.
    To read the data as a directed graph use

    >>> G = nx.read_adjlist("test.adjlist", create_using=nx.DiGraph)

    Notes
    -----
    This format does not store graph or node data.

    See Also
    --------
    write_adjlist
    """
    ...
