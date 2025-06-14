"""
**********
Edge Lists
**********
Read and write NetworkX graphs as edge lists.

The multi-line adjacency list format is useful for graphs with nodes
that can be meaningfully represented as strings.  With the edgelist
format simple edge data can be stored but node or graph data is not.
There is no way of representing isolated nodes unless the node has a
self-loop edge.

Format
------
You can read or write three formats of edge lists with these functions.

Node pairs with no data::

 1 2

Python dictionary as data::

 1 2 {'weight':7, 'color':'green'}

Arbitrary data::

 1 2 7 green
"""

from _typeshed import Incomplete
from collections.abc import Generator

from networkx.utils.backends import _dispatchable

__all__ = [
    "generate_edgelist",
    "write_edgelist",
    "parse_edgelist",
    "read_edgelist",
    "read_weighted_edgelist",
    "write_weighted_edgelist",
]

def generate_edgelist(G, delimiter: str = " ", data: bool = True) -> Generator[Incomplete, None, None]:
    """
    Generate a single line of the graph G in edge list format.

    Parameters
    ----------
    G : NetworkX graph

    delimiter : string, optional
       Separator for node labels

    data : bool or list of keys
       If False generate no edge data.  If True use a dictionary
       representation of edge data.  If a list of keys use a list of data
       values corresponding to the keys.

    Returns
    -------
    lines : string
        Lines of data in adjlist format.

    Examples
    --------
    >>> G = nx.lollipop_graph(4, 3)
    >>> G[1][2]["weight"] = 3
    >>> G[3][4]["capacity"] = 12
    >>> for line in nx.generate_edgelist(G, data=False):
    ...     print(line)
    0 1
    0 2
    0 3
    1 2
    1 3
    2 3
    3 4
    4 5
    5 6

    >>> for line in nx.generate_edgelist(G):
    ...     print(line)
    0 1 {}
    0 2 {}
    0 3 {}
    1 2 {'weight': 3}
    1 3 {}
    2 3 {}
    3 4 {'capacity': 12}
    4 5 {}
    5 6 {}

    >>> for line in nx.generate_edgelist(G, data=["weight"]):
    ...     print(line)
    0 1
    0 2
    0 3
    1 2 3
    1 3
    2 3
    3 4
    4 5
    5 6

    See Also
    --------
    write_adjlist, read_adjlist
    """
    ...
def write_edgelist(G, path, comments: str = "#", delimiter: str = " ", data: bool = True, encoding: str = "utf-8") -> None:
    """
    Write graph as a list of edges.

    Parameters
    ----------
    G : graph
       A NetworkX graph
    path : file or string
       File or filename to write. If a file is provided, it must be
       opened in 'wb' mode. Filenames ending in .gz or .bz2 will be compressed.
    comments : string, optional
       The character used to indicate the start of a comment
    delimiter : string, optional
       The string used to separate values.  The default is whitespace.
    data : bool or list, optional
       If False write no edge data.
       If True write a string representation of the edge data dictionary..
       If a list (or other iterable) is provided, write the  keys specified
       in the list.
    encoding: string, optional
       Specify which encoding to use when writing file.

    Examples
    --------
    >>> G = nx.path_graph(4)
    >>> nx.write_edgelist(G, "test.edgelist")
    >>> G = nx.path_graph(4)
    >>> fh = open("test.edgelist", "wb")
    >>> nx.write_edgelist(G, fh)
    >>> nx.write_edgelist(G, "test.edgelist.gz")
    >>> nx.write_edgelist(G, "test.edgelist_nodata.gz", data=False)

    >>> G = nx.Graph()
    >>> G.add_edge(1, 2, weight=7, color="red")
    >>> nx.write_edgelist(G, "test.edgelist_bigger_nodata", data=False)
    >>> nx.write_edgelist(G, "test.edgelist_color", data=["color"])
    >>> nx.write_edgelist(G, "test.edgelist_color_weight", data=["color", "weight"])

    See Also
    --------
    read_edgelist
    write_weighted_edgelist
    """
    ...
@_dispatchable
def parse_edgelist(lines, comments: str = "#", delimiter=None, create_using=None, nodetype=None, data: bool = True):
    """
    Parse lines of an edge list representation of a graph.

    Parameters
    ----------
    lines : list or iterator of strings
        Input data in edgelist format
    comments : string, optional
       Marker for comment lines. Default is `'#'`. To specify that no character
       should be treated as a comment, use ``comments=None``.
    delimiter : string, optional
       Separator for node labels. Default is `None`, meaning any whitespace.
    create_using : NetworkX graph constructor, optional (default=nx.Graph)
       Graph type to create. If graph instance, then cleared before populated.
    nodetype : Python type, optional
       Convert nodes to this type. Default is `None`, meaning no conversion is
       performed.
    data : bool or list of (label,type) tuples
       If `False` generate no edge data or if `True` use a dictionary
       representation of edge data or a list tuples specifying dictionary
       key names and types for edge data.

    Returns
    -------
    G: NetworkX Graph
        The graph corresponding to lines

    Examples
    --------
    Edgelist with no data:

    >>> lines = ["1 2", "2 3", "3 4"]
    >>> G = nx.parse_edgelist(lines, nodetype=int)
    >>> list(G)
    [1, 2, 3, 4]
    >>> list(G.edges())
    [(1, 2), (2, 3), (3, 4)]

    Edgelist with data in Python dictionary representation:

    >>> lines = ["1 2 {'weight': 3}", "2 3 {'weight': 27}", "3 4 {'weight': 3.0}"]
    >>> G = nx.parse_edgelist(lines, nodetype=int)
    >>> list(G)
    [1, 2, 3, 4]
    >>> list(G.edges(data=True))
    [(1, 2, {'weight': 3}), (2, 3, {'weight': 27}), (3, 4, {'weight': 3.0})]

    Edgelist with data in a list:

    >>> lines = ["1 2 3", "2 3 27", "3 4 3.0"]
    >>> G = nx.parse_edgelist(lines, nodetype=int, data=(("weight", float),))
    >>> list(G)
    [1, 2, 3, 4]
    >>> list(G.edges(data=True))
    [(1, 2, {'weight': 3.0}), (2, 3, {'weight': 27.0}), (3, 4, {'weight': 3.0})]

    See Also
    --------
    read_weighted_edgelist
    """
    ...
