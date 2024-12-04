from networkx.utils.backends import _dispatchable

@_dispatchable
def combinatorial_embedding_to_pos(embedding, fully_triangulate: bool = False):
    """
    Assigns every node a (x, y) position based on the given embedding

    The algorithm iteratively inserts nodes of the input graph in a certain
    order and rearranges previously inserted nodes so that the planar drawing
    stays valid. This is done efficiently by only maintaining relative
    positions during the node placements and calculating the absolute positions
    at the end. For more information see [1]_.

    Parameters
    ----------
    embedding : nx.PlanarEmbedding
        This defines the order of the edges

    fully_triangulate : bool
        If set to True the algorithm adds edges to a copy of the input
        embedding and makes it chordal.

    Returns
    -------
    pos : dict
        Maps each node to a tuple that defines the (x, y) position

    References
    ----------
    .. [1] M. Chrobak and T.H. Payne:
        A Linear-time Algorithm for Drawing a Planar Graph on a Grid 1989
        http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.51.6677
    """
    ...
