"""
Read graphs in LEDA format.

LEDA is a C++ class library for efficient data types and algorithms.

Format
------
See http://www.algorithmic-solutions.info/leda_guide/graphs/leda_native_graph_fileformat.html
"""

from networkx.utils.backends import _dispatchable

@_dispatchable
def read_leda(path, encoding: str = "UTF-8"):
    """
    Read graph in LEDA format from path.

    Parameters
    ----------
    path : file or string
       File or filename to read.  Filenames ending in .gz or .bz2  will be
       uncompressed.

    Returns
    -------
    G : NetworkX graph

    Examples
    --------
    G=nx.read_leda('file.leda')

    References
    ----------
    .. [1] http://www.algorithmic-solutions.info/leda_guide/graphs/leda_native_graph_fileformat.html
    """
    ...
@_dispatchable
def parse_leda(lines):
    """
    Read graph in LEDA format from string or iterable.

    Parameters
    ----------
    lines : string or iterable
       Data in LEDA format.

    Returns
    -------
    G : NetworkX graph

    Examples
    --------
    G=nx.parse_leda(string)

    References
    ----------
    .. [1] http://www.algorithmic-solutions.info/leda_guide/graphs/leda_native_graph_fileformat.html
    """
    ...