@_dispatchable
def read_edgelist(
    path,
    comments: str = "#",
    delimiter=None,
    create_using=None,
    nodetype=None,
    data: bool = True,
    edgetype=None,
    encoding: str = "utf-8",
):
    """
    Read a graph from a list of edges.

    Parameters
    ----------
    path : file or string
       File or filename to read. If a file is provided, it must be
       opened in 'rb' mode.
       Filenames ending in .gz or .bz2 will be decompressed.
    comments : string, optional
       The character used to indicate the start of a comment. To specify that
       no character should be treated as a comment, use ``comments=None``.
    delimiter : string, optional
       The string used to separate values.  The default is whitespace.
    create_using : NetworkX graph constructor, optional (default=nx.Graph)
       Graph type to create. If graph instance, then cleared before populated.
    nodetype : int, float, str, Python type, optional
       Convert node data from strings to specified type
    data : bool or list of (label,type) tuples
       Tuples specifying dictionary key names and types for edge data
    edgetype : int, float, str, Python type, optional OBSOLETE
       Convert edge data from strings to specified type and use as 'weight'
    encoding: string, optional
       Specify which encoding to use when reading file.

    Returns
    -------
    G : graph
       A networkx Graph or other type specified with create_using

    Examples
    --------
    >>> nx.write_edgelist(nx.path_graph(4), "test.edgelist_P4")
    >>> G = nx.read_edgelist("test.edgelist_P4")

    >>> fh = open("test.edgelist_P4", "rb")
    >>> G = nx.read_edgelist(fh)
    >>> fh.close()

    >>> G = nx.read_edgelist("test.edgelist_P4", nodetype=int)
    >>> G = nx.read_edgelist("test.edgelist_P4", create_using=nx.DiGraph)

    Edgelist with data in a list:

    >>> textline = "1 2 3"
    >>> fh = open("test.textline", "w")
    >>> d = fh.write(textline)
    >>> fh.close()
    >>> G = nx.read_edgelist("test.textline", nodetype=int, data=(("weight", float),))
    >>> list(G)
    [1, 2]
    >>> list(G.edges(data=True))
    [(1, 2, {'weight': 3.0})]

    See parse_edgelist() for more examples of formatting.

    See Also
    --------
    parse_edgelist
    write_edgelist

    Notes
    -----
    Since nodes must be hashable, the function nodetype must return hashable
    types (e.g. int, float, str, frozenset - or tuples of those, etc.)
    """
    ...
def write_weighted_edgelist(G, path, comments: str = "#", delimiter: str = " ", encoding: str = "utf-8") -> None:
    """
    Write graph G as a list of edges with numeric weights.

    Parameters
    ----------
    G : graph
       A NetworkX graph
    path : file or string
       File or filename to write. If a file is provided, it must be
       opened in 'wb' mode.
       Filenames ending in .gz or .bz2 will be compressed.
    comments : string, optional
       The character used to indicate the start of a comment
    delimiter : string, optional
       The string used to separate values.  The default is whitespace.
    encoding: string, optional
       Specify which encoding to use when writing file.

    Examples
    --------
    >>> G = nx.Graph()
    >>> G.add_edge(1, 2, weight=7)
    >>> nx.write_weighted_edgelist(G, "test.weighted.edgelist")

    See Also
    --------
    read_edgelist
    write_edgelist
    read_weighted_edgelist
    """
    ...
@_dispatchable
def read_weighted_edgelist(
    path, comments: str = "#", delimiter=None, create_using=None, nodetype=None, encoding: str = "utf-8"
):
    """
    Read a graph as list of edges with numeric weights.

    Parameters
    ----------
    path : file or string
       File or filename to read. If a file is provided, it must be
       opened in 'rb' mode.
       Filenames ending in .gz or .bz2 will be decompressed.
    comments : string, optional
       The character used to indicate the start of a comment.
    delimiter : string, optional
       The string used to separate values.  The default is whitespace.
    create_using : NetworkX graph constructor, optional (default=nx.Graph)
       Graph type to create. If graph instance, then cleared before populated.
    nodetype : int, float, str, Python type, optional
       Convert node data from strings to specified type
    encoding: string, optional
       Specify which encoding to use when reading file.

    Returns
    -------
    G : graph
       A networkx Graph or other type specified with create_using

    Notes
    -----
    Since nodes must be hashable, the function nodetype must return hashable
    types (e.g. int, float, str, frozenset - or tuples of those, etc.)

    Example edgelist file format.

    With numeric edge data::

     # read with
     # >>> G=nx.read_weighted_edgelist(fh)
     # source target data
     a b 1
     a c 3.14159
     d e 42

    See Also
    --------
    write_weighted_edgelist
    """
    ...
