"""
*************************
Multi-line Adjacency List
*************************
Read and write NetworkX graphs as multi-line adjacency lists.

The multi-line adjacency list format is useful for graphs with
nodes that can be meaningfully represented as strings.  With this format
simple edge data can be stored but node or graph data is not.

Format
------
The first label in a line is the source node label followed by the node degree
d.  The next d lines are target node labels and optional edge data.
That pattern repeats for all nodes in the graph.

The graph with edges a-b, a-c, d-e can be represented as the following
adjacency list (anything following the # in a line is a comment)::

     # example.multiline-adjlist
     a 2
     b
     c
     d 1
     e
"""

from collections.abc import Generator

from networkx.utils.backends import _dispatchable

__all__ = ["generate_multiline_adjlist", "write_multiline_adjlist", "parse_multiline_adjlist", "read_multiline_adjlist"]

def generate_multiline_adjlist(G, delimiter: str = " ") -> Generator[str, None, None]:
    """
    Generate a single line of the graph G in multiline adjacency list format.

    Parameters
    ----------
    G : NetworkX graph

    delimiter : string, optional
       Separator for node labels

    Returns
    -------
    lines : string
        Lines of data in multiline adjlist format.

    Examples
    --------
    >>> G = nx.lollipop_graph(4, 3)
    >>> for line in nx.generate_multiline_adjlist(G):
    ...     print(line)
    0 3
    1 {}
    2 {}
    3 {}
    1 2
    2 {}
    3 {}
    2 1
    3 {}
    3 1
    4 {}
    4 1
    5 {}
    5 1
    6 {}
    6 0

    See Also
    --------
    write_multiline_adjlist, read_multiline_adjlist
    """
    ...
def write_multiline_adjlist(G, path, delimiter=" ", comments="#", encoding="utf-8") -> None:
    """
    Write the graph G in multiline adjacency list format to path

    Parameters
    ----------
    G : NetworkX graph

    path : string or file
       Filename or file handle to write to.
       Filenames ending in .gz or .bz2 will be compressed.

    comments : string, optional
       Marker for comment lines

    delimiter : string, optional
       Separator for node labels

    encoding : string, optional
       Text encoding.

    Examples
    --------
    >>> G = nx.path_graph(4)
    >>> nx.write_multiline_adjlist(G, "test.multi_adjlist")

    The path can be a file handle or a string with the name of the file. If a
    file handle is provided, it has to be opened in 'wb' mode.

    >>> fh = open("test.multi_adjlist2", "wb")
    >>> nx.write_multiline_adjlist(G, fh)

    Filenames ending in .gz or .bz2 will be compressed.

    >>> nx.write_multiline_adjlist(G, "test.multi_adjlist.gz")

    See Also
    --------
    read_multiline_adjlist
    """
    ...
@_dispatchable
def parse_multiline_adjlist(lines, comments: str = "#", delimiter=None, create_using=None, nodetype=None, edgetype=None):
    """
    Parse lines of a multiline adjacency list representation of a graph.

    Parameters
    ----------
    lines : list or iterator of strings
        Input data in multiline adjlist format

    create_using : NetworkX graph constructor, optional (default=nx.Graph)
       Graph type to create. If graph instance, then cleared before populated.

    nodetype : Python type, optional
       Convert nodes to this type.

    edgetype : Python type, optional
       Convert edges to this type.

    comments : string, optional
       Marker for comment lines

    delimiter : string, optional
       Separator for node labels.  The default is whitespace.

    Returns
    -------
    G: NetworkX graph
        The graph corresponding to the lines in multiline adjacency list format.

    Examples
    --------
    >>> lines = [
    ...     "1 2",
    ...     "2 {'weight':3, 'name': 'Frodo'}",
    ...     "3 {}",
    ...     "2 1",
    ...     "5 {'weight':6, 'name': 'Saruman'}",
    ... ]
    >>> G = nx.parse_multiline_adjlist(iter(lines), nodetype=int)
    >>> list(G)
    [1, 2, 3, 5]
    """
    ...
@_dispatchable
def read_multiline_adjlist(
    path, comments: str = "#", delimiter=None, create_using=None, nodetype=None, edgetype=None, encoding: str = "utf-8"
):
    """
    Read graph in multi-line adjacency list format from path.

    Parameters
    ----------
    path : string or file
       Filename or file handle to read.
       Filenames ending in .gz or .bz2 will be decompressed.

    create_using : NetworkX graph constructor, optional (default=nx.Graph)
       Graph type to create. If graph instance, then cleared before populated.

    nodetype : Python type, optional
       Convert nodes to this type.

    edgetype : Python type, optional
       Convert edge data to this type.

    comments : string, optional
       Marker for comment lines

    delimiter : string, optional
       Separator for node labels.  The default is whitespace.

    Returns
    -------
    G: NetworkX graph

    Examples
    --------
    >>> G = nx.path_graph(4)
    >>> nx.write_multiline_adjlist(G, "test.multi_adjlistP4")
    >>> G = nx.read_multiline_adjlist("test.multi_adjlistP4")

    The path can be a file or a string with the name of the file. If a
    file s provided, it has to be opened in 'rb' mode.

    >>> fh = open("test.multi_adjlistP4", "rb")
    >>> G = nx.read_multiline_adjlist(fh)

    Filenames ending in .gz or .bz2 will be compressed.

    >>> nx.write_multiline_adjlist(G, "test.multi_adjlistP4.gz")
    >>> G = nx.read_multiline_adjlist("test.multi_adjlistP4.gz")

    The optional nodetype is a function to convert node strings to nodetype.

    For example

    >>> G = nx.read_multiline_adjlist("test.multi_adjlistP4", nodetype=int)

    will attempt to convert all nodes to integer type.

    The optional edgetype is a function to convert edge data strings to
    edgetype.

    >>> G = nx.read_multiline_adjlist("test.multi_adjlistP4")

    The optional create_using parameter is a NetworkX graph container.
    The default is Graph(), an undirected graph.  To read the data as
    a directed graph use

    >>> G = nx.read_multiline_adjlist("test.multi_adjlistP4", create_using=nx.DiGraph)

    Notes
    -----
    This format does not store graph, node, or edge data.

    See Also
    --------
    write_multiline_adjlist
    """
    ...
