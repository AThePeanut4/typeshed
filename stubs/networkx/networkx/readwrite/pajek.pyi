"""
*****
Pajek
*****
Read graphs in Pajek format.

This implementation handles directed and undirected graphs including
those with self loops and parallel edges.

Format
------
See http://vlado.fmf.uni-lj.si/pub/networks/pajek/doc/draweps.htm
for format information.
"""

from _typeshed import Incomplete
from collections.abc import Generator

from networkx.utils.backends import _dispatchable

__all__ = ["read_pajek", "parse_pajek", "generate_pajek", "write_pajek"]

def generate_pajek(G) -> Generator[Incomplete, None, None]: ...
def write_pajek(G, path, encoding: str = "UTF-8") -> None: ...
@_dispatchable
def read_pajek(path, encoding: str = "UTF-8"):
    """
    Read graph in Pajek format from path.

    Parameters
    ----------
    path : file or string
       File or filename to write.
       Filenames ending in .gz or .bz2 will be uncompressed.

    Returns
    -------
    G : NetworkX MultiGraph or MultiDiGraph.

    Examples
    --------
    >>> G = nx.path_graph(4)
    >>> nx.write_pajek(G, "test.net")
    >>> G = nx.read_pajek("test.net")

    To create a Graph instead of a MultiGraph use

    >>> G1 = nx.Graph(G)

    References
    ----------
    See http://vlado.fmf.uni-lj.si/pub/networks/pajek/doc/draweps.htm
    for format information.
    """
    ...
@_dispatchable
def parse_pajek(lines):
    """
    Parse Pajek format graph from string or iterable.

    Parameters
    ----------
    lines : string or iterable
       Data in Pajek format.

    Returns
    -------
    G : NetworkX graph

    See Also
    --------
    read_pajek
    """
    ...
