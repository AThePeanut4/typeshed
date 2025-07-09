"""
====================
Biadjacency matrices
====================
"""

from _typeshed import Incomplete
from collections.abc import Iterable

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["biadjacency_matrix", "from_biadjacency_matrix"]

@_dispatchable
def biadjacency_matrix(
    G: Graph[_Node],
    row_order: Iterable[_Node],
    column_order: Iterable[Incomplete] | None = None,
    dtype=None,
    weight: str | None = "weight",
    format="csr",
): ...  # Return is a complex union of scipy classes depending on the format param
@_dispatchable
def from_biadjacency_matrix(A, create_using: Graph[_Node] | None = None, edge_attribute: str = "weight"):
    """
    Creates a new bipartite graph from a biadjacency matrix given as a
    SciPy sparse array.

    Parameters
    ----------
    A: scipy sparse array
      A biadjacency matrix representation of a graph

    create_using: NetworkX graph
       Use specified graph for result.  The default is Graph()

    edge_attribute: string
       Name of edge attribute to store matrix numeric value. The data will
       have the same type as the matrix entry (int, float, (real,imag)).

    Notes
    -----
    The nodes are labeled with the attribute `bipartite` set to an integer
    0 or 1 representing membership in part 0 or part 1 of the bipartite graph.

    If `create_using` is an instance of :class:`networkx.MultiGraph` or
    :class:`networkx.MultiDiGraph` and the entries of `A` are of
    type :class:`int`, then this function returns a multigraph (of the same
    type as `create_using`) with parallel edges. In this case, `edge_attribute`
    will be ignored.

    See Also
    --------
    biadjacency_matrix
    from_numpy_array

    References
    ----------
    [1] https://en.wikipedia.org/wiki/Adjacency_matrix#Adjacency_matrix_of_a_bipartite_graph
    """
    ...
