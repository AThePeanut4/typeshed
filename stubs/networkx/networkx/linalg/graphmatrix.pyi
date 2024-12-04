"""Adjacency matrix and incidence matrix of graphs."""

from _typeshed import Incomplete

from networkx.utils.backends import _dispatchable

@_dispatchable
def incidence_matrix(
    G,
    nodelist: Incomplete | None = None,
    edgelist: Incomplete | None = None,
    oriented: bool = False,
    weight: Incomplete | None = None,
):
    """
    Returns incidence matrix of G.

    The incidence matrix assigns each row to a node and each column to an edge.
    For a standard incidence matrix a 1 appears wherever a row's node is
    incident on the column's edge.  For an oriented incidence matrix each
    edge is assigned an orientation (arbitrarily for undirected and aligning to
    direction for directed).  A -1 appears for the source (tail) of an edge and
    1 for the destination (head) of the edge.  The elements are zero otherwise.

    Parameters
    ----------
    G : graph
       A NetworkX graph

    nodelist : list, optional   (default= all nodes in G)
       The rows are ordered according to the nodes in nodelist.
       If nodelist is None, then the ordering is produced by G.nodes().

    edgelist : list, optional (default= all edges in G)
       The columns are ordered according to the edges in edgelist.
       If edgelist is None, then the ordering is produced by G.edges().

    oriented: bool, optional (default=False)
       If True, matrix elements are +1 or -1 for the head or tail node
       respectively of each edge.  If False, +1 occurs at both nodes.

    weight : string or None, optional (default=None)
       The edge data key used to provide each value in the matrix.
       If None, then each edge has weight 1.  Edge weights, if used,
       should be positive so that the orientation can provide the sign.

    dtype : a NumPy dtype or None (default=None)
        The dtype of the output sparse array. This type should be a compatible
        type of the weight argument, eg. if weight would return a float this
        argument should also be a float.
        If None, then the default for SciPy is used.

    Returns
    -------
    A : SciPy sparse array
      The incidence matrix of G.

    Notes
    -----
    For MultiGraph/MultiDiGraph, the edges in edgelist should be
    (u,v,key) 3-tuples.

    "Networks are the best discrete model for so many problems in
    applied mathematics" [1]_.

    References
    ----------
    .. [1] Gil Strang, Network applications: A = incidence matrix,
       http://videolectures.net/mit18085f07_strang_lec03/
    """
    ...
@_dispatchable
def adjacency_matrix(G, nodelist: Incomplete | None = None, dtype: Incomplete | None = None, weight: str = "weight"):
    """
    Returns adjacency matrix of `G`.

    Parameters
    ----------
    G : graph
       A NetworkX graph

    nodelist : list, optional
       The rows and columns are ordered according to the nodes in `nodelist`.
       If ``nodelist=None`` (the default), then the ordering is produced by
       ``G.nodes()``.

    dtype : NumPy data-type, optional
        The desired data-type for the array.
        If `None`, then the NumPy default is used.

    weight : string or None, optional (default='weight')
       The edge data key used to provide each value in the matrix.
       If None, then each edge has weight 1.

    Returns
    -------
    A : SciPy sparse array
      Adjacency matrix representation of G.

    Notes
    -----
    For directed graphs, entry ``i, j`` corresponds to an edge from ``i`` to ``j``.

    If you want a pure Python adjacency matrix representation try
    :func:`~networkx.convert.to_dict_of_dicts` which will return a
    dictionary-of-dictionaries format that can be addressed as a
    sparse matrix.

    For multigraphs with parallel edges the weights are summed.
    See :func:`networkx.convert_matrix.to_numpy_array` for other options.

    The convention used for self-loop edges in graphs is to assign the
    diagonal matrix entry value to the edge weight attribute
    (or the number 1 if the edge has no weight attribute).  If the
    alternate convention of doubling the edge weight is desired the
    resulting SciPy sparse array can be modified as follows::

        >>> G = nx.Graph([(1, 1)])
        >>> A = nx.adjacency_matrix(G)
        >>> A.toarray()
        array([[1]])
        >>> A.setdiag(A.diagonal() * 2)
        >>> A.toarray()
        array([[2]])

    See Also
    --------
    to_numpy_array
    to_scipy_sparse_array
    to_dict_of_dicts
    adjacency_spectrum
    """
    ...
