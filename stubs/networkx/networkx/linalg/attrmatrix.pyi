"""Functions for constructing matrix-like objects from graph attributes."""

from networkx.utils.backends import _dispatchable

__all__ = ["attr_matrix", "attr_sparse_matrix"]

@_dispatchable
def attr_matrix(G, edge_attr=None, node_attr=None, normalized: bool = False, rc_order=None, dtype=None, order=None):
    """
    Returns the attribute matrix using attributes from `G` as a numpy array.

    If only `G` is passed in, then the adjacency matrix is constructed.

    Let A be a discrete set of values for the node attribute `node_attr`. Then
    the elements of A represent the rows and columns of the constructed matrix.
    Now, iterate through every edge e=(u,v) in `G` and consider the value
    of the edge attribute `edge_attr`.  If ua and va are the values of the
    node attribute `node_attr` for u and v, respectively, then the value of
    the edge attribute is added to the matrix element at (ua, va).

    Parameters
    ----------
    G : graph
        The NetworkX graph used to construct the attribute matrix.

    edge_attr : str, optional (default: number of edges for each matrix element)
        Each element of the matrix represents a running total of the
        specified edge attribute for edges whose node attributes correspond
        to the rows/cols of the matrix. The attribute must be present for
        all edges in the graph. If no attribute is specified, then we
        just count the number of edges whose node attributes correspond
        to the matrix element.

    node_attr : str, optional (default: use nodes of the graph)
        Each row and column in the matrix represents a particular value
        of the node attribute.  The attribute must be present for all nodes
        in the graph. Note, the values of this attribute should be reliably
        hashable. So, float values are not recommended. If no attribute is
        specified, then the rows and columns will be the nodes of the graph.

    normalized : bool, optional (default: False)
        If True, then each row is normalized by the summation of its values.

    rc_order : list, optional (default: order of nodes in G)
        A list of the node attribute values. This list specifies the ordering
        of rows and columns of the array. If no ordering is provided, then
        the ordering will be the same as the node order in `G`.
        When `rc_order` is `None`, the function returns a 2-tuple ``(matrix, ordering)``

    Other Parameters
    ----------------
    dtype : NumPy data-type, optional
        A valid NumPy dtype used to initialize the array. Keep in mind certain
        dtypes can yield unexpected results if the array is to be normalized.
        The parameter is passed to numpy.zeros(). If unspecified, the NumPy
        default is used.

    order : {'C', 'F'}, optional
        Whether to store multidimensional data in C- or Fortran-contiguous
        (row- or column-wise) order in memory. This parameter is passed to
        numpy.zeros(). If unspecified, the NumPy default is used.

    Returns
    -------
    M : 2D NumPy ndarray
        The attribute matrix.

    ordering : list
        If `rc_order` was specified, then only the attribute matrix is returned.
        However, if `rc_order` was None, then the ordering used to construct
        the matrix is returned as well.

    Examples
    --------
    Construct an adjacency matrix:

    >>> G = nx.Graph()
    >>> G.add_edge(0, 1, thickness=1, weight=3)
    >>> G.add_edge(0, 2, thickness=2)
    >>> G.add_edge(1, 2, thickness=3)
    >>> nx.attr_matrix(G, rc_order=[0, 1, 2])
    array([[0., 1., 1.],
           [1., 0., 1.],
           [1., 1., 0.]])

    Alternatively, we can obtain the matrix describing edge thickness.

    >>> nx.attr_matrix(G, edge_attr="thickness", rc_order=[0, 1, 2])
    array([[0., 1., 2.],
           [1., 0., 3.],
           [2., 3., 0.]])

    We can also color the nodes and ask for the probability distribution over
    all edges (u,v) describing:

        Pr(v has color Y | u has color X)

    >>> G.nodes[0]["color"] = "red"
    >>> G.nodes[1]["color"] = "red"
    >>> G.nodes[2]["color"] = "blue"
    >>> rc = ["red", "blue"]
    >>> nx.attr_matrix(G, node_attr="color", normalized=True, rc_order=rc)
    array([[0.33333333, 0.66666667],
           [1.        , 0.        ]])

    For example, the above tells us that for all edges (u,v):

        Pr( v is red  | u is red)  = 1/3
        Pr( v is blue | u is red)  = 2/3

        Pr( v is red  | u is blue) = 1
        Pr( v is blue | u is blue) = 0

    Finally, we can obtain the total weights listed by the node colors.

    >>> nx.attr_matrix(G, edge_attr="weight", node_attr="color", rc_order=rc)
    array([[3., 2.],
           [2., 0.]])

    Thus, the total weight over all edges (u,v) with u and v having colors:

        (red, red)   is 3   # the sole contribution is from edge (0,1)
        (red, blue)  is 2   # contributions from edges (0,2) and (1,2)
        (blue, red)  is 2   # same as (red, blue) since graph is undirected
        (blue, blue) is 0   # there are no edges with blue endpoints
    """
    ...
@_dispatchable
def attr_sparse_matrix(G, edge_attr=None, node_attr=None, normalized: bool = False, rc_order=None, dtype=None):
    """
    Returns a SciPy sparse array using attributes from G.

    If only `G` is passed in, then the adjacency matrix is constructed.

    Let A be a discrete set of values for the node attribute `node_attr`. Then
    the elements of A represent the rows and columns of the constructed matrix.
    Now, iterate through every edge e=(u,v) in `G` and consider the value
    of the edge attribute `edge_attr`.  If ua and va are the values of the
    node attribute `node_attr` for u and v, respectively, then the value of
    the edge attribute is added to the matrix element at (ua, va).

    Parameters
    ----------
    G : graph
        The NetworkX graph used to construct the NumPy matrix.

    edge_attr : str, optional (default: number of edges for each matrix element)
        Each element of the matrix represents a running total of the
        specified edge attribute for edges whose node attributes correspond
        to the rows/cols of the matrix. The attribute must be present for
        all edges in the graph. If no attribute is specified, then we
        just count the number of edges whose node attributes correspond
        to the matrix element.

    node_attr : str, optional (default: use nodes of the graph)
        Each row and column in the matrix represents a particular value
        of the node attribute.  The attribute must be present for all nodes
        in the graph. Note, the values of this attribute should be reliably
        hashable. So, float values are not recommended. If no attribute is
        specified, then the rows and columns will be the nodes of the graph.

    normalized : bool, optional (default: False)
        If True, then each row is normalized by the summation of its values.

    rc_order : list, optional (default: order of nodes in G)
        A list of the node attribute values. This list specifies the ordering
        of rows and columns of the array and the return value. If no ordering
        is provided, then the ordering will be that of nodes in `G`.

    Other Parameters
    ----------------
    dtype : NumPy data-type, optional
        A valid NumPy dtype used to initialize the array. Keep in mind certain
        dtypes can yield unexpected results if the array is to be normalized.
        The parameter is passed to numpy.zeros(). If unspecified, the NumPy
        default is used.

    Returns
    -------
    M : SciPy sparse array
        The attribute matrix.

    ordering : list
        If `rc_order` was specified, then only the matrix is returned.
        However, if `rc_order` was None, then the ordering used to construct
        the matrix is returned as well.

    Examples
    --------
    Construct an adjacency matrix:

    >>> G = nx.Graph()
    >>> G.add_edge(0, 1, thickness=1, weight=3)
    >>> G.add_edge(0, 2, thickness=2)
    >>> G.add_edge(1, 2, thickness=3)
    >>> M = nx.attr_sparse_matrix(G, rc_order=[0, 1, 2])
    >>> M.toarray()
    array([[0., 1., 1.],
           [1., 0., 1.],
           [1., 1., 0.]])

    Alternatively, we can obtain the matrix describing edge thickness.

    >>> M = nx.attr_sparse_matrix(G, edge_attr="thickness", rc_order=[0, 1, 2])
    >>> M.toarray()
    array([[0., 1., 2.],
           [1., 0., 3.],
           [2., 3., 0.]])

    We can also color the nodes and ask for the probability distribution over
    all edges (u,v) describing:

        Pr(v has color Y | u has color X)

    >>> G.nodes[0]["color"] = "red"
    >>> G.nodes[1]["color"] = "red"
    >>> G.nodes[2]["color"] = "blue"
    >>> rc = ["red", "blue"]
    >>> M = nx.attr_sparse_matrix(G, node_attr="color", normalized=True, rc_order=rc)
    >>> M.toarray()
    array([[0.33333333, 0.66666667],
           [1.        , 0.        ]])

    For example, the above tells us that for all edges (u,v):

        Pr( v is red  | u is red)  = 1/3
        Pr( v is blue | u is red)  = 2/3

        Pr( v is red  | u is blue) = 1
        Pr( v is blue | u is blue) = 0

    Finally, we can obtain the total weights listed by the node colors.

    >>> M = nx.attr_sparse_matrix(G, edge_attr="weight", node_attr="color", rc_order=rc)
    >>> M.toarray()
    array([[3., 2.],
           [2., 0.]])

    Thus, the total weight over all edges (u,v) with u and v having colors:

        (red, red)   is 3   # the sole contribution is from edge (0,1)
        (red, blue)  is 2   # contributions from edges (0,2) and (1,2)
        (blue, red)  is 2   # same as (red, blue) since graph is undirected
        (blue, blue) is 0   # there are no edges with blue endpoints
    """
    ...
